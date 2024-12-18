// import type { APIContext } from "astro";
import { defineMiddleware } from "astro/middleware";
import PocketBase from "pocketbase";

export const onRequest = defineMiddleware(
    async ({ locals, cookies }, next) => {
      const token = cookies.get("token");
      const pocketbase = new PocketBase(
        "http://0.0.0.0:8091",
      );
  
      if (token) {
        pocketbase.authStore.save(token.value);
        try {
          pocketbase.authStore.isValid &&
            (await pocketbase.collection("users").authRefresh());
        } catch (error) {
          pocketbase.authStore.clear();
        }
      }
  
      locals.api = pocketbase;
  
      if (token && pocketbase.authStore.isValid) {
        locals.user = pocketbase.authStore.model;
        locals.token = token.value;
      } else {
        locals.user = null;
        locals.token = null;
      }
  
      const response = await next();
  
      if (pocketbase.authStore.isValid) {
        response.headers.append(
          "set-cookie",
          pocketbase.authStore.exportToCookie(),
        );
      }
  
      return response.json();
    },
  );