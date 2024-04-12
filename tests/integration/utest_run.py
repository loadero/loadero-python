"""Run resource integration tests.
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
    AudioFeed,
    Location,
    Network,
    VideoFeed,
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
class UTestRun:
    @staticmethod
    def utest_participants():
        rp = Project().runs()[0][0].participants()[0][0]

        assert rp.params.run_participant_id == 1629895
        assert rp.params.run_id == 27059
        assert rp.params.created == parser.parse("2022-08-04 14:11:16+00:00")
        assert rp.params.updated == parser.parse("2022-08-04 14:11:16+00:00")
        assert rp.params.participant_num == 0
        assert rp.params.participant_name == "p 1"
        assert rp.params.group_num == 0
        assert rp.params.group_name == "group 1"
        assert rp.params.audio_feed == AudioFeed.AF_NEG_50DB
        assert rp.params.browser is not None
        assert rp.params.location == Location.L_US_WEST_2
        assert rp.params.network == Network.N_50PACKET
        assert rp.params.video_feed == VideoFeed.VF_480P_MARKED_TOP_LEFT
        assert rp.params.record_audio is False
