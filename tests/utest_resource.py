"""Resource module tests"""


# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import pytest
from loadero_python.resources.resource import to_json, from_json, to_string


class UTestToJSON:
    def utest_valid(self):
        r = {"_created": "yesterday", "resource_id": 5, "ignored": "hello"}
        am = {"_created": "created", "resource_id": "id"}
        ba = {"id"}

        assert to_json(r, am, ba) == {"id": 5}

    def utest_required_param_none(self):
        r = {"resource_id": None}
        am = {"_created": "created", "resource_id": "id"}
        ba = {"id"}

        with pytest.raises(Exception):
            to_json(r, am, ba)


class UTestFromJSON:
    def utest_valid(self):
        r = {"_created": "yesterday", "resource_id": 5, "ignored": "hello"}
        jv = {"created": "tomorrow", "id": 4, "unused": "field"}
        am = {"_created": "created", "resource_id": "id"}

        cd = {"created": lambda x: x + "_morning"}

        assert from_json(r, jv, am, cd) is None
        assert r == {
            "_created": "tomorrow_morning",
            "ignored": "hello",
            "resource_id": 4,
        }


def utest_to_string():
    r = {"_created": "yesterday", "resource_id": 5, "ignored": "hello"}
    am = {"_created": "created", "resource_id": "id"}

    assert (
        to_string(r, am)
        == """|---------|-----------|
| created | yesterday |
| id      | 5         |"""
    )
