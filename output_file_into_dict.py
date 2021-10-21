import json

with open('output-file1.json', 'r') as f:
    json_object = json.loads(f.read())

print(json_object)