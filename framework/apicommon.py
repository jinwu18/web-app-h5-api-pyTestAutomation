__author__ = 'panyongjun'
import requests


class ApiCommon:
    def __init__(self, host):
        self.host = host

    def httpget(self, url='', params=[]):
        return requests.get(self.host + url, params)

    def httppost(self, url='', json={}):
        return requests.post(self.host + url, json)
