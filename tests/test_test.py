"""Test resource tests"""

from loadero_python.resources import test
from loadero_python.api_client.api_client import ApiClient


def test_test_params():
    tp = test.TestParams(start_interval=4)
    assert tp.start_interval == 4

    tp.in_project(5)
    assert tp.project_id == 5


def test_test():
    api = ApiClient()
    tp = test.TestParams(start_interval=4)

    t = test.Test(params=tp)

    t.read(api)

    assert 1 == 2
