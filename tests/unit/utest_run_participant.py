"""Run participant resource tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.run_participant import (
    RunParticipant,
    RunParticipantParams,
    RunParticipantAPI,
)
from loadero_python.resources.classificator import (
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
)
from . import common


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE, False)

    # read
    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}"
        + f"projects/{common.PROJECT_ID}/"
        + f"runs/{common.RUN_ID}/"
        + f"participants/{common.RUN_PARTICIPANT_ID}/",
        body=json.dumps(common.RUN_PARTICIPANT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.RUN_PARTICIPANT_JSON, common.RUN_PARTICIPANT_JSON]

    httpretty.register_uri(
        httpretty.GET,
        f"{common.API_BASE}"
        + f"projects/{common.PROJECT_ID}/"
        + f"runs/{common.RUN_ID}/"
        + "participants/",
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestRunParticipantParams:
    @staticmethod
    def utest_created():
        rp = RunParticipantParams()
        rp.__dict__["_created"] = common.CREATED_TIME
        assert rp.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        rp = RunParticipantParams()
        rp.__dict__["_updated"] = common.UPDATED_TIME
        assert rp.updated == common.UPDATED_TIME

    @staticmethod
    def utest_participant_num():
        rp = RunParticipantParams()
        rp.__dict__["_participant_num"] = 123
        assert rp.participant_num == 123

    @staticmethod
    def utest_participants_name():
        rp = RunParticipantParams()
        rp.__dict__["_participant_name"] = "lol"
        assert rp.participant_name == "lol"

    @staticmethod
    def utest_group_num():
        rp = RunParticipantParams()
        rp.__dict__["_group_num"] = 123
        assert rp.group_num == 123

    @staticmethod
    def utest_group_name():
        rp = RunParticipantParams()
        rp.__dict__["_group_name"] = "lol"
        assert rp.group_name == "lol"

    @staticmethod
    def utest_compute_unit():
        rp = RunParticipantParams()
        rp.__dict__["_compute_unit"] = ComputeUnit.CU_G2
        assert rp.compute_unit == ComputeUnit.CU_G2

    @staticmethod
    def utest_audio_feed():
        rp = RunParticipantParams()
        rp.__dict__["_audio_feed"] = AudioFeed.AF_DEFAULT
        assert rp.audio_feed == AudioFeed.AF_DEFAULT

    @staticmethod
    def utest_browser():
        rp = RunParticipantParams()
        rp.__dict__["_browser"] = Browser.B_CHROMELATEST
        assert rp.browser == Browser.B_CHROMELATEST

    @staticmethod
    def utest_location():
        rp = RunParticipantParams()
        rp.__dict__["_location"] = Location.L_AP_EAST_1
        assert rp.location == Location.L_AP_EAST_1

    @staticmethod
    def utest_network():
        rp = RunParticipantParams()
        rp.__dict__["_network"] = Network.N_ASYMMETRIC
        assert rp.network == Network.N_ASYMMETRIC

    @staticmethod
    def utest_video_feed():
        rp = RunParticipantParams()
        rp.__dict__["_video_feed"] = VideoFeed.VF_1080P_15FPS
        assert rp.video_feed == VideoFeed.VF_1080P_15FPS

    @staticmethod
    def utest_record_audio():
        rp = RunParticipantParams()
        rp.__dict__["_record_audio"] = True
        assert rp.record_audio is True

    @staticmethod
    def utest_builder_with_id():
        rp = RunParticipantParams()
        rp.with_id(123)
        assert rp.run_participant_id == 123

    @staticmethod
    def utest_str():
        rp = RunParticipantParams()
        rp.from_dict(common.RUN_PARTICIPANT_JSON)

        assert (
            str(rp)
            == """{
    "id": 233992,
    "run_id": 937561,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00",
    "participant_num": 123,
    "participant_name": "participant name",
    "group_num": 23,
    "group_name": "group name",
    "compute_unit": "g4",
    "audio_feed": "silence",
    "browser": "chromeLatest",
    "location": "eu-central-1",
    "network": "4g",
    "video_feed": "480p-15fps",
    "record_audio": true
}"""
        )


@pytest.mark.usefixtures("mock")
class UTestRunParticipant:
    @staticmethod
    def utest_init():
        rp = RunParticipant(
            run_participant_id=common.RUN_PARTICIPANT_ID,
            run_id=common.RUN_ID,
        )

        assert rp.params.run_participant_id == common.RUN_PARTICIPANT_ID
        assert rp.params.run_id == common.RUN_ID

    @staticmethod
    def utest_read():
        rp = RunParticipant(
            params=RunParticipantParams(
                run_participant_id=common.RUN_PARTICIPANT_ID,
                run_id=common.RUN_ID,
            )
        )

        rp.read()

        common.check_run_participant_params(rp.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body


@pytest.mark.usefixtures("mock")
class UTestRunParticipantAPI:
    @staticmethod
    def utest_read():
        common.check_run_participant_params(
            RunParticipantAPI.read(
                RunParticipantParams(
                    run_participant_id=common.RUN_PARTICIPANT_ID,
                    run_id=common.RUN_ID,
                )
            )
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all():
        resp = RunParticipantAPI.read_all(common.RUN_ID)

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_run_participant_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert (
            RunParticipantAPI.route(common.RUN_ID)
            == "projects/538591/runs/937561/participants/"
        )
        assert (
            RunParticipantAPI.route(common.RUN_ID, common.RUN_PARTICIPANT_ID)
            == "projects/538591/runs/937561/participants/233992/"
        )

    @staticmethod
    def utest_validate_identifiers():
        with pytest.raises(Exception):
            RunParticipantAPI.read(RunParticipantParams())

        with pytest.raises(Exception):
            RunParticipantAPI.read(RunParticipantParams(run_id=common.RUN_ID))
