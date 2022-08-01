"""File resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member
# pylint: disable=unused-variable


import re
import json
import pytest
import httpretty


from loadero_python.resources.file import FileParams, File, FileAPI
from loadero_python.api_client import APIClient
from loadero_python.resources.classificator import FileType
from . import common


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE)

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/\d*/$"),
        body=json.dumps(common.FILE_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all
    pg = common.PAGED_RESPONSE.copy()
    pg["results"] = [common.FILE_JSON, common.FILE_JSON]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/"),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestFileParams:
    @staticmethod
    def utest_init():
        fp = FileParams(file_id=4)
        assert fp.file_id == 4

        fp = FileParams()
        assert fp.file_id is None

    @staticmethod
    def utest_created():
        fp = FileParams()
        fp.__dict__["_created"] = common.CREATED_TIME

        assert fp.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        fp = FileParams()
        fp.__dict__["_updated"] = common.UPDATED_TIME
        assert fp.updated == common.UPDATED_TIME

    @staticmethod
    def utest_file_type():
        fp = FileParams()
        fp.__dict__["_file_type"] = FileType.FT_TEST_SCRIPT
        assert fp.file_type is FileType.FT_TEST_SCRIPT

    @staticmethod
    def utest_content():
        fp = FileParams()
        fp.__dict__["_content"] = "test script"
        assert fp.content == "test script"

    @staticmethod
    def utest_from_dict():
        common.check_file_params(FileParams().from_dict(common.FILE_JSON))


@pytest.mark.usefixtures("mock")
class UTestFile:
    @staticmethod
    def utest_read():
        common.check_file_params(File(common.FILE_ID).read().params)


@pytest.mark.usefixtures("mock")
class UTestFileAPI:
    @staticmethod
    def utest_read():
        common.check_file_params(
            FileAPI().read(FileParams(file_id=common.FILE_ID))
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_invalid_params():
        with pytest.raises(Exception):
            FileAPI.read(FileParams())

    @staticmethod
    def utest_read_all():
        resp = FileAPI.read_all()

        assert len(resp) == 2

        for ret in resp:
            common.check_file_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_no_results():
        pg = common.PAGED_RESPONSE.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(r"^http://mock\.loadero\.api/v2/projects/\d*/files/"),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        resp = FileAPI.read_all()

        assert len(resp) == 0
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert FileAPI.route() == "projects/538591/files/"
        assert FileAPI.route(common.FILE_ID) == "projects/538591/files/923/"
