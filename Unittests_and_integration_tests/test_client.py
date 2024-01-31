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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test GithubOrgClient.public_repos """

        """ Define the mocked return values for
            get_json and _public_repos_url """
        mock_repos_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = mock_repos_payload
        mock_public_repos_url = 'http://mocked.url/repos'

        """ Use patch as a context manager to mock
            GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = mock_public_repos_url

            """ Instantiate the GithubOrgClient """
            github_org_client = GithubOrgClient("some_org")

            """ Get the public repositories """
            public_repos = github_org_client.public_repos()

            """ Check that the list of repos matches the mocked payload """
            self.assertEqual(public_repos,
                             [repo['name'] for repo in mock_repos_payload])

            """ Check that the mocked property and get_json
                were called once """
            mock_repo_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_public_repos_url)