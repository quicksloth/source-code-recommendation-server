# Source Code Recommendation Server

Implements Evaluation Component of QuickSloth system

## Prerequisites

* python3

## Used Concepts

* Complex Network of Words
* NLP
* Structural Context
* Software engineer metrics

## Install and run

### Run local (development)

`pip3 install -r requirements.txt`

`cd src/`

`export FLASK_APP=server.py`

`flask run --reload`

(optional `--host=AnyHostYouWant --port=AnyPortYouWant`)

### Run on PROD server

`FLASK_APP=server.py flask run --host=0.0.0.0 --port=10443`

### Using gunicorn (with async worker eventlet)
`cd src; gunicorn -b 0.0.0.0:10443 --worker-class eventlet server:app`

