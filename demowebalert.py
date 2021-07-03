import urllib.request
import requests


url1 = "https://www.facebook.com"
url2 = "http://getstatuscode.com/500"
page = requests.get(url2)
print(page.status_code)


def opsgenieaert():
    url = "https://api.opsgenie.com/v2/alerts"
    body = '''{    
               "message": "disk memory full ",
               "alias": "max disk usage  ",
               "description": "very low success rate for the web call",
               "responders": [
                 {
                   "name": "ops",
                   "type": "team"
                 }
               ],
               "actions": [
                 "Restart",
                 "check the logs"
               ],
               "tags": [
                 "down",
                 "Critical"
               ],
               "details": {
                 "key1": "value1",
                 "key2": "value2"
               },
               "entity": "An example entity",
               "priority": "P1" }'''
    headers = {
        'content-type': "application/json",
        'Authorization': "GenieKey 368cb009-2ffa-4b27-9ab3-1fc9529f6075"
    }
    response = requests.post(url, data=body, headers=headers)
    response1 = response.json()

    if response.status_code == 202:
        print("Alert is sent to opsgenie")

    else:
        print("API request failed due to following error code: %s and The response was: %s" % (
        response.status_code, response1) + '\n')


if page.status_code != 200:
    opsgenieaert()
else:
    print("website is up")