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
    url = 'http://0.0.0.0:6060/source-codes'
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
            {
                'documentation': 'When you’re working with Python, you don’t need to import a library in order to read and write files. It’s handled natively in the language, albeit in a unique manner.',
                'url': 'http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python',
                'sourceCode': [
                    '''file_object = open(“filename”, “mode”) where\nfile_object is the variable to add the file object.''',
                    '''file = open("testfile.txt","w")\nfile.write("Hello World")\nfile.close()''',
                ],
            },
        ],
    }
    headers = {'Content-Type': 'application/json'}

    requests.post(url=url, data=json.dumps(data), headers=headers)

    return json.dumps({'success': True})


@app.route('/run_get')
def run_get():
    url = 'http://0.0.0.0:6060/code-recommendations'
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
    app.run(host='0.0.0.0', port=1111)
