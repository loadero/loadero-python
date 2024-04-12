"""File resource tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member
# pylint: disable=unused-variable


import json
from urllib.parse import urlparse, parse_qs
import pytest
import httpretty
from loadero_python.resources.file import (
    FileFilterKey,
    FileParams,
    File,
    FileAPI,
)
from loadero_python.api_client import APIClient
from loadero_python.resources.classificator import FileType
from . import common


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE, False)

    # create
    httpretty.register_uri(
        httpretty.POST,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/files/",
        body=json.dumps(common.FILE_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/"
        f"files/{common.FILE_ID}/",
        body=json.dumps(common.FILE_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    httpretty.register_uri(
        httpretty.PUT,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/"
        f"files/{common.FILE_ID}/",
        body=json.dumps(common.FILE_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.DELETE,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/"
        f"files/{common.FILE_ID}/",
    )

    # read all
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.FILE_JSON, common.FILE_JSON]

    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}projects/{common.PROJECT_ID}/files/",
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
    def utest_from_dict():
        common.check_file_params(FileParams().from_dict(common.FILE_JSON))

    @staticmethod
    def utest_to_dict():
        fp = FileParams().from_dict(common.FILE_JSON)
        fp.password = "hello"

        assert fp.to_dict() == {
            "content": "pytest test script",
            "file_type": "test_script",
            "password": "hello",
        }


@pytest.mark.usefixtures("mock")
class UTestFile:
    @staticmethod
    def utest_create():
        common.check_file_params(
            File(
                params=FileParams(
                    file_type=FileType.FT_SSL_CERTIFICATE, content="hello world"
                )
            )
            .create()
            .params
        )

    @staticmethod
    def utest_read():
        common.check_file_params(File(file_id=common.FILE_ID).read().params)

    @staticmethod
    def utest_update():
        common.check_file_params(
            File(
                file_id=common.FILE_ID,
                params=FileParams(
                    file_type=FileType.FT_SSL_CERTIFICATE, content="hello world"
                ),
            )
            .update()
            .params
        )

    @staticmethod
    def utest_delete():
        File(file_id=common.FILE_ID).delete()


@pytest.mark.usefixtures("mock")
class UTestFileAPI:
    @staticmethod
    def utest_create():
        common.check_file_params(
            FileAPI.create(
                FileParams(
                    file_type=FileType.FT_TEST_SCRIPT,
                    content="pytest test script",
                )
            )
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "content": "pytest test script",
            "file_type": "test_script",
        }

    @staticmethod
    def utest_read():
        common.check_file_params(
            FileAPI().read(FileParams(file_id=common.FILE_ID))
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        common.check_file_params(
            FileAPI.update(
                FileParams(
                    file_id=common.FILE_ID,
                    file_type=FileType.FT_TEST_SCRIPT,
                    content="pytest test script",
                )
            )
        )

        assert httpretty.last_request().method == httpretty.PUT
        assert httpretty.last_request().parsed_body == {
            "content": "pytest test script",
            "file_type": "test_script",
        }

    @staticmethod
    def utest_delete():
        assert FileAPI.delete(FileParams(file_id=common.FILE_ID)) is None

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all():
        resp = FileAPI.read_all()

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_file_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_with_query_params():
        resp = FileAPI.read_all(common.build_query_params(list(FileFilterKey)))

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_file_params(ret)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(FileFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert FileAPI.route() == "projects/538591/files/"
        assert FileAPI.route(common.FILE_ID) == "projects/538591/files/923/"

    @staticmethod
    def utest_validate_identifiers():
        with pytest.raises(ValueError):
            FileAPI.read(FileParams())

        with pytest.raises(ValueError):
            FileAPI.update(FileParams())

        with pytest.raises(ValueError):
            FileAPI.delete(FileParams())
