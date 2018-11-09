responses = []


class Response:
    def __init__(self):
        self.__keys = []
        self.description = ''
        responses.append(self)

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, key):
        for k in key:
            self.__keys.append(k.lower())

    def response(self):
        pass
