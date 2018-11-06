import vk
from app import config

version = float(config.get_param('api_version', 'BOT'))
session = vk.Session()
api = vk.API(session, v=version)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)

