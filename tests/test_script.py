"""Script file resource tests"""

# pylint: disable=W0613
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=wildcard-import
# pylint: disable=protected-access
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import re
import json
import pytest
import httpretty
from dateutil import parser
from loadero_python.resources.script import *
from . import identifiers


# Relative to repo root dir.
sample_test_script_py_path = "tests/res/sample_test_script.py"
sample_test_script_py_data = """def test_on_loadero(driver: TestUIDriver):
    print("hello test")
"""


created_time = parser.parse("2022-04-01T13:54:25.689Z")
updated_time = parser.parse("2024-02-03T15:42:54.689Z")


sample_json = {
    "content": "pytest test script",
    "created": "2022-04-01T13:54:25.689Z",
    "file_type": "test_script",
    "id": identifiers.script_file_id,
    "project_id": identifiers.project_id,
    "updated": "2024-02-03T15:42:54.689Z",
}


@pytest.fixture
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(
        identifiers.project_id, identifiers.access_token, identifiers.api_base
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/\d*/$"),
        body=json.dumps(sample_json),
        forcing_headers={"Content-Type": "application/json"},
    )


class TestFileParams:
    def test_init(self):
        fp = FileParams(file_id=4)

        assert fp.file_id == 4

        fp = FileParams()

        assert fp.file_id is None

    def test_created(self):
        fp = FileParams()
        fp.__dict__["_created"] = created_time

        assert fp.created == created_time

    def test_updated(self):
        fp = FileParams()
        fp.__dict__["_updated"] = updated_time

        assert fp.updated == updated_time

    def test_file_type(self):
        fp = FileParams()
        # TODO: change to classificator
        fp.__dict__["_file_type"] = "script file type"

        assert fp.file_type == "script file type"

    def test_content(self):
        fp = FileParams()
        fp.__dict__["_content"] = "test script"

        assert fp.content == "test script"

    def test_from_json(self):
        fp = FileParams()
        fp.from_json(sample_json)

        assert fp.file_id == identifiers.script_file_id
        assert fp.created == created_time
        assert fp.updated == updated_time
        assert fp.file_type == "test_script"
        assert fp.content == "pytest test script"


class TestScript:
    def test_init_from_id(self):
        s = Script(script_id=2)

        assert s._params.file_id == 2

    def test_init_from_content(self):
        s = Script(content="script content")

        assert s.content == "script content"

    def test_init_from_file(self):
        s = Script(script_file=sample_test_script_py_path)

        assert s.content == sample_test_script_py_data

    def test_string(self):
        s = Script()

        assert str(s) == "empty script"

        s.from_content("script content")

        assert str(s) == "script content"

    def test_content(self):
        s = Script()

        assert s.content == ""

        s.from_content("script content")

        assert s.content == "script content"

        fp = FileParams()
        fp.__dict__["_content"] = "file content"
        s.__dict__["_params"] = fp

        assert s.content == "file content"

    def test_from_file(self):
        s1 = Script(script_file=sample_test_script_py_path)

        assert s1.content == sample_test_script_py_data

        s2 = Script()
        s2.from_file(sample_test_script_py_path)

        assert s2.content == sample_test_script_py_data

    def test_from_content(self):
        s1 = Script(content=sample_test_script_py_data)

        assert s1.content == sample_test_script_py_data

        s2 = Script()
        s2.from_content(sample_test_script_py_data)

        assert s2.content == sample_test_script_py_data

    def test_to_json(self):
        s = Script(content="script content")

        assert s.to_json() == "script content"

    def test_read(self, mock):
        s = Script(script_id=2)

        s.read()

        assert s.content == "pytest test script"

        assert httpretty.last_request().parsed_body == ""


class TestFileAPI:
    def test_api_read(self, mock):
        fp = FileParams(file_id=identifiers.script_file_id)

        FileAPI().read(fp)

        assert fp.file_id == identifiers.script_file_id
        assert fp.created == created_time
        assert fp.updated == updated_time
        assert fp.file_type == "test_script"
        assert fp.content == "pytest test script"

        assert httpretty.last_request().parsed_body == ""

    def test_api_read_invalid_params(self):
        with pytest.raises(Exception):
            FileAPI.read(FileParams())
