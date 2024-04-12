"""Project resource integration tests.
"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-variable

import os
import pytest
from dateutil import parser
from loadero_python.api_client import APIClient
from loadero_python.resources.project import Project
from loadero_python.resources.classificator import (
    FileType,
    TestMode,
    Language,
    IncrementStrategy,
)


@pytest.fixture(scope="module")
def api_client():
    APIClient(
        project_id=int(os.environ.get("PROJECT_ID")),
        access_token=os.environ.get("ACCESS_TOKEN"),
        api_base=os.environ.get("API_BASE"),
    )

    yield


@pytest.mark.usefixtures("api_client")
class UTestProject:
    @staticmethod
    def utest_read():
        p = Project().read()

        assert p.params.project_id == 1154197
        assert p.params.created == parser.parse("2022-08-04 14:04:42+00:00")
        assert p.params.name == "Loadero API Client Tests [DO NOT DELETE]"
        assert p.params.member_count == 2
        assert p.params.language == Language.L_PYTHON

    @staticmethod
    def utest_tests():
        tests, _, _ = Project().tests()

        assert len(tests) == 1

        test = tests[0]

        assert test.params.test_id == 657448
        assert test.params.name == "black coffee test"
        assert test.params.start_interval == 1
        assert test.params.participant_timeout == 600
        assert test.params.mode == TestMode.TM_PERFORMANCE
        assert test.params.increment_strategy == IncrementStrategy.IS_RANDOM
        assert test.params.created == parser.parse("2022-08-04 14:09:49+00:00")
        assert test.params.script.file_id == 588205
        assert test.params.group_count == 1
        assert test.params.participant_count == 2

    @staticmethod
    def utest_files():
        files, _, _ = Project().files()

        assert len(files) == 24
        assert files[0].params.file_type == FileType.FT_TEST_SCRIPT

    @staticmethod
    def utest_runs():
        runs, _, _ = Project().runs()

        assert len(runs) == 1
        assert runs[0].params.test_mode == TestMode.TM_PERFORMANCE
