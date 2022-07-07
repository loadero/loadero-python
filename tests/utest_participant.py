"""Participant resource tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.participant import (
    Participant,
    ParticipantParams,
    ParticipantAPI,
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

    APIClient(common.project_id, common.access_token, common.api_base)

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/$"
        ),
        body=json.dumps(common.participant_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/$"
        ),
        body=json.dumps(common.participant_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    upd = common.participant_json.copy()
    upd["count"] = 4
    upd["name"] = "pytest updated participant"
    upd["compute_unit"] = "g6"
    upd["record_audio"] = True
    upd["audio_feed"] = "visqol-speech"
    upd["browser"] = "firefoxLatest"
    upd["location"] = "ap-northeast-2"
    upd["network"] = "3g"
    upd["video_feed"] = "360p-15fps"

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

    # duplicate
    dupl = common.participant_json.copy()
    dupl["id"] += 1
    dupl["name"] = "pytest duplicate participant"

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/copy/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all participants in test
    pg = common.paged_response.copy()
    p1 = common.participant_json.copy()
    p1["id"] += 1

    p2 = common.participant_json.copy()
    p2["id"] += 2

    pg["results"] = [p1, p2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all participants in group
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/groups/\d*/participants/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestParticipantsParams:
    def utest_string(self):
        p = ParticipantParams()
        p.from_dict(common.participant_json)

        assert (
            str(p)
            == """{
    "id": 92559,
    "test_id": 12734,
    "name": "pytest participant",
    "count": 3,
    "compute_unit": "g4",
    "group_id": 34421,
    "record_audio": false,
    "audio_feed": "silence",
    "browser": "chromeLatest",
    "location": "eu-central-1",
    "network": "4g",
    "video_feed": "480p-15fps",
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00"
}"""
        )

    def utest_created(self):
        p = ParticipantParams()
        p.__dict__["_created"] = common.created_time
        assert p.created == common.created_time

    def utest_updated(self):
        p = ParticipantParams()
        p.__dict__["_updated"] = common.updated_time
        assert p.updated == common.updated_time

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
                group_id=common.group_id,
                test_id=common.test_id,
                count=3,
                record_audio=False,
                name="pytest participant",
                compute_unit=ComputeUnit.CU_G4,
                audio_feed=AudioFeed.AF_SILENCE,
                browser=Browser.B_CHROMELATEST,
                network=Network.N_4G,
                location=Location.L_EU_CENTRAL_1,
                video_feed=VideoFeed.VF_480P_15FPS,
            )
        )

        p.create()

        assert p.params.participant_id == common.participant_id
        assert p.params.group_id == common.group_id
        assert p.params.test_id == common.test_id
        assert p.params.created == common.created_time
        assert p.params.updated == common.updated_time
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
            participant_id=common.participant_id,
            test_id=common.test_id,
        )

        p.read()

        assert p.params.participant_id == common.participant_id
        assert p.params.group_id == common.group_id
        assert p.params.test_id == common.test_id
        assert p.params.created == common.created_time
        assert p.params.updated == common.updated_time
        assert p.params.count == 3
        assert p.params.record_audio is False
        assert p.params.name == "pytest participant"
        assert p.params.compute_unit is ComputeUnit.CU_G4
        assert p.params.audio_feed is AudioFeed.AF_SILENCE
        assert p.params.browser is Browser.B_CHROMELATEST
        assert p.params.location is Location.L_EU_CENTRAL_1
        assert p.params.network is Network.N_4G
        assert p.params.video_feed is VideoFeed.VF_480P_15FPS

        assert not httpretty.last_request().parsed_body

    def utest_update(self):
        p = Participant(
            params=ParticipantParams(
                participant_id=common.participant_id,
                test_id=common.test_id,
                group_id=common.group_id,
                name="pytest updated participant",
                count=4,
                record_audio=True,
                compute_unit=ComputeUnit.CU_G6,
                audio_feed=AudioFeed.AF_VISQOL_SPEECH,
                browser=Browser.B_FIREFOXLATEST,
                location=Location.L_AP_NORTHEAST_2,
                network=Network.N_3G,
                video_feed=VideoFeed.VF_360P_15FPS,
            )
        )

        p.update()

        assert p.params.participant_id == common.participant_id
        assert p.params.group_id == common.group_id
        assert p.params.test_id == common.test_id
        assert p.params.created == common.created_time
        assert p.params.updated == common.updated_time
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
                participant_id=common.participant_id,
                test_id=common.test_id,
            )
        )

        p.delete()

        assert p.params.test_id == common.test_id
        assert p.params.participant_id == common.participant_id

        assert not httpretty.last_request().parsed_body

    def utest_duplicate(self):
        p = Participant(
            params=ParticipantParams(
                participant_id=common.participant_id,
                test_id=common.test_id,
                group_id=common.group_id,
            )
        )

        dupl = p.duplicate("pytest duplicate participant")

        assert p.params.participant_id == common.participant_id
        assert p.params.group_id == common.group_id
        assert p.params.test_id == common.test_id
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

        assert dupl.params.participant_id == common.participant_id + 1
        assert dupl.params.group_id == common.group_id
        assert dupl.params.test_id == common.test_id
        assert dupl.params.created == common.created_time
        assert dupl.params.updated == common.updated_time
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
    def utest_create(self):
        ret = ParticipantAPI.create(
            ParticipantParams(
                name="pytest participant",
                count=3,
                test_id=common.test_id,
                group_id=common.group_id,
                record_audio=False,
                compute_unit=ComputeUnit.CU_G4,
                audio_feed=AudioFeed.AF_SILENCE,
                browser=Browser.B_CHROMELATEST,
                network=Network.N_4G,
                location=Location.L_EU_CENTRAL_1,
                video_feed=VideoFeed.VF_480P_15FPS,
            )
        )

        assert ret.participant_id == common.participant_id
        assert ret.group_id == common.group_id
        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
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

    def utest_create_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.create(ParticipantParams())

    def utest_read(self):
        p = ParticipantParams(
            test_id=common.test_id,
            participant_id=common.participant_id,
        )

        ret = ParticipantAPI.read(p)

        assert ret.participant_id == common.participant_id
        assert ret.group_id == common.group_id
        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
        assert ret.count == 3
        assert ret.record_audio is False
        assert ret.name == "pytest participant"
        assert ret.compute_unit is ComputeUnit.CU_G4
        assert ret.audio_feed is AudioFeed.AF_SILENCE
        assert ret.browser is Browser.B_CHROMELATEST
        assert ret.location is Location.L_EU_CENTRAL_1
        assert ret.network is Network.N_4G
        assert ret.video_feed is VideoFeed.VF_480P_15FPS

        assert not httpretty.last_request().parsed_body

    def utest_read_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.read(ParticipantParams(test_id=common.test_id))

        with pytest.raises(Exception):
            ParticipantAPI.read(
                ParticipantParams(participant_id=common.participant_id)
            )

    def utest_update(self):
        ret = ParticipantAPI.update(
            ParticipantParams(
                participant_id=common.participant_id,
                test_id=common.test_id,
                group_id=common.group_id,
                name="pytest updated participant",
                count=4,
                record_audio=True,
                compute_unit=ComputeUnit.CU_G6,
                audio_feed=AudioFeed.AF_VISQOL_SPEECH,
                browser=Browser.B_FIREFOXLATEST,
                location=Location.L_AP_NORTHEAST_2,
                network=Network.N_3G,
                video_feed=VideoFeed.VF_360P_15FPS,
            )
        )

        assert ret.participant_id == common.participant_id
        assert ret.group_id == common.group_id
        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
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

    def utest_update_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.update(ParticipantParams(test_id=common.test_id))

        with pytest.raises(Exception):
            ParticipantAPI.update(
                ParticipantParams(participant_id=common.participant_id)
            )

    def utest_delete(self):
        ret = ParticipantAPI.delete(
            ParticipantParams(
                participant_id=common.participant_id,
                test_id=common.test_id,
            )
        )

        assert ret is None

        assert not httpretty.last_request().parsed_body

    def utest_delete_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.delete(ParticipantParams(test_id=1))

        with pytest.raises(Exception):
            ParticipantAPI.delete(ParticipantParams(participant_id=1))

    def utest_duplicate(self):
        ret = ParticipantAPI.duplicate(
            ParticipantParams(
                participant_id=common.participant_id,
                test_id=common.test_id,
                name="pytest duplicate participant",
            )
        )

        assert ret.participant_id == common.participant_id + 1
        assert ret.group_id == common.group_id
        assert ret.test_id == common.test_id
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time
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

    def utest_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            ParticipantAPI.duplicate(ParticipantParams(test_id=1))

        with pytest.raises(Exception):
            ParticipantAPI.duplicate(ParticipantParams(participant_id=1))

    def utest_read_all_in_test(self):
        resp = ParticipantAPI.read_all(common.test_id)

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.participant_id == common.participant_id + i + 1
            assert ret.group_id == common.group_id
            assert ret.test_id == common.test_id
            assert ret.created == common.created_time
            assert ret.updated == common.updated_time
            assert ret.count == 3
            assert ret.record_audio is False
            assert ret.name == "pytest participant"
            assert ret.compute_unit is ComputeUnit.CU_G4
            assert ret.audio_feed is AudioFeed.AF_SILENCE
            assert ret.browser is Browser.B_CHROMELATEST
            assert ret.location is Location.L_EU_CENTRAL_1
            assert ret.network is Network.N_4G
            assert ret.video_feed is VideoFeed.VF_480P_15FPS

    def utest_read_all_in_group(self):
        resp = ParticipantAPI.read_all(common.test_id, common.group_id)

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.participant_id == common.participant_id + i + 1
            assert ret.group_id == common.group_id
            assert ret.test_id == common.test_id
            assert ret.created == common.created_time
            assert ret.updated == common.updated_time
            assert ret.count == 3
            assert ret.record_audio is False
            assert ret.name == "pytest participant"
            assert ret.compute_unit is ComputeUnit.CU_G4
            assert ret.audio_feed is AudioFeed.AF_SILENCE
            assert ret.browser is Browser.B_CHROMELATEST
            assert ret.location is Location.L_EU_CENTRAL_1
            assert ret.network is Network.N_4G
            assert ret.video_feed is VideoFeed.VF_480P_15FPS

        assert not httpretty.last_request().parsed_body

    def utest_read_no_results(self):
        pg = common.paged_response.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                r"^http://mock\.loadero\.api/v2/"
                r"projects/\d*/tests/\d*/participants/$"
            ),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        resp = ParticipantAPI.read_all(common.test_id)

        assert len(resp) == 0
        assert not httpretty.last_request().parsed_body

    def utest_route(self):
        assert (
            ParticipantAPI.route(common.test_id)
            == "http://mock.loadero.api"
            + "/v2/projects/538591/tests/12734/participants/"
        )
        assert (
            ParticipantAPI.route(common.test_id, group_id=common.group_id)
            == "http://mock.loadero.api"
            + "/v2/projects/538591/tests/12734/groups/34421/participants/"
        )
        assert (
            ParticipantAPI.route(common.test_id, common.participant_id)
            == "http://mock.loadero.api"
            + "/v2/projects/538591/tests/12734/participants/92559/"
        )
        assert (
            ParticipantAPI.route(
                common.test_id,
                common.participant_id,
                common.group_id,
            )
            == "http://mock.loadero.api"
            + "/v2/projects/538591/tests/12734/groups/34421/participants/92559/"
        )
