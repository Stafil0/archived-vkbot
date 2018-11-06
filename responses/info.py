from repository import responses


def info():
    message = ''
    for c in responses.responses:
        message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


response = responses.Response()
response.keys = ['помощь', 'помоги', 'help']
response.description = 'Показать список команд'
response.process = info
