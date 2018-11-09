import os
import importlib
from service import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_string \
    if not config.get_boolean_param('debug') \
    else config.get_param('connection_string_debug', 'DATABASE')

db = SQLAlchemy(app)


__models = 'models'
__controllers = 'controllers'
__models_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, __models))
__controllers_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, __controllers))
for __imports in [__models_folder, __controllers_folder]:
    for __imported in [__import
                       for __import in os.listdir(__imports)
                       if __import.endswith('.py') and not __import.startswith('__')]:
        importlib.import_module(f'{os.path.basename(__imports)}.{__imported[0:-3]}')