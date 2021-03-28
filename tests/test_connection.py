"""Test to get status code from website"""


def test_connection_established(connection):
    assert connection.status_code == 200, "Response status code isn't 200"
    assert connection.reason == 'OK', "Connection isn't established"
