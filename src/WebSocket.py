from flask import Flask, request, json
from flask_socketio import SocketIO
import requests
from logging.config import fileConfig
import logging

from Controllers.EvaluatorController import EvaluatorController

# fileConfig('logging.conf')
# log = logging.getLogger(__name__)
from Modules.Concepts.ComplexNetwork import ComplexNetwork

app = Flask(__name__, static_folder='')
app.config['SECRET_KEY'] = '@server-secret'
# socketio = SocketIO(app, allow_upgrades=True, engineio_logger=log, logger=log)

socketio = SocketIO(app, allow_upgrades=True)
complex_network = ComplexNetwork()
evaluator_controller = EvaluatorController(complex_network=complex_network)


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


@socketio.on('connect')
def connect():
    print('CONECTADO A UM CLIENTE ', request.sid)


@socketio.on('getCodes', namespace='/code-recommendations')
def get_recommendation_codes(data):
    data = json.loads(data)
    print(data)
    evaluator_controller.get_recommendation_code(request_id=request.sid,
                                                 language=data['language'],
                                                 query=data['query'],
                                                 comments=data['comments'],
                                                 libs=data['libs'])


def run_server():
    socketio.run(app, host='0.0.0.0', port=10443, threaded=True)


if __name__ == "__main__":
    socketio.start_background_task(run_server)
    # socketio.run(app, host='0.0.0.0', port=10443, threaded=True)
