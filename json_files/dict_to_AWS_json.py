import json

mydict = {
    "people": [
        {
            "name": {"S":"Joe"},
            "age": {"N": "33"},
            "story": {"B": "True"},
            "home": {"S": "house"}
        },
        {
            "name": {"S":"Mary"},
            "age": {"N": "30"},
            "story": {"B": "False"},
            "home": {"S": "penthouse"}
        },
        {
            "name": {"S":"Mark"},
            "age": {"N": "28"},
            "story": {"B": "True"},
            "home": {"S": "tent"}
        },
        {
            "name": {"S":"Sue"},
            "age": {"N": "38"},
            "story": {"B": "False"},
            "home": {"S": "shanty"}
        }
    ]
}

json_string = json.dumps(mydict, indent=2)
with open("data-files/people-out-aws.json", "w") as f:
    f.write(json_string)