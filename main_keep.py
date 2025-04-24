import os

contents = os.listdir('./Keep')
json_files = []
for content in contents:
    if content.endswith('.json'):
        print(content)