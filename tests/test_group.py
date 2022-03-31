"""Group resource tests"""

from datetime import datetime
import pytest
from loadero_python.resources import group
from loadero_python.api_client import APIClient


time_now = datetime.now()

# pylint: disable=W0613


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
        g.__dict__["_project_id"] = 5
        assert g.project_id == 5

    def test_test_id(self):
        g = group.GroupParams()
        g.__dict__["_test_id"] = 6
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

    def test_builder_test_id(self):
        g = group.GroupParams()
        g.in_test(5)
        assert g.test_id == 5


class TestGroupAPI:
    """Group API tests"""

    test_id = 77

    @pytest.fixture
    def api_client(self):
        APIClient(
            2,
            "ede7b9e3154e7f8bf6f412db59de9744be6f99e9e529c156",
            "http://localhost:9080/v2/",
        )

    def test_create(self, api_client):
        ret = group.GroupAPI.create(
            group.GroupParams(
                name="pytest_group", count=8, test_id=self.test_id
            )
        )

        assert ret.name == "pytest_group"
        assert ret.count == 8
        assert ret.test_id == self.test_id
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.group_id is not None
        assert ret.created is not None
        assert ret.updated is not None

        group.GroupAPI.delete(ret)

    def test_read(self, api_client):
        gid = group.GroupAPI.create(
            group.GroupParams(
                name="pytest_group", count=8, test_id=self.test_id
            )
        ).group_id

        ret = group.GroupAPI.read(
            group.GroupParams(
                name="pytest_group", count=8, test_id=self.test_id, group_id=gid
            )
        )

        assert ret.name == "pytest_group"
        assert ret.count == 8
        assert ret.test_id == self.test_id
        assert ret.group_id == gid
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created is not None
        assert ret.updated is not None

        group.GroupAPI.delete(ret)

    def test_update(self, api_client):
        gid = group.GroupAPI.create(
            group.GroupParams(
                name="pytest_group", count=8, test_id=self.test_id
            )
        ).group_id

        ret = group.GroupAPI.update(
            group.GroupParams(
                group_id=gid,
                test_id=self.test_id,
                name="updated pytest group name",
                count=1,
            )
        )

        assert ret.name == "updated pytest group name"
        assert ret.count == 1
        assert ret.test_id == self.test_id
        assert ret.group_id == gid
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created is not None
        assert ret.updated is not None

        group.GroupAPI.delete(ret)

    def test_delete(self, api_client):
        gid = group.GroupAPI.create(
            group.GroupParams(
                name="pytest_group", count=8, test_id=self.test_id
            )
        ).group_id

        ret = group.GroupAPI.delete(
            group.GroupParams(test_id=self.test_id, group_id=gid)
        )

        assert ret is None

    def test_duplicate(self, api_client):
        gid = group.GroupAPI.create(
            group.GroupParams(
                name="pytest_group", count=8, test_id=self.test_id
            )
        ).group_id

        ret = group.GroupAPI.duplicate(
            group.GroupParams(
                group_id=gid,
                test_id=self.test_id,
                name="duplicate pytest group name",
            )
        )

        assert ret.name == "duplicate pytest group name"
        assert ret.count == 8
        assert ret.test_id == self.test_id
        assert ret.group_id > gid
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created is not None
        assert ret.updated is not None

        group.GroupAPI.delete(
            group.GroupParams(test_id=self.test_id, group_id=gid)
        )
        group.GroupAPI.delete(ret)


def test_group_params():
    gp = group.GroupParams(count=4)
    assert gp.count == 4

    gp.in_test(5)
    assert gp.test_id == 5
