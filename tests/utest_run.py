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

    APIClient(common.project_id, common.access_token, common.api_base)

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/runs/$"
        ),
        body=json.dumps(common.run_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/$"),
        body=json.dumps(common.run_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    pg = common.paged_response.copy()
    pg["results"] = [common.run_json, common.run_json]

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
    pg = common.paged_response.copy()
    pg["results"] = [common.result_json, common.result_json]

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
    def utest_str(self):
        r = RunParams()
        r.from_dict(common.run_json)
        assert (
            str(r)
            == """{
    "id": 937561,
    "test_id": 12734,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00",
    "status": "done",
    "metric_status": "calculating",
    "mos_status": "available",
    "test_mode": "load",
    "increment_strategy": "linear",
    "processing_started": "2025-07-29 19:31:29.468000+00:00",
    "processing_finished": "2019-07-09 18:39:30.488000+00:00",
    "execution_started": "2021-02-26 14:53:24.228000+00:00",
    "execution_finished": "2023-06-26 19:38:25.268000+00:00",
    "script_file_id": 294325,
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

    def utest_created(self):
        r = RunParams()
        r.__dict__["_created"] = common.created_time
        assert r.created == common.created_time

    def utest_updated(self):
        r = RunParams()
        r.__dict__["_updated"] = common.updated_time
        assert r.updated == common.updated_time

    def utest_status(self):
        r = RunParams()
        r.__dict__["_status"] = RunStatus.RS_ABORTED
        assert r.status == RunStatus.RS_ABORTED

    def utest_metric_status(self):
        r = RunParams()
        r.__dict__["_metric_status"] = MetricStatus.MS_CALCULATING
        assert r.metric_status == MetricStatus.MS_CALCULATING

    def utest_test_mode(self):
        r = RunParams()
        r.__dict__["_test_mode"] = TestMode.TM_LOAD
        assert r.test_mode == TestMode.TM_LOAD

    def utest_increment_strategy(self):
        r = RunParams()
        r.__dict__["_increment_strategy"] = IncrementStrategy.IS_LINEAR_GROUP
        assert r.increment_strategy == IncrementStrategy.IS_LINEAR_GROUP

    def utest_mos_status(self):
        r = RunParams()
        r.__dict__["_mos_status"] = MetricStatus.MS_CALCULATING
        assert r.mos_status == MetricStatus.MS_CALCULATING

    def utest_processing_started(self):
        r = RunParams()
        r.__dict__["_processing_started"] = common.processing_started
        assert r.processing_started == common.processing_started

    def utest_processing_finished(self):
        r = RunParams()
        r.__dict__["_processing_finished"] = common.processing_finished
        assert r.processing_finished == common.processing_finished

    def utest_execution_started(self):
        r = RunParams()
        r.__dict__["_execution_started"] = common.execution_started
        assert r.execution_started == common.execution_started

    def utest_execution_finished(self):
        r = RunParams()
        r.__dict__["_execution_finished"] = common.execution_finished
        assert r.execution_finished == common.execution_finished

    def utest_script_file_id(self):
        r = RunParams()
        r.__dict__["_script_file_id"] = common.file_id
        assert r.script_file_id == common.file_id

    def utest_test_name(self):
        r = RunParams()
        r.__dict__["_test_name"] = "test name"
        assert r.test_name == "test name"

    def utest_start_interval(self):
        r = RunParams()
        r.__dict__["_start_interval"] = 134
        assert r.start_interval == 134

    def utest_participant_timeout(self):
        r = RunParams()
        r.__dict__["_participant_timeout"] = 933
        assert r.participant_timeout == 933

    def utest_launching_account_id(self):
        r = RunParams()
        r.__dict__["_launching_account_id"] = 923
        assert r.launching_account_id == 923

    def utest_success_rate(self):
        r = RunParams()
        r.__dict__["_success_rate"] = 0.8
        assert r.success_rate == 0.8

    def utest_total_cu_count(self):
        r = RunParams()
        r.__dict__["_total_cu_count"] = 9.0
        assert r.total_cu_count == 9.0

    def utest_group_count(self):
        r = RunParams()
        r.__dict__["_group_count"] = 8
        assert r.group_count == 8

    def utest_participant_count(self):
        r = RunParams()
        r.__dict__["_participant_count"] = 9
        assert r.participant_count == 9

    def utest_mos_test(self):
        r = RunParams()
        r.__dict__["_mos_test"] = True
        assert r.mos_test is True

    def utest_with_id(self):
        r = RunParams()
        r.with_id(34)
        assert r.run_id == 34

    def utest_in_test(self):
        r = RunParams()
        r.in_test(34)
        assert r.test_id == 34


@pytest.mark.usefixtures("mock")
class UTestRun:
    def utest_init(self):
        r = Run()

        assert not r.params.run_id

        r = Run(
            run_id=common.run_id,
            test_id=common.test_id,
            params=RunParams(
                run_id=1,
                test_id=2,
            ),
        )

        assert r.params.run_id == common.run_id
        assert r.params.test_id == common.test_id

    def utest_create(self):
        common.check_run_params(
            Run(run_id=common.run_id, test_id=common.test_id).create().params
        )

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    def utest_read(self):
        common.check_run_params(Run(run_id=common.run_id).read().params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_stop(self):
        Run(run_id=common.run_id, test_id=common.test_id).stop()

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    def utest_poll(self):
        httpretty.reset()

        running_resp = common.run_json.copy()
        running_resp["status"] = "running"

        class Handler:
            responses = [
                running_resp,
                running_resp,
                running_resp,
                running_resp,
                common.run_json,
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

        common.check_run_params(Run(run_id=common.run_id).poll(0.1, 1).params)

        assert h.response_counter == len(h.responses)

    def utest_poll_timeout(self):
        httpretty.reset()

        ret = common.run_json.copy()
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
            Run(run_id=common.run_id).poll(0.1, 0.1)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_results(self):
        resp = Run(run_id=common.run_id).results()

        assert len(resp) == 2

        for ret in resp:
            common.check_result_params(ret.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_results_invalid_run_id(self):
        r = Run()
        with pytest.raises(ValueError):
            r.results()


@pytest.mark.usefixtures("mock")
class UTestRunAPI:
    def utest_create(self):
        common.check_run_params(
            RunAPI.create(RunParams(test_id=common.test_id))
        )

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    def utest_read(self):
        common.check_run_params(RunAPI.read(RunParams(run_id=common.run_id)))

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_all_parent_project(self):
        resp = RunAPI.read_all()

        assert len(resp) == 2

        for ret in resp:
            common.check_run_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_all_parent_test(self):
        resp = RunAPI.read_all(common.test_id)

        assert len(resp) == 2

        for ret in resp:
            common.check_run_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_all_no_results(self):
        pg = common.paged_response.copy()
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

    def utest_stop(self):
        RunAPI.stop(RunParams(run_id=common.run_id, test_id=common.test_id))

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    def utest_route(self):
        assert (
            RunAPI.route() == "http://mock.loadero.api/v2/projects/538591/runs/"
        )
        assert (
            RunAPI.route(test_id=common.test_id)
            == "http://mock.loadero.api/v2/projects/538591/tests/12734/runs/"
        )
        assert (
            RunAPI.route(run_id=common.run_id)
            == "http://mock.loadero.api/v2/projects/538591/runs/937561/"
        )
        assert (
            RunAPI.route(test_id=common.test_id, run_id=common.run_id)
            == "http://mock.loadero.api/"
            "v2/projects/538591/tests/12734/runs/937561/"
        )

    def utest_validate_identifiers(self):
        with pytest.raises(Exception):
            RunAPI.read(RunParams())

        with pytest.raises(ValueError):
            RunAPI.create(RunParams())
