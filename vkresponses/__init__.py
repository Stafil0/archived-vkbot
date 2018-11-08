import os
import importlib

path = os.path.abspath(os.path.join(__file__, os.pardir))
name = os.path.basename(path)
files = [f for f in os.listdir(path) if f.endswith('.py') and f != 'handlers.py']
for f in files:
    import_name = f'{name}.{f[0:-3]}'
    importlib.import_module(import_name)
