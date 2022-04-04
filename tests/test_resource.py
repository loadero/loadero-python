"""Resource module tests"""


# pylint: disable=wildcard-import


import pytest
from loadero_python.resources.resource import to_json
from .utils import *


def test_to_json():
    am = {"_created": "created", "resource_id": "id"}
    ba = {"id"}

    r = {"_created": "yesterday", "resource_id": 5, "ignored": "hello"}

    assert to_json(r, am, ba) == {"id": 5}

    r = {"resource_id": None}

    with pytest.raises(Exception):
        to_json(r, am, ba)
