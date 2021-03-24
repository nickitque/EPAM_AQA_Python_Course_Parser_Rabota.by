
def connection_pytest(connection_test):
    status_code =  connection_test.status
    status_info = connection_test.reason
    assert status_code == 200 and status_info == 'OK'



#old_ver
# import urllib.request
#
#
# def connect(http_client):
#     try:
#         urllib.request.urlopen('https://rabota.by/')
#         return True
#     except:
#         return False
# assert( 'Connection is ok!' if connect() else 'There is a problem with connection!' )
