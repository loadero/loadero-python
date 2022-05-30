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
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
    Operator,
)
from loadero_python.resources.metric_path import MetricPath
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
    upd = common.test_json.copy()
    upd["name"] = "updated pytest name"
    upd["start_interval"] = 45
    upd["participant_timeout"] = 94
    upd["mode"] = "performance"
    upd["increment_strategy"] = "random"
    upd["mos_test"] = True

    httpretty.register_uri(
        httpretty.PUT,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/$"),
        body=json.dumps(upd),
        forcing_headers={"Content-Type": "application/json"},
    )

    # delete
    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/$"),
    )

    dupl = common.test_json.copy()
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
        body=json.dumps(common.file_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all tests
    pg = common.paged_response.copy()
    t1 = common.test_json.copy()
    t1["id"] += 1

    t2 = common.test_json.copy()
    t2["id"] += 2

    pg["results"] = [t1, t2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/tests/$"),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all groups
    gpg = common.paged_response.copy()
    g1 = common.group_json.copy()
    g1["id"] += 1

    g2 = common.group_json.copy()
    g2["id"] += 2

    gpg["results"] = [g1, g2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(gpg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all participants
    ppg = common.paged_response.copy()
    p1 = common.participant_json.copy()
    p1["id"] += 1

    p2 = common.participant_json.copy()
    p2["id"] += 2

    ppg["results"] = [p1, p2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/$"
        ),
        body=json.dumps(ppg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all asserts
    apg = common.paged_response.copy()
    a1 = common.assert_json.copy()
    a1["id"] += 1

    a2 = common.assert_json.copy()
    a2["id"] += 2

    apg["results"] = [a1, a2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/$"
        ),
        body=json.dumps(apg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestTestParams:
    def utest_string(self):
        t = TestParams()
        t.from_dict(common.test_json)

        print(t)

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
        assert t.script.content == "hello"


@pytest.mark.usefixtures("mock")
class UTestTest:
    def utest_create(self):
        t = Test(
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

        t.create()

        assert t.params.test_id == common.test_id
        assert t.params.created == common.created_time
        assert t.params.updated == common.updated_time
        assert t.params.name == "pytest test"
        assert t.params.start_interval == 12
        assert t.params.participant_timeout == 13
        assert t.params.mode is TestMode.TM_LOAD
        assert t.params.increment_strategy is IncrementStrategy.IS_LINEAR
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

    def utest_read(self):
        t = Test(test_id=common.test_id)

        t.read()

        assert t.params.test_id == common.test_id
        assert t.params.created == common.created_time
        assert t.params.updated == common.updated_time
        assert t.params.name == "pytest test"
        assert t.params.start_interval == 12
        assert t.params.participant_timeout == 13
        assert t.params.mode is TestMode.TM_LOAD
        assert t.params.increment_strategy is IncrementStrategy.IS_LINEAR
        assert t.params.script.content == "pytest test script"
        assert t.params.group_count == 52
        assert t.params.participant_count == 9355
        assert t.params.deleted is None

        assert httpretty.last_request().parsed_body == ""

    def utest_update(self):
        t = Test(
            params=TestParams(
                test_id=common.test_id,
                name="updated pytest name",
                start_interval=45,
                participant_timeout=94,
                mode=TestMode.TM_PERFORMANCE,
                increment_strategy=IncrementStrategy.IS_RANDOM,
                script=Script(content="updated test script"),
                mos_test=True,
            )
        )

        t.update()

        assert t.params.test_id == common.test_id
        assert t.params.created == common.created_time
        assert t.params.updated == common.updated_time
        assert t.params.name == "updated pytest name"
        assert t.params.start_interval == 45
        assert t.params.participant_timeout == 94
        assert t.params.mode is TestMode.TM_PERFORMANCE
        assert t.params.increment_strategy is IncrementStrategy.IS_RANDOM
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

    def utest_delete(self):
        t = Test(test_id=common.test_id)

        t.delete()

        assert t.params.test_id == common.test_id
        assert t.params.deleted is True

        assert httpretty.last_request().parsed_body == ""

    def utest_duplicate(self):
        t = Test(test_id=common.test_id)

        dupl = t.duplicate("pytest duplicate test")

        assert t.params.test_id == common.test_id
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

        assert dupl.params.test_id == common.test_id + 1
        assert dupl.params.created == common.created_time
        assert dupl.params.updated == common.updated_time
        assert dupl.params.name == "pytest duplicate test"
        assert dupl.params.start_interval == 12
        assert dupl.params.participant_timeout == 13
        assert dupl.params.mode is TestMode.TM_LOAD
        assert dupl.params.increment_strategy is IncrementStrategy.IS_LINEAR
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

    def utest_groups(self):
        t = Test(test_id=common.test_id)

        resp = t.groups()

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.params.group_id == common.group_id + i + 1
            assert ret.params.name == "pytest_group"
            assert ret.params.count == 8
            assert ret.params.test_id == common.test_id
            assert ret.params.participant_count is None  # omit empty
            assert ret.params.total_cu_count is None  # omit empty
            assert ret.params.created == common.created_time
            assert ret.params.updated == common.updated_time

        assert httpretty.last_request().parsed_body == ""

    def utest_participants(self):
        t = Test(test_id=common.test_id)

        resp = t.participants()

        assert len(resp) == 2

        b = Browser.B_CHROMELATEST

        print(resp[0].params.browser.to_dict())
        print(b, b.to_dict())

        for i, ret in enumerate(resp):
            assert ret.params.participant_id == common.participant_id + i + 1
            assert ret.params.group_id == common.group_id
            assert ret.params.test_id == common.test_id
            assert ret.params.created == common.created_time
            assert ret.params.updated == common.updated_time
            assert ret.params.count == 3
            assert ret.params.record_audio is False
            assert ret.params.name == "pytest participant"
            assert ret.params.compute_unit is ComputeUnit.CU_G4
            assert ret.params.audio_feed is AudioFeed.AF_SILENCE
            assert ret.params.browser is Browser.B_CHROMELATEST
            assert ret.params.location is Location.L_EU_CENTRAL_1
            assert ret.params.network is Network.N_4G
            assert ret.params.video_feed is VideoFeed.VF_480P_15FPS

        assert httpretty.last_request().parsed_body == ""

    def utest_asserts(self):
        t = Test(test_id=common.test_id)

        resp = t.asserts()

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.params.assert_id == common.assert_id + i + 1
            assert ret.params.test_id == common.test_id
            assert ret.params.created == common.created_time
            assert ret.params.updated == common.updated_time
            assert ret.params.expected == "892"
            assert ret.params.operator is Operator.O_GT
            assert ret.params.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert httpretty.last_request().parsed_body == ""


@pytest.mark.usefixtures("mock")
class UTestTestAPI:
    def utest_create(self):
        ret = TestAPI().create(
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

        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.name == "pytest test"
        assert ret.start_interval == 12
        assert ret.participant_timeout == 13
        assert ret.mode is TestMode.TM_LOAD
        assert ret.increment_strategy is IncrementStrategy.IS_LINEAR
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

    def utest_read(self):
        ret = TestAPI().read(TestParams(test_id=common.test_id))

        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.name == "pytest test"
        assert ret.start_interval == 12
        assert ret.participant_timeout == 13
        assert ret.mode is TestMode.TM_LOAD
        assert ret.increment_strategy is IncrementStrategy.IS_LINEAR
        assert ret.script.content == "pytest test script"
        assert ret.group_count == 52
        assert ret.participant_count == 9355
        assert ret.deleted is None

        assert httpretty.last_request().parsed_body == ""

    def utest_read_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.read(TestParams())

    def utest_update(self):
        ret = TestAPI().update(
            TestParams(
                test_id=common.test_id,
                name="updated pytest name",
                start_interval=45,
                participant_timeout=94,
                mode=TestMode.TM_PERFORMANCE,
                increment_strategy=IncrementStrategy.IS_RANDOM,
                script=Script(content="updated test script"),
                mos_test=True,
            )
        )

        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.name == "updated pytest name"
        assert ret.start_interval == 45
        assert ret.participant_timeout == 94
        assert ret.mode is TestMode.TM_PERFORMANCE
        assert ret.increment_strategy is IncrementStrategy.IS_RANDOM
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

    def utest_update_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.update(TestParams())

    def utest_delete(self):
        ret = TestAPI().delete(TestParams(test_id=common.test_id))

        assert ret.test_id == common.test_id
        assert ret.deleted is True

        assert httpretty.last_request().parsed_body == ""

    def utest_delete_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.delete(TestParams())

    def utest_duplicate(self):
        ret = TestAPI().duplicate(
            TestParams(test_id=common.test_id, name="pytest duplicate test")
        )

        assert ret.test_id == common.test_id + 1
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.name == "pytest duplicate test"
        assert ret.start_interval == 12
        assert ret.participant_timeout == 13
        assert ret.mode is TestMode.TM_LOAD
        assert ret.increment_strategy is IncrementStrategy.IS_LINEAR
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

    def utest_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            TestAPI.duplicate(TestParams())

    def utest_read_all(self):
        resp = TestAPI().read_all()

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.test_id == common.test_id + i + 1
            assert ret.created == common.created_time
            assert ret.updated == common.updated_time
            assert ret.name == "pytest test"
            assert ret.start_interval == 12
            assert ret.participant_timeout == 13
            assert ret.mode is TestMode.TM_LOAD
            assert ret.increment_strategy is IncrementStrategy.IS_LINEAR
            assert ret.script is None
            assert ret.group_count == 52
            assert ret.participant_count == 9355
            assert ret.deleted is None

        assert httpretty.last_request().parsed_body == ""

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

        assert httpretty.last_request().parsed_body == ""

    def utest_route(self):
        assert (
            TestAPI().route()
            == "http://mock.loadero.api/v2/projects/538591/tests/"
        )
        assert (
            TestAPI().route(common.test_id)
            == "http://mock.loadero.api/v2/projects/538591/tests/12734/"
        )
