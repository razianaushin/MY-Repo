import requests
import json

url = "http://report-pages.wugo.io/register"

#datas which need for registration new user
#note: for every new running you need to new "name" and "email"
# as "name" and "email" must be unique
#otherwise it returns error
data = {
"name": "Test User Mou",
 "email": "testusermoudsfgbggsdds@gmail.com",
 "password": "12345dsffgfgsdf6783"
}

#datas which need to check pass or fail
resp ={
    "message": "Account created successfully!",
    "status": True
}

#send request post via api to register new user
response = requests.post(url, data=data)
#get response message
message = response.json()

#check pass or fail
if message['message']== resp['message'] and message['status']== resp['status'] and message['data']:
	print("The new user is created")
	print("The response details are: \n")
	print(message)
	print("PASS") 
else:
	print("FAIL")