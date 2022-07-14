"""Run participant resource tests"""


# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from loadero_python.resources.run_participant import RunParticipantParams
from loadero_python.resources.classificator import (
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
)
from . import common


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
    def utest_run_id():
        rp = RunParticipantParams()
        rp.__dict__["_run_id"] = 123
        assert rp.run_id == 123

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
    "run_id": 937561,
    "record_audio": true
}"""
        )
