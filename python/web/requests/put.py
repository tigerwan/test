import requests


api_url = "https://jsonplaceholder.typicode.com/todos/10"

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.status_code)
print(response.json())

response = requests.get(api_url)
print(response.status_code)
print(response.json())