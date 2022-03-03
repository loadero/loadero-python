"""Group resource tests"""

from datetime import datetime
from loadero_python.resources import group
from loadero_python.api_client import APIClient


time_now = datetime.now()


class TestGroupParams:
    """Group parameters tests"""

    def test_created(self):
        g = group.GroupParams()
        g.__dict__["_created"] = time_now
        assert g.created == time_now

    def test_updated(self):
        g = group.GroupParams()
        g.__dict__["_updated"] = time_now
        assert g.updated == time_now

    def test_participant_count(self):
        g = group.GroupParams()
        g.__dict__["_participant_count"] = 3
        assert g.participant_count == 3

    def test_total_cu_count(self):
        g = group.GroupParams()
        g.__dict__["_total_cu_count"] = 4
        assert g.total_cu_count == 4

    def test_project_id(self):
        g = group.GroupParams()
        g.__dict__["_project_id_path"] = 5
        assert g.project_id == 5

    def test_test_id(self):
        g = group.GroupParams()
        g.__dict__["_test_id_path"] = 6
        assert g.test_id == 6

    def test_builder_id(self):
        g = group.GroupParams()
        g.with_id(5)
        assert g.group_id == 5

    def test_builder_name(self):
        g = group.GroupParams()
        g.with_name("group")
        assert g.name == "group"

    def test_builder_count(self):
        g = group.GroupParams()
        g.with_count(5)
        assert g.count == 5

    def test_builder_project_id(self):
        g = group.GroupParams()
        g.in_project(5)
        assert g.project_id == 5

    def test_builder_test_id(self):
        g = group.GroupParams()
        g.in_test(5)
        assert g.test_id == 5


def test_group_params():
    gp = group.GroupParams(count=4)
    assert gp.count == 4

    gp.in_project(5)
    assert gp.project_id == 5


def test_group():
    api = APIClient()
    gp = group.GroupParams(count=4)

    g = group.Group(params=gp)

    g.read(api)
