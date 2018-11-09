import vk
from service import config

version = float(config.get_param('api_version', 'BOT'))
session = vk.Session()
api = vk.API(session, v=version)


def send_peer(peer_id, token, message, attachment=''):
    api.messages.send(access_token=token, peer_id=str(peer_id),
                      message=message, attachment=attachment)


def send_chat(chat_id, token, message, attachment=''):
    api.messages.send(access_token=token, chat_id=str(chat_id),
                      message=message, attachment=attachment)


def send_user(user_id, token, message, attachment=''):
    api.messages.send(access_token=token, user_id=str(user_id),
                      message=message, attachment=attachment)

