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
    upd = common.assert_json.copy()
    upd["expected"] = "532"
    upd["operator"] = "lt"
    upd["path"] = "machine/cpu/used/avg"

    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/$"
        ),
        body=json.dumps(upd),
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
    dupl = common.assert_json.copy()
    dupl["id"] += 1

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/copy/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all
    pg = common.paged_response.copy()
    a1 = common.assert_json.copy()
    a1["id"] += 1

    a2 = common.assert_json.copy()
    a2["id"] += 2

    pg["results"] = [a1, a2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/$"
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

        assert a.params.assert_id == common.assert_id
        assert a.params.test_id == common.test_id
        assert a.params.created == common.created_time
        assert a.params.updated == common.updated_time
        assert a.params.expected == "892"
        assert a.params.operator is Operator.O_GT
        assert a.params.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert httpretty.last_request().parsed_body == {
            "expected": "892",
            "operator": "gt",
            "path": "machine/network/bitrate/in/avg",
        }

    def utest_read(self):
        a = Assert(
            assert_id=common.assert_id,
            test_id=common.test_id,
        )

        a.read()

        assert a.params.assert_id == common.assert_id
        assert a.params.test_id == common.test_id
        assert a.params.created == common.created_time
        assert a.params.updated == common.updated_time
        assert a.params.expected == "892"
        assert a.params.operator is Operator.O_GT
        assert a.params.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert httpretty.last_request().parsed_body == ""

    def utest_update(self):
        a = Assert(
            params=AssertParams(
                assert_id=common.assert_id,
                test_id=common.test_id,
                path=MetricPath.MACHINE_CPU_USED_AVG,
                operator=Operator.O_LT,
                expected="532",
            )
        )

        a.update()

        assert a.params.assert_id == common.assert_id
        assert a.params.test_id == common.test_id
        assert a.params.created == common.created_time
        assert a.params.updated == common.updated_time
        assert a.params.expected == "532"
        assert a.params.operator is Operator.O_LT
        assert a.params.path is MetricPath.MACHINE_CPU_USED_AVG

        assert httpretty.last_request().parsed_body == {
            "expected": "532",
            "operator": "lt",
            "path": "machine/cpu/used/avg",
        }

    def utest_delete(self):
        a = Assert(
            params=AssertParams(
                assert_id=common.assert_id, test_id=common.test_id
            )
        )

        a.delete()

        assert a.params.assert_id == common.assert_id
        assert a.params.test_id == common.test_id
        assert a.params.created is None
        assert a.params.updated is None
        assert a.params.expected is None
        assert a.params.operator is None
        assert a.params.path is None

        assert not httpretty.last_request().parsed_body

    def utest_duplicate(self):
        a = Assert(
            params=AssertParams(
                assert_id=common.assert_id, test_id=common.test_id
            )
        )

        dupl = a.duplicate()

        assert dupl.params.assert_id == common.assert_id + 1
        assert dupl.params.test_id == common.test_id
        assert dupl.params.created == common.created_time
        assert dupl.params.updated == common.updated_time
        assert dupl.params.expected == "892"
        assert dupl.params.operator is Operator.O_GT
        assert dupl.params.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert a.params.assert_id == common.assert_id
        assert a.params.test_id == common.test_id
        assert a.params.created is None
        assert a.params.updated is None
        assert a.params.expected is None
        assert a.params.operator is None
        assert a.params.path is None

        assert not httpretty.last_request().parsed_body


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

        assert ret.assert_id == common.assert_id
        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.expected == "892"
        assert ret.operator is Operator.O_GT
        assert ret.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert httpretty.last_request().parsed_body == {
            "expected": "892",
            "operator": "gt",
            "path": "machine/network/bitrate/in/avg",
        }

    def utest_create_invalid_params(self):
        with pytest.raises(Exception):
            AssertAPI.create(AssertParams())

    def utest_read(self):
        ret = AssertAPI.read(
            AssertParams(
                assert_id=common.assert_id,
                test_id=common.test_id,
            )
        )

        assert ret.assert_id == common.assert_id
        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.expected == "892"
        assert ret.operator is Operator.O_GT
        assert ret.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert not httpretty.last_request().parsed_body

    def utest_read_invalid_params(self):
        with pytest.raises(Exception):
            AssertAPI.read(AssertParams(assert_id=common.assert_id))

        with pytest.raises(Exception):
            AssertAPI.read(AssertParams(test_id=common.test_id))

        with pytest.raises(Exception):
            AssertAPI.read(AssertParams())

    def utest_update(self):
        ret = AssertAPI.update(
            AssertParams(
                assert_id=common.assert_id,
                test_id=common.test_id,
                path=MetricPath.MACHINE_CPU_USED_AVG,
                operator=Operator.O_LT,
                expected="532",
            )
        )

        assert ret.assert_id == common.assert_id
        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.expected == "532"
        assert ret.operator is Operator.O_LT
        assert ret.path is MetricPath.MACHINE_CPU_USED_AVG

        assert httpretty.last_request().parsed_body == {
            "expected": "532",
            "operator": "lt",
            "path": "machine/cpu/used/avg",
        }

    def utest_update_invalid_params(self):
        with pytest.raises(Exception):
            AssertAPI.update(AssertParams(assert_id=common.assert_id))

        with pytest.raises(Exception):
            AssertAPI.update(AssertParams(test_id=common.test_id))

        with pytest.raises(Exception):
            AssertAPI.update(AssertParams())

    def utest_delete(self):
        ret = AssertAPI.delete(
            AssertParams(assert_id=common.assert_id, test_id=common.test_id)
        )

        assert ret is None

        assert not httpretty.last_request().parsed_body

    def utest_delete_invalid_params(self):
        with pytest.raises(Exception):
            AssertAPI.delete(AssertParams(assert_id=common.assert_id))

        with pytest.raises(Exception):
            AssertAPI.delete(AssertParams(test_id=common.test_id))

        with pytest.raises(Exception):
            AssertAPI.delete(AssertParams())

    def utest_duplicate(self):
        ret = AssertAPI.duplicate(
            AssertParams(assert_id=common.assert_id, test_id=common.test_id)
        )

        assert ret.assert_id == common.assert_id + 1
        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.expected == "892"
        assert ret.operator is Operator.O_GT
        assert ret.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert not httpretty.last_request().parsed_body

    def utest_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            AssertAPI.duplicate(AssertParams(assert_id=common.assert_id))

        with pytest.raises(Exception):
            AssertAPI.duplicate(AssertParams(test_id=common.test_id))

        with pytest.raises(Exception):
            AssertAPI.duplicate(AssertParams())

    def utest_read_all(self):
        resp = AssertAPI.read_all(common.test_id)

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.assert_id == common.assert_id + i + 1
            assert ret.test_id == common.test_id
            assert ret.created == common.created_time
            assert ret.updated == common.updated_time
            assert ret.expected == "892"
            assert ret.operator is Operator.O_GT
            assert ret.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

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

        resp = AssertAPI.read_all(common.test_id)

        assert len(resp) == 0
        assert not httpretty.last_request().parsed_body

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
