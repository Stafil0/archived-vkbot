import configparser
import inspect
import os

CURRENT_DIR = inspect.getfile(inspect.currentframe())

config = configparser.ConfigParser()
path = os.path.abspath(os.path.join(os.path.dirname(CURRENT_DIR), os.pardir, 'app.config'))
config.read(path)


def get_boolean_param(param_name, section='DEFAULT'):
    return config.getboolean(section, param_name, fallback=None)


def get_param(param_name, section='DEFAULT'):
    return config.get(section, param_name, fallback=None)


def get_param_or_default(param_name, section='DEFAULT', default_value=None):
    param_value = get_param(param_name, section)
    return default_value if param_value is None else param_value


port = get_param('port', 'DEFAULT')
token = get_param('token', 'BOT')
confirmation_token = get_param('confirmation_token', 'BOT')
access_token = get_param('access_token', 'BOT')