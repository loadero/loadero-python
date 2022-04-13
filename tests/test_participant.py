"""Participant resource tests"""

# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=wildcard-import
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.participant import *
from . import identifiers


created_time = parser.parse("2022-04-01T13:54:25.689Z")
updated_time = parser.parse("2024-02-03T15:42:54.689Z")


sample_participant_json = {
    "id": identifiers.participant_id,
    "group_id": identifiers.group_id,
    "test_id": identifiers.test_id,
    "created": "2022-04-01T13:54:25.689Z",
    "updated": "2024-02-03T15:42:54.689Z",
    "profile_id": 87,
    "count": 3,
    "record_audio": False,
    "name": "pytest participant",
    "compute_unit": "g4",
    "audio_feed": "silence",
    "browser": "chrome100",
    "location": "eu-central-1",
    "media_type": "custom",
    "network": "4g",
    "video_feed": "480p-15fps",
}


@pytest.fixture
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(
        identifiers.project_id, identifiers.access_token, identifiers.api_base
    )

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/$"
        ),
        body=json.dumps(sample_participant_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/$"
        ),
        body=json.dumps(sample_participant_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    upd = sample_participant_json.copy()
    upd["count"] = 4
    upd["name"] = "pytest updated participant"
    upd["compute_unit"] = "g6"
    upd["record_audio"] = True
    upd["audio_feed"] = "visqol-speech"
    upd["browser"] = "chrome99"
    upd["location"] = "ap-northeast-2"
    upd["network"] = "3g"
    upd["video_feed"] = "360p-15fps"

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/$"
        ),
        body=json.dumps(upd),
        forcing_headers={"Content-Type": "application/json"},
    )

    # delete
    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/$"
        ),
    )

    dupl = sample_participant_json.copy()
    dupl["id"] += 1
    dupl["name"] = "pytest duplicate participant"

    # duplicate
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/copy/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )


class TestParticipantsParams:
    def test_string(self):
        p = ParticipantParams()
        dupl = sample_participant_json.copy()
        p.from_json(dupl)

        assert (
            str(p)
            == """|--------------|----------------------------------|
| audio_feed   | silence                          |
| browser      | chrome100                        |
| compute_unit | g4                               |
| count        | 3                                |
| created      | 2022-04-01 13:54:25.689000+00:00 |
| group_id     | 34421                            |
| id           | 92559                            |
| location     | eu-central-1                     |
| name         | pytest participant               |
| network      | 4g                               |
| record_audio | False                            |
| test_id      | 12734                            |
| updated      | 2024-02-03 15:42:54.689000+00:00 |
| video_feed   | 480p-15fps                       |"""
        )

    def test_created(self):
        p = ParticipantParams()
        p.__dict__["_created"] = created_time
        assert p.created == created_time

    def test_updated(self):
        p = ParticipantParams()
        p.__dict__["_updated"] = updated_time
        assert p.updated == updated_time

    def test_project_id(self):
        p = ParticipantParams()
        p.__dict__["_project_id"] = 5
        assert p.project_id == 5

    def test_test_id(self):
        p = ParticipantParams()
        p.__dict__["test_id"] = 5
        assert p.test_id == 5

    def test_builder_id(self):
        p = ParticipantParams()
        p.with_id(5)
        assert p.participant_id == 5

    def test_builder_test_id(self):
        p = ParticipantParams()
        p.in_test(5)
        assert p.test_id == 5

    def test_builder_project_id(self):
        p = ParticipantParams()
        p.in_project(5)
        assert p.project_id == 5

    def test_builder_name(self):
        p = ParticipantParams()
        p.with_name("participant")
        assert p.name == "participant"

    def test_builder_count(self):
        p = ParticipantParams()
        p.with_count(3)
        assert p.count == 3

    def test_builder_comute_unit(self):
        p = ParticipantParams()
        p.with_compute_unit("g6")
        assert p.compute_unit == "g6"

    def test_builder_group_id(self):
        p = ParticipantParams()
        p.in_group(5)
        assert p.group_id == 5

    def test_builder_record_audio(self):
        p = ParticipantParams()
        p.with_record_audio(True)
        assert p.record_audio is True

    def test_builder_audio_feed(self):
        p = ParticipantParams()
        p.with_audio_feed("silence")
        assert p.audio_feed == "silence"

    def test_builder_browser(self):
        p = ParticipantParams()
        p.with_browser("chrome")
        assert p.browser == "chrome"

    def test_builder_location(self):
        p = ParticipantParams()
        p.with_location("us-west-2")
        assert p.location == "us-west-2"

    def test_builder_network(self):
        p = ParticipantParams()
        p.with_network("100perc")
        assert p.network == "100perc"

    def test_builder_video_feed(self):
        p = ParticipantParams()
        p.with_video_feed("1080p")
        assert p.video_feed == "1080p"


class TestParticipant:
    def test_create(self, mock):
        p = Participant(
            params=ParticipantParams(
                group_id=identifiers.group_id,
                test_id=identifiers.test_id,
                count=3,
                record_audio=False,
                name="pytest participant",
                compute_unit="g4",
                audio_feed="silence",
                browser="chrome100",
                network="4g",
                location="eu-central-1",
                video_feed="480p-15fps",
            )
        )

        p.create()

        assert p.params.participant_id == identifiers.participant_id
        assert p.params.group_id == identifiers.group_id
        assert p.params.test_id == identifiers.test_id
        assert p.params.created == created_time
        assert p.params.updated == updated_time
        assert p.params.count == 3
        assert p.params.record_audio is False
        assert p.params.name == "pytest participant"
        assert p.params.compute_unit == "g4"
        assert p.params.audio_feed == "silence"
        assert p.params.browser == "chrome100"
        assert p.params.location == "eu-central-1"
        assert p.params.network == "4g"
        assert p.params.video_feed == "480p-15fps"

        assert httpretty.last_request().parsed_body == {
            "audio_feed": "silence",
            "browser": "chrome100",
            "compute_unit": "g4",
            "count": 3,
            "group_id": 34421,
            "location": "eu-central-1",
            "name": "pytest participant",
            "network": "4g",
            "record_audio": False,
            "video_feed": "480p-15fps",
        }

    def test_read(self, mock):
        p = Participant(
            participant_id=identifiers.participant_id,
            test_id=identifiers.test_id,
        )

        p.read()

        assert p.params.participant_id == identifiers.participant_id
        assert p.params.group_id == identifiers.group_id
        assert p.params.test_id == identifiers.test_id
        assert p.params.created == created_time
        assert p.params.updated == updated_time
        assert p.params.count == 3
        assert p.params.record_audio is False
        assert p.params.name == "pytest participant"
        assert p.params.compute_unit == "g4"
        assert p.params.audio_feed == "silence"
        assert p.params.browser == "chrome100"
        assert p.params.location == "eu-central-1"
        assert p.params.network == "4g"
        assert p.params.video_feed == "480p-15fps"

        assert httpretty.last_request().parsed_body == ""

    def test_update(self, mock):
        p = Participant(
            params=ParticipantParams(
                participant_id=identifiers.participant_id,
                test_id=identifiers.test_id,
                group_id=identifiers.group_id,
                name="pytest updated participant",
                count=4,
                compute_unit="g6",
                record_audio=True,
                audio_feed="visqol-speech",
                browser="chrome99",
                location="ap-northeast-2",
                network="3g",
                video_feed="360p-15fps",
            )
        )

        p.update()

        assert p.params.participant_id == identifiers.participant_id
        assert p.params.group_id == identifiers.group_id
        assert p.params.test_id == identifiers.test_id
        assert p.params.created == created_time
        assert p.params.updated == updated_time
        assert p.params.count == 4
        assert p.params.record_audio is True
        assert p.params.name == "pytest updated participant"
        assert p.params.compute_unit == "g6"
        assert p.params.audio_feed == "visqol-speech"
        assert p.params.browser == "chrome99"
        assert p.params.location == "ap-northeast-2"
        assert p.params.network == "3g"
        assert p.params.video_feed == "360p-15fps"

        assert httpretty.last_request().parsed_body == {
            "audio_feed": "visqol-speech",
            "browser": "chrome99",
            "compute_unit": "g6",
            "count": 4,
            "group_id": 34421,
            "location": "ap-northeast-2",
            "name": "pytest updated participant",
            "network": "3g",
            "record_audio": True,
            "video_feed": "360p-15fps",
        }

    def test_delete(self, mock):
        p = Participant(
            params=ParticipantParams(
                participant_id=identifiers.participant_id,
                test_id=identifiers.test_id,
            )
        )

        p.delete()

        assert p.params.test_id == identifiers.test_id
        assert p.params.participant_id == identifiers.participant_id

        assert httpretty.last_request().parsed_body == ""

    def test_duplicate(self, mock):
        p = Participant(
            params=ParticipantParams(
                participant_id=identifiers.participant_id,
                test_id=identifiers.test_id,
                group_id=identifiers.group_id,
            )
        )

        dupl = p.duplicate("pytest duplicate participant")

        assert p.params.participant_id == identifiers.participant_id
        assert p.params.group_id == identifiers.group_id
        assert p.params.test_id == identifiers.test_id
        assert p.params.created is None
        assert p.params.updated is None
        assert p.params.count is None
        assert p.params.record_audio is None
        assert p.params.name is None
        assert p.params.compute_unit is None
        assert p.params.audio_feed is None
        assert p.params.browser is None
        assert p.params.location is None
        assert p.params.network is None
        assert p.params.video_feed is None

        assert dupl.params.participant_id == identifiers.participant_id + 1
        assert dupl.params.group_id == identifiers.group_id
        assert dupl.params.test_id == identifiers.test_id
        assert dupl.params.created == created_time
        assert dupl.params.updated == updated_time
        assert dupl.params.count == 3
        assert dupl.params.record_audio is False
        assert dupl.params.name == "pytest duplicate participant"
        assert dupl.params.compute_unit == "g4"
        assert dupl.params.audio_feed == "silence"
        assert dupl.params.browser == "chrome100"
        assert dupl.params.location == "eu-central-1"
        assert dupl.params.network == "4g"
        assert dupl.params.video_feed == "480p-15fps"

        assert httpretty.last_request().parsed_body == {
            "name": "pytest duplicate participant"
        }


class TestParticipantAPI:
    def test_api_create(self, mock):
        ret = ParticipantAPI.create(
            ParticipantParams(
                name="pytest participant",
                count=3,
                compute_unit="g4",
                test_id=identifiers.test_id,
                group_id=identifiers.group_id,
                record_audio=False,
                audio_feed="silence",
                browser="chrome100",
                location="eu-central-1",
                network="4g",
                video_feed="480p-15fps",
            )
        )

        assert ret.participant_id == identifiers.participant_id
        assert ret.group_id == identifiers.group_id
        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.count == 3
        assert ret.record_audio is False
        assert ret.name == "pytest participant"
        assert ret.compute_unit == "g4"
        assert ret.audio_feed == "silence"
        assert ret.browser == "chrome100"
        assert ret.location == "eu-central-1"
        assert ret.network == "4g"
        assert ret.video_feed == "480p-15fps"

        assert httpretty.last_request().parsed_body == {
            "audio_feed": "silence",
            "browser": "chrome100",
            "compute_unit": "g4",
            "count": 3,
            "group_id": 34421,
            "location": "eu-central-1",
            "name": "pytest participant",
            "network": "4g",
            "record_audio": False,
            "video_feed": "480p-15fps",
        }

    def test_api_create_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.create(ParticipantParams())

    def test_api_read(self, mock):
        p = ParticipantParams(
            test_id=identifiers.test_id,
            participant_id=identifiers.participant_id,
        )

        ret = ParticipantAPI.read(p)

        assert ret.participant_id == identifiers.participant_id
        assert ret.group_id == identifiers.group_id
        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.count == 3
        assert ret.record_audio is False
        assert ret.name == "pytest participant"
        assert ret.compute_unit == "g4"
        assert ret.audio_feed == "silence"
        assert ret.browser == "chrome100"
        assert ret.location == "eu-central-1"
        assert ret.network == "4g"
        assert ret.video_feed == "480p-15fps"

        assert httpretty.last_request().parsed_body == ""

    def test_api_read_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.read(ParticipantParams(test_id=identifiers.test_id))

        with pytest.raises(Exception):
            ParticipantAPI.read(
                ParticipantParams(participant_id=identifiers.participant_id)
            )

    def test_api_update(self, mock):
        ret = ParticipantAPI.update(
            ParticipantParams(
                participant_id=identifiers.participant_id,
                test_id=identifiers.test_id,
                group_id=identifiers.group_id,
                name="pytest updated participant",
                count=4,
                compute_unit="g6",
                record_audio=True,
                audio_feed="visqol-speech",
                browser="chrome99",
                location="ap-northeast-2",
                network="3g",
                video_feed="360p-15fps",
            )
        )

        assert ret.participant_id == identifiers.participant_id
        assert ret.group_id == identifiers.group_id
        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.count == 4
        assert ret.record_audio is True
        assert ret.name == "pytest updated participant"
        assert ret.compute_unit == "g6"
        assert ret.audio_feed == "visqol-speech"
        assert ret.browser == "chrome99"
        assert ret.location == "ap-northeast-2"
        assert ret.network == "3g"
        assert ret.video_feed == "360p-15fps"

        assert httpretty.last_request().parsed_body == {
            "audio_feed": "visqol-speech",
            "browser": "chrome99",
            "compute_unit": "g6",
            "count": 4,
            "group_id": 34421,
            "location": "ap-northeast-2",
            "name": "pytest updated participant",
            "network": "3g",
            "record_audio": True,
            "video_feed": "360p-15fps",
        }

    def test_api_update_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.update(
                ParticipantParams(test_id=identifiers.test_id)
            )

        with pytest.raises(Exception):
            ParticipantAPI.update(
                ParticipantParams(participant_id=identifiers.participant_id)
            )

    def test_api_delete(self, mock):
        ret = ParticipantAPI.delete(
            ParticipantParams(
                participant_id=identifiers.participant_id,
                test_id=identifiers.test_id,
            )
        )

        assert ret is None

        assert httpretty.last_request().parsed_body == ""

    def test_api_delete_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.delete(ParticipantParams(test_id=1))

        with pytest.raises(Exception):
            ParticipantAPI.delete(ParticipantParams(participant_id=1))

    def test_api_duplicate(self, mock):
        ret = ParticipantAPI.duplicate(
            ParticipantParams(
                participant_id=identifiers.participant_id,
                test_id=identifiers.test_id,
                name="pytest duplicate participant",
            )
        )

        assert ret.participant_id == identifiers.participant_id + 1
        assert ret.group_id == identifiers.group_id
        assert ret.test_id == identifiers.test_id
        assert ret.created == created_time
        assert ret.updated == updated_time
        assert ret.count == 3
        assert ret.record_audio is False
        assert ret.name == "pytest duplicate participant"
        assert ret.compute_unit == "g4"
        assert ret.audio_feed == "silence"
        assert ret.browser == "chrome100"
        assert ret.location == "eu-central-1"
        assert ret.network == "4g"
        assert ret.video_feed == "480p-15fps"

        assert httpretty.last_request().parsed_body == {
            "name": "pytest duplicate participant"
        }

    def test_api_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.duplicate(ParticipantParams(test_id=1))

        with pytest.raises(Exception):
            ParticipantAPI.duplicate(ParticipantParams(participant_id=1))

    def test_api_read_all(self):
        ParticipantAPI.read_all(5)
