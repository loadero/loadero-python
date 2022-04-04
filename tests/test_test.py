"""Test resource tests"""


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
from loadero_python.api_client import APIClient
from loadero_python.resources.script import Script
from loadero_python.resources.test import *
from .utils import *
from .test_script import sample_json as sample_file_json


access_token = os.environ.get("ACCESS_TOKEN", default="LOADERO_ACCESS_TOKEN")
api_base = os.environ.get("API_BASE", default="http://mock.loadero.api/v2/")
mock_api = os.environ.get("MOCK_API", default="true") == "true"
project_id = int(os.environ.get("PROJECT_ID", default="45"))


time_now = datetime.now()

sample_script = Script(content="pytest test script")

sample_json = {
    "created": "2022-04-04T05:18:02.102Z",
    "id": 61,
    "increment_strategy": "linear",
    "mode": "load",
    "name": "pytest test",
    "participant_timeout": 13,
    "project_id": 0,  # set by ids fixture
    "script_file_id": 65,
    "start_interval": 12,
    "updated": "2022-04-04T05:18:02.102Z",
}


@pytest.fixture(scope="module", autouse=True)
def ids():
    if mock_api:
        httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(project_id, access_token, api_base)

    idso = IDs()

    idso.project_id = project_id

    yield idso


@pytest.fixture
def mock():
    if not mock_api:
        return

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/$"),
        body=json.dumps(sample_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/$"),
        body=json.dumps(sample_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    upd = sample_json.copy()
    upd["name"] = "updated pytest name"
    upd["start_interval"] = 45
    upd["participant_timeout"] = 94
    upd["mode"] = "performance"
    upd["increment_strategy"] = "random"
    upd["mos_test"] = True

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/$"),
        body=json.dumps(upd),
        forcing_headers={"Content-Type": "application/json"},
    )

    # delete
    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/" r"projects/\d*/tests/\d*/$"
        ),
    )

    dupl = sample_json.copy()
    dupl["id"] += 1
    dupl["name"] = "pytest duplicate test"

    # duplicate
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/copy/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read file
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/\d*/$"),
        body=json.dumps(sample_file_json),
        forcing_headers={"Content-Type": "application/json"},
    )


def test_params_string():
    dupl = sample_json.copy()
    dupl["project_id"] = 81

    t = TestParams()
    t.from_json(dupl)

    assert (
        str(t)
        == """|---------------------|----------------------------------|
| created             | 2022-04-04 05:18:02.102000+00:00 |
| id                  | 61                               |
| increment_strategy  | linear                           |
| mode                | load                             |
| mos_test            |                                  |
| name                | pytest test                      |
| participant_timeout | 13                               |
| project_id          | 81                               |
| script              |                                  |
| script_file_id      | 65                               |
| start_interval      | 12                               |
| updated             | 2022-04-04 05:18:02.102000+00:00 |"""
    )


def test_params_created():
    t = TestParams()
    t.__dict__["_created"] = time_now
    assert t.created == time_now


def test_params_updated():
    t = TestParams()
    t.__dict__["_updated"] = time_now
    assert t.updated == time_now


def test_params_group_count():
    t = TestParams()
    t.__dict__["_group_count"] = 5
    assert t.group_count == 5


def test_params_participant_count():
    t = TestParams()
    t.__dict__["_participant_count"] = 5
    assert t.participant_count == 5


def test_params_deleted():
    t = TestParams()
    t.__dict__["_deleted"] = True

    assert t.deleted is True


def test_params_project_id():
    t = TestParams()
    t.__dict__["_project_id"] = 5
    assert t.project_id == 5


def test_params_builder_id():
    t = TestParams()
    t.with_id(5)
    assert t.test_id == 5


def test_params_builder_name():
    t = TestParams()
    t.with_name("test")
    assert t.name == "test"


def test_params_builder_start_interval():
    t = TestParams()
    t.with_start_interval(5)
    assert t.start_interval == 5


def test_params_builder_participant_timeout():
    t = TestParams()
    t.with_participant_timeout(5)
    assert t.participant_timeout == 5


def test_params_builder_mode():
    t = TestParams()
    t.with_mode("load")
    assert t.mode == "load"


def test_params_builder_increment_strategy():
    t = TestParams()
    t.with_increment_strategy("linear")
    assert t.increment_strategy == "linear"


def test_params_builder_mos_test():
    t = TestParams()
    t.with_mos_test(True)
    assert t.mos_test is True


def test_params_builder_script():
    t = TestParams()
    t.with_script(Script(content="hello"))
    assert t.script.content == "hello"


def test_create(mock, ids, pause):
    t = Test(
        params=TestParams(
            name="pytest test",
            start_interval=12,
            participant_timeout=13,
            mode="load",
            increment_strategy="linear",
            mos_test=False,
            script=sample_script,
        )
    )

    t.create()

    assert t.params.test_id is not None
    assert t.params.name == "pytest test"
    assert t.params.start_interval == 12
    assert t.params.participant_timeout == 13
    assert t.params.mode == "load"
    assert t.params.increment_strategy == "linear"
    assert t.params.script.content == "pytest test script"
    assert t.params.created is not None
    assert t.params.updated is not None
    assert t.params.group_count is None
    assert t.params.participant_count is None

    t.delete()


def test_read(mock, ids, pause):
    tid = (
        TestAPI()
        .create(
            TestParams(
                name="pytest test",
                start_interval=12,
                participant_timeout=13,
                mode="load",
                increment_strategy="linear",
                mos_test=False,
                script=sample_script,
            )
        )
        .test_id
    )

    t = Test(test_id=tid)

    t.read()

    assert t.params.test_id is not None
    assert t.params.name == "pytest test"
    assert t.params.start_interval == 12
    assert t.params.participant_timeout == 13
    assert t.params.mode == "load"
    assert t.params.increment_strategy == "linear"
    assert t.params.script.content == "pytest test script"
    assert t.params.created is not None
    assert t.params.updated is not None
    assert t.params.group_count is None
    assert t.params.participant_count is None

    t.delete()


def test_update(mock, ids, pause):
    tid = (
        TestAPI()
        .create(
            TestParams(
                name="pytest test",
                start_interval=12,
                participant_timeout=13,
                mode="load",
                increment_strategy="linear",
                mos_test=False,
                script=sample_script,
            )
        )
        .test_id
    )

    t = Test(
        params=TestParams(
            test_id=tid,
            name="updated pytest name",
            start_interval=45,
            participant_timeout=94,
            mode="performance",
            increment_strategy="random",
            script=Script(content="updated test script"),
            mos_test=True,
        )
    )

    t.update()

    assert t.params.test_id == tid
    assert t.params.name == "updated pytest name"
    assert t.params.start_interval == 45
    assert t.params.participant_timeout == 94
    assert t.params.mode == "performance"
    assert t.params.increment_strategy == "random"
    assert t.params.script.content == "updated test script"
    assert t.params.created is not None
    assert t.params.updated is not None
    assert t.params.group_count is None
    assert t.params.participant_count is None
    # assert ret.mos_test is True it will be

    t.delete()


def test_delete(mock, ids, pause):
    tid = (
        TestAPI()
        .create(
            TestParams(
                name="pytest test",
                start_interval=12,
                participant_timeout=13,
                mode="load",
                increment_strategy="linear",
                mos_test=False,
                script=sample_script,
            )
        )
        .test_id
    )

    t = Test(test_id=tid)

    t.delete()

    assert t.params.test_id == tid
    assert t.params.deleted is True


def test_duplicate(mock, ids, pause):
    tid = (
        TestAPI()
        .create(
            TestParams(
                name="pytest test",
                start_interval=12,
                participant_timeout=13,
                mode="load",
                increment_strategy="linear",
                mos_test=False,
                script=sample_script,
            )
        )
        .test_id
    )

    print(tid)

    t = Test(test_id=tid)

    dupl = t.duplicate("pytest duplicate test")

    assert dupl.params.test_id > tid
    assert dupl.params.name == "pytest duplicate test"
    assert dupl.params.start_interval == 12
    assert dupl.params.participant_timeout == 13
    assert dupl.params.mode == "load"
    assert dupl.params.increment_strategy == "linear"
    assert dupl.params.script.content == "pytest test script"
    assert dupl.params.created is not None
    assert dupl.params.updated is not None
    assert dupl.params.group_count is None
    assert dupl.params.participant_count is None
    assert dupl.params.deleted is None

    t.delete()
    TestAPI().delete(TestParams(test_id=tid))


def test_api_create(mock, ids, pause):
    ret = TestAPI().create(
        TestParams(
            name="pytest test",
            start_interval=12,
            participant_timeout=13,
            mode="load",
            increment_strategy="linear",
            mos_test=False,
            script=sample_script,
        )
    )

    assert ret.test_id is not None
    assert ret.name == "pytest test"
    assert ret.start_interval == 12
    assert ret.participant_timeout == 13
    assert ret.mode == "load"
    assert ret.increment_strategy == "linear"
    assert ret.script.content == "pytest test script"
    assert ret.created is not None
    assert ret.updated is not None
    assert ret.group_count is None
    assert ret.participant_count is None

    TestAPI().delete(ret)


def test_api_read(mock, ids, pause):
    tid = (
        TestAPI()
        .create(
            TestParams(
                name="pytest test",
                start_interval=12,
                participant_timeout=13,
                mode="load",
                increment_strategy="linear",
                mos_test=False,
                script=sample_script,
            )
        )
        .test_id
    )

    ret = TestAPI().read(TestParams(test_id=tid))

    assert ret.test_id == tid
    assert ret.name == "pytest test"
    assert ret.start_interval == 12
    assert ret.participant_timeout == 13
    assert ret.mode == "load"
    assert ret.increment_strategy == "linear"
    assert ret.script.content == "pytest test script"
    assert ret.created is not None
    assert ret.updated is not None
    assert ret.group_count is None
    assert ret.participant_count is None
    assert ret.deleted is None

    TestAPI().delete(ret)


def test_api_read_invalid_params():
    with pytest.raises(Exception):
        TestAPI.read(TestParams())


def test_api_update(mock, ids, pause):
    tid = (
        TestAPI()
        .create(
            TestParams(
                name="pytest test",
                start_interval=12,
                participant_timeout=13,
                mode="load",
                increment_strategy="linear",
                mos_test=False,
                script=sample_script,
            )
        )
        .test_id
    )

    ret = TestAPI().update(
        TestParams(
            test_id=tid,
            name="updated pytest name",
            start_interval=45,
            participant_timeout=94,
            mode="performance",
            increment_strategy="random",
            script=Script(content="updated test script"),
            mos_test=True,
        )
    )

    assert ret.test_id == tid
    assert ret.name == "updated pytest name"
    assert ret.start_interval == 45
    assert ret.participant_timeout == 94
    assert ret.mode == "performance"
    # assert ret.mos_test is True it will be
    assert ret.increment_strategy == "random"
    assert ret.script.content == "updated test script"
    assert ret.created is not None
    assert ret.updated is not None
    assert ret.group_count is None
    assert ret.participant_count is None

    TestAPI().delete(ret)


def test_api_update_invalid_params():
    with pytest.raises(Exception):
        TestAPI.update(TestParams())


def test_api_delete(mock, ids, pause):
    tid = (
        TestAPI()
        .create(
            TestParams(
                name="pytest test",
                start_interval=12,
                participant_timeout=13,
                mode="load",
                increment_strategy="linear",
                mos_test=False,
                script=sample_script,
            )
        )
        .test_id
    )

    ret = TestAPI().delete(TestParams(test_id=tid))

    assert ret.test_id == tid
    assert ret.deleted is True


def test_api_delete_invalid_params():
    with pytest.raises(Exception):
        TestAPI.delete(TestParams())


def test_api_duplicate(mock, ids, pause):
    tid = (
        TestAPI()
        .create(
            TestParams(
                name="pytest test",
                start_interval=12,
                participant_timeout=13,
                mode="load",
                increment_strategy="linear",
                mos_test=False,
                script=sample_script,
            )
        )
        .test_id
    )

    ret = TestAPI().duplicate(
        TestParams(test_id=tid, name="pytest duplicate test")
    )

    assert ret.test_id > tid
    assert ret.name == "pytest duplicate test"
    assert ret.start_interval == 12
    assert ret.participant_timeout == 13
    assert ret.mode == "load"
    assert ret.increment_strategy == "linear"
    assert ret.script.content == "pytest test script"
    assert ret.created is not None
    assert ret.updated is not None
    assert ret.group_count is None
    assert ret.participant_count is None
    assert ret.deleted is None

    TestAPI().delete(ret)
    TestAPI().delete(TestParams(test_id=tid))


def test_api_duplicate_invalid_params():
    with pytest.raises(Exception):
        TestAPI.duplicate(TestParams())


def test_api_read_all():
    TestAPI().read_all()
