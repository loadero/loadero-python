"""Group resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.project import (
    PlanLimitsParams,
    SubscriptionSettingsParams,
    SubscriptionParams,
    ProjectComputeUnitUsageParams,
    ProjectParams,
    Project,
    ProjectAPI,
)
from . import common


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE)

    # read
    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/",
        body=json.dumps(common.PROJECT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all tests
    pg = common.PAGED_RESPONSE.copy()
    pg["results"] = [common.test_json, common.test_json]

    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/tests/",
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all files
    pg = common.PAGED_RESPONSE.copy()
    pg["results"] = [common.FILE_JSON, common.FILE_JSON]

    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/files/",
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    pg = common.PAGED_RESPONSE.copy()
    pg["results"] = [common.RUN_JSON, common.RUN_JSON]

    # read all runs
    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/runs/",
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )


class UTestPlanLimitsParams:
    @staticmethod
    def utest_properties():
        common.check_plan_limits_params(
            PlanLimitsParams().from_dict(common.PLAN_LIMITS_JSON)
        )


class UTestSubscriptionSettingsParams:
    @staticmethod
    def utest_properties():
        common.check_subscription_settings_params(
            SubscriptionSettingsParams().from_dict(
                common.SUBSCRIPTION_SETTINGS_JSON
            )
        )


class UTestSubscriptionParams:
    @staticmethod
    def utest_properties():
        common.check_subscription_params(
            SubscriptionParams().from_dict(common.SUBSCRIPTION_JSON)
        )


class UTestProjectComputeUnitUsageParams:
    @staticmethod
    def utest_properties():
        common.check_project_compute_unit_usage_params(
            ProjectComputeUnitUsageParams().from_dict(
                common.PROJECT_COMPUTE_UNIT_USAGE_JSON
            )
        )


class UTestProjectParams:
    @staticmethod
    def utest_properties():
        common.check_project_params(
            ProjectParams().from_dict(common.PROJECT_JSON)
        )


@pytest.mark.usefixtures("mock")
class UTestProject:
    @staticmethod
    def utest_read():
        common.check_project_params(Project().read().params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_tests():
        resp = Project().tests()

        assert len(resp) == 2

        for ret in resp:
            common.check_test_params(ret.params, False)

        assert not httpretty.last_request().parsed_body
        assert httpretty.last_request().method == httpretty.GET

    @staticmethod
    def utest_files():
        resp = Project().files()

        assert len(resp) == 2

        for ret in resp:
            common.check_file_params(ret.params)

        assert not httpretty.last_request().parsed_body
        assert httpretty.last_request().method == httpretty.GET

    @staticmethod
    def utest_runs():
        resp = Project().runs()

        assert len(resp) == 2

        for ret in resp:
            common.check_run_params(ret.params)

        assert not httpretty.last_request().parsed_body
        assert httpretty.last_request().method == httpretty.GET


@pytest.mark.usefixtures("mock")
class UTestProjectAPI:
    @staticmethod
    def utest_read():
        common.check_project_params(ProjectAPI().read())

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body
