from flask import Flask, request, json
from flask_socketio import SocketIO, emit, disconnect
import requests

from Controllers.EvaluatorController import EvaluatorController

app = Flask(__name__, static_folder='')
app.config['SECRET_KEY'] = '@server-secret'
socketio = SocketIO(app)

clients = []

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

# TRY SOCKET -----------------------------
# Object that represents a socket connection
class Socket:
    def __init__(self, sid):
        self.sid = sid
        self.connected = True
        print('init Socket')

    # Emits data to a socket's unique room
    def emit(self, event, data):
        print('going to emit in ', self.sid)
        with app.app_context():
            emit(event, data, room=self.sid)


@socketio.on('connect')
def foo():
    print('connect')
    # EvaluatorController
    # clients.append(Socket(request.sid))
    print(request.sid)
    # print(clients)
    # clients[0].emit('message', {'show': True})
    EvaluatorController().init_get_recommendation_code_fake(request_id=request.sid)

# @socketio.on('disconnect')
# def disconnect():
#     print("%s disconnected" % (request.namespace.socket.sessid))
#     clients.remove(request.namespace)


def hello_to_random_client(request_id):
    import random
    from datetime import datetime
    print('hello_to_random_client')
    Socket(request_id).emit('message', {'show': True})
    # print(clients)
    # if clients:
    #     clients[0].emit('message', { 'show': True})
    # k = random.randint(0, len(clients) - 1)
    # print("Saying hello to %s" % (clients[k].socket.sessid))
    # clients[k].emit('message', "Hello at %s" % (datetime.now()))


@socketio.on('json')
def handle_json(json):
    print('handle_json')
    print('received json: ' + str(json))
# https://flask-socketio.readthedocs.io/en/latest/


@socketio.on('try')
def receive():
    # print('sendMessage')
    emit('teste', {'data': 42})
    disconnect()


@socketio.on('serverMessage')
def handle_server_message(message):
    print('the message is %s', message)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('my event')
    print('received json: ' + str(json))

# TRY SOCKET -----------------------------

if __name__ == "__main__":
    socketio.run(app, debug=True)
