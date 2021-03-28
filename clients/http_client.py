"""Module contains class HTTP client to perform http requests."""


import requests


class HttpClient:

    @staticmethod
    def get(url, headers):
        """Method for retrieving data."""
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def post(url, data, headers):
        """This method is used to send entities to a specific resource."""
        response = requests.post(url, data, headers=headers)
        return response

    @staticmethod
    def delete(url, headers):
        """This method removes the specified resource."""
        response = requests.delete(url, headers=headers)
        return response
