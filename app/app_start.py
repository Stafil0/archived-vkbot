from vkrequests.handlers import requests
from app import config
from flask import Flask, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.get_param('connection_string', 'DATABASE')

ok = 'ok'
bad_request = 'bad'


@app.route('/')
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


if __name__ == '__main__':
    app.run(debug=True, port=config.port)
