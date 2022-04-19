# coding: utf-8

"""
Loadero participant resource.
Participant resources is seperated into two parts ParticipantParams class that
describes participant attributes and Participant class that in combination with
ParticipantParams and APIClient allows to perform CRUD operations on Loadero
participant resources.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .resource import LoaderoResource, to_json, from_json, to_string


class ParticipantParams(LoaderoResource):
    """
    ParticipantParams represents Loadero participant resources attributes.
    ParticipantParams has a builder pattern for Participant resource read and
    write attributes.
    """

    # Describes python object attribute name mapping to Loadero resources
    # JSON field names.
    __attribute_map = {
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
        "test_id": "test_id",
        "_created": "created",
        "_updated": "updated",
    }

    # TODO: make group id optional

    # Describes Loadero resources JSON field names that are required for CRUD
    # operations.
    __body_attributes = [
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

    # Describes a mapping from Loadero resources JSON field names to custom
    # deserialization functions.
    __custom_deserializers = {
        "created": parser.parse,
        "updated": parser.parse,
    }

    participant_id = None
    test_id = None

    name = None
    count = None
    compute_unit = None  # classificator
    group_id = None
    record_audio = None

    audio_feed = None
    browser = None
    location = None
    network = None
    video_feed = None

    _project_id = None
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
        self.test_id = test_id
        self._project_id = project_id
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

    def __str__(self) -> str:
        return to_string(self.__dict__, self.__attribute_map)

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    @property
    def project_id(self) -> int:
        return self._project_id

    def with_id(self, pid: int) -> ParticipantParams:
        self.participant_id = pid

        return self

    def in_test(self, tid: int) -> ParticipantParams:
        self.test_id = tid

        return self

    def in_project(self, pid: int) -> ParticipantParams:
        self._project_id = pid

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

    def to_json(
        self, body_attributes: list[str] or None = None
    ) -> dict[str, any]:
        """Serializes participant resource to JSON.

        Args:
            body_attributes (list[str] or None, optional): String list of JSON
                field names that will be serialized. Defaults to None, then
                the default body attributed for participant resource are used.

        Returns:
            dict[str, any]: JSON dictionary.
        """

        if body_attributes is None:
            body_attributes = self.__body_attributes

        return to_json(self.__dict__, self.__attribute_map, body_attributes)

    def from_json(self, json_value: dict[str, any]) -> ParticipantParams:
        """Serializes participant resource from JSON.

        Args:
            json_value (dict[str, any]): JSON dictionary.

        Returns:
            ParticipantParams: Serialized participant resource.
        """

        from_json(
            self.__dict__,
            json_value,
            self.__attribute_map,
            self.__custom_deserializers,
        )

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
        participant_id: int or None = None,
        test_id: int or None = None,
        params: ParticipantParams or None = None,
    ) -> None:
        if params is not None:
            self.params = params
        else:
            self.params = ParticipantParams()

        if participant_id is not None:
            self.params.participant_id = participant_id

        if test_id is not None:
            self.params.test_id = test_id

    def create(self) -> Participant:
        """Creates new participant with given data.

        Returns:
            Participant: Created participant resource.
        """

        ParticipantAPI.create(self.params)

        return self

    def read(self) -> Participant:
        """Reads information about an existing participant.

        Returns:
            Participant: Read participant resource.
        """

        ParticipantAPI.read(self.params)

        return self

    def update(
        self,
    ) -> Participant:
        """Updates particpant with given parameters.

        Returns:
            Participant: Updated participant resource.
        """

        ParticipantAPI.update(self.params)

        return self

    def delete(self) -> None:
        """Deletes and existing participant."""

        ParticipantAPI.delete(self.params)

    def duplicate(self, name: str) -> Participant:
        """Duplicates and existing participant.

        Returns:
            Participant: Duplicate instance of participant.
        """

        dp = ParticipantParams(
            participant_id=self.params.participant_id,
            test_id=self.params.test_id,
            name=name,
        )

        dupl = Participant(params=ParticipantAPI.duplicate(dp))

        return dupl


class ParticipantAPI:
    """
    ParticipantAPI defines Loadero API operations for participant resources.
    """

    @staticmethod
    def create(params: ParticipantParams) -> ParticipantParams:
        """Create a new participant resource.

        Args:
            params (ParticipantParams): Describes the participant resource to
                be created.

        Raises:
            Exception: ParticipantParams.test_id was not defined.

        Returns:
            ParticipantParams: Created participant resource.
        """

        if params.test_id is None:
            raise Exception("ParticipantParams.test_id must be a valid int")

        return params.from_json(
            APIClient().post(
                ParticipantAPI().route(params.test_id),
                params.to_json(),
            )
        )

    @staticmethod
    def read(params: ParticipantParams) -> ParticipantParams:
        """Read an existing participant resource.

        Args:
            params (ParticipantParams): Describes the participant resource to
                read.

        Raises:
            Exception: ParticipantParams.test_id was not defined.
            Exception: ParticipantParams.participant_id was not defined.

        Returns:
            ParticipantParams: Read participant resource.
        """

        if params.test_id is None:
            raise Exception("ParticipantParams.test_id must be a valid int")

        if params.participant_id is None:
            raise Exception(
                "ParticipantParams.participant_id must be a valid int"
            )

        return params.from_json(
            APIClient().get(
                ParticipantAPI().route(params.test_id, params.participant_id)
            )
        )

    @staticmethod
    def update(params: ParticipantParams) -> ParticipantParams:
        """Update an existing participant resource.

        Args:
            params (ParticipantParams): Describes the participant resource to
                update.

        Raises:
            Exception: ParticipantParams.test_id was not defined.
            Exception: ParticipantParams.participant_id was not defined.

        Returns:
            ParticipantParams: Updated participant resource.
        """

        if params.test_id is None:
            raise Exception("ParticipantParams.test_id must be a valid int")

        if params.participant_id is None:
            raise Exception(
                "ParticipantParams.participant_id must be a valid int"
            )

        return params.from_json(
            APIClient().put(
                ParticipantAPI().route(params.test_id, params.participant_id),
                params.to_json(),
            )
        )

    @staticmethod
    def delete(params: ParticipantParams) -> None:
        """Delete an existing participant resource.

        Args:
            params (ParticipantParams): Describes the participant resource to
                delete.

        Raises:
            Exception: ParticipantParams.test_id was not defined.
            Exception: ParticipantParams.participant_id was not defined.
        """

        if params.test_id is None:
            raise Exception("ParticipantParams.test_id must be a valid int")

        if params.participant_id is None:
            raise Exception(
                "ParticipantParams.participant_id must be a valid int"
            )

        APIClient().delete(
            ParticipantAPI().route(params.test_id, params.participant_id)
        )

    @staticmethod
    def duplicate(params: ParticipantParams) -> ParticipantParams:
        """Duplicate an existing participant resource.

        Args:
            params (ParticipantParams): Describes the participant resource to
                duplicate and the name of duplicate participant resource.

        Raises:
            Exception: ParticipantParams.test_id was not defined.
            Exception: ParticipantParams.participant_id was not defined.

        Returns:
            ParticipantParams: Duplicate participant resource.
        """

        if params.test_id is None:
            raise Exception("ParticipantParams.test_id must be a valid int")

        if params.participant_id is None:
            raise Exception(
                "ParticipantParams.participant_id must be a valid int"
            )

        dupl = ParticipantParams()

        return dupl.from_json(
            APIClient().post(
                ParticipantAPI().route(params.test_id, params.participant_id)
                + "copy/",
                params.to_json(["name"]),
            )
        )

    @staticmethod
    def read_all(test_id: int):
        # TODO: implement.
        pass

    @staticmethod
    def route(test_id: int, participant_id: int or None = None) -> str:
        """Build participant resource url route.

        Args:
            test_id (int): Test resource id.
            participant_id (int, optional): Participant resource id. Defaults
                to None. If omitted the route will point to all participant
                resources.

        Returns:
            str: Route to participant resource/s.
        """
        r = APIClient().project_url + f"tests/{test_id}/participants/"

        if participant_id is not None:
            r += f"{participant_id}/"

        return r
