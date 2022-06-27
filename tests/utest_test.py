"""Test resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.script import Script
from loadero_python.resources.test import Test, TestParams, TestAPI
from loadero_python.resources.classificator import (
    TestMode,
    IncrementStrategy,
)
from . import common


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.project_id, common.access_token, common.api_base)

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/$"),
        body=json.dumps(common.test_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/$"),
        body=json.dumps(common.test_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/$"),
        body=json.dumps(common.test_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # delete
    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/$"),
    )

    # duplicate
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/copy/$"
        ),
        body=json.dumps(common.test_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read file
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/\d*/$"),
        body=json.dumps(common.file_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all tests
    pg = common.paged_response.copy()
    pg["results"] = [common.test_json, common.test_json]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/$"),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all groups
    pg = common.paged_response.copy()
    pg["results"] = [common.group_json, common.group_json]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all participants
    pg = common.paged_response.copy()
    pg["results"] = [common.participant_json, common.participant_json]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all asserts
    pg = common.paged_response.copy()
    pg["results"] = [common.assert_json, common.assert_json]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # launch test
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/runs/$"
        ),
        body=json.dumps(common.run_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestTestParams:
    def utest_string(self):
        t = TestParams()
        t.from_dict(common.test_json)

        assert (
            str(t)
            == """{
    "id": 12734,
    "name": "pytest test",
    "start_interval": 12,
    "participant_timeout": 13,
    "mode": "load",
    "increment_strategy": "linear",
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00",
    "script_file_id": 65,
    "group_count": 52,
    "participant_count": 9355
}"""
        )

    def utest_created(self):
        t = TestParams()
        t.__dict__["_created"] = common.created_time
        assert t.created == common.created_time

    def utest_updated(self):
        t = TestParams()
        t.__dict__["_updated"] = common.updated_time
        assert t.updated == common.updated_time

    def utest_group_count(self):
        t = TestParams()
        t.__dict__["_group_count"] = 5
        assert t.group_count == 5

    def utest_participant_count(self):
        t = TestParams()
        t.__dict__["_participant_count"] = 5
        assert t.participant_count == 5

    def utest_deleted(self):
        t = TestParams()
        t.__dict__["_deleted"] = True

        assert t.deleted is True

    def utest_script(self):
        t = TestParams()
        t.__dict__["_script"] = common.script

        assert t.script.content == common.script.content

    def utest_set_script(self):
        t = TestParams()
        t.script = common.script

        assert t.script.content == common.script.content

    def utest_builder_id(self):
        t = TestParams()
        t.with_id(5)
        assert t.test_id == 5

    def utest_builder_name(self):
        t = TestParams()
        t.with_name("test")
        assert t.name == "test"

    def utest_builder_start_interval(self):
        t = TestParams()
        t.with_start_interval(5)
        assert t.start_interval == 5

    def utest_builder_participant_timeout(self):
        t = TestParams()
        t.with_participant_timeout(5)
        assert t.participant_timeout == 5

    def utest_builder_mode(self):
        t = TestParams()
        t.with_mode(TestMode.TM_LOAD)
        assert t.mode is TestMode.TM_LOAD

    def utest_builder_increment_strategy(self):
        t = TestParams()
        t.with_increment_strategy(IncrementStrategy.IS_LINEAR)
        assert t.increment_strategy is IncrementStrategy.IS_LINEAR

    def utest_builder_mos_test(self):
        t = TestParams()
        t.with_mos_test(True)
        assert t.mos_test is True

    def utest_builder_script(self):
        t = TestParams()
        t.with_script(Script(content="hello"))

        print(Script().content)
        assert t.script.content == "hello"


@pytest.mark.usefixtures("mock")
class UTestTest:
    def utest_create(self):
        common.check_test_params(
            Test(
                params=TestParams(
                    name="pytest test",
                    start_interval=12,
                    participant_timeout=13,
                    mode=TestMode.TM_LOAD,
                    increment_strategy=IncrementStrategy.IS_LINEAR,
                    mos_test=False,
                    script=common.script,
                )
            )
            .create()
            .params
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "increment_strategy": "linear",
            "mode": "load",
            "mos_test": False,
            "name": "pytest test",
            "participant_timeout": 13,
            "script": "pytest test script",
            "start_interval": 12,
        }

    def utest_read(self):
        common.check_test_params(Test(test_id=common.test_id).read().params)

        # read test
        assert httpretty.latest_requests()[-2].method == httpretty.GET
        assert not httpretty.latest_requests()[-2].parsed_body

        # read script
        assert httpretty.latest_requests()[-1].method == httpretty.GET
        assert not httpretty.latest_requests()[-1].parsed_body

    def utest_update(self):
        common.check_test_params(
            Test(
                params=TestParams(
                    test_id=common.test_id,
                    name="updated pytest name",
                    start_interval=45,
                    participant_timeout=94,
                    mode=TestMode.TM_PERFORMANCE,
                    increment_strategy=IncrementStrategy.IS_RANDOM,
                    script=Script(content="pytest test script"),
                    mos_test=True,
                )
            )
            .update()
            .params
        )

        # update test
        assert httpretty.last_request().method == httpretty.PUT
        assert httpretty.last_request().parsed_body == {
            "increment_strategy": "random",
            "mode": "performance",
            "mos_test": True,
            "name": "updated pytest name",
            "participant_timeout": 94,
            "script": "pytest test script",
            "start_interval": 45,
        }

    def utest_delete(self):
        t = Test(test_id=common.test_id).delete()

        assert t.params.test_id == common.test_id
        assert t.params.deleted is True

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    def utest_duplicate(self):
        common.check_test_params(
            Test(test_id=common.test_id)
            .duplicate("pytest duplicate test")
            .params
        )

        # duplicate test
        assert httpretty.latest_requests()[-2].method == httpretty.POST
        assert httpretty.latest_requests()[-2].parsed_body == {
            "name": "pytest duplicate test"
        }

        # read script
        assert httpretty.latest_requests()[-1].method == httpretty.GET
        assert httpretty.latest_requests()[-1].parsed_body == ""

    def utest_launch(self):
        common.check_run_params(Test(test_id=common.test_id).launch().params)

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    def utest_groups(self):
        t = Test(test_id=common.test_id)

        resp = t.groups()

        assert len(resp) == 2

        for ret in resp:
            common.check_group_params(ret.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_participants(self):
        t = Test(test_id=common.test_id)

        resp = t.participants()

        assert len(resp) == 2

        for ret in resp:
            common.check_participant_params(ret.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_asserts(self):
        t = Test(test_id=common.test_id)

        resp = t.asserts()

        assert len(resp) == 2

        for ret in resp:
            common.check_assert_params(ret.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body


@pytest.mark.usefixtures("mock")
class UTestTestAPI:
    def utest_create(self):
        common.check_test_params(
            TestAPI().create(
                TestParams(
                    name="pytest test",
                    start_interval=12,
                    participant_timeout=13,
                    mode=TestMode.TM_LOAD,
                    increment_strategy=IncrementStrategy.IS_LINEAR,
                    mos_test=False,
                    script=common.script,
                )
            )
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "increment_strategy": "linear",
            "mode": "load",
            "mos_test": False,
            "name": "pytest test",
            "participant_timeout": 13,
            "script": "pytest test script",
            "start_interval": 12,
        }

    def utest_read(self):
        common.check_test_params(
            TestAPI().read(TestParams(test_id=common.test_id)), False
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.read(TestParams())

    def utest_update(self):
        common.check_test_params(
            TestAPI().update(
                TestParams(
                    test_id=common.test_id,
                    name="updated pytest name",
                    start_interval=45,
                    participant_timeout=94,
                    mode=TestMode.TM_PERFORMANCE,
                    increment_strategy=IncrementStrategy.IS_RANDOM,
                    script=Script(content="pytest test script"),
                    mos_test=True,
                )
            ),
        )

        assert httpretty.last_request().method == httpretty.PUT
        assert httpretty.last_request().parsed_body == {
            "increment_strategy": "random",
            "mode": "performance",
            "mos_test": True,
            "name": "updated pytest name",
            "participant_timeout": 94,
            "script": "pytest test script",
            "start_interval": 45,
        }

    def utest_update_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.update(TestParams())

    def utest_delete(self):
        ret = TestAPI().delete(TestParams(test_id=common.test_id))

        assert ret.test_id == common.test_id
        assert ret.deleted is True

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    def utest_delete_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.delete(TestParams())

    def utest_duplicate(self):
        common.check_test_params(
            TestAPI().duplicate(
                TestParams(test_id=common.test_id), "pytest duplicate test"
            ),
            False,
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "name": "pytest duplicate test"
        }

    def utest_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.duplicate(TestParams(), "pytest duplicate test")

    def utest_read_all(self):
        resp = TestAPI().read_all()

        assert len(resp) == 2

        for ret in resp:
            common.check_test_params(ret, False)

        assert not httpretty.last_request().parsed_body
        assert httpretty.last_request().method == httpretty.GET

    def utest_read_all_no_results(self):
        pg = common.paged_response.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/$"),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        resp = TestAPI().read_all()

        assert len(resp) == 0

        assert not httpretty.last_request().parsed_body
        assert httpretty.last_request().method == httpretty.GET

    def utest_route(self):
        assert (
            TestAPI().route()
            == "http://mock.loadero.api/v2/projects/538591/tests/"
        )
        assert (
            TestAPI().route(common.test_id)
            == "http://mock.loadero.api/v2/projects/538591/tests/12734/"
        )
