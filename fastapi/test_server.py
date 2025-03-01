import requests

# get all Items
# print(requests.get("http://127.0.0.1:8000/items").json())

# get Item by item_id
# print(requests.get("http://127.0.0.1:8000/items/1").json())

# get Item by matching data from the query parameters
# print(requests.get("http://127.0.0.1:8000/items/?name=nails&price=1.99&category=consumables").json())

# path + query parameters mixed
# print(requests.get("http://127.0.0.1:8000/items/1/information?name=pliers").json())
