"""Utility functions and types for tests"""


# pylint: disable=missing-function-docstring


import time
import os
import pytest


mock_api = os.environ.get("MOCK_API", default="true") == "true"


class IDs:
    project_id = None
    group_id = None
    test_id = None
    file_id = None


@pytest.fixture
def pause():
    if mock_api:
        return

    # Avoid rate limits when running tests on real Loadero API.
    time.sleep(0.35)
