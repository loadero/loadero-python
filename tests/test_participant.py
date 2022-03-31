"""Participant resource tests"""

from datetime import datetime
from loadero_python.resources import participant


time_now = datetime.now()


class TestParticipantParams:
    """Participant parameters tests"""

    def test_created(self):
        p = participant.ParticipantParams()
        p.__dict__["_created"] = time_now
        assert p.created == time_now

    def test_updated(self):
        p = participant.ParticipantParams()
        p.__dict__["_updated"] = time_now
        assert p.updated == time_now

    def test_project_id(self):
        p = participant.ParticipantParams()
        p.__dict__["_project_id"] = 5
        assert p.project_id == 5

    def test_test_id(self):
        p = participant.ParticipantParams()
        p.__dict__["_test_id"] = 5
        assert p.test_id == 5

    def test_builder_id(self):
        p = participant.ParticipantParams()
        p.with_id(5)
        assert p.participant_id == 5

    def test_builder_test_id(self):
        p = participant.ParticipantParams()
        p.in_test(5)
        assert p.test_id == 5

    def test_builder_project_id(self):
        p = participant.ParticipantParams()
        p.in_project(5)
        assert p.project_id == 5

    def test_builder_name(self):
        p = participant.ParticipantParams()
        p.with_name("participant")
        assert p.name == "participant"

    def test_builder_comute_unit(self):
        p = participant.ParticipantParams()
        p.with_compute_unit("g6")
        assert p.compute_unit == "g6"

    def test_builder_group_id(self):
        p = participant.ParticipantParams()
        p.in_group(5)
        assert p.group_id == 5

    def test_builder_record_audio(self):
        p = participant.ParticipantParams()
        p.with_record_audio(True)
        assert p.record_audio is True

    def test_builder_audio_feed(self):
        p = participant.ParticipantParams()
        p.with_audio_feed("silence")
        assert p.audio_feed == "silence"

    def test_builder_browser(self):
        p = participant.ParticipantParams()
        p.with_browser("chrome")
        assert p.browser == "chrome"

    def test_builder_location(self):
        p = participant.ParticipantParams()
        p.with_location("us-west-2")
        assert p.location == "us-west-2"

    def test_builder_network(self):
        p = participant.ParticipantParams()
        p.with_network("100perc")
        assert p.network == "100perc"

    def test_builder_video_feed(self):
        p = participant.ParticipantParams()
        p.with_video_feed("1080p")
        assert p.video_feed == "1080p"


def test_participant_params():
    pp = participant.ParticipantParams(count=4)
    assert pp.count == 4

    pp.in_project(5)
    assert pp.project_id == 5
