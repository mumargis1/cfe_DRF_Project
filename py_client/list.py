import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password?\n")
auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password })
print(auth_response.json())

if auth_response.status_code==200:
    token = auth_response.json()['token']
    endpoint = "http://localhost:8000/api/products/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    data = response.json()
    next = data['next']
    results = data['results']
    print("next url", next)
    print(results)
