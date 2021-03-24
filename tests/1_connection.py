from clients import http_client
import urllib.request


def connect():
    try:
        urllib.request.urlopen('https://rabota.by/')
        return True
    except:
        return False
assert( 'Connection is ok!' if connect() else 'There is a problem with connection!' )