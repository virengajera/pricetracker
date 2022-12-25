import json

def read_db():
    json_file = open('db.json', 'r')
    data = json.load(json_file)
    json_file.close()
    return data


def update_db(data):
    json_file = open('db.json', 'w')
    json.dump(data, json_file)
    json_file.close()
    print("Data Updated")
