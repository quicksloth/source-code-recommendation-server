from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# TODO: temporary until all set client and crawler
@app.route('/crawl', methods=['GET'])
def crawl():
    request_body = request.get_json()
    url = 'http://127.0.0.1:5000/source-codes'
    data = {
        "requestID": request_body.get('requestID'),
        'searchResult': [
            {
                'documentation': 'reading a file',
                'url': 'https://url.com',
                'sourceCode': [
                    '''import json\n''',
                    '''import json\n\n\n\n\n\n\n\n\n\n\n\n\n''',
                    '''import json\nfrom uuid import uuid4\n# you may also want''',
                    '''with open(fname) as f:\n    content = f.readlines()\n# you may also want to remove whitespace characters like `\\n` at the end of each line\ncontent = [x.strip() for x in content] \nprint(2)\n'''
                ],
            },
        ],
    }
    headers = {'Content-Type': 'application/json'}

    requests.post(url=url, data=json.dumps(data), headers=headers)

    return json.dumps({'success': True})


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


def train_database():
    url = 'http://127.0.0.1:5000/train-network'
    headers = {'Content-Type': 'application/json'}
    data = {
        'train_text': ['read file', 'flask', 'request',
                       'json', 'comments', '122', 'todo: test', 'language',
                       'Python', 'sites stackoverflow lore lorem', 'lorem ipsumb amdksd'],
    }
    requests.request(url=url, method='POST', data=data, headers=headers)


if __name__ == "__main__":
    app.run(port=5001)
