from vkresponses import handlers


def info():
    message = ''
    for c in handlers.responses:
        message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


response = handlers.Response()
response.keys = ['помощь', 'помоги', 'help']
response.description = 'Показать список команд'
response.response = info
