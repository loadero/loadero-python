"""Assert resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member
# pylint: disable=unused-variable


import json
import re
from urllib.parse import urlparse, parse_qs
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.assert_precondition import (
    AssertPreconditionFilterKey,
)
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

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE, False)

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/asserts/$"
        ),
        body=json.dumps(common.ASSERT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/$"
        ),
        body=json.dumps(common.ASSERT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/$"
        ),
        body=json.dumps(common.ASSERT_JSON),
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
        body=json.dumps(common.ASSERT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

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

    # read all preconditions
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [
        common.ASSERT_PRECONDITION_JSON,
        common.ASSERT_PRECONDITION_JSON,
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
    @staticmethod
    def utest_str():
        a = AssertParams()
        a.from_dict(common.ASSERT_JSON)

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

    @staticmethod
    def utest_created():
        a = AssertParams()
        a.__dict__["_created"] = common.CREATED_TIME
        assert a.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        a = AssertParams()
        a.__dict__["_updated"] = common.UPDATED_TIME
        assert a.updated == common.UPDATED_TIME

    @staticmethod
    def utest_with_id():
        a = AssertParams()
        a.with_id(5)
        assert a.assert_id == 5

    @staticmethod
    def utest_in_test():
        a = AssertParams()
        a.in_test(5)
        assert a.test_id == 5

    @staticmethod
    def utest_with_path():
        a = AssertParams()
        a.with_path(MetricPath.MACHINE_CPU_PERCENT_25TH)
        assert a.path is MetricPath.MACHINE_CPU_PERCENT_25TH

    @staticmethod
    def utest_with_operator():
        a = AssertParams()
        a.with_operator(Operator.O_GT)
        assert a.operator is Operator.O_GT

    @staticmethod
    def utest_with_expected():
        a = AssertParams()
        a.with_expected("123")
        assert a.expected == "123"


@pytest.mark.usefixtures("mock")
class UTestAssert:
    @staticmethod
    def utest_create():
        common.check_assert_params(
            Assert(
                params=AssertParams(
                    test_id=common.TEST_ID,
                    path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                    operator=Operator.O_GT,
                    expected="892",
                )
            )
            .create()
            .params
        )

        assert httpretty.last_request().method == httpretty.POST
        assert (
            httpretty.last_request().parsed_body == common.assert_request_json
        )

    @staticmethod
    def utest_read():
        common.check_assert_params(
            Assert(
                assert_id=common.ASSERT_ID,
                test_id=common.TEST_ID,
            )
            .read()
            .params
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        common.check_assert_params(
            Assert(
                params=AssertParams(
                    assert_id=common.ASSERT_ID,
                    test_id=common.TEST_ID,
                    path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                    operator=Operator.O_GT,
                    expected="892",
                )
            )
            .update()
            .params
        )

        assert httpretty.last_request().method == httpretty.PUT
        assert (
            httpretty.last_request().parsed_body == common.assert_request_json
        )

    @staticmethod
    def utest_delete():
        Assert(
            params=AssertParams(
                assert_id=common.ASSERT_ID, test_id=common.TEST_ID
            )
        ).delete()

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_duplicate():
        common.check_assert_params(
            Assert(
                params=AssertParams(
                    assert_id=common.ASSERT_ID, test_id=common.TEST_ID
                )
            )
            .duplicate()
            .params
        )

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_preconditions():
        preconditions, pagination, filters = Assert(
            assert_id=common.ASSERT_ID, test_id=common.TEST_ID
        ).preconditions(
            common.build_query_params(list(AssertPreconditionFilterKey))
        )

        common.check_pagination_params(pagination)
        assert filters == common.FILTER_JSON

        assert len(preconditions) == 2

        for ret in preconditions:
            common.check_assert_precondition_params(ret.params)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(AssertPreconditionFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_preconditions_invalid_params():
        a = Assert()

        with pytest.raises(ValueError):
            a.preconditions()

        a = Assert(test_id=common.TEST_ID)

        with pytest.raises(ValueError):
            a.preconditions()


@pytest.mark.usefixtures("mock")
class UTestAssertAPI:
    @staticmethod
    def utest_create():
        common.check_assert_params(
            AssertAPI.create(
                AssertParams(
                    test_id=common.TEST_ID,
                    path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                    operator=Operator.O_GT,
                    expected="892",
                )
            )
        )

        assert httpretty.last_request().method == httpretty.POST
        assert (
            httpretty.last_request().parsed_body == common.assert_request_json
        )

    @staticmethod
    def utest_read():
        common.check_assert_params(
            AssertAPI.read(
                AssertParams(
                    assert_id=common.ASSERT_ID,
                    test_id=common.TEST_ID,
                )
            )
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        common.check_assert_params(
            AssertAPI.update(
                AssertParams(
                    assert_id=common.ASSERT_ID,
                    test_id=common.TEST_ID,
                    path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                    operator=Operator.O_GT,
                    expected="892",
                )
            )
        )

        assert httpretty.last_request().method == httpretty.PUT
        assert (
            httpretty.last_request().parsed_body == common.assert_request_json
        )

    @staticmethod
    def utest_delete():
        ret = AssertAPI.delete(
            AssertParams(assert_id=common.ASSERT_ID, test_id=common.TEST_ID)
        )

        assert ret is None

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_duplicate():
        common.check_assert_params(
            AssertAPI.duplicate(
                AssertParams(assert_id=common.ASSERT_ID, test_id=common.TEST_ID)
            )
        )

        assert httpretty.last_request().method == httpretty.POST
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all():
        resp = AssertAPI.read_all(common.TEST_ID)

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:  # pylint: disable=not-an-iterable
            common.check_assert_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert (
            AssertAPI.route(common.TEST_ID)
            == "projects/538591/tests/12734/asserts/"
        )
        assert (
            AssertAPI.route(common.TEST_ID, common.ASSERT_ID)
            == "projects/538591/tests/12734/asserts/29643/"
        )

    @staticmethod
    def utest_validate_identifiers():
        with pytest.raises(Exception):
            AssertAPI.read(AssertParams())

        with pytest.raises(Exception):
            AssertAPI.read(AssertParams(test_id=common.TEST_ID))
