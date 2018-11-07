import os
import importlib
from repository.handlers import handlers
from app import config
from flask import Flask, request

app = Flask(__name__)

path = os.path.abspath(os.path.join(__file__, '../..', 'handlers'))
files = [f for f in os.listdir(path) if f.endswith('.py')]
for f in files:
    importlib.import_module('handlers.' + f[0:-3])


@app.route('/')
def get():
    return 'Hello, world!'


@app.route('/', methods=['POST'])
def post():
    data = request.json
    confirm = handlers['confirmation'].handle(data)
    if confirm == config.confirmation_token:
        data_type = data['type']
        handlers[data_type].handle(data)

    return 'ok'


if __name__ == '__main__':
    app.run(port=config.port)
