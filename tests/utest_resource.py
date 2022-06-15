"""Resource module tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import pytest
from dateutil import parser
from loadero_python.resources.resource import (
    Serializable,
    ParamsSerializer,
    from_dict_as_list,
)
from loadero_python.resources.group import GroupParams
from . import common


class UTestSerializable:
    def utest_to_dict(self):
        s = Serializable()
        with pytest.raises(NotImplementedError):
            s.to_dict()

    def utest_to_dict_full(self):
        s = Serializable()
        with pytest.raises(NotImplementedError):
            s.to_dict_full()

    def utest_from_dict(self):
        s = Serializable()
        with pytest.raises(NotImplementedError):
            s.from_dict({})


class UTestParamsSerializer:
    def utest_to_dict(self):
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

    def utest_to_dict_ignore_missing(self):
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

    def utest_to_dict_required_missing(self):
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

    def utest_to_dict_list_field(self):
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
        ps.__dict__["_down"] = [common.created_time, common.updated_time]
        ps.__dict__["_left"] = "999"

        assert ps.to_dict() == {
            "up": [
                "2022-04-01 13:54:25.689000+00:00",
                "2024-02-03 15:42:54.689000+00:00",
            ],
            "right": "999",
        }

    def utest_to_dict_full(self):
        ps = ParamsSerializer(
            attribute_map={
                "hi": "bye",
                "up": "_down",
                "right": "_left",
            },
        )

        ps.__dict__["bye"] = 123
        ps.__dict__["_down"] = [common.created_time, common.updated_time]
        ps.__dict__["_left"] = "999"

        assert ps.to_dict_full() == {
            "up": [
                "2022-04-01 13:54:25.689000+00:00",
                "2024-02-03 15:42:54.689000+00:00",
            ],
            "right": "999",
            "hi": 123,
        }

    def utest_from_dict(self):
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
        assert ps._down == [common.created_time, common.updated_time]
        assert ps._left == "999"


def utest_from_dict_as_list():

    f = from_dict_as_list(GroupParams)

    ret = f([])
    assert not ret

    g1 = common.group_json.copy()
    g1["id"] += 1

    g2 = common.group_json.copy()
    g2["id"] += 2

    g3 = common.group_json.copy()
    g3["id"] += 3

    ret = f([g1, g2, g3])

    assert len(ret) == 3

    for i, g in enumerate(ret):
        assert g.group_id == common.group_id + i + 1
        assert g.test_id == common.test_id
        assert g.created == common.created_time
        assert g.updated == common.updated_time
        assert g.name == "pytest_group"
        assert g.count == 8
        assert g.participant_count is None  # omit empty
        assert g.total_cu_count is None  # omit empty
