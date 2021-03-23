
import urllib.request


def connect():
#    assertTrue(x)
    try:
        urllib.request.urlopen('https://rabota.by/')
        return True
    except:
        return False
print( 'Connection is ok!' if connect() else 'There is a problem with connection!' )
