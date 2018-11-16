import json


def generate(id, action, status):
    global data
    d = str(id)
    s = str(status)
    if action == 'insert':
        action = 1
        data = {
            'card_id': d,
            'status': s,
            'action': action
        }
    elif action == 'withdraw':
        action = 0
        data = {
            'card_id': d,
            'status': s,
            'action': action
        }

    elif action == 'view':
        op = 'view-operation'
        data = {
            'options': op,
            'card_id': d
        }
    data = json.dumps(data)
    return data
