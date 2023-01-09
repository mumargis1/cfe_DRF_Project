import requests

endpoint = "http://localhost:8000/api/3224214"

response = requests.get(endpoint)
print(response.json())