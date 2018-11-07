handlers = {}


class Handler:
    def __init__(self, name):
        self.name = name
        self.description = ''
        handlers[name] = self

    def handle(self, data):
        pass
