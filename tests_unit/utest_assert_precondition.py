"""Assert precondition resource tests"""


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
    AssertPreconditionParams,
    AssertPrecondition,
    AssertPreconditionAPI,
)
from loadero_python.resources.classificator import Operator, Property
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
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/$"
        ),
        body=json.dumps(common.ASSERT_PRECONDITION_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/\d*/$"
        ),
        body=json.dumps(common.ASSERT_PRECONDITION_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/\d*/$"
        ),
        body=json.dumps(common.ASSERT_PRECONDITION_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # delete
    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/\d*/$"
        ),
    )

    # read all
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


class UTestAssertPreconditionParams:
    @staticmethod
    def utest_str():
        ap = AssertPreconditionParams().from_dict(
            common.ASSERT_PRECONDITION_JSON
        )

        assert (
            str(ap)
            == """{
    "id": 9862123,
    "assert_id": 29643,
    "expected": "10",
    "operator": "gt",
    "property": "group_num",
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00"
}"""
        )

    @staticmethod
    def utest_created():
        ap = AssertPreconditionParams()
        ap.__dict__["_created"] = common.CREATED_TIME
        assert ap.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        ap = AssertPreconditionParams()
        ap.__dict__["_updated"] = common.UPDATED_TIME
        assert ap.updated == common.UPDATED_TIME

    @staticmethod
    def utest_with_id():
        ap = AssertPreconditionParams()
        ap.with_id(common.ASSERT_PRECONDITION_ID)
        assert ap.assert_precondition_id == common.ASSERT_PRECONDITION_ID

    @staticmethod
    def utest_for_assert():
        ap = AssertPreconditionParams()
        ap.for_assert(common.ASSERT_ID)
        assert ap.assert_id == common.ASSERT_ID

    @staticmethod
    def utest_in_test():
        ap = AssertPreconditionParams()
        ap.in_test(common.TEST_ID)
        assert ap.test_id == common.TEST_ID

    @staticmethod
    def utest_with_expected():
        ap = AssertPreconditionParams()
        ap.with_expected("hi")
        assert ap.expected == "hi"

    @staticmethod
    def utest_with_operator():
        ap = AssertPreconditionParams()
        ap.with_operator(Operator.O_LT)
        assert ap.operator == Operator.O_LT

    @staticmethod
    def utest_with_property():
        ap = AssertPreconditionParams()
        ap.with_property(Property.P_LOCATION)
        assert ap.precondition_property == Property.P_LOCATION


@pytest.mark.usefixtures("mock")
class UTestAssertPrecondition:
    @staticmethod
    def utest_init():
        ap = AssertPrecondition(
            test_id=common.TEST_ID,
            assert_id=common.ASSERT_ID,
            assert_precondition_id=common.ASSERT_PRECONDITION_ID,
        )

        assert ap.params.test_id == common.TEST_ID
        assert ap.params.assert_id == common.ASSERT_ID
        assert ap.params.assert_precondition_id == common.ASSERT_PRECONDITION_ID

    @staticmethod
    def utest_create():
        ap = AssertPrecondition(
            params=AssertPreconditionParams(
                test_id=common.TEST_ID,
                assert_id=common.ASSERT_ID,
                expected="10",
                operator=Operator.O_GT,
                precondition_property=Property.P_GROUP_NUM,
            )
        )

        ap.create()

        common.check_assert_precondition_params(ap.params)

        assert httpretty.last_request().method == httpretty.POST
        assert (
            httpretty.last_request().parsed_body
            == common.ASSERT_PRECONDITION_REQUEST_JSON
        )

    @staticmethod
    def utest_read():
        ap = AssertPrecondition(
            params=AssertPreconditionParams(
                test_id=common.TEST_ID,
                assert_id=common.ASSERT_ID,
                assert_precondition_id=common.ASSERT_PRECONDITION_ID,
            )
        )

        ap.read()

        common.check_assert_precondition_params(ap.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        ap = AssertPrecondition(
            params=AssertPreconditionParams(
                test_id=common.TEST_ID,
                assert_id=common.ASSERT_ID,
                assert_precondition_id=common.ASSERT_PRECONDITION_ID,
                expected="10",
                operator=Operator.O_GT,
                precondition_property=Property.P_GROUP_NUM,
            )
        )

        ap.update()

        common.check_assert_precondition_params(ap.params)

        assert httpretty.last_request().method == httpretty.PUT
        assert (
            httpretty.last_request().parsed_body
            == common.ASSERT_PRECONDITION_REQUEST_JSON
        )

    @staticmethod
    def utest_delete():
        ap = AssertPrecondition(
            params=AssertPreconditionParams()
            .from_dict(common.ASSERT_PRECONDITION_JSON)
            .in_test(common.TEST_ID)
        )

        ap.delete()

        common.check_assert_precondition_params(ap.params)

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body


@pytest.mark.usefixtures("mock")
class UTestAssertPreconditionAPI:
    @staticmethod
    def utest_create():
        ret = AssertPreconditionAPI.create(
            AssertPreconditionParams(
                test_id=common.TEST_ID,
                assert_id=common.ASSERT_ID,
                expected="10",
                operator=Operator.O_GT,
                precondition_property=Property.P_GROUP_NUM,
            )
        )

        common.check_assert_precondition_params(ret)

        assert httpretty.last_request().method == httpretty.POST
        assert (
            httpretty.last_request().parsed_body
            == common.ASSERT_PRECONDITION_REQUEST_JSON
        )

    @staticmethod
    def utest_read():
        ret = AssertPreconditionAPI.read(
            AssertPreconditionParams(
                test_id=common.TEST_ID,
                assert_id=common.ASSERT_ID,
                assert_precondition_id=common.ASSERT_PRECONDITION_ID,
            )
        )

        common.check_assert_precondition_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        ret = AssertPreconditionAPI.update(
            AssertPreconditionParams(
                test_id=common.TEST_ID,
                assert_id=common.ASSERT_ID,
                assert_precondition_id=common.ASSERT_PRECONDITION_ID,
                expected="10",
                operator=Operator.O_GT,
                precondition_property=Property.P_GROUP_NUM,
            )
        )

        common.check_assert_precondition_params(ret)

        assert httpretty.last_request().method == httpretty.PUT
        assert (
            httpretty.last_request().parsed_body
            == common.ASSERT_PRECONDITION_REQUEST_JSON
        )

    @staticmethod
    def utest_delete():
        assert (
            AssertPreconditionAPI.delete(
                AssertPreconditionParams(
                    test_id=common.TEST_ID,
                    assert_id=common.ASSERT_ID,
                    assert_precondition_id=common.ASSERT_PRECONDITION_ID,
                )
            )
            is None
        )

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all():
        resp = AssertPreconditionAPI.read_all(common.TEST_ID, common.ASSERT_ID)

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_assert_precondition_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_with_query_params():
        resp = AssertPreconditionAPI.read_all(
            common.TEST_ID,
            common.ASSERT_ID,
            query_params=common.build_query_params(
                list(AssertPreconditionFilterKey)
            ),
        )

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_assert_precondition_params(ret)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(AssertPreconditionFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert (
            AssertPreconditionAPI.route(
                common.TEST_ID, common.ASSERT_ID, common.ASSERT_PRECONDITION_ID
            )
            == "projects/538591/tests/12734/asserts/29643/"
            "preconditions/9862123/"
        )

        assert (
            AssertPreconditionAPI.route(common.TEST_ID, common.ASSERT_ID)
            == "projects/538591/tests/12734/asserts/29643/preconditions/"
        )

    @staticmethod
    def utest_validate_identifier():
        with pytest.raises(ValueError):
            AssertPreconditionAPI.read(AssertPreconditionParams())

        with pytest.raises(ValueError):
            AssertPreconditionAPI.read(
                AssertPreconditionParams(test_id=common.TEST_ID)
            )

        with pytest.raises(ValueError):
            AssertPreconditionAPI.read(
                AssertPreconditionParams(
                    test_id=common.TEST_ID, assert_id=common.ASSERT_ID
                )
            )
