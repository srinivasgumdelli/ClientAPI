__author__ = 'Srinivas Prasad Gumdelli'

import requests


class ClientAPI:
    """
    Creates an API Client Object

   """
    base_url = ''

    def __init__(self, base_url, user_id=None, api_key=None):
        """

        :param base_url: The base url of the API that needs to be hit
        :param user_id: user_id if any
        :param api_key: api_key if any
        """
        self.base_url = base_url
        self.api_key = api_key
        self.user_id = user_id

    def __repr__(self):
        return 'ClientAPi(base_url=%s, user_id=%s, api_key=%s)' % (self.base_url, self.user_id, self.api_key)

    @staticmethod
    def request_method(payload):
        """

        :rtype : object
        :param base_url: The base url for the project
        :param payload: The payload that needs to be passed in as arguments
        :return: Returns response objects for now
        """
        return requests.get(ClientAPI.base_url,payload)
