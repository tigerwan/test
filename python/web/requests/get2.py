
import requests
params = {"q": "cloudguru"}
api_url = "http://www.google.com"
response = requests.get(api_url, params)

print(response.status_code)
print(response.content)
print(response.headers)