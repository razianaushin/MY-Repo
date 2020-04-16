import requests
import json
import sys



url1 = "https://report-pages.wugo.io/v1/oauth/token"

header1 = {
 "grant_type":"password",
 "username": "testuser@gmail.com",
 "password": "12345678",
 "client_id": 2,
 "client_secret": "CM9hRWfZLVeBQ2Gi2ZgK5XUUbfp0AViM8LUVTxVq"

}

response1 = requests.post(url1, data=header1)
message = response1.json()	

# message['access_token'] is access token you need to use for other API's
value = str(message['token_type']) + " " + str(message['access_token'])


url = "https://report-pages.wugo.io/report/keepa/product-landed-rank"


payload = "  {\"data\": { \"asins\": [1371] }, \"request_type\": \"get_json\" }"
headers = {
  'Authorization': value,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)
print(response.json())


