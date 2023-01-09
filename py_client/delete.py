import requests

product_id = input("WHAT is the product you want to delete?\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    response = requests.delete(endpoint)
    print(response.status_code, response.status_code==204)