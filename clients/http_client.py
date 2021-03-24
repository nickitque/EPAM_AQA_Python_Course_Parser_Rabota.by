import requests

class HTTPClient:
    """
    Module with HTTP client.
    """
    def get(self, url, params=None, **kwargs):
        response = requests.get(url, params=params, **kwargs)
        return response
    def post(self, url, data=None, json=None, **kwargs):
        response = requests.post(url,data=data, json=json, **kwargs)
        return response
    def delete(self, url, **kwargs):
        response = requests.delete(url, **kwargs)
        return response
