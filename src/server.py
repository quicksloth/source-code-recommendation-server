import flask
import time
from flask import Flask, request, json
# from logging.config import fileConfig
# import logging

from Controllers.EvaluatorController import EvaluatorController

# fileConfig('logging.conf')
# log = logging.getLogger(__name__)
from Modules.Concepts.ComplexNetwork import ComplexNetwork

app = Flask(__name__, static_folder='')

complex_network = ComplexNetwork()
evaluator_controller = EvaluatorController(complex_network=complex_network)


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10443)
