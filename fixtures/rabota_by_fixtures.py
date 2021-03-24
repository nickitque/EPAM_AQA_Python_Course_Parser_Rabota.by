from clients import http_client
from models import parser
import pytest

@pytest.fixture()
def response(params):
    response = GetRequests(params).get_response()
    return response