import json

with open('data-files/people-out.json', 'r') as f:
    json_object = json.loads(f.read())

print(json_object)