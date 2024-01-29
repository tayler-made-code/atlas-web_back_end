#!/usr/bin/env python3

""" Unittests for utils.py """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access_nested_map function with exception """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """ Class for testing get_json function """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get json function """

        """ create a mock response object with a json method """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get') as mock_get:
            
            """ patch requests.get to return our mock response """
            mock_get.return_value = mock_response

            """ Call the function under test """
            result = get_json(test_url)

            """ Assert that the mock was called with the right arguments """
            mock_get.assert_called_once_with(test_url)

            """ Assert that the function returned the expected result """
            self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """ Class for testing memoize function """

    def test_memoize(self):
        """ Test memoize function """

        class TestClass:
            """ Test class """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test = TestClass()
        test.a_property
        test.a_property

        self.assertEqual(test.a_property, 42)
