"""Project resource integration tests.
"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-variable

import os
import pytest
from loadero_python.api_client import APIClient
from loadero_python.resources.project import Project
from loadero_python.resources.classificator import FileType, TestMode


@pytest.fixture(scope="module")
def api_client():
    print(
        os.environ.get("PROJECT_ID"),
        os.environ.get("ACCESS_TOKEN"),
        os.environ.get("API_BASE"),
        os.environ,
    )

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

        assert (
            str(p)
            == """{
    "id": 44806,
    "created": "2020-01-02 08:55:42+00:00",
    "updated": "2021-05-27 13:12:01+00:00",
    "name": "API Automation [DO NOT DELETE]",
    "member_count": 7,
    "language": "javascript",
    "subscription_id": 22038,
    "plan_limits": {
        "max_test_duration": "45m",
        "included_test_duration": "45m",
        "max_test_cu": 10000,
        "max_monthly_cu": 200000,
        "included_compute_units": 10000,
        "mos_enabled": false,
        "compute_units": [
            "g0.5",
            "g1",
            "g2",
            "g4",
            "g6"
        ],
        "api_access": true,
        "aws_access": false,
        "session_recording_access": true,
        "assert_preconditions_access": true
    },
    "subscription": {
        "created": "2021-05-27 13:12:01+00:00",
        "updated": "2022-06-02 06:05:06+00:00",
        "payment_plan": "yearly",
        "activation_date": "2021-05-31 07:10:57+00:00",
        "payment_status": "success",
        "billing_email": "dev@loadero.com",
        "settings": {
            "max_participant_cu": "g6",
            "max_test_duration": "45m",
            "max_monthly_cu": 200000,
            "max_test_cu": 10000,
            "mos_enabled": false
        }
    },
    "compute_unit_usage": {
        "included": 10000,
        "used": 0
    }
}"""
        )

    @staticmethod
    def utest_tests():
        tests = Project().tests()

        assert len(tests) == 1

        assert (
            str(tests[0])
            == """{
    "id": 27002,
    "name": "Test",
    "start_interval": 20,
    "participant_timeout": 60,
    "mode": "performance",
    "increment_strategy": "random",
    "created": "2020-01-02 09:33:20+00:00",
    "updated": "2020-05-29 11:28:23+00:00",
    "script_file_id": 174,
    "group_count": 1,
    "participant_count": 2
}"""
        )

    @staticmethod
    def utest_files():
        files = Project().files()

        assert len(files) == 7
        assert files[0].params.file_type == FileType.FT_TEST_SCRIPT

    @staticmethod
    def utest_runs():
        runs = Project().runs()

        assert len(runs) == 6
        assert runs[0].params.test_mode == TestMode.TM_PERFORMANCE
