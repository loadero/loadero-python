"""Resource module tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-variable

import os
import httpretty
import pytest
from dateutil import parser
from loadero_python.resources.classificator import TestMode
from loadero_python.resources.resource import (
    LoaderoResource,
    QueryParams,
    Serializable,
    ParamsSerializer,
    from_dict_as_list,
    LoaderoResourceParams,
    URL,
)
from loadero_python.resources.group import GroupParams
from loadero_python.resources.test import TestFilterKey
from loadero_python.resources.metric_path import MetricPath, MetricBasePath
from loadero_python.api_client import APIClient
from . import common


@pytest.fixture(scope="class")
def api():
    httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(
        project_id=common.PROJECT_ID,
        access_token=common.ACCESS_TOKEN,
        api_base=common.API_BASE,
        rate_limit=False,
    )

    yield

    httpretty.disable()


@pytest.fixture(scope="function")
def reset():
    httpretty.reset()
    yield


class UTestSerializable:
    @staticmethod
    def utest_to_dict():
        s = Serializable()
        with pytest.raises(NotImplementedError):
            s.to_dict()

    @staticmethod
    def utest_to_dict_full():
        s = Serializable()
        with pytest.raises(NotImplementedError):
            s.to_dict_full()

    @staticmethod
    def utest_from_dict():
        s = Serializable()
        with pytest.raises(NotImplementedError):
            s.from_dict({})


class UTestParamsSerializer:
    @staticmethod
    def utest_to_dict():
        ps = ParamsSerializer(
            attribute_map={
                "hi": "bye",
                "up": "_down",
                "right": "_left",
            },
            body_attributes=[
                "up",
                "right",
            ],
            required_body_attributes=[
                "up",
            ],
        )

        ps.__dict__["bye"] = 123
        ps.__dict__["_down"] = "777"
        ps.__dict__["_left"] = "999"

        assert ps.to_dict() == {
            "up": "777",
            "right": "999",
        }

    @staticmethod
    def utest_to_dict_ignore_missing():
        ps = ParamsSerializer(
            attribute_map={
                "hi": "bye",
                "up": "_down",
                "right": "_left",
            },
            body_attributes=[
                "up",
                "right",
                "hi",
            ],
        )

        ps.__dict__["bye"] = None
        ps.__dict__["_down"] = None
        ps.__dict__["_left"] = None

        assert not ps.to_dict()

    @staticmethod
    def utest_to_dict_required_missing():
        ps = ParamsSerializer(
            attribute_map={
                "hi": "bye",
                "up": "_down",
                "right": "_left",
            },
            body_attributes=[
                "up",
                "right",
            ],
            required_body_attributes=[
                "up",
            ],
        )

        ps.__dict__["bye"] = 123
        ps.__dict__["_down"] = None
        ps.__dict__["_left"] = "999"

        with pytest.raises(ValueError):
            ps.to_dict()

    @staticmethod
    def utest_to_dict_list_field():
        ps = ParamsSerializer(
            attribute_map={
                "hi": "bye",
                "up": "_down",
                "right": "_left",
            },
            body_attributes=[
                "up",
                "right",
            ],
            required_body_attributes=[
                "up",
            ],
        )

        ps.__dict__["bye"] = 123
        ps.__dict__["_down"] = [common.CREATED_TIME, common.UPDATED_TIME]
        ps.__dict__["_left"] = "999"

        assert ps.to_dict() == {
            "up": [
                "2022-04-01 13:54:25.689000+00:00",
                "2024-02-03 15:42:54.689000+00:00",
            ],
            "right": "999",
        }

    @staticmethod
    def utest_to_dict_full():
        ps = ParamsSerializer(
            attribute_map={
                "hi": "bye",
                "up": "_down",
                "right": "_left",
            },
        )

        ps.__dict__["bye"] = 123
        ps.__dict__["_down"] = [common.CREATED_TIME, common.UPDATED_TIME]
        ps.__dict__["_left"] = "999"

        assert ps.to_dict_full() == {
            "up": [
                "2022-04-01 13:54:25.689000+00:00",
                "2024-02-03 15:42:54.689000+00:00",
            ],
            "right": "999",
            "hi": 123,
        }

    @staticmethod
    def utest_from_dict():
        ps = ParamsSerializer(
            attribute_map={
                "hi": "bye",
                "up": "_down",
                "right": "_left",
            },
            custom_deserializers={"up": lambda x: [parser.parse(d) for d in x]},
        )

        ps.from_dict(
            {
                "hi": 123,
                "up": [
                    "2022-04-01 13:54:25.689000+00:00",
                    "2024-02-03 15:42:54.689000+00:00",
                ],
                "right": "999",
            }
        )

        # pylint: disable=no-member
        # pylint: disable=protected-access
        assert ps.bye == 123
        assert ps._down == [common.CREATED_TIME, common.UPDATED_TIME]
        assert ps._left == "999"


class UTestLoaderoResourceParams:
    @staticmethod
    def utest_str():
        p1 = LoaderoResourceParams(
            attribute_map={
                "aaaa": "_aaaa",
                "bbbb": "_bbbb",
                "cccc": "_cccc",
            },
        )

        p1.__dict__["_aaaa"] = "111"
        p1.__dict__["_bbbb"] = 222
        p1.__dict__["_cccc"] = 333

        p2 = LoaderoResourceParams(
            attribute_map={
                "dddd": "_dddd",
                "eeee": "_eeee",
                "ffff": "ffff",
            },
        )

        p2.__dict__["_dddd"] = 123
        p2.__dict__["_eeee"] = "eeee"
        p2.__dict__["ffff"] = p1

        assert (
            str(p2)
            == """{
    "dddd": 123,
    "eeee": "eeee",
    "ffff": {
        "aaaa": "111",
        "bbbb": 222,
        "cccc": 333
    }
}"""
        )


class UTestLoaderoResource:
    @staticmethod
    def utest_str():
        p1 = LoaderoResourceParams(
            attribute_map={
                "aaaa": "_aaaa",
                "bbbb": "_bbbb",
                "cccc": "_cccc",
            },
        )

        p1.__dict__["_aaaa"] = "111"
        p1.__dict__["_bbbb"] = 222
        p1.__dict__["_cccc"] = 333

        p2 = LoaderoResourceParams(
            attribute_map={
                "dddd": "_dddd",
                "eeee": "_eeee",
                "ffff": "ffff",
            },
        )

        p2.__dict__["_dddd"] = 123
        p2.__dict__["_eeee"] = "eeee"
        p2.__dict__["ffff"] = p1

        assert (
            str(LoaderoResource(p2))
            == """{
    "dddd": 123,
    "eeee": "eeee",
    "ffff": {
        "aaaa": "111",
        "bbbb": 222,
        "cccc": 333
    }
}"""
        )


class UTestFromDictAsList:
    @staticmethod
    def utest_valid():
        f = from_dict_as_list(GroupParams)

        g1 = common.GROUP_JSON.copy()
        g1["id"] += 1

        g2 = common.GROUP_JSON.copy()
        g2["id"] += 2

        g3 = common.GROUP_JSON.copy()
        g3["id"] += 3

        ret = f([g1, g2, g3])

        assert len(ret) == 3

        for i, g in enumerate(ret):
            assert g.group_id == common.GROUP_ID + i + 1
            assert g.test_id == common.TEST_ID
            assert g.created == common.CREATED_TIME
            assert g.updated == common.UPDATED_TIME
            assert g.name == "pytest_group"
            assert g.count == 8
            assert g.participant_count == 331
            assert g.total_cu_count == 1234

    @staticmethod
    def utest_empty_json_value():
        f = from_dict_as_list(GroupParams)
        # pylint: disable=use-implicit-booleaness-not-comparison
        assert f([]) == []

    @staticmethod
    def utest_null_json_value():
        f = from_dict_as_list(GroupParams)
        # pylint: disable=use-implicit-booleaness-not-comparison
        assert f(None) == []


class UTestQueryParams:
    @staticmethod
    def utest_limit():
        qp = QueryParams()
        qp.limit(30)
        assert qp.parse() == [("limit", 30)]

    @staticmethod
    def utest_offset():
        qp = QueryParams()
        qp.offset(30)
        assert qp.parse() == [("offset", 30)]

    @staticmethod
    def utest_filter_str():
        qp = QueryParams()
        qp.filter(TestFilterKey.TEST_MODE, "test_mode")
        assert qp.parse() == [
            ("filter_test_mode", "test_mode"),
        ]

        qp = QueryParams()
        qp.filter(TestFilterKey.TEST_MODE, "test_mode", "test_mode2")
        assert qp.parse() == [
            ("filter_test_mode", "test_mode"),
            ("filter_test_mode", "test_mode2"),
        ]

    @staticmethod
    def utest_filter_int():
        qp = QueryParams()
        qp.filter(TestFilterKey.TEST_MODE, 1)
        assert qp.parse() == [
            ("filter_test_mode", 1),
        ]

        qp = QueryParams()
        qp.filter(TestFilterKey.TEST_MODE, 1, 3)
        assert qp.parse() == [
            ("filter_test_mode", 1),
            ("filter_test_mode", 3),
        ]

    @staticmethod
    def utest_filter_classificator():
        qp = QueryParams()
        qp.filter(TestFilterKey.TEST_MODE, TestMode.TM_PERFORMANCE)
        assert qp.parse() == [
            ("filter_test_mode", "performance"),
        ]

        qp = QueryParams()
        qp.filter(
            TestFilterKey.TEST_MODE, TestMode.TM_PERFORMANCE, TestMode.TM_LOAD
        )
        assert qp.parse() == [
            ("filter_test_mode", "performance"),
            ("filter_test_mode", "load"),
        ]

    @staticmethod
    def utest_filter_metric_path():
        qp = QueryParams()
        qp.filter(TestFilterKey.TEST_MODE, MetricPath.MACHINE_CPU_USED_1ST)
        assert qp.parse() == [
            ("filter_test_mode", "machine/cpu/used/1st"),
        ]

        qp = QueryParams()
        qp.filter(
            TestFilterKey.TEST_MODE,
            MetricPath.MACHINE_CPU_PERCENT_50TH,
            MetricBasePath.MACHINE_CPU_PERCENT,
        )
        assert qp.parse() == [
            ("filter_test_mode", "machine/cpu/percent/50th"),
            ("filter_test_mode", "machine/cpu/percent"),
        ]

    @staticmethod
    def utest_filter_no_values():
        qp = QueryParams()
        qp.filter(TestFilterKey.TEST_MODE)

        assert not qp.parse()


class UTestURL:
    @staticmethod
    def utest_init():
        u = URL()
        assert u.url() == ""

        u = URL("hello")
        assert u.url() == "hello"

    @staticmethod
    @pytest.mark.usefixtures("api", "reset")
    def utest_download():
        httpretty.register_uri(
            httpretty.GET,
            common.API_BASE + "route/file",
            body='{"hello":"world"}',
        )

        u = URL(common.API_BASE + "route/file")
        u.download()

        with open("file", "rb") as f:
            assert f.read() == b'{"hello":"world"}'

        os.remove("file")
