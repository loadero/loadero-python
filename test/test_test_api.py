# coding: utf-8

"""
    Loadero Controller

    This application serves main Loadero's endpoints that can be used to manipulate test data and other services  # noqa: E501

    OpenAPI spec version: {{ .Version }}
    Contact: support@loadero.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.test_api import TestApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTestApi(unittest.TestCase):
    """TestApi unit test stubs"""

    def setUp(self):
        self.api = TestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_test(self):
        """Test case for create_test

        Create new test  # noqa: E501
        """
        pass

    def test_delete_test(self):
        """Test case for delete_test

        Delete existing test  # noqa: E501
        """
        pass

    def test_duplicate_test(self):
        """Test case for duplicate_test

        Duplicate existing test  # noqa: E501
        """
        pass

    def test_read_all_tests(self):
        """Test case for read_all_tests

        Get all existing tests for project  # noqa: E501
        """
        pass

    def test_read_test(self):
        """Test case for read_test

        Read test info  # noqa: E501
        """
        pass

    def test_update_test(self):
        """Test case for update_test

        Update existing test  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
