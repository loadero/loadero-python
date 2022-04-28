"""Participant resource tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=wildcard-import
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.participant import *
from loadero_python.resources.classificator import (
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
)
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
    "browser": "chromeLatest",
    "location": "eu-central-1",
    "media_type": "custom",
    "network": "4g",
    "video_feed": "480p-15fps",
}


@pytest.fixture(scope="module")
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
    upd["browser"] = "firefoxLatest"
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

    yield

    httpretty.disable()


class UTestParticipantsParams:
    def utest_string(self):
        p = ParticipantParams()
        dupl = sample_participant_json.copy()
        p.from_json(dupl)

        assert (
            str(p)
            == """|--------------|----------------------------------|
| audio_feed   | silence                          |
| browser      | chromeLatest                     |
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

    def utest_created(self):
        p = ParticipantParams()
        p.__dict__["_created"] = created_time
        assert p.created == created_time

    def utest_updated(self):
        p = ParticipantParams()
        p.__dict__["_updated"] = updated_time
        assert p.updated == updated_time

    def utest_builder_id(self):
        p = ParticipantParams()
        p.with_id(5)
        assert p.participant_id == 5

    def utest_builder_test_id(self):
        p = ParticipantParams()
        p.in_test(5)
        assert p.test_id == 5

    def utest_builder_name(self):
        p = ParticipantParams()
        p.with_name("participant")
        assert p.name == "participant"

    def utest_builder_count(self):
        p = ParticipantParams()
        p.with_count(3)
        assert p.count == 3

    def utest_builder_comute_unit(self):
        p = ParticipantParams()
        p.with_compute_unit(ComputeUnit.CU_G6)
        assert p.compute_unit is ComputeUnit.CU_G6

    def utest_builder_group_id(self):
        p = ParticipantParams()
        p.in_group(5)
        assert p.group_id == 5

    def utest_builder_record_audio(self):
        p = ParticipantParams()
        p.with_record_audio(True)
        assert p.record_audio is True

    def utest_builder_audio_feed(self):
        p = ParticipantParams()
        p.with_audio_feed(AudioFeed.AF_SILENCE)
        assert p.audio_feed is AudioFeed.AF_SILENCE

    def utest_builder_browser(self):
        p = ParticipantParams()
        p.with_browser(Browser.B_CHROMELATEST)
        assert p.browser is Browser.B_CHROMELATEST

    def utest_builder_location(self):
        p = ParticipantParams()
        p.with_location(Location.L_US_WEST_2)
        assert p.location is Location.L_US_WEST_2

    def utest_builder_network(self):
        p = ParticipantParams()
        p.with_network(Network.N_100PACKET)
        assert p.network is Network.N_100PACKET

    def utest_builder_video_feed(self):
        p = ParticipantParams()
        p.with_video_feed(VideoFeed.VF_1080P)
        assert p.video_feed is VideoFeed.VF_1080P


@pytest.mark.usefixtures("mock")
class UTestParticipant:
    def utest_create(self):
        p = Participant(
            params=ParticipantParams(
                group_id=identifiers.group_id,
                test_id=identifiers.test_id,
                count=3,
                record_audio=False,
                name="pytest participant",
                compute_unit="g4",
                audio_feed="silence",
                browser="chromeLatest",
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
        assert p.params.compute_unit is ComputeUnit.CU_G4
        assert p.params.audio_feed is AudioFeed.AF_SILENCE
        assert p.params.browser is Browser.B_CHROMELATEST
        assert p.params.location is Location.L_EU_CENTRAL_1
        assert p.params.network is Network.N_4G
        assert p.params.video_feed is VideoFeed.VF_480P_15FPS

        assert httpretty.last_request().parsed_body == {
            "audio_feed": "silence",
            "browser": "chromeLatest",
            "compute_unit": "g4",
            "count": 3,
            "group_id": 34421,
            "location": "eu-central-1",
            "name": "pytest participant",
            "network": "4g",
            "record_audio": False,
            "video_feed": "480p-15fps",
        }

    def utest_read(self):
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
        assert p.params.compute_unit is ComputeUnit.CU_G4
        assert p.params.audio_feed is AudioFeed.AF_SILENCE
        assert p.params.browser is Browser.B_CHROMELATEST
        assert p.params.location is Location.L_EU_CENTRAL_1
        assert p.params.network is Network.N_4G
        assert p.params.video_feed is VideoFeed.VF_480P_15FPS

        assert httpretty.last_request().parsed_body == ""

    def utest_update(self):
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
                browser="firefoxLatest",
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
        assert p.params.compute_unit is ComputeUnit.CU_G6
        assert p.params.audio_feed is AudioFeed.AF_VISQOL_SPEECH
        assert p.params.browser is Browser.B_FIREFOXLATEST
        assert p.params.location is Location.L_AP_NORTHEAST_2
        assert p.params.network is Network.N_3G
        assert p.params.video_feed is VideoFeed.VF_360P_15FPS

        assert httpretty.last_request().parsed_body == {
            "audio_feed": "visqol-speech",
            "browser": "firefoxLatest",
            "compute_unit": "g6",
            "count": 4,
            "group_id": 34421,
            "location": "ap-northeast-2",
            "name": "pytest updated participant",
            "network": "3g",
            "record_audio": True,
            "video_feed": "360p-15fps",
        }

    def utest_delete(self):
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

    def utest_duplicate(self):
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
        assert dupl.params.compute_unit is ComputeUnit.CU_G4
        assert dupl.params.audio_feed is AudioFeed.AF_SILENCE
        assert dupl.params.browser is Browser.B_CHROMELATEST
        assert dupl.params.location is Location.L_EU_CENTRAL_1
        assert dupl.params.network is Network.N_4G
        assert dupl.params.video_feed is VideoFeed.VF_480P_15FPS

        assert httpretty.last_request().parsed_body == {
            "name": "pytest duplicate participant"
        }


@pytest.mark.usefixtures("mock")
class UTestParticipantAPI:
    def utest_api_create(self):
        ret = ParticipantAPI.create(
            ParticipantParams(
                name="pytest participant",
                count=3,
                compute_unit="g4",
                test_id=identifiers.test_id,
                group_id=identifiers.group_id,
                record_audio=False,
                audio_feed="silence",
                browser="chromeLatest",
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
        assert ret.compute_unit is ComputeUnit.CU_G4
        assert ret.audio_feed is AudioFeed.AF_SILENCE
        assert ret.browser is Browser.B_CHROMELATEST
        assert ret.location is Location.L_EU_CENTRAL_1
        assert ret.network is Network.N_4G
        assert ret.video_feed is VideoFeed.VF_480P_15FPS

        assert httpretty.last_request().parsed_body == {
            "audio_feed": "silence",
            "browser": "chromeLatest",
            "compute_unit": "g4",
            "count": 3,
            "group_id": 34421,
            "location": "eu-central-1",
            "name": "pytest participant",
            "network": "4g",
            "record_audio": False,
            "video_feed": "480p-15fps",
        }

    def utest_api_create_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.create(ParticipantParams())

    def utest_api_read(self):
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
        assert ret.compute_unit is ComputeUnit.CU_G4
        assert ret.audio_feed is AudioFeed.AF_SILENCE
        assert ret.browser is Browser.B_CHROMELATEST
        assert ret.location is Location.L_EU_CENTRAL_1
        assert ret.network is Network.N_4G
        assert ret.video_feed is VideoFeed.VF_480P_15FPS

        assert httpretty.last_request().parsed_body == ""

    def utest_api_read_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.read(ParticipantParams(test_id=identifiers.test_id))

        with pytest.raises(Exception):
            ParticipantAPI.read(
                ParticipantParams(participant_id=identifiers.participant_id)
            )

    def utest_api_update(self):
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
                browser="firefoxLatest",
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
        assert ret.compute_unit is ComputeUnit.CU_G6
        assert ret.audio_feed is AudioFeed.AF_VISQOL_SPEECH
        assert ret.browser is Browser.B_FIREFOXLATEST
        assert ret.location is Location.L_AP_NORTHEAST_2
        assert ret.network is Network.N_3G
        assert ret.video_feed is VideoFeed.VF_360P_15FPS

        assert httpretty.last_request().parsed_body == {
            "audio_feed": "visqol-speech",
            "browser": "firefoxLatest",
            "compute_unit": "g6",
            "count": 4,
            "group_id": 34421,
            "location": "ap-northeast-2",
            "name": "pytest updated participant",
            "network": "3g",
            "record_audio": True,
            "video_feed": "360p-15fps",
        }

    def utest_api_update_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.update(
                ParticipantParams(test_id=identifiers.test_id)
            )

        with pytest.raises(Exception):
            ParticipantAPI.update(
                ParticipantParams(participant_id=identifiers.participant_id)
            )

    def utest_api_delete(self):
        ret = ParticipantAPI.delete(
            ParticipantParams(
                participant_id=identifiers.participant_id,
                test_id=identifiers.test_id,
            )
        )

        assert ret is None

        assert httpretty.last_request().parsed_body == ""

    def utest_api_delete_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.delete(ParticipantParams(test_id=1))

        with pytest.raises(Exception):
            ParticipantAPI.delete(ParticipantParams(participant_id=1))

    def utest_api_duplicate(self):
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
        assert ret.compute_unit is ComputeUnit.CU_G4
        assert ret.audio_feed is AudioFeed.AF_SILENCE
        assert ret.browser is Browser.B_CHROMELATEST
        assert ret.location is Location.L_EU_CENTRAL_1
        assert ret.network is Network.N_4G
        assert ret.video_feed is VideoFeed.VF_480P_15FPS

        assert httpretty.last_request().parsed_body == {
            "name": "pytest duplicate participant"
        }

    def utest_api_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.duplicate(ParticipantParams(test_id=1))

        with pytest.raises(Exception):
            ParticipantAPI.duplicate(ParticipantParams(participant_id=1))

    def utest_api_read_all(self):
        ParticipantAPI.read_all(5)
