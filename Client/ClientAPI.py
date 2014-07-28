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

    def request_method(self, payload):
        """

        :rtype: object
        :param payload: The payload that needs to be passed in as arguments
        :return: Returns response objects for now
        """
        effective_url = self.base_url + payload
        response = requests.get(effective_url)
        if response.status_code == 200:
            return response.content
        response.raise_for_status()
