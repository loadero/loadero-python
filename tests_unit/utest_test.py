"""Test resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
from urllib.parse import urlparse, parse_qs
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.assert_resource import AssertFilterKey
from loadero_python.resources.group import GroupFilterKey
from loadero_python.resources.participant import ParticipantFilterKey
from loadero_python.resources.run import RunFilterKey
from loadero_python.resources.test import (
    Test,
    TestFilterKey,
    TestParams,
    Script,
    TestAPI,
)
from loadero_python.resources.classificator import (
    TestMode,
    IncrementStrategy,
)
from . import common


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE, False)

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
        body=json.dumps(common.FILE_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all tests
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.test_json, common.test_json]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/$"),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all groups
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.GROUP_JSON, common.GROUP_JSON]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all participants
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.PARTICIPANT_JSON, common.PARTICIPANT_JSON]

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
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.ASSERT_JSON, common.ASSERT_JSON]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all runs
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.RUN_JSON, common.RUN_JSON]

    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/"
        f"tests/{common.TEST_ID}/runs/",
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # launch test
    httpretty.register_uri(
        httpretty.POST,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/"
        f"tests/{common.TEST_ID}/runs/",
        body=json.dumps(common.RUN_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


@pytest.mark.usefixtures("mock")
class UTestScript:
    @staticmethod
    def utest_init_from_id():
        s = Script(file_id=2)
        assert s.file_id == 2

    @staticmethod
    def utest_init_from_content():
        s = Script(content="script content")
        assert s.content == "script content"

    @staticmethod
    def utest_init_from_file():
        s = Script(filepath=common.SCRIPT_FILE_PATH)
        assert s.content == common.SCRIPT_FILE_DATA

    @staticmethod
    def utest_string():
        s = Script()
        assert str(s) == "<no script>"

        s.content = "script content"
        assert str(s) == "script content"

    @staticmethod
    def utest_from_file():
        s = Script()
        s.from_file(common.SCRIPT_FILE_PATH)
        assert s.content == common.SCRIPT_FILE_DATA

    @staticmethod
    def utest_to_dict():
        s = Script(content="script content")
        assert s.to_dict() == "script content"

    @staticmethod
    def utest_to_dict_full():
        s = Script(content="script content")
        assert s.to_dict_full() == "script content"

    @staticmethod
    def utest_from_dict():
        s = Script()
        s.from_dict(common.FILE_JSON)
        assert not s.content

    @staticmethod
    def utest_read():
        s = Script(file_id=2).read()
        assert s.content == "pytest test script"
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body


class UTestTestParams:
    @staticmethod
    def utest_string():
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

    @staticmethod
    def utest_created():
        t = TestParams()
        t.__dict__["_created"] = common.CREATED_TIME
        assert t.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        t = TestParams()
        t.__dict__["_updated"] = common.UPDATED_TIME
        assert t.updated == common.UPDATED_TIME

    @staticmethod
    def utest_group_count():
        t = TestParams()
        t.__dict__["_group_count"] = 5
        assert t.group_count == 5

    @staticmethod
    def utest_participant_count():
        t = TestParams()
        t.__dict__["_participant_count"] = 5
        assert t.participant_count == 5

    @staticmethod
    def utest_deleted():
        t = TestParams()
        t.__dict__["_deleted"] = True
        assert t.deleted is True

    @staticmethod
    def utest_script():
        t = TestParams()
        t.__dict__["_script"] = common.SCRIPT
        assert t.script.content == common.SCRIPT.content

    @staticmethod
    def utest_set_script():
        t = TestParams()
        t.script = common.SCRIPT
        assert t.script.content == common.SCRIPT.content

    @staticmethod
    def utest_builder_id():
        t = TestParams()
        t.with_id(5)
        assert t.test_id == 5

    @staticmethod
    def utest_builder_name():
        t = TestParams()
        t.with_name("test")
        assert t.name == "test"

    @staticmethod
    def utest_builder_start_interval():
        t = TestParams()
        t.with_start_interval(5)
        assert t.start_interval == 5

    @staticmethod
    def utest_builder_participant_timeout():
        t = TestParams()
        t.with_participant_timeout(5)
        assert t.participant_timeout == 5

    @staticmethod
    def utest_builder_mode():
        t = TestParams()
        t.with_mode(TestMode.TM_LOAD)
        assert t.mode is TestMode.TM_LOAD

    @staticmethod
    def utest_builder_increment_strategy():
        t = TestParams()
        t.with_increment_strategy(IncrementStrategy.IS_LINEAR)
        assert t.increment_strategy is IncrementStrategy.IS_LINEAR

    @staticmethod
    def utest_builder_mos_test():
        t = TestParams()
        t.with_mos_test(True)
        assert t.mos_test is True

    @staticmethod
    def utest_builder_script():
        t = TestParams()
        t.with_script(Script(content="hello"))
        assert t.script.content == "hello"


@pytest.mark.usefixtures("mock")
class UTestTest:
    @staticmethod
    def utest_create():
        common.check_test_params(
            Test(
                params=TestParams(
                    name="pytest test",
                    start_interval=12,
                    participant_timeout=13,
                    mode=TestMode.TM_LOAD,
                    increment_strategy=IncrementStrategy.IS_LINEAR,
                    mos_test=False,
                    script=common.SCRIPT,
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

    @staticmethod
    def utest_read():
        common.check_test_params(Test(test_id=common.TEST_ID).read().params)

        # read test
        assert httpretty.latest_requests()[-2].method == httpretty.GET
        assert not httpretty.latest_requests()[-2].parsed_body

        # read script
        assert httpretty.latest_requests()[-1].method == httpretty.GET
        assert not httpretty.latest_requests()[-1].parsed_body

    @staticmethod
    def utest_update():
        common.check_test_params(
            Test(
                params=TestParams(
                    test_id=common.TEST_ID,
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

    @staticmethod
    def utest_delete():
        t = Test(test_id=common.TEST_ID).delete()

        assert t.params.test_id == common.TEST_ID
        assert t.params.deleted is True

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_duplicate():
        common.check_test_params(
            Test(test_id=common.TEST_ID)
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
        assert not httpretty.latest_requests()[-1].parsed_body

    @staticmethod
    def utest_launch():
        common.check_run_params(Test(test_id=common.TEST_ID).launch().params)

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_groups():
        groups, pagination, filters = Test(test_id=common.TEST_ID).groups(
            common.build_query_params(list(GroupFilterKey))
        )

        common.check_pagination_params(pagination)
        assert filters == common.FILTER_JSON

        assert len(groups) == 2

        for ret in groups:
            common.check_group_params(ret.params)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(GroupFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_groups_invalid_params():
        with pytest.raises(ValueError):
            Test().groups()

    @staticmethod
    def utest_participants():
        participants, pagination, filters = Test(
            test_id=common.TEST_ID
        ).participants(common.build_query_params(list(ParticipantFilterKey)))

        common.check_pagination_params(pagination)
        assert filters == common.FILTER_JSON

        assert len(participants) == 2

        for ret in participants:
            common.check_participant_params(ret.params)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(ParticipantFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_participants_invalid_params():
        with pytest.raises(ValueError):
            Test().participants()

    @staticmethod
    def utest_asserts():
        asserts, pagination, filters = Test(test_id=common.TEST_ID).asserts(
            common.build_query_params(list(AssertFilterKey))
        )

        common.check_pagination_params(pagination)
        assert filters == common.FILTER_JSON

        assert len(asserts) == 2

        for ret in asserts:
            common.check_assert_params(ret.params)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(AssertFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_asserts_invalid_params():
        with pytest.raises(ValueError):
            Test().asserts()

    @staticmethod
    def utest_runs():
        runs, pagination, filters = Test(test_id=common.TEST_ID).runs(
            common.build_query_params(list(RunFilterKey))
        )

        common.check_pagination_params(pagination)
        assert filters == common.FILTER_JSON

        assert len(runs) == 2

        for ret in runs:
            common.check_run_params(ret.params)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(RunFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_runs_invalid_params():
        with pytest.raises(ValueError):
            Test().runs()


@pytest.mark.usefixtures("mock")
class UTestTestAPI:
    @staticmethod
    def utest_create():
        common.check_test_params(
            TestAPI().create(
                TestParams(
                    name="pytest test",
                    start_interval=12,
                    participant_timeout=13,
                    mode=TestMode.TM_LOAD,
                    increment_strategy=IncrementStrategy.IS_LINEAR,
                    mos_test=False,
                    script=common.SCRIPT,
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

    @staticmethod
    def utest_read():
        common.check_test_params(
            TestAPI().read(TestParams(test_id=common.TEST_ID)), False
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_invalid_params():
        with pytest.raises(Exception):
            TestAPI.read(TestParams())

    @staticmethod
    def utest_update():
        common.check_test_params(
            TestAPI().update(
                TestParams(
                    test_id=common.TEST_ID,
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

    @staticmethod
    def utest_update_invalid_params():
        with pytest.raises(Exception):
            TestAPI.update(TestParams())

    @staticmethod
    def utest_delete():
        ret = TestAPI().delete(TestParams(test_id=common.TEST_ID))

        assert ret.test_id == common.TEST_ID
        assert ret.deleted is True

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_delete_invalid_params():
        with pytest.raises(Exception):
            TestAPI.delete(TestParams())

    @staticmethod
    def utest_duplicate():
        common.check_test_params(
            TestAPI().duplicate(
                TestParams(test_id=common.TEST_ID), "pytest duplicate test"
            ),
            False,
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "name": "pytest duplicate test"
        }

    @staticmethod
    def utest_duplicate_invalid_params():
        with pytest.raises(Exception):
            TestAPI.duplicate(TestParams(), "pytest duplicate test")

    @staticmethod
    def utest_read_all():
        resp = TestAPI().read_all()

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_test_params(ret, False)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_with_query_params():
        resp = TestAPI().read_all(
            common.build_query_params(list(TestFilterKey))
        )

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_test_params(ret, False)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(TestFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert TestAPI().route() == "projects/538591/tests/"
        assert TestAPI().route(common.TEST_ID) == "projects/538591/tests/12734/"
