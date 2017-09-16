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

`pip3 install -r requirements.txt`

`cd src/`

`export FLASK_APP=server.py`

`flask run --reload`

(optional `--host=0.0.0.0`)

Using gunicorn
==

`cd src; gunicorn -b 0.0.0.0:6060 server:app`
(`cd src; gunicorn -b 0.0.0.0:10443 server:app`)
