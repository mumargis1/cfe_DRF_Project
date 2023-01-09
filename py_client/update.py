import requests

endpoint = "http://localhost:8000/api/products/1/update/"

content = {
    "title": "Hellow World my old friend",
    "price": 129.99
}

response = requests.put(endpoint, json=content)
print(response.json())