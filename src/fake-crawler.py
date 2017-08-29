from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# TODO: temporary until all set client and crawler
@app.route('/run_post', methods=['GET'])
def run_post():
    requestId = request.get_json()
    url = 'http://127.0.0.1:5000/source'
    data = {
        "requestID": requestId.get('requestID'),
        'searchResult': [
            {
                'documentation': 'reading a file',
                'url': 'https://url.com',
                'sourceCode': [
                    '''import json\n''',
                    '''import json\nfrom uuid import uuid4\n''',
                    '''with open(fname) as f:\n    content = f.readlines()\n# you may also want to remove whitespace characters like `\\n` at the end of each line\ncontent = [x.strip() for x in content] \nprint(2)\n'''
                ],
            },
        ],
    }
    headers = {'Content-Type': 'application/json'}

    requests.post(url=url, data=json.dumps(data), headers=headers)

    return 'post'
    # return json.dumps(r.json(), indent=4)


@app.route('/run_get')
def run_get():
    url = 'http://127.0.0.1:5000/code-recommendations'
    data = {
        'query': 'read file',
        'libs': ['flask', 'request', 'json'],
        'comments': ['122', 'todo: test'],
        'language': 'Python',
        'sites': ['stackoverflow'],
    }

    requests.request(url=url, method='GET', data=data)

    return 'get'


if __name__ == "__main__":
    app.run(port=5001)