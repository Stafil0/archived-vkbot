import os
import importlib

__imports = os.path.dirname(__file__)
__module = os.path.basename(__imports)
__imported = [__importing for __importing in os.listdir(__imports) if __importing.endswith('.py')]
for __import in __imported:
    importlib.import_module(f'{__module}.{__import[0:-3]}')