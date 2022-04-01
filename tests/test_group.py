"""Group resource tests"""


# pylint: disable=W0613
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=wildcard-import


from datetime import datetime
import os
import json
import re
import pytest
import httpretty
from loadero_python.resources.group import *
from loadero_python.api_client import APIClient

time_now = datetime.now()


access_token = os.environ.get("ACCESS_TOKEN", default="LOADERO_ACCESS_TOKEN")
api_base = os.environ.get("API_BASE", default="http://mock.loadero.api/v2/")
mock_api = os.environ.get("MOCK_API", default="true") == "true"

project_id = int(os.environ.get("PROJECT_ID", default="45"))
test_id = int(os.environ.get("TEST_ID", default="89"))


sample_group_json = {
    "count": 8,
    "created": "2022-04-01T13:54:25.689Z",
    "id": 35,
    "name": "pytest_group",
    "test_id": test_id,
    "updated": "2022-04-01T13:54:25.689Z",
}


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


def test_params_str():
    g = GroupParams()

    g.from_json(sample_group_json)

    gstr = """|---------|----------------------------------|
| count   | 8                                |
| created | 2022-04-01 13:54:25.689000+00:00 |
| id      | 35                               |
| name    | pytest_group                     |
| test_id | 89                               |
| updated | 2022-04-01 13:54:25.689000+00:00 |"""

    assert str(g) == gstr


@pytest.fixture
def api():
    if mock_api:
        httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(project_id, access_token, api_base)


@pytest.fixture
def mock_create():
    if not mock_api:
        return

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(sample_group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
    )


def test_api_create(api, mock_create):
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


def test_create(api, mock_create):
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


@pytest.fixture
def mock_read():
    if not mock_api:
        return

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(sample_group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
        body=json.dumps(sample_group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
    )


def test_api_read(api, mock_read):
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


def test_read(api, mock_read):
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


@pytest.fixture
def mock_update():
    if not mock_api:
        return

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(sample_group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    dupl = sample_group_json.copy()

    dupl["count"] = 1
    dupl["name"] = "updated pytest group name"

    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )

    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
    )


def test_api_update(api, mock_update):
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


def test_update(api, mock_update):
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


@pytest.fixture
def mock_delete():
    if not mock_api:
        return

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(sample_group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
    )


def test_api_delete(api, mock_delete):
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


def test_delete(api, mock_delete):
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


@pytest.fixture
def mock_duplicate():
    if not mock_api:
        return

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(sample_group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    dupl = sample_group_json.copy()
    dupl["id"] += 1
    dupl["name"] = "duplicate pytest group name"

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/groups/\d*/copy/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )

    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
    )


def test_api_duplicate(api, mock_duplicate):
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


def test_duplicate(api, mock_duplicate):
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


def test_api_read_all():
    GroupAPI.read_all(5)
