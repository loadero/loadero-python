"""Script file resource tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import re
import json
import pytest
import httpretty
from loadero_python.resources.script import Script, FileParams, FileAPI
from loadero_python.api_client import APIClient
from loadero_python.resources.classificator import FileType
from . import common


# Relative to repo root dir.
sample_test_script_py_path = "tests/res/sample_test_script.py"
sample_test_script_py_data = """def test_on_loadero(driver: TestUIDriver):
    print("hello test")
"""


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.project_id, common.access_token, common.api_base)

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/\d*/$"),
        body=json.dumps(common.file_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all
    pg = common.paged_response.copy()

    f1 = common.file_json.copy()
    f1["id"] += 1

    f2 = common.file_json.copy()
    f2["id"] += 2

    pg["results"] = [f1, f2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/"),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestFileParams:
    def utest_init(self):
        fp = FileParams(file_id=4)

        assert fp.file_id == 4

        fp = FileParams()

        assert fp.file_id is None

    def utest_created(self):
        fp = FileParams()
        fp.__dict__["_created"] = common.created_time

        assert fp.created == common.created_time

    def utest_updated(self):
        fp = FileParams()
        fp.__dict__["_updated"] = common.updated_time

        assert fp.updated == common.updated_time

    def utest_file_type(self):
        fp = FileParams()
        fp.__dict__["_file_type"] = FileType.FT_TEST_SCRIPT

        assert fp.file_type is FileType.FT_TEST_SCRIPT

    def utest_content(self):
        fp = FileParams()
        fp.__dict__["_content"] = "test script"

        assert fp.content == "test script"

    def utest_from_json(self):
        fp = FileParams()
        fp.from_json(common.file_json)

        assert fp.file_id == common.file_id
        assert fp.created == common.created_time
        assert fp.updated == common.updated_time
        assert fp.file_type is FileType.FT_TEST_SCRIPT
        assert fp.content == "pytest test script"


@pytest.mark.usefixtures("mock")
class UTestScript:
    def utest_init_from_id(self):
        s = Script(script_id=2)

        assert s._params.file_id == 2

    def utest_init_from_content(self):
        s = Script(content="script content")

        assert s.content == "script content"

    def utest_init_from_file(self):
        s = Script(script_file=sample_test_script_py_path)

        assert s.content == sample_test_script_py_data

    def utest_string(self):
        s = Script()

        assert str(s) == "<empty script>"

        s.from_content("script content")

        assert str(s) == "script content"

    def utest_content(self):
        s = Script()

        assert s.content == ""

        s.from_content("script content")

        assert s.content == "script content"

        fp = FileParams()
        fp.__dict__["_content"] = "file content"
        s.__dict__["_params"] = fp

        assert s.content == "file content"

    def utest_from_file(self):
        s1 = Script(script_file=sample_test_script_py_path)

        assert s1.content == sample_test_script_py_data

        s2 = Script()
        s2.from_file(sample_test_script_py_path)

        assert s2.content == sample_test_script_py_data

    def utest_from_content(self):
        s1 = Script(content=sample_test_script_py_data)

        assert s1.content == sample_test_script_py_data

        s2 = Script()
        s2.from_content(sample_test_script_py_data)

        assert s2.content == sample_test_script_py_data

    def utest_to_json(self):
        s = Script(content="script content")

        assert s.to_json() == "script content"

    def utest_read(self):
        s = Script(script_id=2)

        s.read()

        assert s.content == "pytest test script"

        assert httpretty.last_request().parsed_body == ""


@pytest.mark.usefixtures("mock")
class UTestFileAPI:
    def utest_api_read(self):
        fp = FileParams(file_id=common.file_id)

        FileAPI().read(fp)

        assert fp.file_id == common.file_id
        assert fp.created == common.created_time
        assert fp.updated == common.updated_time
        assert fp.file_type is FileType.FT_TEST_SCRIPT
        assert fp.content == "pytest test script"

        assert httpretty.last_request().parsed_body == ""

    def utest_api_read_invalid_params(self):
        with pytest.raises(Exception):
            FileAPI.read(FileParams())

    def utest_api_read_all(self):
        resp = FileAPI.read_all()

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.file_id == common.file_id + i + 1
            assert ret.created == common.created_time
            assert ret.updated == common.updated_time
            assert ret.file_type is FileType.FT_TEST_SCRIPT
            assert ret.content == "pytest test script"

        assert httpretty.last_request().parsed_body == ""

    def utest_api_read_no_results(self):
        pg = common.paged_response.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/"),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        resp = FileAPI.read_all()

        assert len(resp) == 0
        assert httpretty.last_request().parsed_body == ""
