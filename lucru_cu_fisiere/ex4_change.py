import json

with open("ex_json.json", "r") as j:
    d = json.load(j)
    print(d)

d["nocar"] = 32
d["car"] = "vw"
print(d)

with open("ex_json.json", "w") as j:
    json.dump(d, j)