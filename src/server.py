import os

import flask
import time
from flask import Flask, request, json
from flask_socketio import SocketIO
import requests
# from logging.config import fileConfig
# import logging

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


@app.route('/')
def index():
    return 'Hello, World new version!'


@app.route('/source-codes', methods=['POST'])
def source_codes():
    start = time.time()
    evaluator_controller.evaluate_search_codes(request)
    end = time.time()
    print('Receive Source code and evaluate took', (end - start), 'seconds')
    return json.dumps({'success': True})


def get_source_codes(data):
    url = os.environ.get('CRAWLER_HOST', 'http://0.0.0.0:1111/crawl')
    headers = {'Content-Type': 'application/json'}
    print('going to request new version')
    requests.request(url=url, method='GET', data=data, headers=headers)


@app.route('/train-network', methods=['POST'])
def train_network():
    print('Train Start')
    start = time.time()
    evaluator_controller.train_network(train_database=request.get_json().get('train_text'))
    end = time.time()
    print('TrainNetwork took', (end - start), 'seconds')
    return json.dumps({'success': True})


@app.route('/word-complex-network', methods=['GET'])
def get_complex_network():
    resp = flask.Response(json.dumps(complex_network.adjacency_list))
    resp.headers['Content-Type'] = 'application/json'
    return resp


@app.route('/word-complex-network-cluster', methods=['GET'])
def get_complex_network_cluster():
    resp = flask.Response(json.dumps(complex_network.cluster_list))
    resp.headers['Content-Type'] = 'application/json'
    return resp


# TODO: maybe use on connect
@socketio.on('connect')
def connect():
    print('connectttsssss')


@socketio.on('getCodes', namespace='/code-recommendations')
def get_recommendation_codes(data):
    data = json.loads(data)
    print(data)
    evaluator_controller.get_recommendation_code(request_id=request.sid,
                                                 language=data['language'],
                                                 query=data['query'],
                                                 comments=data['comments'],
                                                 libs=data['libs'])


def emit_code_recommendations(request_id, data):
    Socket(request_id).emit('recommendationCodes', data)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    # The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
    socketio.run(app, host='0.0.0.0', port=port)
