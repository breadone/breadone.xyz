import json
from datetime import datetime as dt
from urllib import request as req


def lambda_handler(event, context):
    r = req.Request('https://www.creators.com/read/heathcliff', headers={'User-Agent': 'Mozilla/5.0'})
    html = req.urlopen(r).read().decode("utf8")

    urlStart = html.index('https://cdn.alphacomedy.com')
    imageUrl = html[urlStart:].split("\"")[0]

    response = {
        'statusCode': 200,
        'body': imageUrl
    }
    
    print(response)
    
    return response

# old code below, still might use to get previous dates

# def lh2(event, context):

#     try:
#         date = event['body']['date']
#     except Exception:
#         date = dt.today().strftime('%Y/%m/%d')
#     print(event)
#     dateComps = date.split("/")
    
#     # check is date has been passed in the event, else use today
#     # if ('body' not in event) or ('date' not in event['body']):
#     #     date = dt.today().strftime('%Y/%m/%d')
#     #     dateComps = date.split("/")
#     # else:
#     #     date = event['body']['date']
#     #     dateComps = date.split("/")
    
#     fp = req.urlopen(f"https://www.gocomics.com/heathcliff/{date}")
#     mybytes = fp.read()

#     html = mybytes.decode("utf8")
#     fp.close()

#     # check to make sure image exists today
#     if "data-image" in html:
#         urlStart = html.index("data-image") + 12
#         imageUrl = html[urlStart:].split("\"")[0]
#     else:
#         return {
#             'statusCode': 404,
#             'body': date
#         }
#         # newDate = '/'.join([dateComps[0], dateComps[1], str(int(dateComps[2])-1)]) # use yesterdays date if not there
#         # newEvent = event
#         # newEvent['body'] = {"date": newDate}
#         # return lambda_handler(newEvent, context)
    
#     response = {
#         'statusCode': 200,
#         'body': imageUrl
#     }
    
#     print(response)
    
#     return response
