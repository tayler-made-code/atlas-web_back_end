#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        """ Test GithubOrgClient.org method """

        """ Create a mock response """
        mock_response = Mock()
        mock_response.json.return_value = {'login': org}

        """ patch get_json to return mock response """
        mock_get_json.return_value = mock_response

        """ create an instance of GithubOrgClient """
        github_client = GithubOrgClient()
