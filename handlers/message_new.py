import os
import importlib
from app import vkapi
from app import config
from repository import responses, handlers

path = os.path.abspath(os.path.join(__file__, '../..', 'responses'))
files = [f for f in os.listdir(path) if f.endswith('.py')]
for f in files:
    importlib.import_module('responses.' + f[0:-3])


def is_directed(text):
    return config.get_param('group_id', 'BOT') in text


def get_answers(text):
    return [response.process() for response in responses.responses if set(text.split()).intersection(response.keys)]


def handle(data):
    data_object = data['object']
    peer_id = data_object['peer_id']
    text = data_object['text'].lower()

    if is_directed(text):
        answers = get_answers(text)
        for message, attachment in answers:
            vkapi.send_peer(peer_id, config.token, message, attachment)


handler = handlers.Handler('message_new')
handler.handle = handle
