# coding: utf-8

"""
Loadero participant resource.
Participant resources is seperated into two parts ParticipantParams class that
describes participant attributes and Participant class that in combination with
ParticipantParams and APIClient allows to perform CRUD operations on Loadero
participant resources.
"""

from __future__ import annotations
from ..api_client import APIClient


class ParticipantParams:
    """
    ParticipantParams represents Loadero participant resources attributes.
    ParticipantParams has a builder pattern for Participant resource read and
    write attributes.
    """

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
    network = None
    video_feed = None

    # route paths
    _project_id_path = None
    _test_id_path = None

    _created = None
    _updated = None

    def __init__(
        self,
        participant_id: int or None = None,
        test_id: int or None = None,
        project_id: int or None = None,
        name: str or None = None,
        count: int or None = None,
        compute_unit: str or None = None,  # classificator
        group_id: int or None = None,
        record_audio: bool or None = None,
        audio_feed: str or None = None,  # classificator
        browser: str or None = None,  # classificator
        location: str or None = None,  # classificator
        network: str or None = None,  # classificator
        video_feed: str or None = None,  # classificator
    ) -> None:
        self.participant_id = participant_id
        self._test_id_path = test_id
        self._project_id_path = project_id
        self.name = name
        self.count = count
        self.compute_unit = compute_unit
        self.group_id = group_id
        self.record_audio = record_audio
        self.audio_feed = audio_feed
        self.browser = browser
        self.location = location
        self.network = network
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
    def with_network(self, nt: str) -> ParticipantParams:
        self.network = nt

        return self

    # TODO: change to classificator
    def with_video_feed(self, vf: str) -> ParticipantParams:
        self.video_feed = vf

        return self


class Participant:
    """
    Participant class allows to perform CRUD operations on Loadero participant
    resources. APIClient must be previously initialized with a valid Loadero
    access token. The target Loadero participant resource is determined by
    ParticipantParams.
    """

    def __init__(
        self,
        test_id: int or None = None,
        params: ParticipantParams or None = None,
    ) -> None:
        if params is not None:
            self.params = params
        else:
            if self.params is None:
                self.params = ParticipantParams()

            self.params.test_id = test_id

    def create(self, api_client: APIClient) -> Participant:
        """Creates new participant with given data.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Participant: created participant resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def read(self, api_client: APIClient) -> Participant:
        """Reads information about an existing participant.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Participant: retrived participant resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def update(self, api_client: APIClient) -> Participant:
        """Updates particpant with given parameters.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Participant: updated participant resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def delete(self, api_client: APIClient) -> None:
        """Deletes and existing participant.

        Args:
            api_client (APIClient): initalized instance of API client
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

    def duplicate(self, api_client: APIClient) -> Participant:
        """Duplicates and existing participant.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Participant: duplicate instance of participant
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self
