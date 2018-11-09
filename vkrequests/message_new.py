import os
import importlib
from service import vkapi, config
from vkresponses.handlers import responses
from vkrequests.handlers import Request
from helpers.strings import damerau_levenshtein_distance

path = os.path.abspath(os.path.join(__file__, '../..', 'vkresponses'))
files = [f for f in os.listdir(path) if f.endswith('.py')]
for f in files:
    importlib.import_module('vkresponses.' + f[0:-3])


def is_directed(data):
    return config.get_param('group_id', 'BOT') in data['text'] or data['peer_id'] == data['from_id']


def need_answer(response, text):
    return any(damerau_levenshtein_distance(text, k) < len(text)*0.4 for k in response.keys)


def get_answers(text):
    return [r.response() for r in responses if need_answer(r, text)]


def handle(data):
    data_object = data['object']
    peer_id = data_object['peer_id']

    if is_directed(data_object):
        text = data_object['text'].lower()
        answers = get_answers(text)
        for message, attachment in answers:
            vkapi.send_peer(peer_id, config.token, message, attachment)


handler = Request('message_new')
handler.request = handle
