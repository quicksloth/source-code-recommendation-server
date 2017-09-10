import requests
from flask import json


def train_database():
    url = 'http://0.0.0.0:6060/train-network'
    headers = {'Content-Type': 'application/json'}
    data = {
        'train_text': ['read file', 'flask', 'request',
                       'json', 'comments', '122', 'todo: test', 'language',
                       'Python', 'sites stackoverflow lore lorem', 'lorem ipsumb amdksd'],
    }
    print('going to request')
    requests.post(url=url, data=json.dumps(data), headers=headers)


train_database()
