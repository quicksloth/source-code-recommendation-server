from flask import Flask, request, json
from flask_socketio import SocketIO, leave_room
import requests

from Controllers.EvaluatorController import EvaluatorController

app = Flask(__name__, static_folder='')
app.config['SECRET_KEY'] = '@server-secret'
socketio = SocketIO(app)


class Socket:
    """
        Class used to emit answer to specific client
    """
    def __init__(self, sid):
        self.sid = sid
        self.connected = True

    # Emits data to a socket's unique room
    def emit(self, event, data):
        print('going to emit in ', self.sid)
        socketio.emit(event, data, room=self.sid)


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


# TODO: fix all names and function calls
@socketio.on('connect')
def foo():
    EvaluatorController().init_get_recommendation_code_fake(request_id=request.sid)


def emit_code_recommendations(request_id, data):
    print('hello_to_random_client')
    Socket(request_id).emit('message', data)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=6060, debug=True)
