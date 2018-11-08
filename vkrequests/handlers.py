requests = {}


class Request:
    def __init__(self, name):
        self.name = name
        self.description = ''
        requests[name] = self

    def request(self, data):
        pass
