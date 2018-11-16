import json


def extract(data_received):
    data = json.loads(data_received)
    name = data['name']
    surname = data['surname']
    creation_date = data['creation_date']
    password = data['password']
    code = data['code']
    image = data['image']
    balance = data['balance']
    status = data['status']
    type = data['type']
    user_name = data['user_name']
    return status
