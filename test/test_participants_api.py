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
from swagger_client.api.participants_api import ParticipantsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestParticipantsApi(unittest.TestCase):
    """ParticipantsApi unit test stubs"""

    def setUp(self):
        self.api = ParticipantsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_participant(self):
        """Test case for create_participant

        Create new participant.  # noqa: E501
        """
        pass

    def test_delete_participant(self):
        """Test case for delete_participant

        Delete existing participant.  # noqa: E501
        """
        pass

    def test_duplicate_participant(self):
        """Test case for duplicate_participant

        Duplicate existing participant  # noqa: E501
        """
        pass

    def test_read_all_participants(self):
        """Test case for read_all_participants

        Get all existing participants for test.  # noqa: E501
        """
        pass

    def test_read_participant(self):
        """Test case for read_participant

        Get existing participant.  # noqa: E501
        """
        pass

    def test_update_participant(self):
        """Test case for update_participant

        Update existing participant.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
