"""Participant resource tests"""

# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=wildcard-import


from datetime import datetime
import os
import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.script import Script
from loadero_python.resources.test import TestParams, TestAPI
from loadero_python.resources.group import GroupParams, GroupAPI
from loadero_python.resources.participant import *
from .utils import *


access_token = os.environ.get("ACCESS_TOKEN", default="LOADERO_ACCESS_TOKEN")
api_base = os.environ.get("API_BASE", default="http://mock.loadero.api/v2/")
mock_api = os.environ.get("MOCK_API", default="true") == "true"
project_id = int(os.environ.get("PROJECT_ID", default="45"))


time_now = datetime.now()


sample_participant_json = {
    "audio_feed": "silence",
    "browser": "chrome100",
    "compute_unit": "g4",
    "count": 3,
    "created": "2022-04-01T17:09:53.499Z",
    "group_id": 0,  # set by ids fixture
    "id": 36,
    "location": "eu-central-1",
    "media_type": "custom",
    "name": "pytest participant",
    "network": "4g",
    "profile_id": 87,
    "record_audio": False,
    "test_id": 0,  # set by ids fixture
    "updated": "2022-04-01T17:09:53.499Z",
    "video_feed": "480p-15fps",
}


@pytest.fixture(scope="module", autouse=True)
def ids():
    if mock_api:
        httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(project_id, access_token, api_base)

    idso = IDs()

    # default ids
    idso.project_id = project_id
    idso.test_id = 89
    idso.group_id = 76

    t = TestParams(
        name="pytest test",
        start_interval=1,
        participant_timeout=2,
        mode="load",
        increment_strategy="linear",
        mos_test=False,
        script=Script(content="pytest test script"),
    )

    g = GroupParams(name="pytest_group", count=8)

    if not mock_api:
        TestAPI.create(t)
        idso.test_id = t.test_id

        g.test_id = t.test_id
        GroupAPI().create(g)
        idso.group_id = g.group_id

    sample_participant_json["test_id"] = idso.test_id
    sample_participant_json["group_id"] = idso.group_id

    yield idso

    if mock_api:
        return

    GroupAPI.delete(g)
    TestAPI.delete(t)


@pytest.fixture
def mock():
    if not mock_api:
        return

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


def test_params_string():
    p = ParticipantParams()
    dupl = sample_participant_json.copy()

    dupl["test_id"] = 98
    dupl["group_id"] = 35

    p.from_json(dupl)

    assert (
        str(p)
        == """|--------------|----------------------------------|
| audio_feed   | silence                          |
| browser      | chrome100                        |
| compute_unit | g4                               |
| count        | 3                                |
| created      | 2022-04-01 17:09:53.499000+00:00 |
| group_id     | 35                               |
| id           | 36                               |
| location     | eu-central-1                     |
| name         | pytest participant               |
| network      | 4g                               |
| record_audio | False                            |
| test_id      | 98                               |
| updated      | 2022-04-01 17:09:53.499000+00:00 |
| video_feed   | 480p-15fps                       |"""
    )


def test_params_created():
    p = ParticipantParams()
    p.__dict__["_created"] = time_now
    assert p.created == time_now


def test_params_updated():
    p = ParticipantParams()
    p.__dict__["_updated"] = time_now
    assert p.updated == time_now


def test_params_project_id():
    p = ParticipantParams()
    p.__dict__["_project_id"] = 5
    assert p.project_id == 5


def test_params_test_id():
    p = ParticipantParams()
    p.__dict__["test_id"] = 5
    assert p.test_id == 5


def test_params_builder_id():
    p = ParticipantParams()
    p.with_id(5)
    assert p.participant_id == 5


def test_params_builder_test_id():
    p = ParticipantParams()
    p.in_test(5)
    assert p.test_id == 5


def test_params_builder_project_id():
    p = ParticipantParams()
    p.in_project(5)
    assert p.project_id == 5


def test_params_builder_name():
    p = ParticipantParams()
    p.with_name("participant")
    assert p.name == "participant"


def test_params_builder_count():
    p = ParticipantParams()
    p.with_count(3)
    assert p.count == 3


def test_params_builder_comute_unit():
    p = ParticipantParams()
    p.with_compute_unit("g6")
    assert p.compute_unit == "g6"


def test_params_builder_group_id():
    p = ParticipantParams()
    p.in_group(5)
    assert p.group_id == 5


def test_params_builder_record_audio():
    p = ParticipantParams()
    p.with_record_audio(True)
    assert p.record_audio is True


def test_params_builder_audio_feed():
    p = ParticipantParams()
    p.with_audio_feed("silence")
    assert p.audio_feed == "silence"


def test_params_builder_browser():
    p = ParticipantParams()
    p.with_browser("chrome")
    assert p.browser == "chrome"


def test_params_builder_location():
    p = ParticipantParams()
    p.with_location("us-west-2")
    assert p.location == "us-west-2"


def test_params_builder_network():
    p = ParticipantParams()
    p.with_network("100perc")
    assert p.network == "100perc"


def test_params_builder_video_feed():
    p = ParticipantParams()
    p.with_video_feed("1080p")
    assert p.video_feed == "1080p"


def test_create(mock, ids, pause):
    p = Participant(
        params=ParticipantParams(
            name="pytest participant",
            count=3,
            compute_unit="g4",
            test_id=ids.test_id,
            group_id=ids.group_id,
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    )

    p.create()

    assert p.params.name == "pytest participant"
    assert p.params.count == 3
    assert p.params.compute_unit == "g4"
    assert p.params.test_id == ids.test_id
    assert p.params.group_id == ids.group_id
    assert p.params.record_audio is False
    assert p.params.audio_feed == "silence"
    assert p.params.browser == "chrome100"
    assert p.params.location == "eu-central-1"
    assert p.params.video_feed == "480p-15fps"
    assert p.params.participant_id is not None
    assert p.params.created is not None
    assert p.params.updated is not None

    p.delete()


def test_read(mock, ids, pause):
    pid = ParticipantAPI.create(
        ParticipantParams(
            name="pytest participant",
            count=3,
            compute_unit="g4",
            test_id=ids.test_id,
            group_id=ids.group_id,
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    ).participant_id

    p = Participant(participant_id=pid, test_id=ids.test_id)

    p.read()

    assert p.params.name == "pytest participant"
    assert p.params.count == 3
    assert p.params.compute_unit == "g4"
    assert p.params.test_id == ids.test_id
    assert p.params.group_id == ids.group_id
    assert p.params.record_audio is False
    assert p.params.audio_feed == "silence"
    assert p.params.browser == "chrome100"
    assert p.params.location == "eu-central-1"
    assert p.params.video_feed == "480p-15fps"
    assert p.params.participant_id == pid
    assert p.params.created is not None
    assert p.params.updated is not None

    p.delete()


def test_update(mock, ids, pause):
    pid = ParticipantAPI.create(
        ParticipantParams(
            test_id=ids.test_id,
            group_id=ids.group_id,
            name="pytest participant",
            count=3,
            compute_unit="g4",
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    ).participant_id

    p = Participant(
        params=ParticipantParams(
            participant_id=pid,
            test_id=ids.test_id,
            group_id=ids.group_id,
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

    assert p.params.name == "pytest updated participant"
    assert p.params.count == 4
    assert p.params.compute_unit == "g6"
    assert p.params.test_id == ids.test_id
    assert p.params.group_id == ids.group_id
    assert p.params.record_audio is True
    assert p.params.audio_feed == "visqol-speech"
    assert p.params.browser == "chrome99"
    assert p.params.location == "ap-northeast-2"
    assert p.params.video_feed == "360p-15fps"
    assert p.params.participant_id == pid
    assert p.params.created is not None
    assert p.params.updated is not None

    p.delete()


def test_delete(mock, ids, pause):
    pid = ParticipantAPI.create(
        ParticipantParams(
            test_id=ids.test_id,
            group_id=ids.group_id,
            name="pytest participant",
            count=3,
            compute_unit="g4",
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    ).participant_id

    p = Participant(
        params=ParticipantParams(participant_id=pid, test_id=ids.test_id)
    )

    p.delete()

    assert p.params.test_id == ids.test_id
    assert p.params.participant_id == pid


def test_duplicate(mock, ids, pause):
    p = Participant(
        params=ParticipantParams(
            test_id=ids.test_id,
            group_id=ids.group_id,
            name="pytest participant",
            count=3,
            compute_unit="g4",
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    )

    p.create()

    dupl = p.duplicate("pytest duplicate participant")

    assert dupl.params.name == "pytest duplicate participant"
    assert dupl.params.count == 3
    assert dupl.params.compute_unit == "g4"
    assert dupl.params.test_id == ids.test_id
    assert dupl.params.group_id == ids.group_id
    assert dupl.params.record_audio is False
    assert dupl.params.audio_feed == "silence"
    assert dupl.params.browser == "chrome100"
    assert dupl.params.location == "eu-central-1"
    assert dupl.params.video_feed == "480p-15fps"
    assert dupl.params.participant_id is not None
    assert dupl.params.created is not None
    assert dupl.params.updated is not None

    p.delete()
    dupl.delete()


def test_api_create(mock, ids, pause):
    ret = ParticipantAPI.create(
        ParticipantParams(
            name="pytest participant",
            count=3,
            compute_unit="g4",
            test_id=ids.test_id,
            group_id=ids.group_id,
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    )

    assert ret.name == "pytest participant"
    assert ret.count == 3
    assert ret.compute_unit == "g4"
    assert ret.test_id == ids.test_id
    assert ret.group_id == ids.group_id
    assert ret.record_audio is False
    assert ret.audio_feed == "silence"
    assert ret.browser == "chrome100"
    assert ret.location == "eu-central-1"
    assert ret.video_feed == "480p-15fps"
    assert ret.participant_id is not None
    assert ret.created is not None
    assert ret.updated is not None

    ParticipantAPI.delete(ret)


def test_api_create_invalid_params():
    with pytest.raises(Exception):
        ParticipantAPI.create(ParticipantParams())


def test_api_read(mock, ids, pause):
    ret = ParticipantAPI.create(
        ParticipantParams(
            name="pytest participant",
            count=3,
            compute_unit="g4",
            test_id=ids.test_id,
            group_id=ids.group_id,
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    )

    p = ParticipantParams(
        test_id=ids.test_id, participant_id=ret.participant_id
    )

    ParticipantAPI.read(p)

    assert ret.name == "pytest participant"
    assert ret.count == 3
    assert ret.compute_unit == "g4"
    assert ret.test_id == ids.test_id
    assert ret.group_id == ids.group_id
    assert ret.record_audio is False
    assert ret.audio_feed == "silence"
    assert ret.browser == "chrome100"
    assert ret.location == "eu-central-1"
    assert ret.video_feed == "480p-15fps"
    assert ret.participant_id == ret.participant_id
    assert ret.created is not None
    assert ret.updated is not None

    ParticipantAPI.delete(ret)


def test_api_read_invalid_params():
    with pytest.raises(Exception):
        ParticipantAPI.read(ParticipantParams(test_id=1))

    with pytest.raises(Exception):
        ParticipantAPI.read(ParticipantParams(participant_id=1))


def test_api_update(mock, ids, pause):
    pid = ParticipantAPI.create(
        ParticipantParams(
            test_id=ids.test_id,
            group_id=ids.group_id,
            name="pytest participant",
            count=3,
            compute_unit="g4",
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    ).participant_id

    ret = ParticipantAPI.update(
        ParticipantParams(
            participant_id=pid,
            test_id=ids.test_id,
            group_id=ids.group_id,
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

    assert ret.name == "pytest updated participant"
    assert ret.count == 4
    assert ret.compute_unit == "g6"
    assert ret.test_id == ids.test_id
    assert ret.group_id == ids.group_id
    assert ret.record_audio is True
    assert ret.audio_feed == "visqol-speech"
    assert ret.browser == "chrome99"
    assert ret.location == "ap-northeast-2"
    assert ret.video_feed == "360p-15fps"
    assert ret.participant_id == pid
    assert ret.created is not None
    assert ret.updated is not None

    ParticipantAPI.delete(ret)


def test_api_update_invalid_params():
    with pytest.raises(Exception):
        ParticipantAPI.update(ParticipantParams(test_id=1))

    with pytest.raises(Exception):
        ParticipantAPI.update(ParticipantParams(participant_id=1))


def test_api_delete(mock, ids, pause):
    pid = ParticipantAPI.create(
        ParticipantParams(
            test_id=ids.test_id,
            group_id=ids.group_id,
            name="pytest participant",
            count=3,
            compute_unit="g4",
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    ).participant_id

    ret = ParticipantAPI.delete(
        ParticipantParams(participant_id=pid, test_id=ids.test_id)
    )

    assert ret is None


def test_api_delete_invalid_params():
    with pytest.raises(Exception):
        ParticipantAPI.delete(ParticipantParams(test_id=1))

    with pytest.raises(Exception):
        ParticipantAPI.delete(ParticipantParams(participant_id=1))


def test_api_duplicate(mock, ids, pause):
    p = ParticipantAPI.create(
        ParticipantParams(
            test_id=ids.test_id,
            group_id=ids.group_id,
            name="pytest participant",
            count=3,
            compute_unit="g4",
            record_audio=False,
            audio_feed="silence",
            browser="chrome100",
            location="eu-central-1",
            network="4g",
            video_feed="480p-15fps",
        )
    )

    ret = ParticipantAPI.duplicate(
        ParticipantParams(
            participant_id=p.participant_id,
            test_id=ids.test_id,
            name="pytest duplicate participant",
        )
    )

    assert ret.name == "pytest duplicate participant"
    assert ret.count == 3
    assert ret.compute_unit == "g4"
    assert ret.test_id == ids.test_id
    assert ret.group_id == ids.group_id
    assert ret.record_audio is False
    assert ret.audio_feed == "silence"
    assert ret.browser == "chrome100"
    assert ret.location == "eu-central-1"
    assert ret.video_feed == "480p-15fps"
    assert ret.participant_id is not None
    assert ret.created is not None
    assert ret.updated is not None

    ParticipantAPI.delete(p)
    ParticipantAPI.delete(ret)


def test_api_duplicate_invalid_params():
    with pytest.raises(Exception):
        ParticipantAPI.duplicate(ParticipantParams(test_id=1))

    with pytest.raises(Exception):
        ParticipantAPI.duplicate(ParticipantParams(participant_id=1))


def test_api_read_all():
    ParticipantAPI.read_all(5)
