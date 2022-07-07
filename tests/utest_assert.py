"""Assert resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.assert_resource import (
    AssertParams,
    Assert,
    AssertAPI,
)
from loadero_python.resources.classificator import Operator
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
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/asserts/$"
        ),
        body=json.dumps(common.assert_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/$"
        ),
        body=json.dumps(common.assert_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/$"
        ),
        body=json.dumps(common.assert_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # delete
    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/$"
        ),
    )

    # duplicate
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/copy/$"
        ),
        body=json.dumps(common.assert_json),
        forcing_headers={"Content-Type": "application/json"},
    )

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

    # read all preconditions
    pg = common.paged_response.copy()
    pg["results"] = [
        common.assert_precondition_json,
        common.assert_precondition_json,
    ]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestAssertParams:
    def utest_str(self):
        a = AssertParams()
        a.from_dict(common.assert_json)

        assert (
            str(a)
            == """{
    "id": 29643,
    "test_id": 12734,
    "path": "machine/network/bitrate/in/avg",
    "operator": "gt",
    "expected": "892",
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00"
}"""
        )

    def utest_created(self):
        a = AssertParams()
        a.__dict__["_created"] = common.created_time
        assert a.created == common.created_time

    def utest_updated(self):
        a = AssertParams()
        a.__dict__["_updated"] = common.updated_time
        assert a.updated == common.updated_time

    def utest_with_id(self):
        a = AssertParams()
        a.with_id(5)
        assert a.assert_id == 5

    def utest_in_test(self):
        a = AssertParams()
        a.in_test(5)
        assert a.test_id == 5

    def utest_with_path(self):
        a = AssertParams()
        a.with_path(MetricPath.MACHINE_CPU_PERCENT_25TH)
        assert a.path is MetricPath.MACHINE_CPU_PERCENT_25TH

    def utest_with_operator(self):
        a = AssertParams()
        a.with_operator(Operator.O_GT)
        assert a.operator is Operator.O_GT

    def utest_with_expected(self):
        a = AssertParams()
        a.with_expected("123")
        assert a.expected == "123"


@pytest.mark.usefixtures("mock")
class UTestAssert:
    def utest_create(self):
        a = Assert(
            params=AssertParams(
                test_id=common.test_id,
                path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                operator=Operator.O_GT,
                expected="892",
            )
        )

        a.create()

        common.check_assert_params(a.params)

        assert httpretty.last_request().method == httpretty.POST
        assert (
            httpretty.last_request().parsed_body == common.assert_request_json
        )

    def utest_read(self):
        a = Assert(
            assert_id=common.assert_id,
            test_id=common.test_id,
        )

        a.read()

        common.check_assert_params(a.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_update(self):
        a = Assert(
            params=AssertParams(
                assert_id=common.assert_id,
                test_id=common.test_id,
                path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                operator=Operator.O_GT,
                expected="892",
            )
        )

        a.update()

        common.check_assert_params(a.params)

        assert httpretty.last_request().method == httpretty.PUT
        assert (
            httpretty.last_request().parsed_body == common.assert_request_json
        )

    def utest_delete(self):
        a = Assert(
            params=AssertParams(
                assert_id=common.assert_id, test_id=common.test_id
            )
        )

        a.delete()

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    def utest_duplicate(self):
        a = Assert(
            params=AssertParams(
                assert_id=common.assert_id, test_id=common.test_id
            )
        )

        dupl = a.duplicate()

        common.check_assert_params(dupl.params)

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    def utest_preconditions(self):
        a = Assert(assert_id=common.assert_id, test_id=common.test_id)

        ps = a.preconditions()

        for p in ps:
            common.check_assert_precondition_params(p.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_preconditions_invalid_params(self):
        a = Assert()

        with pytest.raises(ValueError):
            a.preconditions()

        a = Assert(test_id=common.test_id)

        with pytest.raises(ValueError):
            a.preconditions()


@pytest.mark.usefixtures("mock")
class UTestAssertAPI:
    def utest_create(self):
        ret = AssertAPI.create(
            AssertParams(
                test_id=common.test_id,
                path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                operator=Operator.O_GT,
                expected="892",
            )
        )

        common.check_assert_params(ret)

        assert httpretty.last_request().method == httpretty.POST
        assert (
            httpretty.last_request().parsed_body == common.assert_request_json
        )

    def utest_read(self):
        ret = AssertAPI.read(
            AssertParams(
                assert_id=common.assert_id,
                test_id=common.test_id,
            )
        )

        common.check_assert_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_update(self):
        ret = AssertAPI.update(
            AssertParams(
                assert_id=common.assert_id,
                test_id=common.test_id,
                path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                operator=Operator.O_GT,
                expected="892",
            )
        )

        common.check_assert_params(ret)

        assert httpretty.last_request().method == httpretty.PUT
        assert (
            httpretty.last_request().parsed_body == common.assert_request_json
        )

    def utest_delete(self):
        ret = AssertAPI.delete(
            AssertParams(assert_id=common.assert_id, test_id=common.test_id)
        )

        assert ret is None

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    def utest_duplicate(self):
        ret = AssertAPI.duplicate(
            AssertParams(assert_id=common.assert_id, test_id=common.test_id)
        )

        common.check_assert_params(ret)

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    def utest_read_all(self):
        ret = AssertAPI.read_all(common.test_id)

        assert len(ret) == 2

        for r in ret:
            common.check_assert_params(r)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_all_no_results(self):
        pg = common.paged_response.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                r"^http://mock\.loadero\.api/v2/"
                r"projects/\d*/tests/\d*/asserts/$"
            ),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        ret = AssertAPI.read_all(common.test_id)

        assert len(ret) == 0

        assert httpretty.last_request().method == httpretty.GET
        assert httpretty.last_request().parsed_body == ""

    def utest_route(self):
        assert (
            AssertAPI.route(common.test_id)
            == "http://mock.loadero.api/v2/projects/538591/tests/12734/asserts/"
        )
        assert (
            AssertAPI.route(common.test_id, common.assert_id)
            == "http://mock.loadero.api"
            "/v2/projects/538591/tests/12734/asserts/29643/"
        )

    def utest_validate_identifiers(self):
        with pytest.raises(Exception):
            AssertAPI.read(AssertParams())

        with pytest.raises(Exception):
            AssertAPI.read(AssertParams(test_id=common.test_id))
