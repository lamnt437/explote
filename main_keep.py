import os
import json

contents = os.listdir('./Keep')
json_files = []
for content in contents:
    if content.endswith('.json'):
        print(content)

filename = 'Poor Man_s CS bootcamp.json'
with open(f"./Keep/{filename}", 'r') as file:
    data = json.load(file)
    print("data", data)
    for item in data.items():
        print("item", item)
        print("type(item)", type(item))

    for key in data.keys():
        print("key", key)

    for value in data.values():
        print("value", value)