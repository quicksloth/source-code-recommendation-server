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
    EvaluatorController().evaluate_search_codes(request)
    return json.dumps({'success': True})


def get_source_codes(data):
    url = 'http://127.0.0.1:5001/crawl'
    headers = {'Content-Type': 'application/json'}
    requests.request(url=url, method='GET', data=data, headers=headers)


@app.route('/train-network', methods=['POST'])
def train_network():
    print('teste')
    train_base = request.get_json().get('train_text')
    print(train_base)
    EvaluatorController().train_network(train_database=train_base)
    return json.dumps({'success': True})

if __name__ == "__main__":
    app.run(host=5000)
