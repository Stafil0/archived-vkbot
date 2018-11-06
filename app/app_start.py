from app import config
from handlers import messages
from flask import Flask, request

app = Flask(__name__)

bad_request = 'Bad request'
actions = {
    'confirmation': lambda d, t:
        config.confirmation_token if d['group_id'] == int(config.get_param('group_id', 'BOT')) else bad_request,
    'message_new': lambda d, t: messages.create_answer(d, t)
}


@app.route('/')
def get():
    return 'Hello, world!'


@app.route('/', methods=['POST'])
def post():
    data = request.json
    if 'type' not in data.keys():
        return bad_request

    data_type = data['type']
    return actions[data_type](data, config.token)


if __name__ == '__main__':
    app.run(port=config.port)
