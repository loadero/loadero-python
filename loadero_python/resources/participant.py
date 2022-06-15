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
from .resource import (
    LoaderoResourceParams,
    DuplicateResourceBodyParams,
    from_dict_as_list,
)
from .classificator import (
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
)


class ParticipantParams(LoaderoResourceParams):
    """
    ParticipantParams represents Loadero participant resources attributes.
    ParticipantParams has a builder pattern for Participant resource read and
    write attributes.
    """

    participant_id = None
    test_id = None

    name = None
    count = None
    compute_unit = None
    group_id = None
    record_audio = None

    audio_feed = None
    browser = None
    location = None
    network = None
    video_feed = None

    _created = None
    _updated = None

    def __init__(
        self,
        participant_id: int or None = None,
        test_id: int or None = None,
        name: str or None = None,
        count: int or None = None,
        compute_unit: ComputeUnit or None = None,
        group_id: int or None = None,
        record_audio: bool or None = None,
        audio_feed: AudioFeed or None = None,
        browser: Browser or None = None,
        location: Location or None = None,
        network: Network or None = None,
        video_feed: VideoFeed or None = None,
    ) -> None:
        super().__init__(
            attribute_map={
                "id": "participant_id",
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
                "created": "_created",
                "updated": "_updated",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "compute_unit": ComputeUnit.from_dict,
                "audio_feed": AudioFeed.from_dict,
                "browser": Browser.from_dict,
                "location": Location.from_dict,
                "network": Network.from_dict,
                "video_feed": VideoFeed.from_dict,
            },
            body_attributes=[
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
            ],
            required_body_attributes=[
                "name",
                "count",
                "compute_unit",
                "record_audio",
                "audio_feed",
                "browser",
                "location",
                "network",
                "video_feed",
            ],
        )

        self.participant_id = participant_id
        self.test_id = test_id
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

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    def with_id(self, pid: int) -> ParticipantParams:
        self.participant_id = pid

        return self

    def in_test(self, tid: int) -> ParticipantParams:
        self.test_id = tid

        return self

    def with_name(self, name: str) -> ParticipantParams:
        self.name = name

        return self

    def with_count(self, c: int) -> ParticipantParams:
        self.count = c

        return self

    def with_compute_unit(self, cu: ComputeUnit) -> ParticipantParams:
        self.compute_unit = cu

        return self

    def in_group(self, gid: int) -> ParticipantParams:
        self.group_id = gid

        return self

    def with_record_audio(self, ra: bool) -> ParticipantParams:
        self.record_audio = ra

        return self

    def with_audio_feed(self, af: AudioFeed) -> ParticipantParams:
        self.audio_feed = af

        return self

    def with_browser(self, browser: Browser) -> ParticipantParams:
        self.browser = browser

        return self

    def with_location(self, loc: Location) -> ParticipantParams:
        self.location = loc

        return self

    def with_network(self, nt: Network) -> ParticipantParams:
        self.network = nt

        return self

    def with_video_feed(self, vf: VideoFeed) -> ParticipantParams:
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

    def update(self) -> Participant:
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

        Args:
            name (str): New name for the duplicate participant.

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

        return params.from_dict(
            APIClient().post(
                ParticipantAPI().route(params.test_id),
                params.to_dict(),
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

        return params.from_dict(
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

        return params.from_dict(
            APIClient().put(
                ParticipantAPI().route(params.test_id, params.participant_id),
                params.to_dict(),
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

        req = DuplicateResourceBodyParams(name=params.name)

        return dupl.from_dict(
            APIClient().post(
                ParticipantAPI().route(params.test_id, params.participant_id)
                + "copy/",
                req.to_dict(),
            )
        )

    @staticmethod
    def read_all(
        test_id: int, group_id: int or None = None
    ) -> list[ParticipantParams]:
        """Real all participant resources.

        Args:
            test_id (int): Parent test resource id.
            group_id (int, optional): Parent group resource id. Defaults to
                None. If omitted all participants in parent test will be read.

        Returns:
            list[ParticipantParams]: List of all participant resources in test
                or group.
        """
        r = ParticipantAPI.route(test_id, group_id=group_id)

        resp = APIClient().get(r)

        if "results" not in resp or resp["results"] is None:
            return []

        return from_dict_as_list(ParticipantParams)(resp["results"])

    @staticmethod
    def route(
        test_id: int,
        participant_id: int or None = None,
        group_id: int or None = None,
    ) -> str:
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

        if group_id is not None:
            r = (
                APIClient().project_url
                + f"tests/{test_id}/groups/{group_id}/participants/"
            )

        if participant_id is not None:
            r += f"{participant_id}/"

        return r
