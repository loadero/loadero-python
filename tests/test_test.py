"""Test resource tests"""


# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=wildcard-import
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.script import Script
from loadero_python.resources.test import *
from . import identifiers
from .test_script import sample_json as sample_file_json


created_time = parser.parse("2022-04-01T13:54:25.689Z")
updated_time = parser.parse("2024-02-03T15:42:54.689Z")


sample_script = Script(content="pytest test script")

sample_json = {
    "id": identifiers.test_id,
    "created": "2022-04-01T13:54:25.689Z",
    "updated": "2024-02-03T15:42:54.689Z",
    "increment_strategy": "linear",
    "mode": "load",
    "name": "pytest test",
    "participant_timeout": 13,
    "project_id": identifiers.project_id,
    "script_file_id": 65,
    "start_interval": 12,
    "group_count": 52,
    "participant_count": 9355,
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


class TestTestParams:
    def test_string(self):
        dupl = sample_json.copy()
        dupl["project_id"] = 81

        t = TestParams()
        t.from_json(dupl)

        assert (
            str(t)
            == """|---------------------|----------------------------------|
| created             | 2022-04-01 13:54:25.689000+00:00 |
| group_count         | 52                               |
| id                  | 12734                            |
| increment_strategy  | linear                           |
| mode                | load                             |
| mos_test            |                                  |
| name                | pytest test                      |
| participant_count   | 9355                             |
| participant_timeout | 13                               |
| project_id          | 81                               |
| script              |                                  |
| script_file_id      | 65                               |
| start_interval      | 12                               |
| updated             | 2024-02-03 15:42:54.689000+00:00 |"""
        )

    def test_created(self):
        t = TestParams()
        t.__dict__["_created"] = created_time
        assert t.created == created_time

    def test_updated(self):
        t = TestParams()
        t.__dict__["_updated"] = updated_time
        assert t.updated == updated_time

    def test_group_count(self):
        t = TestParams()
        t.__dict__["_group_count"] = 5
        assert t.group_count == 5

    def test_participant_count(self):
        t = TestParams()
        t.__dict__["_participant_count"] = 5
        assert t.participant_count == 5

    def test_deleted(self):
        t = TestParams()
        t.__dict__["_deleted"] = True

        assert t.deleted is True

    def test_builder_id(self):
        t = TestParams()
        t.with_id(5)
        assert t.test_id == 5

    def test_builder_name(self):
        t = TestParams()
        t.with_name("test")
        assert t.name == "test"

    def test_builder_start_interval(self):
        t = TestParams()
        t.with_start_interval(5)
        assert t.start_interval == 5

    def test_builder_participant_timeout(self):
        t = TestParams()
        t.with_participant_timeout(5)
        assert t.participant_timeout == 5

    def test_builder_mode(self):
        t = TestParams()
        t.with_mode("load")
        assert t.mode == "load"

    def test_builder_increment_strategy(self):
        t = TestParams()
        t.with_increment_strategy("linear")
        assert t.increment_strategy == "linear"

    def test_builder_mos_test(self):
        t = TestParams()
        t.with_mos_test(True)
        assert t.mos_test is True

    def test_builder_script(self):
        t = TestParams()
        t.with_script(Script(content="hello"))
        assert t.script.content == "hello"


class TestTest:
    def test_create(self, mock):
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

        assert t.params.test_id == identifiers.test_id
        assert t.params.created == created_time
        assert t.params.updated == updated_time
        assert t.params.name == "pytest test"
        assert t.params.start_interval == 12
        assert t.params.participant_timeout == 13
        assert t.params.mode == "load"
        assert t.params.increment_strategy == "linear"
        assert t.params.script.content == "pytest test script"
        assert t.params.group_count == 52
        assert t.params.participant_count == 9355
        assert t.params.deleted is None

        assert httpretty.last_request().parsed_body == {
            "increment_strategy": "linear",
            "mode": "load",
            "mos_test": False,
            "name": "pytest test",
            "participant_timeout": 13,
            "script": "pytest test script",
            "start_interval": 12,
        }

    def test_read(self, mock):
        t = Test(test_id=identifiers.test_id)

        t.read()

        assert t.params.test_id == identifiers.test_id
        assert t.params.created == created_time
        assert t.params.updated == updated_time
        assert t.params.name == "pytest test"
        assert t.params.start_interval == 12
        assert t.params.participant_timeout == 13
        assert t.params.mode == "load"
        assert t.params.increment_strategy == "linear"
        assert t.params.script.content == "pytest test script"
        assert t.params.group_count == 52
        assert t.params.participant_count == 9355
        assert t.params.deleted is None

        assert httpretty.last_request().parsed_body == ""

    def test_update(self, mock):
        t = Test(
            params=TestParams(
                test_id=identifiers.test_id,
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

        assert t.params.test_id == identifiers.test_id
        assert t.params.created == created_time
        assert t.params.updated == updated_time
        assert t.params.name == "updated pytest name"
        assert t.params.start_interval == 45
        assert t.params.participant_timeout == 94
        assert t.params.mode == "performance"
        assert t.params.increment_strategy == "random"
        assert t.params.script.content == "updated test script"
        assert t.params.group_count == 52
        assert t.params.participant_count == 9355
        assert t.params.deleted is None

        assert httpretty.last_request().parsed_body == {
            "increment_strategy": "random",
            "mode": "performance",
            "mos_test": True,
            "name": "updated pytest name",
            "participant_timeout": 94,
            "script": "updated test script",
            "start_interval": 45,
        }

    def test_delete(self, mock):
        t = Test(test_id=identifiers.test_id)

        t.delete()

        assert t.params.test_id == identifiers.test_id
        assert t.params.deleted is True

        assert httpretty.last_request().parsed_body == ""

    def test_duplicate(self, mock):
        t = Test(test_id=identifiers.test_id)

        dupl = t.duplicate("pytest duplicate test")

        assert t.params.test_id == identifiers.test_id
        assert t.params.created is None
        assert t.params.updated is None
        assert t.params.name is None
        assert t.params.start_interval is None
        assert t.params.participant_timeout is None
        assert t.params.mode is None
        assert t.params.increment_strategy is None
        assert t.params.script is None
        assert t.params.group_count is None
        assert t.params.participant_count is None
        assert t.params.deleted is None

        assert dupl.params.test_id == identifiers.test_id + 1
        assert dupl.params.created == created_time
        assert dupl.params.updated == updated_time
        assert dupl.params.name == "pytest duplicate test"
        assert dupl.params.start_interval == 12
        assert dupl.params.participant_timeout == 13
        assert dupl.params.mode == "load"
        assert dupl.params.increment_strategy == "linear"
        assert dupl.params.script.content == "pytest test script"
        assert dupl.params.group_count == 52
        assert dupl.params.participant_count == 9355
        assert dupl.params.deleted is None

        # duplicate test
        assert httpretty.latest_requests()[-2].parsed_body == {
            "name": "pytest duplicate test"
        }

        # read script
        assert httpretty.latest_requests()[-1].parsed_body == ""


class TestTestAPI:
    def test_api_create(self, mock):
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

        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.name == "pytest test"
        assert ret.start_interval == 12
        assert ret.participant_timeout == 13
        assert ret.mode == "load"
        assert ret.increment_strategy == "linear"
        assert ret.script.content == "pytest test script"
        assert ret.group_count == 52
        assert ret.participant_count == 9355
        assert ret.deleted is None

        assert httpretty.last_request().parsed_body == {
            "increment_strategy": "linear",
            "mode": "load",
            "mos_test": False,
            "name": "pytest test",
            "participant_timeout": 13,
            "script": "pytest test script",
            "start_interval": 12,
        }

    def test_api_read(self, mock):
        ret = TestAPI().read(TestParams(test_id=identifiers.test_id))

        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.name == "pytest test"
        assert ret.start_interval == 12
        assert ret.participant_timeout == 13
        assert ret.mode == "load"
        assert ret.increment_strategy == "linear"
        assert ret.script.content == "pytest test script"
        assert ret.group_count == 52
        assert ret.participant_count == 9355
        assert ret.deleted is None

        assert httpretty.last_request().parsed_body == ""

    def test_api_read_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.read(TestParams())

    def test_api_update(self, mock):
        ret = TestAPI().update(
            TestParams(
                test_id=identifiers.test_id,
                name="updated pytest name",
                start_interval=45,
                participant_timeout=94,
                mode="performance",
                increment_strategy="random",
                script=Script(content="updated test script"),
                mos_test=True,
            )
        )

        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.name == "updated pytest name"
        assert ret.start_interval == 45
        assert ret.participant_timeout == 94
        assert ret.mode == "performance"
        assert ret.increment_strategy == "random"
        assert ret.script.content == "updated test script"
        assert ret.group_count == 52
        assert ret.participant_count == 9355
        assert ret.deleted is None

        assert httpretty.last_request().parsed_body == {
            "increment_strategy": "random",
            "mode": "performance",
            "mos_test": True,
            "name": "updated pytest name",
            "participant_timeout": 94,
            "script": "updated test script",
            "start_interval": 45,
        }

    def test_api_update_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.update(TestParams())

    def test_api_delete(self, mock):
        ret = TestAPI().delete(TestParams(test_id=identifiers.test_id))

        assert ret.test_id == identifiers.test_id
        assert ret.deleted is True

        assert httpretty.last_request().parsed_body == ""

    def test_api_delete_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.delete(TestParams())

    def test_api_duplicate(self, mock):
        ret = TestAPI().duplicate(
            TestParams(
                test_id=identifiers.test_id, name="pytest duplicate test"
            )
        )

        assert ret.test_id == identifiers.test_id + 1
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.name == "pytest duplicate test"
        assert ret.start_interval == 12
        assert ret.participant_timeout == 13
        assert ret.mode == "load"
        assert ret.increment_strategy == "linear"
        assert ret.script.content == "pytest test script"
        assert ret.group_count == 52
        assert ret.participant_count == 9355
        assert ret.deleted is None

        # duplicate test
        assert httpretty.latest_requests()[-2].parsed_body == {
            "name": "pytest duplicate test"
        }

        # read script
        assert httpretty.latest_requests()[-1].parsed_body == ""

    def test_api_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.duplicate(TestParams())

    def test_api_read_all(self):
        TestAPI().read_all()
