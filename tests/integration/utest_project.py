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
    "id": 1154197,
    "created": "2022-08-04 14:04:42+00:00",
    "updated": "2022-08-04 14:05:24+00:00",
    "name": "Loadero API Client Tests [DO NOT DELETE]",
    "member_count": 1,
    "language": "python",
    "subscription_id": 62025,
    "plan_limits": {
        "max_test_duration": "2h",
        "included_test_duration": "2h",
        "max_test_cu": 50000,
        "max_monthly_cu": 200000,
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
        "created": "2022-08-04 14:05:24+00:00",
        "updated": "2022-08-04 14:06:27+00:00",
        "payment_plan": "single_pro",
        "activation_date": "2022-08-04 14:06:25+00:00",
        "payment_status": "success",
        "billing_email": "rudolfs.zvejs@loadero.com",
        "settings": {
            "max_participant_cu": "g6",
            "max_test_duration": "2h",
            "max_monthly_cu": 200000,
            "max_test_cu": 50000,
            "mos_enabled": false
        }
    },
    "compute_unit_usage": {
        "used": 3
    }
}"""
        )

    @staticmethod
    def utest_tests():
        tests, _, _ = Project().tests()

        assert len(tests) == 1

        assert (
            str(tests[0])
            == """{
    "id": 657448,
    "name": "black coffee test",
    "start_interval": 1,
    "participant_timeout": 600,
    "mode": "performance",
    "increment_strategy": "random",
    "created": "2022-08-04 14:09:49+00:00",
    "updated": "2022-08-04 14:09:49+00:00",
    "script_file_id": 588205,
    "group_count": 1,
    "participant_count": 2
}"""
        )

    @staticmethod
    def utest_files():
        files, _, _ = Project().files()

        assert len(files) == 19
        assert files[0].params.file_type == FileType.FT_TEST_SCRIPT

    @staticmethod
    def utest_runs():
        runs, _, _ = Project().runs()

        assert len(runs) == 1
        assert runs[0].params.test_mode == TestMode.TM_PERFORMANCE
