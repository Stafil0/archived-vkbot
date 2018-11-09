import threading
import datetime

cached_data = {}
timer = 60


def cached(data):
    return data in cached_data.values()


def add(data):
    now = datetime.datetime.now()
    cached_data[now] = data


def __manage():
    map(cached_data.pop,
        [k for k in cached_data.keys() if k < datetime.datetime.now() - datetime.timedelta(seconds=timer)])
    threading.Timer(timer, __manage).start()


__manage()
