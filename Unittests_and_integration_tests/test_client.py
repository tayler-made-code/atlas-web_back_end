#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
        self.assertEqual(
            github_org_client._public_repos_url,
            "https://api.github.com/orgs/google/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test GithubOrgClient.public_repos """

        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]

        """ Test that GithubOrgClient.public_repos returns the
            correct value """
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "www.yes.com"
            test_class = GithubOrgClient("test")
            result = test_class.public_repos()
            self.assertEqual(result, ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    """ Test GithubOrgClient.public_repos with the
        side_effect """
    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)

@parameterized_class(["org_payload", "repos_payload", "expected_repos", "apache2_repos"], [
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define the side effects for the mocked requests.get call
        cls.mock_get.side_effect = [
            Mock(status_code=200, json=lambda: cls.org_payload),
            Mock(status_code=200, json=lambda: cls.repos_payload),
            Mock(status_code=200, json=lambda: cls.apache2_repos)
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        github_org_client = GithubOrgClient("test_org")
        repos = github_org_client.public_repos()
        self.assertEqual(repos, self.expected_repos)
