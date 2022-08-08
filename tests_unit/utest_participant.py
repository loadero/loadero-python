"""Participant resource tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member
# pylint: disable=unused-variable


import json
import re
from urllib.parse import urlparse, parse_qs
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.participant import (
    Participant,
    ParticipantParams,
    ParticipantAPI,
    ParticipantFilterKey,
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

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/$"
        ),
        body=json.dumps(common.PARTICIPANT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/$"
        ),
        body=json.dumps(common.PARTICIPANT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/$"
        ),
        body=json.dumps(common.PARTICIPANT_JSON),
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
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/participants/\d*/copy/$"
        ),
        body=json.dumps(common.PARTICIPANT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all participants in test
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.PARTICIPANT_JSON, common.PARTICIPANT_JSON]

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
    @staticmethod
    def utest_string():
        p = ParticipantParams()
        p.from_dict(common.PARTICIPANT_JSON)

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

    @staticmethod
    def utest_created():
        p = ParticipantParams()
        p.__dict__["_created"] = common.CREATED_TIME
        assert p.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        p = ParticipantParams()
        p.__dict__["_updated"] = common.UPDATED_TIME
        assert p.updated == common.UPDATED_TIME

    @staticmethod
    def utest_builder_id():
        p = ParticipantParams()
        p.with_id(5)
        assert p.participant_id == 5

    @staticmethod
    def utest_builder_test_id():
        p = ParticipantParams()
        p.in_test(5)
        assert p.test_id == 5

    @staticmethod
    def utest_builder_name():
        p = ParticipantParams()
        p.with_name("participant")
        assert p.name == "participant"

    @staticmethod
    def utest_builder_count():
        p = ParticipantParams()
        p.with_count(3)
        assert p.count == 3

    @staticmethod
    def utest_builder_comute_unit():
        p = ParticipantParams()
        p.with_compute_unit(ComputeUnit.CU_G6)
        assert p.compute_unit is ComputeUnit.CU_G6

    @staticmethod
    def utest_builder_group_id():
        p = ParticipantParams()
        p.in_group(5)
        assert p.group_id == 5

    @staticmethod
    def utest_builder_record_audio():
        p = ParticipantParams()
        p.with_record_audio(True)
        assert p.record_audio is True

    @staticmethod
    def utest_builder_audio_feed():
        p = ParticipantParams()
        p.with_audio_feed(AudioFeed.AF_SILENCE)
        assert p.audio_feed is AudioFeed.AF_SILENCE

    @staticmethod
    def utest_builder_browser():
        p = ParticipantParams()
        p.with_browser(Browser.B_CHROMELATEST)
        assert p.browser is Browser.B_CHROMELATEST

    @staticmethod
    def utest_builder_location():
        p = ParticipantParams()
        p.with_location(Location.L_US_WEST_2)
        assert p.location is Location.L_US_WEST_2

    @staticmethod
    def utest_builder_network():
        p = ParticipantParams()
        p.with_network(Network.N_100PACKET)
        assert p.network is Network.N_100PACKET

    @staticmethod
    def utest_builder_video_feed():
        p = ParticipantParams()
        p.with_video_feed(VideoFeed.VF_1080P)
        assert p.video_feed is VideoFeed.VF_1080P


@pytest.mark.usefixtures("mock")
class UTestParticipant:
    @staticmethod
    def utest_create():
        common.check_participant_params(
            Participant(
                params=ParticipantParams(
                    group_id=common.GROUP_ID,
                    test_id=common.TEST_ID,
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
            .create()
            .params
        )

        assert httpretty.last_request().method == httpretty.POST
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

    @staticmethod
    def utest_read():
        common.check_participant_params(
            Participant(
                participant_id=common.PARTICIPANT_ID,
                test_id=common.TEST_ID,
            )
            .read()
            .params
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        common.check_participant_params(
            Participant(
                params=ParticipantParams(
                    participant_id=common.PARTICIPANT_ID,
                    test_id=common.TEST_ID,
                    group_id=common.GROUP_ID,
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
            .update()
            .params
        )

        assert httpretty.last_request().method == httpretty.PUT
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

    @staticmethod
    def utest_delete():
        Participant(
            params=ParticipantParams(
                participant_id=common.PARTICIPANT_ID,
                test_id=common.TEST_ID,
            )
        ).delete()

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_duplicate():
        common.check_participant_params(
            Participant(
                params=ParticipantParams(
                    participant_id=common.PARTICIPANT_ID,
                    test_id=common.TEST_ID,
                    group_id=common.GROUP_ID,
                )
            )
            .duplicate("pytest duplicate participant")
            .params
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "name": "pytest duplicate participant"
        }


@pytest.mark.usefixtures("mock")
class UTestParticipantAPI:
    @staticmethod
    def utest_create():
        common.check_participant_params(
            ParticipantAPI.create(
                ParticipantParams(
                    name="pytest participant",
                    count=3,
                    test_id=common.TEST_ID,
                    group_id=common.GROUP_ID,
                    record_audio=False,
                    compute_unit=ComputeUnit.CU_G4,
                    audio_feed=AudioFeed.AF_SILENCE,
                    browser=Browser.B_CHROMELATEST,
                    network=Network.N_4G,
                    location=Location.L_EU_CENTRAL_1,
                    video_feed=VideoFeed.VF_480P_15FPS,
                )
            )
        )

        assert httpretty.last_request().method == httpretty.POST
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

    @staticmethod
    def utest_read():
        common.check_participant_params(
            ParticipantAPI.read(
                ParticipantParams(
                    test_id=common.TEST_ID,
                    participant_id=common.PARTICIPANT_ID,
                )
            )
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        common.check_participant_params(
            ParticipantAPI.update(
                ParticipantParams(
                    participant_id=common.PARTICIPANT_ID,
                    test_id=common.TEST_ID,
                    group_id=common.GROUP_ID,
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
        )

        assert httpretty.last_request().method == httpretty.PUT
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

    @staticmethod
    def utest_delete():
        assert (
            ParticipantAPI.delete(
                ParticipantParams(
                    participant_id=common.PARTICIPANT_ID,
                    test_id=common.TEST_ID,
                )
            )
            is None
        )

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_duplicate():
        common.check_participant_params(
            ParticipantAPI.duplicate(
                ParticipantParams(
                    participant_id=common.PARTICIPANT_ID,
                    test_id=common.TEST_ID,
                ),
                "pytest duplicate participant",
            )
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "name": "pytest duplicate participant"
        }

    @staticmethod
    def utest_read_all_in_test():
        resp = ParticipantAPI.read_all(common.TEST_ID)

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:  # pylint: disable=not-an-iterable
            common.check_participant_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_in_group():
        resp = ParticipantAPI.read_all(common.TEST_ID, common.GROUP_ID)

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:  # pylint: disable=not-an-iterable
            common.check_participant_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_with_query_params():
        resp = ParticipantAPI.read_all(
            common.TEST_ID,
            common.GROUP_ID,
            common.build_query_params(list(ParticipantFilterKey)),
        )

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:  # pylint: disable=not-an-iterable
            common.check_participant_params(ret)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(ParticipantFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert (
            ParticipantAPI.route(common.TEST_ID)
            == "projects/538591/tests/12734/participants/"
        )
        assert (
            ParticipantAPI.route(common.TEST_ID, group_id=common.GROUP_ID)
            == "projects/538591/tests/12734/groups/34421/participants/"
        )
        assert (
            ParticipantAPI.route(common.TEST_ID, common.PARTICIPANT_ID)
            == "projects/538591/tests/12734/participants/92559/"
        )
        assert (
            ParticipantAPI.route(
                common.TEST_ID,
                common.PARTICIPANT_ID,
                common.GROUP_ID,
            )
            == "projects/538591/tests/12734/groups/34421/participants/92559/"
        )

    @staticmethod
    def utest_validate_identifiers():
        with pytest.raises(ValueError):
            ParticipantAPI.create(ParticipantParams())

        with pytest.raises(ValueError):
            ParticipantAPI.read(ParticipantParams())

        with pytest.raises(ValueError):
            ParticipantAPI.read(ParticipantParams(test_id=common.TEST_ID))

        with pytest.raises(ValueError):
            ParticipantAPI.update(ParticipantParams())

        with pytest.raises(ValueError):
            ParticipantAPI.update(ParticipantParams(test_id=common.TEST_ID))

        with pytest.raises(ValueError):
            ParticipantAPI.delete(ParticipantParams())

        with pytest.raises(ValueError):
            ParticipantAPI.delete(ParticipantParams(test_id=common.TEST_ID))

        with pytest.raises(ValueError):
            ParticipantAPI.duplicate(ParticipantParams(), "")

        with pytest.raises(ValueError):
            ParticipantAPI.duplicate(
                ParticipantParams(test_id=common.TEST_ID), ""
            )
