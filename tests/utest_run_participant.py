"""Run participant resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


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
    def utest_created(self):
        rp = RunParticipantParams()
        rp.__dict__["_created"] = common.created_time
        assert rp.created == common.created_time

    def utest_updated(self):
        rp = RunParticipantParams()
        rp.__dict__["_updated"] = common.updated_time
        assert rp.updated == common.updated_time

    def utest_participant_num(self):
        rp = RunParticipantParams()
        rp.__dict__["_participant_num"] = 123
        assert rp.participant_num == 123

    def utest_participants_name(self):
        rp = RunParticipantParams()
        rp.__dict__["_participant_name"] = "lol"
        assert rp.participant_name == "lol"

    def utest_group_num(self):
        rp = RunParticipantParams()
        rp.__dict__["_group_num"] = 123
        assert rp.group_num == 123

    def utest_group_name(self):
        rp = RunParticipantParams()
        rp.__dict__["_group_name"] = "lol"
        assert rp.group_name == "lol"

    def utest_compute_unit(self):
        rp = RunParticipantParams()
        rp.__dict__["_compute_unit"] = ComputeUnit.CU_G2
        assert rp.compute_unit == ComputeUnit.CU_G2

    def utest_audio_feed(self):
        rp = RunParticipantParams()
        rp.__dict__["_audio_feed"] = AudioFeed.AF_DEFAULT
        assert rp.audio_feed == AudioFeed.AF_DEFAULT

    def utest_browser(self):
        rp = RunParticipantParams()
        rp.__dict__["_browser"] = Browser.B_CHROMELATEST
        assert rp.browser == Browser.B_CHROMELATEST

    def utest_location(self):
        rp = RunParticipantParams()
        rp.__dict__["_location"] = Location.L_AP_EAST_1
        assert rp.location == Location.L_AP_EAST_1

    def utest_network(self):
        rp = RunParticipantParams()
        rp.__dict__["_network"] = Network.N_ASYMMETRIC
        assert rp.network == Network.N_ASYMMETRIC

    def utest_video_feed(self):
        rp = RunParticipantParams()
        rp.__dict__["_video_feed"] = VideoFeed.VF_1080P_15FPS
        assert rp.video_feed == VideoFeed.VF_1080P_15FPS

    def utest_run_id(self):
        rp = RunParticipantParams()
        rp.__dict__["_run_id"] = 123
        assert rp.run_id == 123

    def utest_record_audio(self):
        rp = RunParticipantParams()
        rp.__dict__["_record_audio"] = True
        assert rp.record_audio is True

    def utest_builder_with_id(self):
        rp = RunParticipantParams()
        rp.with_id(123)
        assert rp.run_participant_id == 123

    def utest_str(self):
        rp = RunParticipantParams()
        rp.from_dict(common.run_participant_json)

        print(rp)
        assert (
            str(rp)
            == """{
    "id": 233992,
    "updated": "2024-02-03 15:42:54.689000+00:00",
    "created": "2022-04-01 13:54:25.689000+00:00",
    "run_id": 937561,
    "group_name": "group name",
    "group_num": 23,
    "participant_name": "participant name",
    "participant_num": 123,
    "record_audio": true,
    "compute_unit": "g4",
    "audio_feed": "silence",
    "browser": "chromeLatest",
    "location": "eu-central-1",
    "network": "4g",
    "video_feed": "480p-15fps"
}"""
        )
