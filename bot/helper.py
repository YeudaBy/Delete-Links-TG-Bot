import json

def json_load(file):
    with open(file, 'r', encoding='UTF-8') as file_read:
        var = json.load(file_read)
        return var

def json_dump(var, file):
    with open(file, 'w', encoding='UTF-8') as file_writing:
        json.dump(var, file_writing, indent=4)
        return True
