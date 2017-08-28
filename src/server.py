from flask import Flask, request, jsonify
import requests
import json
from Controllers.EvaluatorController import EvaluatorController

app = Flask(__name__)

# TODO: look at
# request.headers.get('X-Forwarded-For', request.remote_addr)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# TODO: temporary until all set client and crawler
# @app.route('/run_post')
# def run_post():
#     url = '0.0.0.0:5000'
#     data = {
#         'query': 'read file',
#         'libs': ['flask', 'request', 'json'],
#         'comments': ['122', 'todo: test'],
#         'language': 'Python',
#         'sites': ['stackoverflow'],
#     }
#     headers = {'Content-Type': 'application/json'}
#
#     r = requests.post(url, data, headers=headers)
#
#     # return r.text
#     return json.dumps(r.json(), indent=4)


@app.route('/code-recommendations', methods=['GET'])
def code_recommendations():
    # print(request.__dict__)
    # json_dict = json.loads(request.body.raw)
    # print(json_dict)

    return 'my code'


@app.route('/source', methods=['POST'])
def source():
    print('CANDJSNJAKSDBNKJASNDKJSANDJKSANDJKSANK')
    # t = jsonify(json.loads(request.data))
    # print(t.__dict__)
    # print(t)
    EvaluatorController().evaluate_search_codes(request)
    return 'source'


def get_source_codes(data):
    url = 'http://127.0.0.1:5001/run_post'
    headers = {'Content-Type': 'application/json'}
    requests.request(url=url, method='GET', data=data, headers=headers)

if __name__ == "__main__":
    app.run(host=5000)
