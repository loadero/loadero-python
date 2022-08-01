"""Run resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.run import RunParams, RunAPI, Run
from loadero_python.resources.classificator import (
    RunStatus,
    MetricStatus,
    TestMode,
    IncrementStrategy,
)
from . import common


@pytest.fixture
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE)

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/runs/$"
        ),
        body=json.dumps(common.RUN_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/$"),
        body=json.dumps(common.RUN_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    pg = common.PAGED_RESPONSE.copy()
    pg["results"] = [common.RUN_JSON, common.RUN_JSON]

    # read all, parent project
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/runs/$"),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all, parent test
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/runs/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all results
    pg = common.PAGED_RESPONSE.copy()
    pg["results"] = [common.RESULT_JSON, common.RESULT_JSON]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/results/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # stop
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/runs/\d*/stop/$"
        ),
        body="",
    )

    yield

    httpretty.disable()


class UTestRunParams:
    @staticmethod
    def utest_str():
        r = RunParams()
        r.from_dict(common.RUN_JSON)
        assert (
            str(r)
            == """{
    "id": 937561,
    "test_id": 12734,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00",
    "status": "done",
    "metric_status": "calculating",
    "test_mode": "load",
    "increment_strategy": "linear",
    "mos_status": "available",
    "processing_started": "2025-07-29 19:31:29.468000+00:00",
    "processing_finished": "2019-07-09 18:39:30.488000+00:00",
    "execution_started": "2021-02-26 14:53:24.228000+00:00",
    "execution_finished": "2023-06-26 19:38:25.268000+00:00",
    "script_file_id": 923,
    "test_name": "pytest test",
    "start_interval": 98,
    "participant_timeout": 92,
    "launching_account_id": 12,
    "success_rate": 0.3,
    "total_cu_count": 3.3,
    "group_count": 5,
    "participant_count": 89,
    "mos_test": true
}"""
        )

    @staticmethod
    def utest_created():
        r = RunParams()
        r.__dict__["_created"] = common.CREATED_TIME
        assert r.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        r = RunParams()
        r.__dict__["_updated"] = common.UPDATED_TIME
        assert r.updated == common.UPDATED_TIME

    @staticmethod
    def utest_status():
        r = RunParams()
        r.__dict__["_status"] = RunStatus.RS_ABORTED
        assert r.status == RunStatus.RS_ABORTED

    @staticmethod
    def utest_metric_status():
        r = RunParams()
        r.__dict__["_metric_status"] = MetricStatus.MS_CALCULATING
        assert r.metric_status == MetricStatus.MS_CALCULATING

    @staticmethod
    def utest_test_mode():
        r = RunParams()
        r.__dict__["_test_mode"] = TestMode.TM_LOAD
        assert r.test_mode == TestMode.TM_LOAD

    @staticmethod
    def utest_increment_strategy():
        r = RunParams()
        r.__dict__["_increment_strategy"] = IncrementStrategy.IS_LINEAR_GROUP
        assert r.increment_strategy == IncrementStrategy.IS_LINEAR_GROUP

    @staticmethod
    def utest_mos_status():
        r = RunParams()
        r.__dict__["_mos_status"] = MetricStatus.MS_CALCULATING
        assert r.mos_status == MetricStatus.MS_CALCULATING

    @staticmethod
    def utest_processing_started():
        r = RunParams()
        r.__dict__["_processing_started"] = common.PROCESSING_STARTED
        assert r.processing_started == common.PROCESSING_STARTED

    @staticmethod
    def utest_processing_finished():
        r = RunParams()
        r.__dict__["_processing_finished"] = common.PROCESSING_FINISHED
        assert r.processing_finished == common.PROCESSING_FINISHED

    @staticmethod
    def utest_execution_started():
        r = RunParams()
        r.__dict__["_execution_started"] = common.EXECUTION_STARTED
        assert r.execution_started == common.EXECUTION_STARTED

    @staticmethod
    def utest_execution_finished():
        r = RunParams()
        r.__dict__["_execution_finished"] = common.EXECUTION_FINISHED
        assert r.execution_finished == common.EXECUTION_FINISHED

    @staticmethod
    def utest_script_file_id():
        r = RunParams()
        r.__dict__["_script_file_id"] = common.FILE_ID
        assert r.script_file_id == common.FILE_ID

    @staticmethod
    def utest_test_name():
        r = RunParams()
        r.__dict__["_test_name"] = "test name"
        assert r.test_name == "test name"

    @staticmethod
    def utest_start_interval():
        r = RunParams()
        r.__dict__["_start_interval"] = 134
        assert r.start_interval == 134

    @staticmethod
    def utest_participant_timeout():
        r = RunParams()
        r.__dict__["_participant_timeout"] = 933
        assert r.participant_timeout == 933

    @staticmethod
    def utest_launching_account_id():
        r = RunParams()
        r.__dict__["_launching_account_id"] = 923
        assert r.launching_account_id == 923

    @staticmethod
    def utest_success_rate():
        r = RunParams()
        r.__dict__["_success_rate"] = 0.8
        assert r.success_rate == 0.8

    @staticmethod
    def utest_total_cu_count():
        r = RunParams()
        r.__dict__["_total_cu_count"] = 9.0
        assert r.total_cu_count == 9.0

    @staticmethod
    def utest_group_count():
        r = RunParams()
        r.__dict__["_group_count"] = 8
        assert r.group_count == 8

    @staticmethod
    def utest_participant_count():
        r = RunParams()
        r.__dict__["_participant_count"] = 9
        assert r.participant_count == 9

    @staticmethod
    def utest_mos_test():
        r = RunParams()
        r.__dict__["_mos_test"] = True
        assert r.mos_test is True

    @staticmethod
    def utest_with_id():
        r = RunParams()
        r.with_id(34)
        assert r.run_id == 34

    @staticmethod
    def utest_in_test():
        r = RunParams()
        r.in_test(34)
        assert r.test_id == 34


@pytest.mark.usefixtures("mock")
class UTestRun:
    @staticmethod
    def utest_init():
        r = Run()

        assert not r.params.run_id

        r = Run(
            run_id=common.RUN_ID,
            test_id=common.TEST_ID,
            params=RunParams(
                run_id=1,
                test_id=2,
            ),
        )

        assert r.params.run_id == common.RUN_ID
        assert r.params.test_id == common.TEST_ID

    @staticmethod
    def utest_create():
        common.check_run_params(
            Run(run_id=common.RUN_ID, test_id=common.TEST_ID).create().params
        )

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read():
        common.check_run_params(Run(run_id=common.RUN_ID).read().params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_stop():
        Run(run_id=common.RUN_ID, test_id=common.TEST_ID).stop()

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_poll():
        httpretty.reset()

        running_resp = common.RUN_JSON.copy()
        running_resp["status"] = "running"

        class Handler:
            responses = [
                running_resp,
                running_resp,
                running_resp,
                running_resp,
                common.RUN_JSON,
            ]
            response_counter = 0

            def handle(self, _, __, ___):
                self.response_counter += 1
                return (
                    200,
                    {"Content-Type": "application/json"},
                    json.dumps(self.responses[self.response_counter - 1]),
                )

        h = Handler()

        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/$"
            ),
            body=h.handle,
            forcing_headers={"Content-Type": "application/json"},
        )

        common.check_run_params(Run(run_id=common.RUN_ID).poll(0.1, 1).params)

        assert h.response_counter == len(h.responses)

    @staticmethod
    def utest_poll_timeout():
        httpretty.reset()

        ret = common.RUN_JSON.copy()
        ret["status"] = "running"

        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/$"
            ),
            body=json.dumps(ret),
            forcing_headers={"Content-Type": "application/json"},
        )

        with pytest.raises(TimeoutError):
            Run(run_id=common.RUN_ID).poll(0.1, 0.1)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_results():
        resp = Run(run_id=common.RUN_ID).results()

        assert len(resp) == 2

        for ret in resp:
            common.check_result_params(ret.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_results_invalid_run_id():
        r = Run()
        with pytest.raises(ValueError):
            r.results()


@pytest.mark.usefixtures("mock")
class UTestRunAPI:
    @staticmethod
    def utest_create():
        common.check_run_params(
            RunAPI.create(RunParams(test_id=common.TEST_ID))
        )

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read():
        common.check_run_params(RunAPI.read(RunParams(run_id=common.RUN_ID)))

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_parent_project():
        resp = RunAPI.read_all()

        assert len(resp) == 2

        for ret in resp:
            common.check_run_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_parent_test():
        resp = RunAPI.read_all(common.TEST_ID)

        assert len(resp) == 2

        for ret in resp:
            common.check_run_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_no_results():
        pg = common.PAGED_RESPONSE.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/runs/$"),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        resp = RunAPI.read_all()

        assert len(resp) == 0
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_stop():
        RunAPI.stop(RunParams(run_id=common.RUN_ID, test_id=common.TEST_ID))

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert RunAPI.route() == "projects/538591/runs/"
        assert (
            RunAPI.route(test_id=common.TEST_ID)
            == "projects/538591/tests/12734/runs/"
        )
        assert (
            RunAPI.route(run_id=common.RUN_ID) == "projects/538591/runs/937561/"
        )
        assert (
            RunAPI.route(test_id=common.TEST_ID, run_id=common.RUN_ID)
            == "projects/538591/tests/12734/runs/937561/"
        )

    @staticmethod
    def utest_validate_identifiers():
        with pytest.raises(Exception):
            RunAPI.read(RunParams())

        with pytest.raises(ValueError):
            RunAPI.create(RunParams())
