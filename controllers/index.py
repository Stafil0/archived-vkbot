from vkrequests.handlers import requests
from service import config
from service import app
from flask import request


ok = 'ok'
bad_request = 'bad'


@app.route('/', methods=['GET'])
def get():
    return 'Hello, world!'


@app.route('/', methods=['POST'])
def post():
    response = ok
    data = request.json

    confirm = requests['confirmation'].request(data)
    if confirm == config.confirmation_token:
        data_type = data['type']
        result = requests[data_type].request(data)
        response = result if result is not None else response

    return response
