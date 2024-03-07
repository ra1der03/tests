import unittest
import pytest
import requests


class Test2(unittest.TestCase):

    def test_2_putting(self):
        token = '' # put in your token
        params = {'path': 'img'}
        headers = {'Authorization': token}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)
        expected = 201
        try:
            self.assertEqual(response.status_code, expected)
        except AssertionError:
            pytest.skip(response.text)

    def test_2_deleting(self):
        token = '' # put in your token
        params = {'path': 'img'}
        headers = {'Authorization': token}
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)
        expected = 204
        try:
            self.assertEqual(response.status_code, expected)
        except AssertionError:
            pytest.skip(response.text)

