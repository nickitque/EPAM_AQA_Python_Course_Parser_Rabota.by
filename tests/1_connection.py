
def connection_pytest(connection_test):
    status_code =  connection_test.status
    status_info = connection_test.reason
    assert status_code == 200 and status_info == 'OK'