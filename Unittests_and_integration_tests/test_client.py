#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock, PropertyMock
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

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        """ Test GithubOrgClient._public_repos_url method """

        """ Create a mock response """
        mock_get_json.return_value = [{"name": "google"}, {"name": "abc"}]

        """ Test that GithubOrgClient._public_repos_url returns
            the correct value """
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client._public_repos_url,
                        "https://api.github.com/orgs/google/repos")

    
    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos(self, mock_public_repos_url):
        """ Test GithubOrgClient.public_repos method """

        """ Create a mock response """
        mock_public_repos_url.return_value = (
            "https://api.github.com/orgs/google/repos"
            )

        """ Test that GithubOrgClient.public_repos returns the 
            correct value """
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client._public_repos_url,
                        "https://api.github.com/orgs/google/repos")
