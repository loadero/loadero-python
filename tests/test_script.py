"""Script file resource tests"""

# pylint: disable=W0613
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=wildcard-import
# pylint: disable=protected-access


import os
import re
import json
import pytest
import httpretty
from dateutil import parser
from loadero_python.resources.test import TestParams, TestAPI
from loadero_python.resources.script import *
from .utils import *


access_token = os.environ.get("ACCESS_TOKEN", default="LOADERO_ACCESS_TOKEN")
api_base = os.environ.get("API_BASE", default="http://mock.loadero.api/v2/")
mock_api = os.environ.get("MOCK_API", default="true") == "true"
project_id = int(os.environ.get("PROJECT_ID", default="45"))


# Relative to repo root dir.
sample_test_script_py_path = "tests/res/sample_test_script.py"
sample_test_script_py_data = """def test_on_loadero(driver: TestUIDriver):
    print("hello test")
"""


time_now = datetime.now()


sample_json = {
    "content": "pytest test script",
    "created": "2022-04-04T10:51:43.363Z",
    "file_type": "test_script",
    "id": 0,  # set by ids fixture
    "project_id": 0,  # set by ids fixture
    "updated": "2022-04-04T10:51:43.363Z",
}


@pytest.fixture(scope="module", autouse=True)
def ids():
    if mock_api:
        httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(project_id, access_token, api_base)

    idso = IDs()
    idso.file_id = 35

    t = TestParams(
        name="pytest test",
        start_interval=1,
        participant_timeout=2,
        mode="load",
        increment_strategy="linear",
        mos_test=False,
        script=Script(content="pytest test script"),
    )

    if not mock_api:
        TestAPI.create(t)
        idso.file_id = t._script_file_id

    sample_json["id"] = idso.file_id
    sample_json["project_id"] = project_id

    yield idso

    if mock_api:
        return

    TestAPI.delete(t)


@pytest.fixture
def mock():
    if not mock_api:
        return

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/\d*/$"),
        body=json.dumps(sample_json),
        forcing_headers={"Content-Type": "application/json"},
    )


def test_params_init():
    fp = FileParams(file_id=4)

    assert fp.file_id == 4

    fp = FileParams()

    assert fp.file_id is None


def test_params_created():
    fp = FileParams()
    fp.__dict__["_created"] = time_now

    assert fp.created == time_now


def test_params_updated():
    fp = FileParams()
    fp.__dict__["_updated"] = time_now

    assert fp.updated == time_now


def test_params_file_type():
    fp = FileParams()
    # TODO: change to classificator
    fp.__dict__["_file_type"] = "script file type"

    assert fp.file_type == "script file type"


def test_params_content():
    fp = FileParams()
    fp.__dict__["_content"] = "test script"

    assert fp.content == "test script"


def test_params_project_id():
    fp = FileParams()
    fp.__dict__["_project_id"] = 13

    assert fp.project_id == 13


def test_params_from_json():
    dupl = sample_json.copy()
    dupl["id"] = 34
    dupl["project_id"] = 54

    fp = FileParams()
    fp.from_json(dupl)

    assert fp.file_id == 34
    assert fp.created == parser.parse("2022-04-04T10:51:43.363Z")
    assert fp.updated == parser.parse("2022-04-04T10:51:43.363Z")
    assert fp.file_type == "test_script"
    assert fp.content == "pytest test script"
    assert fp.project_id == 54


def test_script_string():
    s = Script()

    assert str(s) == "empty script"

    s.from_content("script content")

    assert str(s) == "script content"


def test_script_content():
    s = Script()

    assert s.content == ""

    s.from_content("script content")

    assert s.content == "script content"

    fp = FileParams()
    fp.__dict__["_content"] = "file content"
    s.__dict__["_params"] = fp

    assert s.content == "file content"


def test_script_from_file():
    s1 = Script(script_file=sample_test_script_py_path)

    assert s1.content == sample_test_script_py_data

    s2 = Script()
    s2.from_file(sample_test_script_py_path)

    assert s2.content == sample_test_script_py_data


def test_script_from_content():
    s1 = Script(content=sample_test_script_py_data)

    assert s1.content == sample_test_script_py_data

    s2 = Script()
    s2.from_content(sample_test_script_py_data)

    assert s2.content == sample_test_script_py_data


def test_api_read(mock, ids, pause):
    fp = FileParams(file_id=ids.file_id)

    FileAPI().read(fp)

    assert fp.file_id is not None
    assert fp.created is not None
    assert fp.updated is not None
    assert fp.file_type == "test_script"
    assert fp.content == "pytest test script"
    assert fp.project_id == project_id


def test_api_read_invalid_params():
    with pytest.raises(Exception):
        FileAPI.read(FileParams())
