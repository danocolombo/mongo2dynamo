import json

mydict = {
    "people": [
        {
            "name": {"S": "Joe"},
            "age": 33,
            "story": True,
            "home": "house"
        },
        {
            "name": "Mary",
            "age": 30,
            "story": False,
            "home": "penthouse"
        },
        {
            "name": "Mark",
            "age": 28,
            "story": True,
            "home": "tent"
        },
        {
            "name": "Sue",
            "age": 38,
            "story": False,
            "home": "shanty"
        }
    ]
}

json_string = json.dumps(mydict, indent=2)
with open("people-with-types-out.json", "w") as f:
    f.write(json_string)