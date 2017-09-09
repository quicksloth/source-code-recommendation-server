from flask import Flask, request
import requests
from flask import json

from Controllers.EvaluatorController import EvaluatorController

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/code-recommendations', methods=['GET'])
def code_recommendations():
    return 'my code'


@app.route('/source-codes', methods=['POST'])
def source():
    print('receive data in source-codes')
    EvaluatorController().evaluate_search_codes(request)
    return json.dumps({'success': True})


def get_source_codes(data):
    url = 'http://0.0.0.0:1111/crawl'
    headers = {'Content-Type': 'application/json'}
    print('going to request')
    requests.request(url=url, method='GET', data=data, headers=headers)


@app.route('/train-network', methods=['POST'])
def train_network():
    train_base = request.get_json().get('train_text')
    EvaluatorController().train_network(train_database=train_base)
    return json.dumps({'success': True})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6060)
