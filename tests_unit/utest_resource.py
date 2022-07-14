"""Resource module tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-variable


import pytest
from dateutil import parser
from loadero_python.resources.resource import (
    LoaderoResource,
    Serializable,
    ParamsSerializer,
    from_dict_as_list,
    LoaderoResourceParams,
)
from loadero_python.resources.group import GroupParams
from . import common


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


def utest_from_dict_as_list():
    f = from_dict_as_list(GroupParams)

    ret = f([])
    assert not ret

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
