"""Resource module tests"""


# pylint: disable=missing-class-docstring


import pytest
from loadero_python.resources.resource import to_json, from_json, to_string


class TestToJSON:
    def test_valid(self):
        r = {"_created": "yesterday", "resource_id": 5, "ignored": "hello"}
        am = {"_created": "created", "resource_id": "id"}
        ba = {"id"}

        assert to_json(r, am, ba) == {"id": 5}

    def test_required_param_none(self):
        r = {"resource_id": None}
        am = {"_created": "created", "resource_id": "id"}
        ba = {"id"}

        with pytest.raises(Exception):
            to_json(r, am, ba)


class TestFromJSON:
    def test_valid(self):
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


def test_to_string():
    r = {"_created": "yesterday", "resource_id": 5, "ignored": "hello"}
    am = {"_created": "created", "resource_id": "id"}

    assert (
        to_string(r, am)
        == """|---------|-----------|
| created | yesterday |
| id      | 5         |"""
    )
