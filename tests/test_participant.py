"""Participant resource tests"""

from loadero_python.resources import participant
from loadero_python.api_client.api_client import ApiClient


def test_participant_params():
    pp = participant.ParticipantParams(count=4)
    assert pp.count == 4

    pp.in_project(5)
    assert pp.project_id == 5


def test_participant():
    api = ApiClient()
    pp = participant.ParticipantParams(count=4)
    p = participant.Participant(params=pp)

    p.read(api)
