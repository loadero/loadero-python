"""Group resource tests"""

# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=wildcard-import
# pylint: disable=missing-class-docstring


import json
import re
import pytest
import httpretty
from dateutil import parser
from loadero_python.api_client import APIClient
from loadero_python.resources.group import *
from . import identifiers


created_time = parser.parse("2022-04-01T13:54:25.689Z")
updated_time = parser.parse("2024-02-03T15:42:54.689Z")


sample_group_json = {
    "count": 8,
    "created": "2022-04-01T13:54:25.689Z",
    "id": identifiers.group_id,
    "name": "pytest_group",
    "test_id": identifiers.test_id,
    "updated": "2024-02-03T15:42:54.689Z",
}


@pytest.fixture
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(
        identifiers.project_id, identifiers.access_token, identifiers.api_base
    )

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(sample_group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
        body=json.dumps(sample_group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    upd = sample_group_json.copy()
    upd["count"] = 1
    upd["name"] = "updated pytest group name"

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
        body=json.dumps(upd),
        forcing_headers={"Content-Type": "application/json"},
    )

    # delete
    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
    )

    dupl = sample_group_json.copy()
    dupl["id"] += 1
    dupl["name"] = "duplicate pytest group name"

    # duplicate
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/groups/\d*/copy/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )


class TestGroupParams:
    def test_str(self):
        g = GroupParams()
        dupl = sample_group_json.copy()
        g.from_json(dupl)

        assert (
            str(g)
            == """|---------|----------------------------------|
| count   | 8                                |
| created | 2022-04-01 13:54:25.689000+00:00 |
| id      | 34421                            |
| name    | pytest_group                     |
| test_id | 12734                            |
| updated | 2024-02-03 15:42:54.689000+00:00 |"""
        )

    def test_created(self):
        g = GroupParams()
        g.__dict__["_created"] = created_time
        assert g.created == created_time

    def test_updated(self):
        g = GroupParams()
        g.__dict__["_updated"] = updated_time
        assert g.updated == updated_time

    def test_participant_count(self):
        g = GroupParams()
        g.__dict__["_participant_count"] = 3
        assert g.participant_count == 3

    def test_total_cu_count(self):
        g = GroupParams()
        g.__dict__["_total_cu_count"] = 4
        assert g.total_cu_count == 4

    def test_builder_id(self):
        g = GroupParams()
        g.with_id(5)
        assert g.group_id == 5

    def test_builder_name(self):
        g = GroupParams()
        g.with_name("group")
        assert g.name == "group"

    def test_builder_count(self):
        g = GroupParams()
        g.with_count(5)
        assert g.count == 5

    def test_builder_test_id(self):
        g = GroupParams()
        g.in_test(5)
        assert g.test_id == 5


class TestGroup:
    def test_create(self, mock):
        g = Group(
            params=GroupParams(
                name="pytest_group", count=8, test_id=identifiers.test_id
            )
        )

        g.create()

        assert g.params.test_id == identifiers.test_id
        assert g.params.group_id == identifiers.group_id
        assert g.params.created == created_time
        assert g.params.updated == updated_time
        assert g.params.name == "pytest_group"
        assert g.params.count == 8
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty

        assert httpretty.last_request().parsed_body == {
            "count": 8,
            "name": "pytest_group",
        }

    def test_read(self, mock):
        g = Group(group_id=identifiers.group_id, test_id=identifiers.test_id)

        g.read()

        assert g.params.test_id == identifiers.test_id
        assert g.params.group_id == identifiers.group_id
        assert g.params.created == created_time
        assert g.params.updated == updated_time
        assert g.params.name == "pytest_group"
        assert g.params.count == 8
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty

        assert httpretty.last_request().parsed_body == ""

    def test_update(self, mock):
        g = Group(
            params=GroupParams(
                group_id=identifiers.group_id, test_id=identifiers.test_id
            )
        )

        g.params.count = 1
        g.params.name = "updated pytest group name"

        g.update()

        assert g.params.test_id == identifiers.test_id
        assert g.params.group_id == identifiers.group_id
        assert g.params.created == created_time
        assert g.params.updated == updated_time
        assert g.params.name == "updated pytest group name"
        assert g.params.count == 1
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty

        assert httpretty.last_request().parsed_body == {
            "count": 1,
            "name": "updated pytest group name",
        }

    def test_delete(self, mock):
        g = Group(
            params=GroupParams(
                group_id=identifiers.group_id, test_id=identifiers.test_id
            )
        )

        g.delete()

        assert g.params.name is None
        assert g.params.count is None
        assert g.params.test_id == identifiers.test_id
        assert g.params.group_id == identifiers.group_id
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty
        assert g.params.created is None
        assert g.params.updated is None

        assert httpretty.last_request().parsed_body == ""

    def test_duplicate(self, mock):
        g = Group(
            params=GroupParams(
                group_id=identifiers.group_id, test_id=identifiers.test_id
            )
        )

        dupl = g.duplicate("duplicate pytest group name")

        assert g.params.name is None
        assert g.params.count is None
        assert g.params.test_id == identifiers.test_id
        assert g.params.group_id == identifiers.group_id
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty
        assert g.params.created is None
        assert g.params.updated is None

        assert dupl.params.name == "duplicate pytest group name"
        assert dupl.params.count == 8
        assert dupl.params.test_id == identifiers.test_id
        assert dupl.params.group_id == identifiers.group_id + 1
        assert dupl.params.participant_count is None  # omit empty
        assert dupl.params.total_cu_count is None  # omit empty
        assert dupl.params.created is not None
        assert dupl.params.updated is not None

        assert httpretty.last_request().parsed_body == {
            "name": "duplicate pytest group name"
        }


class TestGroupAPI:
    def test_create(self, mock):
        ret = GroupAPI.create(
            GroupParams(
                name="pytest_group", count=8, test_id=identifiers.test_id
            )
        )

        assert ret.name == "pytest_group"
        assert ret.count == 8
        assert ret.test_id == identifiers.test_id
        assert ret.group_id == identifiers.group_id
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created == created_time
        assert ret.updated == updated_time

        assert httpretty.last_request().parsed_body == {
            "count": 8,
            "name": "pytest_group",
        }

    def test_create_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.create(GroupParams(name="pytest_group", count=8))

    def test_read(self, mock):
        ret = GroupAPI.read(
            GroupParams(
                test_id=identifiers.test_id,
                group_id=identifiers.group_id,
            )
        )

        assert ret.name == "pytest_group"
        assert ret.count == 8
        assert ret.test_id == identifiers.test_id
        assert ret.group_id == identifiers.group_id
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created == created_time
        assert ret.updated == updated_time

        assert httpretty.last_request().parsed_body == ""

    def test_read_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.read(
                GroupParams(
                    name="pytest_group", count=8, test_id=identifiers.test_id
                )
            )

        with pytest.raises(Exception):
            GroupAPI.read(GroupParams(name="pytest_group", count=8, group_id=1))

    def test_update(self, mock):
        ret = GroupAPI.update(
            GroupParams(
                group_id=identifiers.group_id,
                test_id=identifiers.test_id,
                name="updated pytest group name",
                count=1,
            )
        )

        assert ret.name == "updated pytest group name"
        assert ret.count == 1
        assert ret.test_id == identifiers.test_id
        assert ret.group_id == identifiers.group_id
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created == created_time
        assert ret.updated == updated_time

        assert httpretty.last_request().parsed_body == {
            "count": 1,
            "name": "updated pytest group name",
        }

    def test_update_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.update(
                GroupParams(
                    name="pytest_group", count=8, test_id=identifiers.test_id
                )
            )

        with pytest.raises(Exception):
            GroupAPI.update(
                GroupParams(name="pytest_group", count=8, group_id=1)
            )

    def test_delete(self, mock):
        ret = GroupAPI.delete(
            GroupParams(
                test_id=identifiers.test_id, group_id=identifiers.group_id
            )
        )

        assert ret is None

        assert httpretty.last_request().parsed_body == ""

    def test_delete_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.delete(
                GroupParams(
                    name="pytest_group", count=8, test_id=identifiers.test_id
                )
            )

        with pytest.raises(Exception):
            GroupAPI.delete(
                GroupParams(name="pytest_group", count=8, group_id=1)
            )

    def test_duplicate(self, mock):
        ret = GroupAPI.duplicate(
            GroupParams(
                group_id=identifiers.group_id,
                test_id=identifiers.test_id,
                name="duplicate pytest group name",
            )
        )

        assert ret.name == "duplicate pytest group name"
        assert ret.count == 8
        assert ret.test_id == identifiers.test_id
        assert ret.group_id == identifiers.group_id + 1
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created == created_time
        assert ret.updated == updated_time

        assert httpretty.last_request().parsed_body == {
            "name": "duplicate pytest group name"
        }

    def test_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.duplicate(
                GroupParams(
                    name="pytest_group", count=8, test_id=identifiers.test_id
                )
            )

        with pytest.raises(Exception):
            GroupAPI.duplicate(
                GroupParams(name="pytest_group", count=8, group_id=1)
            )

    def test_read_all(self):
        GroupAPI.read_all(5)
