import json


dict = {"masina" : "mercedes", "model" : "GLE", "an" : 2021}

with open("json_file.json", "a") as file:
    json.dump(dict, file)