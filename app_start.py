from service import config
from service import app


if __name__ == '__main__':
    app.run(port=config.port)


