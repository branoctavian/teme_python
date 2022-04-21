import json

with open("ex_json.json") as f:
    continut = json.load(f)
    print(continut)