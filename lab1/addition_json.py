import json


def add_json():
    with open("addition.json", "r") as file:
        data = json.load(file)
        tall1 = int(data["tall1"])
        tall2 = int(data["tall2"])
        result = tall1 + tall2
        print("Summen av tallene er ", result)


add_json()
