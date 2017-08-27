from flask import Flask, request
import requests
import json

app = Flask(__name__)


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
    # print(request.data)
    # json_dict = json.loads(request.body.raw)
    # print(json_dict)

    return 'my code'


@app.route('/source', methods=['POST'])
def source():
    if request.method == 'POST':
        return 'my code'


def get_source_codes():
    url = 'http://127.0.0.1:5001/run_post'
    data = {
        'query': 'read file',
        'libs': ['flask', 'request', 'json'],
        'comments': ['122', 'todo: test'],
        'language': 'Python',
        'sites': ['stackoverflow'],
    }

    requests.request(url=url, method='GET', data=data)

if __name__ == "__main__":
    app.run()
