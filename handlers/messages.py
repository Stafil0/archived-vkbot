import os
import importlib
import inspect
from app import vkapi
from repository import responses

CURRENT_DIR = inspect.getfile(inspect.currentframe())

files = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir, 'responses'))
resp = filter(lambda x: x.endswith('.py'), files)
for r in resp:
    importlib.import_module('responses.' + r[0:-3])


def get_answer(body):
    message = 'WAT'
    attachment = ''
    for r in responses.responses:
        if body in r.keys:
            message, attachment = r.process()
    return message, attachment


def create_answer(data, token):
    data_object = data['object']
    group = data['group_id']
    user_id = data['user_id']
    message, attachment = get_answer(data_object['body'].lower())
    vkapi.send_message(user_id, token, message, attachment)
    return 'Ok'
