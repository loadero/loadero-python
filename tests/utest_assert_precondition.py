"""Assert precondition resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.assert_precondition import (
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

    APIClient(common.project_id, common.access_token, common.api_base)

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/$"
        ),
        body=json.dumps(common.assert_precondition_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/\d*/$"
        ),
        body=json.dumps(common.assert_precondition_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api"
            r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/\d*/$"
        ),
        body=json.dumps(common.assert_precondition_json),
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


class UTestAssertPreconditionParams:
    def utest_str(self):
        ap = AssertPreconditionParams().from_dict(
            common.assert_precondition_json
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

    def utest_created(self):
        ap = AssertPreconditionParams()
        ap.__dict__["_created"] = common.created_time
        assert ap.created == common.created_time

    def utest_updated(self):
        ap = AssertPreconditionParams()
        ap.__dict__["_updated"] = common.updated_time
        assert ap.updated == common.updated_time

    def utest_with_id(self):
        ap = AssertPreconditionParams()
        ap.with_id(common.assert_precondition_id)
        assert ap.assert_precondition_id == common.assert_precondition_id

    def utest_for_assert(self):
        ap = AssertPreconditionParams()
        ap.for_assert(common.assert_id)
        assert ap.assert_id == common.assert_id

    def utest_in_test(self):
        ap = AssertPreconditionParams()
        ap.in_test(common.test_id)
        assert ap.test_id == common.test_id

    def utest_with_expected(self):
        ap = AssertPreconditionParams()
        ap.with_expected("hi")
        assert ap.expected == "hi"

    def utest_with_operator(self):
        ap = AssertPreconditionParams()
        ap.with_operator(Operator.O_LT)
        assert ap.operator == Operator.O_LT

    def utest_with_property(self):
        ap = AssertPreconditionParams()
        ap.with_property(Property.P_LOCATION)
        assert ap.procondition_property == Property.P_LOCATION


@pytest.mark.usefixtures("mock")
class UTestAssertPrecondition:
    def utest_init(self):
        ap = AssertPrecondition(
            test_id=common.test_id,
            assert_id=common.assert_id,
            assert_precondition_id=common.assert_precondition_id,
        )

        assert ap.params.test_id == common.test_id
        assert ap.params.assert_id == common.assert_id
        assert ap.params.assert_precondition_id == common.assert_precondition_id

    def utest_create(self):
        ap = AssertPrecondition(
            params=AssertPreconditionParams(
                test_id=common.test_id,
                assert_id=common.assert_id,
                expected="10",
                operator=Operator.O_GT,
                procondition_property=Property.P_GROUP_NUM,
            )
        )

        ap.create()

        common.check_assert_precondition_params(ap.params)

        assert httpretty.last_request().method == httpretty.POST
        assert (
            httpretty.last_request().parsed_body
            == common.assert_precondition_request_json
        )

    def utest_read(self):
        ap = AssertPrecondition(
            params=AssertPreconditionParams(
                test_id=common.test_id,
                assert_id=common.assert_id,
                assert_precondition_id=common.assert_precondition_id,
            )
        )

        ap.read()

        common.check_assert_precondition_params(ap.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_update(self):
        ap = AssertPrecondition(
            params=AssertPreconditionParams(
                test_id=common.test_id,
                assert_id=common.assert_id,
                assert_precondition_id=common.assert_precondition_id,
                expected="10",
                operator=Operator.O_GT,
                procondition_property=Property.P_GROUP_NUM,
            )
        )

        ap.update()

        common.check_assert_precondition_params(ap.params)

        assert httpretty.last_request().method == httpretty.PUT
        assert (
            httpretty.last_request().parsed_body
            == common.assert_precondition_request_json
        )

    def utest_delete(self):
        ap = AssertPrecondition(
            params=AssertPreconditionParams()
            .from_dict(common.assert_precondition_json)  # set created / updated
            .in_test(common.test_id)
        )

        ap.delete()

        common.check_assert_precondition_params(ap.params)

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body


@pytest.mark.usefixtures("mock")
class UTestAssertPreconditionAPI:
    def utest_create(self):
        ret = AssertPreconditionAPI.create(
            AssertPreconditionParams(
                test_id=common.test_id,
                assert_id=common.assert_id,
                expected="10",
                operator=Operator.O_GT,
                procondition_property=Property.P_GROUP_NUM,
            )
        )

        common.check_assert_precondition_params(ret)

        assert httpretty.last_request().method == httpretty.POST
        assert (
            httpretty.last_request().parsed_body
            == common.assert_precondition_request_json
        )

    def utest_read(self):
        ret = AssertPreconditionAPI.read(
            AssertPreconditionParams(
                test_id=common.test_id,
                assert_id=common.assert_id,
                assert_precondition_id=common.assert_precondition_id,
            )
        )

        common.check_assert_precondition_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_update(self):
        ret = AssertPreconditionAPI.update(
            AssertPreconditionParams(
                test_id=common.test_id,
                assert_id=common.assert_id,
                assert_precondition_id=common.assert_precondition_id,
                expected="10",
                operator=Operator.O_GT,
                procondition_property=Property.P_GROUP_NUM,
            )
        )

        common.check_assert_precondition_params(ret)

        assert httpretty.last_request().method == httpretty.PUT
        assert (
            httpretty.last_request().parsed_body
            == common.assert_precondition_request_json
        )

    def utest_delete(self):
        ret = AssertPreconditionAPI.delete(
            AssertPreconditionParams(
                test_id=common.test_id,
                assert_id=common.assert_id,
                assert_precondition_id=common.assert_precondition_id,
            )
        )

        assert ret is None

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    def utest_read_all(self):
        ret = AssertPreconditionAPI.read_all(common.test_id, common.assert_id)

        assert len(ret) == 2

        for r in ret:
            common.check_assert_precondition_params(r)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_all_no_results(self):
        pg = common.paged_response.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                r"^http://mock\.loadero\.api"
                r"/v2/projects/\d*/tests/\d*/asserts/\d*/preconditions/$"
            ),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        ret = AssertPreconditionAPI.read_all(common.test_id, common.assert_id)

        assert len(ret) == 0

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_route(self):
        assert (
            AssertPreconditionAPI.route(
                common.test_id, common.assert_id, common.assert_precondition_id
            )
            == "http://mock.loadero.api"
            "/v2/projects/538591/tests/12734/asserts/29643"
            "/preconditions/9862123/"
        )

        assert (
            AssertPreconditionAPI.route(common.test_id, common.assert_id)
            == "http://mock.loadero.api"
            "/v2/projects/538591/tests/12734/asserts/29643/preconditions/"
        )

    def utest_validate_identifier(self):
        with pytest.raises(ValueError):
            AssertPreconditionAPI.read(AssertPreconditionParams())

        with pytest.raises(ValueError):
            AssertPreconditionAPI.read(
                AssertPreconditionParams(test_id=common.test_id)
            )

        with pytest.raises(ValueError):
            AssertPreconditionAPI.read(
                AssertPreconditionParams(
                    test_id=common.test_id, assert_id=common.assert_id
                )
            )
