"""File resource integration tests.
"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-variable

import os
import pytest
from loadero_python.api_client import APIClient
from loadero_python.resources.file import FileParams, File
from loadero_python.resources.classificator import FileType
from loadero_python.resources.project import Project


@pytest.fixture(scope="module")
def api_client():
    APIClient(
        project_id=int(os.environ.get("PROJECT_ID")),
        access_token=os.environ.get("ACCESS_TOKEN"),
        api_base=os.environ.get("API_BASE"),
    )

    yield


@pytest.mark.usefixtures("api_client")
class UTestFile:
    @staticmethod
    def utest_create():
        file_count = len(Project().files()[0])

        f = File(
            params=FileParams(
                file_type=FileType.FT_SSL_CERTIFICATE, content="hello"
            )
        )

        f.create()

        assert file_count + 1 == len(Project().files()[0])

        f.delete()

    @staticmethod
    def utest_read():
        files, _, _ = Project().files()
        file_id = files[0].params.file_id

        f = File(file_id=file_id)

        f.read()

        assert (
            f.params.content
            == """def test_on_loadero(driver: TestUIDriver):
    pass"""
        )
        assert f.params.file_type == FileType.FT_TEST_SCRIPT

    @staticmethod
    def utest_update():
        f = File(
            params=FileParams(
                file_type=FileType.FT_SSL_CERTIFICATE, content="hello"
            )
        )

        f.create()

        f.params.content = "world"

        f.update()

        f = File(file_id=f.params.file_id)

        f.read()

        assert f.params.content == "world"

        f.delete()

    @staticmethod
    def utest_delete():
        file_count = len(Project().files()[0])

        f = File(
            params=FileParams(
                file_type=FileType.FT_SSL_CERTIFICATE, content="hello"
            )
        )

        f.create()

        assert file_count + 1 == len(Project().files()[0])

        f.delete()

        assert file_count == len(Project().files()[0])
