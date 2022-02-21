# coding: utf-8

"""
    Loadero participant resource
"""

from __future__ import annotations
from ..api_client import ApiClient


class ParticipantParams:

    """Participant Params"""

    # Describes python object attribute name mapping to Loadero resources
    # JSON field names.
    attribute_map = {
        "participant_id": "id",
        "name": "name",
        "count": "count",
        "compute_unit": "compute_unit",
        "group_id": "group_id",
        "record_audio": "record_audio",
        "audio_feed": "audio_feed",
        "browser": "browser",
        "location": "location",
        "media_type": "media_type",
        "network": "network",
        "video_feed": "video_feed",
        "_test_id_path": "test_id",
        "_created": "created",
        "_updated": "updated",
    }

    body_attributes = [
        "name",
        "count",
        "compute_unit",
        "group_id",
        "record_audio",
        "audio_feed",
        "browser",
        "location",
        "media_type",
        "network",
        "video_feed",
    ]

    # id
    participant_id = None

    # body
    name = None
    count = None
    compute_unit = None  # classificator
    group_id = None
    record_audio = None

    # profile params all classificators
    audio_feed = None
    browser = None
    location = None
    media_type = None
    network = None
    video_feed = None

    # route paths
    _project_id_path = None
    _test_id_path = None

    _created = None
    _updated = None
    # profile id ?

    def __init__(
        self,
        participant_id: int or None = None,
        test_id: int or None = None,
        project_id: int or None = None,
        name: str or None = None,
        count: int or None = None,
        compute_unit: str or None = None,  # classificator
        group_id: int or None = None,
        record_audio: int or None = None,
        audio_feed: str or None = None,  # classificator
        browser: str or None = None,  # classificator
        location: str or None = None,  # classificator
        media_type: str or None = None,  # classificator
        network: str or None = None,  # classificator
        video_feed: str or None = None,  # classificator
    ) -> None:
        if participant_id is not None:
            self.participant_id = participant_id

        if test_id is not None:
            self._test_id_path = test_id

        if project_id is not None:
            self._project_id_path = project_id

        if name is not None:
            self.name = name

        if count is not None:
            self.count = count

        if compute_unit is not None:
            self.compute_unit = compute_unit

        if group_id is not None:
            self.group_id = group_id

        if record_audio is not None:
            self.record_audio = record_audio

        if audio_feed is not None:
            self.audio_feed = audio_feed

        if browser is not None:
            self.browser = browser

        if location is not None:
            self.location = location

        if media_type is not None:
            self.media_type = media_type

        if network is not None:
            self.network = network

        if video_feed is not None:
            self.video_feed = video_feed

    # getters

    @property
    def created(self):  # date time
        return self._created

    @property
    def updated(self):  # date time
        return self._updated

    @property
    def project_id(self) -> int:
        return self._project_id_path

    @property
    def test_id(self) -> int:
        return self._test_id_path

    # builder

    def with_id(self, pid: int) -> ParticipantParams:
        self.participant_id = pid

        return self

    def in_test(self, tid: int) -> ParticipantParams:
        self._test_id_path = tid

        return self

    def in_project(self, pid: int) -> ParticipantParams:
        self._project_id_path = pid

        return self

    def with_name(self, name: str) -> ParticipantParams:
        self.name = name

        return self

    def with_count(self, c: int) -> ParticipantParams:
        self.count = c

        return self

    # TODO: change to classificator
    def with_compute_unit(self, cu: str) -> ParticipantParams:
        self.compute_unit = cu

        return self

    def in_group(self, gid: int) -> ParticipantParams:
        self.group_id = gid

        return self

    def with_record_audio(self, ra: bool) -> ParticipantParams:
        self.record_audio = ra

        return self

    # TODO: change to classificator
    def with_audio_feed(self, af: str) -> ParticipantParams:
        self.audio_feed = af

        return self

    # TODO: change to classificator
    def with_browser(self, browser: str) -> ParticipantParams:
        self.browser = browser

        return self

    # TODO: change to classificator
    def with_location(self, loc: str) -> ParticipantParams:
        self.location = loc

        return self

    # TODO: change to classificator
    def with_media_type(self, mt: str) -> ParticipantParams:
        self.media_type = mt

        return self

    # TODO: change to classificator
    def with_network(self, nt: str) -> ParticipantParams:
        self.network = nt

        return self

    # TODO: change to classificator
    def with_video_feed(self, vf: str) -> ParticipantParams:
        self.video_feed = vf

        return self


class Participant:
    """
    Loadero participant resource
    """

    def __init__(
        self,
        test_id: int or None = None,
        params: ParticipantParams or None = None,
    ) -> None:
        if params is not None:
            self.params = params

        if test_id is not None:
            if self.params is None:
                self.params = ParticipantParams()

            self.params.test_id = test_id

    def create(self, api_client: ApiClient) -> Participant:
        """create operation"""
        api_client.call_api(self.params)

        return self

    def read(self, api_client: ApiClient) -> Participant:
        """read operation"""
        api_client.call_api(self.params)

        return self

    def update(self, api_client: ApiClient) -> Participant:
        """update operation"""
        api_client.call_api(self.params)

        return self

    def delete(self, api_client: ApiClient) -> Participant:
        """delete operation"""
        api_client.call_api(self.params)

        return self

    def duplicate(self, api_client: ApiClient) -> Participant:
        """delete operation"""
        api_client.call_api(self.params)

        return self
