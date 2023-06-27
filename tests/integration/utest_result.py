"""Result resource integration tests.
"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-variable

import os
import pytest
from loadero_python.api_client import APIClient
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
class UTestResult:
    @staticmethod
    def utest_download_log():
        runs, _, _ = Project().runs()
        results, _, _ = runs[0].results()

        result = results[0]
        result.read()

        dest = result.params.log_paths.rru.download()

        assert dest == "bb3d3447-d1bc-4e1a-a011-8235e5a24e29.json"
        assert os.path.exists(dest)
        os.remove(dest)
