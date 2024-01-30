#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
import client


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
        github_org_client = GithubOrgClient(test_org_name)

        """ Test that GithubOrgClient.org returns the correct value """
        github_org_client.org()

        """ Test that get_json was called once """
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(test_org_name)
        )
