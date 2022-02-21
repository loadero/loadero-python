"""Group resource tests"""

from loadero_python.resources import group
from loadero_python.api_client.api_client import ApiClient


def test_group_params():
    gp = group.GroupParams(count=4)
    assert gp.count == 4

    gp.in_project(5)
    assert gp.project_id == 5


def test_group():
    api = ApiClient()
    gp = group.GroupParams(count=4)

    g = group.Group(params=gp)

    g.read(api)
