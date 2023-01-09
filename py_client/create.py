import requests

endpoint = "http://localhost:8000/api/products/"
headers = {'Authorization': 'Bearer a6966cf3df39b51983530176937902e0325ef4f9'}

content = {
    "title": "this field is done",
    "price": 32.99
}

response = requests.post(endpoint, json=content, headers=headers)
print(response.json())