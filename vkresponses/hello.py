from vkresponses import handlers


def hello():
    message = 'Дороу'
    return message, ''


response = handlers.Response()
response.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте', 'дороу']
response.description = 'Приветствие'
response.process = hello
