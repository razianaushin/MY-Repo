import requests
import json
import sys
from access_token import token

url = "https://report-pages.wugo.io/report/shopify/sales/barkshop.com/1"

value = token
payload = "  { \"request_type\": \"get_json\" }"
headers = {
  'Authorization': value,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)
print(response.text.encode())


