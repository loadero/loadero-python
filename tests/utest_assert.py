"""Assert resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from dateutil import parser
from loadero_python.api_client import APIClient
from loadero_python.resources.assert_resource import (
    AssertParams,
    Assert,
    AssertAPI,
)
from loadero_python.resources.classificator import Operator
from loadero_python.resources.metric_path import MetricPath
from . import identifiers


created_time = parser.parse("2022-04-01T13:54:25.689Z")
updated_time = parser.parse("2024-02-03T15:42:54.689Z")


sample_assert_json = {
    "id": identifiers.assert_id,
    "test_id": identifiers.test_id,
    "created": "2022-04-01T13:54:25.689Z",
    "updated": "2024-02-03T15:42:54.689Z",
    "expected": "892",
    "operator": "gt",
    "path": "machine/network/bitrate/in/avg",
}


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(
        identifiers.project_id, identifiers.access_token, identifiers.api_base
    )

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/asserts/$"
        ),
        body=json.dumps(sample_assert_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/$"
        ),
        body=json.dumps(sample_assert_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    upd = sample_assert_json.copy()
    upd["expected"] = "532"
    upd["operator"] = "lt"
    upd["path"] = "machine/cpu/used/avg"

    # update
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

    dupl = sample_assert_json.copy()
    dupl["id"] += 1

    # duplicate
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/asserts/\d*/copy/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestAssertParams:
    def utest_str(self):
        a = AssertParams()
        dupl = sample_assert_json.copy()
        a.from_json(dupl)

        assert (
            str(a)
            == """|----------|----------------------------------|
| created  | 2022-04-01 13:54:25.689000+00:00 |
| expected | 892                              |
| id       | 29643                            |
| operator | gt                               |
| path     | machine/network/bitrate/in/avg   |
| test_id  | 12734                            |
| updated  | 2024-02-03 15:42:54.689000+00:00 |"""
        )

    def utest_created(self):
        a = AssertParams()
        a.__dict__["_created"] = created_time
        assert a.created == created_time

    def utest_updated(self):
        a = AssertParams()
        a.__dict__["_updated"] = updated_time
        assert a.updated == updated_time

    def utest_with_id(self):
        a = AssertParams()
        a.with_id(5)
        assert a.assert_id == 5

    def utest_in_test(self):
        a = AssertParams()
        a.in_test(5)
        assert a.test_id == 5

    def utest_with_pats(self):
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
                test_id=identifiers.test_id,
                path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                operator=Operator.O_GT,
                expected="892",
            )
        )

        a.create()

        assert a.params.assert_id == identifiers.assert_id
        assert a.params.test_id == identifiers.test_id
        assert a.params.created == created_time
        assert a.params.updated == updated_time
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
            assert_id=identifiers.assert_id,
            test_id=identifiers.test_id,
        )

        a.read()

        assert a.params.assert_id == identifiers.assert_id
        assert a.params.test_id == identifiers.test_id
        assert a.params.created == created_time
        assert a.params.updated == updated_time
        assert a.params.expected == "892"
        assert a.params.operator is Operator.O_GT
        assert a.params.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert httpretty.last_request().parsed_body == ""

    def utest_update(self):

        a = Assert(
            params=AssertParams(
                assert_id=identifiers.assert_id,
                test_id=identifiers.test_id,
                path=MetricPath.MACHINE_CPU_USED_AVG,
                operator=Operator.O_LT,
                expected="532",
            )
        )

        a.update()

        assert a.params.assert_id == identifiers.assert_id
        assert a.params.test_id == identifiers.test_id
        assert a.params.created == created_time
        assert a.params.updated == updated_time
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
                assert_id=identifiers.assert_id, test_id=identifiers.test_id
            )
        )

        a.delete()

        assert a.params.assert_id == identifiers.assert_id
        assert a.params.test_id == identifiers.test_id
        assert a.params.created is None
        assert a.params.updated is None
        assert a.params.expected is None
        assert a.params.operator is None
        assert a.params.path is None

        assert httpretty.last_request().parsed_body == ""

    def utest_duplicate(self):
        a = Assert(
            params=AssertParams(
                assert_id=identifiers.assert_id, test_id=identifiers.test_id
            )
        )

        dupl = a.duplicate()

        assert dupl.params.assert_id == identifiers.assert_id + 1
        assert dupl.params.test_id == identifiers.test_id
        assert dupl.params.created == created_time
        assert dupl.params.updated == updated_time
        assert dupl.params.expected == "892"
        assert dupl.params.operator is Operator.O_GT
        assert dupl.params.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert a.params.assert_id == identifiers.assert_id
        assert a.params.test_id == identifiers.test_id
        assert a.params.created is None
        assert a.params.updated is None
        assert a.params.expected is None
        assert a.params.operator is None
        assert a.params.path is None

        assert httpretty.last_request().parsed_body is None


@pytest.mark.usefixtures("mock")
class UTestAssertAPI:
    def utest_create(self):
        ret = AssertAPI.create(
            AssertParams(
                test_id=identifiers.test_id,
                path=MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG,
                operator=Operator.O_GT,
                expected="892",
            )
        )

        assert ret.assert_id == identifiers.assert_id
        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
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
                assert_id=identifiers.assert_id,
                test_id=identifiers.test_id,
            )
        )

        assert ret.assert_id == identifiers.assert_id
        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.expected == "892"
        assert ret.operator is Operator.O_GT
        assert ret.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert httpretty.last_request().parsed_body == ""

    def utest_read_invalid_params(self):
        with pytest.raises(Exception):
            AssertAPI.read(AssertParams(assert_id=identifiers.assert_id))

        with pytest.raises(Exception):
            AssertAPI.read(AssertParams(test_id=identifiers.test_id))

        with pytest.raises(Exception):
            AssertAPI.read(AssertParams())

    def utest_update(self):
        ret = AssertAPI.update(
            AssertParams(
                assert_id=identifiers.assert_id,
                test_id=identifiers.test_id,
                path=MetricPath.MACHINE_CPU_USED_AVG,
                operator=Operator.O_LT,
                expected="532",
            )
        )

        assert ret.assert_id == identifiers.assert_id
        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
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
            AssertAPI.update(AssertParams(assert_id=identifiers.assert_id))

        with pytest.raises(Exception):
            AssertAPI.update(AssertParams(test_id=identifiers.test_id))

        with pytest.raises(Exception):
            AssertAPI.update(AssertParams())

    def utest_delete(self):
        ret = AssertAPI.delete(
            AssertParams(
                assert_id=identifiers.assert_id, test_id=identifiers.test_id
            )
        )

        assert ret is None

        assert httpretty.last_request().parsed_body == ""

    def utest_delete_invalid_params(self):
        with pytest.raises(Exception):
            AssertAPI.delete(AssertParams(assert_id=identifiers.assert_id))

        with pytest.raises(Exception):
            AssertAPI.delete(AssertParams(test_id=identifiers.test_id))

        with pytest.raises(Exception):
            AssertAPI.delete(AssertParams())

    def utest_duplicate(self):
        ret = AssertAPI.duplicate(
            AssertParams(
                assert_id=identifiers.assert_id, test_id=identifiers.test_id
            )
        )

        assert ret.assert_id == identifiers.assert_id + 1
        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.expected == "892"
        assert ret.operator is Operator.O_GT
        assert ret.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG

        assert httpretty.last_request().parsed_body is None

    def utest_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            AssertAPI.duplicate(AssertParams(assert_id=identifiers.assert_id))

        with pytest.raises(Exception):
            AssertAPI.duplicate(AssertParams(test_id=identifiers.test_id))

        with pytest.raises(Exception):
            AssertAPI.duplicate(AssertParams())

    def utest_read_all(self):
        AssertAPI.read_all(5)
