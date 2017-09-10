from flask import Flask, request, json
from flask_socketio import SocketIO, leave_room, emit
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
        print('going to emit to', self.sid)
        socketio.emit(event, data, room=self.sid, namespace='/code-recommendations')


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/source-codes', methods=['POST'])
def source_codes():
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
    print('/train-network')
    print(request.get_json())
    train_base = request.get_json().get('train_text')
    EvaluatorController().train_network(train_database=train_base)
    return json.dumps({'success': True})


# TODO: maybe use on connect
@socketio.on('connect')
def connect():
    print('connectttsssss')


@socketio.on('getCodes', namespace='/code-recommendations')
def get_recommendation_codes(data):
    data = json.loads(data)
    print(data)
    EvaluatorController().get_recommendation_code(request_id=request.sid,
                                                  language=data['language'],
                                                  query=data['query'],
                                                  comments=data['comments'],
                                                  libs=data['libs'])


def emit_code_recommendations(request_id, data):
    Socket(request_id).emit('recommendationCodes', data)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=6060, debug=True)
