import requests
import json
import sys
url = "https://report-pages.wugo.io/v1/oauth/token"

#datas which need for registration new user
#note: for every new running you need to new "name" and "email"
# as "name" and "email" must be unique
#otherwise it returns error
data = {
 "grant_type":"password",
 "username": "testuser@gmail.com",
 "password": "12345678",
 "client_id": 2,
 "client_secret": "CM9hRWfZLVeBQ2Gi2ZgK5XUUbfp0AViM8LUVTxVq"

}
key_list = ["token_type", "expires_in"]
#datas which need to check pass or fail
resp ={
    "token_type": "Bearer",
    "expires_in": 31536000,
   
}
def get_response():
	#send request post via api to register new user
	response = requests.post(url, data=data)
	#get response message
	message = response.json()
	return message
	
message = get_response()
#check pass or fail
for i in key_list:
	if str(resp[i])==str(message[i]):
		pass
	else:
		print("FAIL")
		sys.exit()
print("PASS")

access_token = message["access_token"]
refresh_token = message["refresh_token"]
token_type = message["token_type"]
expires_in = message["expires_in"]
print("Expire In from response is: " + str(expires_in))
print("Token type from response is: " + str(token_type))
print("Access token from response is: " + str(access_token))
print("Refresh token from response is: " + str(refresh_token))