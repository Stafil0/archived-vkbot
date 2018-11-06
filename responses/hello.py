from repository import responses


def hello():
    message = 'Дороу.'
    return message, ''


response = responses.Response()
response.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте']
response.description = 'Приветствие'
response.process = hello
