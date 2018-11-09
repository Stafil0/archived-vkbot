from service import config
from vkrequests import handlers


def handle(data):
    return config.confirmation_token \
        if 'type' in data.keys() and \
           data['group_id'] == int(config.get_param('group_id', 'BOT')) and \
           data['secret'] == config.get_param('access_token', 'BOT') \
        else 'bad'


handler = handlers.Request('confirmation')
handler.request = handle
