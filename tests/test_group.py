"""Group resource tests"""

# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=wildcard-import


from datetime import datetime
import os
import json
import re
import pytest
import httpretty
from loadero_python.resources.script import Script
from loadero_python.resources.test import TestParams, TestAPI
from loadero_python.api_client import APIClient
from loadero_python.resources.group import *
from .utils import *


access_token = os.environ.get("ACCESS_TOKEN", default="LOADERO_ACCESS_TOKEN")
api_base = os.environ.get("API_BASE", default="http://mock.loadero.api/v2/")
mock_api = os.environ.get("MOCK_API", default="true") == "true"
project_id = int(os.environ.get("PROJECT_ID", default="45"))


time_now = datetime.now()

sample_group_json = {
    "count": 8,
    "created": "2022-04-01T13:54:25.689Z",
    "id": 35,
    "name": "pytest_group",
    "test_id": 0,
    "updated": "2022-04-01T13:54:25.689Z",
}


@pytest.fixture(scope="module", autouse=True)
def test_id():
    if mock_api:
        httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(project_id, access_token, api_base)

    tid = 89

    t = TestParams(
        name="pytest test",
        start_interval=1,
        participant_timeout=2,
        mode="load",
        increment_strategy="linear",
        mos_test=False,
        script=Script(content="pytest test script"),
    )

    if not mock_api:
        TestAPI.create(t)
        tid = t.test_id

    sample_group_json["test_id"] = tid

    yield tid

    if mock_api:
        return

    TestAPI.delete(t)


@pytest.fixture
def mock():
    if not mock_api:
        return

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


def test_params_str():
    g = GroupParams()

    dupl = sample_group_json.copy()
    dupl["test_id"] = 10

    g.from_json(dupl)

    assert (
        str(g)
        == """|---------|----------------------------------|
| count   | 8                                |
| created | 2022-04-01 13:54:25.689000+00:00 |
| id      | 35                               |
| name    | pytest_group                     |
| test_id | 10                               |
| updated | 2022-04-01 13:54:25.689000+00:00 |"""
    )


def test_params_created():
    g = GroupParams()
    g.__dict__["_created"] = time_now
    assert g.created == time_now


def test_params_updated():
    g = GroupParams()
    g.__dict__["_updated"] = time_now
    assert g.updated == time_now


def test_params_participant_count():
    g = GroupParams()
    g.__dict__["_participant_count"] = 3
    assert g.participant_count == 3


def test_params_total_cu_count():
    g = GroupParams()
    g.__dict__["_total_cu_count"] = 4
    assert g.total_cu_count == 4


def test_params_project_id():
    g = GroupParams()
    g.__dict__["_project_id"] = 5
    assert g.project_id == 5


def test_params_test_id():
    g = GroupParams()
    g.__dict__["test_id"] = 6
    assert g.test_id == 6


def test_params_builder_id():
    g = GroupParams()
    g.with_id(5)
    assert g.group_id == 5


def test_params_builder_name():
    g = GroupParams()
    g.with_name("group")
    assert g.name == "group"


def test_params_builder_count():
    g = GroupParams()
    g.with_count(5)
    assert g.count == 5


def test_params_builder_test_id():
    g = GroupParams()
    g.in_test(5)
    assert g.test_id == 5


def test_create(mock, test_id, pause):
    g = Group(params=GroupParams(name="pytest_group", count=8, test_id=test_id))

    g.create()

    assert g.params.name == "pytest_group"
    assert g.params.count == 8
    assert g.params.test_id == test_id
    assert g.params.participant_count is None  # omit empty
    assert g.params.total_cu_count is None  # omit empty
    assert g.params.group_id is not None
    assert g.params.created is not None
    assert g.params.updated is not None

    g.delete()


def test_read(mock, test_id, pause):
    g = Group(params=GroupParams(name="pytest_group", count=8, test_id=test_id))

    g.create()

    rg = Group(
        group_id=g.params.group_id,
        test_id=g.params.test_id,
    )

    rg.read()

    assert rg.params.name == "pytest_group"
    assert rg.params.count == 8
    assert rg.params.test_id == test_id
    assert rg.params.participant_count is None  # omit empty
    assert rg.params.total_cu_count is None  # omit empty
    assert rg.params.group_id is not None
    assert rg.params.created is not None
    assert rg.params.updated is not None

    rg.delete()


def test_update(mock, test_id, pause):
    g = Group(params=GroupParams(name="pytest_group", count=8, test_id=test_id))

    g.create()

    gid = g.params.group_id

    g.params.count = 1
    g.params.name = "updated pytest group name"

    g.update()

    assert g.params.name == "updated pytest group name"
    assert g.params.count == 1
    assert g.params.test_id == test_id
    assert g.params.group_id == gid
    assert g.params.participant_count is None  # omit empty
    assert g.params.total_cu_count is None  # omit empty
    assert g.params.created is not None
    assert g.params.updated is not None

    g.delete()


def test_delete(mock, test_id):
    g = Group(params=GroupParams(name="pytest_group", count=8, test_id=test_id))

    g.create()

    g.delete()

    assert g.params.name == "pytest_group"
    assert g.params.count == 8
    assert g.params.test_id == test_id
    assert g.params.participant_count is None  # omit empty
    assert g.params.total_cu_count is None  # omit empty
    assert g.params.group_id is not None
    assert g.params.created is not None
    assert g.params.updated is not None


def test_duplicate(mock, test_id, pause):
    g = Group(params=GroupParams(name="pytest_group", count=8, test_id=test_id))

    g.create()

    gid = g.params.group_id

    dupl = g.duplicate("duplicate pytest group name")

    assert g.params.name == "pytest_group"
    assert g.params.count == 8
    assert g.params.test_id == test_id
    assert g.params.participant_count is None  # omit empty
    assert g.params.total_cu_count is None  # omit empty
    assert g.params.group_id is not None
    assert g.params.created is not None
    assert g.params.updated is not None

    assert dupl.params.name == "duplicate pytest group name"
    assert dupl.params.count == 8
    assert dupl.params.test_id == test_id
    assert dupl.params.group_id > gid
    assert dupl.params.participant_count is None  # omit empty
    assert dupl.params.total_cu_count is None  # omit empty
    assert dupl.params.created is not None
    assert dupl.params.updated is not None

    g.delete()
    dupl.delete()


def test_api_create(mock, test_id, pause):
    ret = GroupAPI.create(
        GroupParams(name="pytest_group", count=8, test_id=test_id)
    )

    assert ret.name == "pytest_group"
    assert ret.count == 8
    assert ret.test_id == test_id
    assert ret.participant_count is None  # omit empty
    assert ret.total_cu_count is None  # omit empty
    assert ret.group_id is not None
    assert ret.created is not None
    assert ret.updated is not None

    GroupAPI.delete(ret)


def test_api_create_invalid_params():
    with pytest.raises(Exception):
        GroupAPI.create(GroupParams(name="pytest_group", count=8))


def test_api_read(mock, test_id, pause):
    gid = GroupAPI.create(
        GroupParams(name="pytest_group", count=8, test_id=test_id)
    ).group_id

    ret = GroupAPI.read(
        GroupParams(name="pytest_group", count=8, test_id=test_id, group_id=gid)
    )

    assert ret.name == "pytest_group"
    assert ret.count == 8
    assert ret.test_id == test_id
    assert ret.group_id == gid
    assert ret.participant_count is None  # omit empty
    assert ret.total_cu_count is None  # omit empty
    assert ret.created is not None
    assert ret.updated is not None

    GroupAPI.delete(ret)


def test_api_read_invalid_params():
    with pytest.raises(Exception):
        GroupAPI.read(
            GroupParams(name="pytest_group", count=8, test_id=test_id)
        )

    with pytest.raises(Exception):
        GroupAPI.read(GroupParams(name="pytest_group", count=8, group_id=1))


def test_api_update(mock, test_id, pause):
    gid = GroupAPI.create(
        GroupParams(name="pytest_group", count=8, test_id=test_id)
    ).group_id

    ret = GroupAPI.update(
        GroupParams(
            group_id=gid,
            test_id=test_id,
            name="updated pytest group name",
            count=1,
        )
    )

    assert ret.name == "updated pytest group name"
    assert ret.count == 1
    assert ret.test_id == test_id
    assert ret.group_id == gid
    assert ret.participant_count is None  # omit empty
    assert ret.total_cu_count is None  # omit empty
    assert ret.created is not None
    assert ret.updated is not None

    GroupAPI.delete(ret)


def test_api_update_invalid_params():
    with pytest.raises(Exception):
        GroupAPI.update(
            GroupParams(name="pytest_group", count=8, test_id=test_id)
        )

    with pytest.raises(Exception):
        GroupAPI.update(GroupParams(name="pytest_group", count=8, group_id=1))


def test_api_delete(mock, test_id, pause):
    gid = GroupAPI.create(
        GroupParams(name="pytest_group", count=8, test_id=test_id)
    ).group_id

    ret = GroupAPI.delete(GroupParams(test_id=test_id, group_id=gid))

    assert ret is None


def test_api_delete_invalid_params():
    with pytest.raises(Exception):
        GroupAPI.delete(
            GroupParams(name="pytest_group", count=8, test_id=test_id)
        )

    with pytest.raises(Exception):
        GroupAPI.delete(GroupParams(name="pytest_group", count=8, group_id=1))


def test_api_duplicate(mock, test_id, pause):
    gid = GroupAPI.create(
        GroupParams(name="pytest_group", count=8, test_id=test_id)
    ).group_id

    ret = GroupAPI.duplicate(
        GroupParams(
            group_id=gid,
            test_id=test_id,
            name="duplicate pytest group name",
        )
    )

    assert ret.name == "duplicate pytest group name"
    assert ret.count == 8
    assert ret.test_id == test_id
    assert ret.group_id > gid
    assert ret.participant_count is None  # omit empty
    assert ret.total_cu_count is None  # omit empty
    assert ret.created is not None
    assert ret.updated is not None

    GroupAPI.delete(GroupParams(test_id=test_id, group_id=gid))
    GroupAPI.delete(ret)


def test_api_duplicate_invalid_params():
    with pytest.raises(Exception):
        GroupAPI.duplicate(
            GroupParams(name="pytest_group", count=8, test_id=test_id)
        )

    with pytest.raises(Exception):
        GroupAPI.duplicate(
            GroupParams(name="pytest_group", count=8, group_id=1)
        )


def test_api_read_all():
    GroupAPI.read_all(5)
