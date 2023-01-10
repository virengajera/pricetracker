import json

def read_db():
    json_file = open('db.json', 'r')
    data = json.load(json_file)
    json_file.close()
    return data


def update_db(data):
    updated = False
    
    try:
        json_file = open('db.json', 'w')
        json.dump(data, json_file)
        print("Data Updated")
        json_file.close()
        updated = True
        return updated

    except Exception as E:
        return updated