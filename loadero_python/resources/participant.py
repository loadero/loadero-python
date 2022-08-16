"""Loadero participant resource.

Participant resources is seperated into three parts
    - ParticipantParams class describes participant attributes
    - ParticipantAPI groups all API operations with participant resource.
    - Participant class combines ParticipantParams and ParticipantAPI.

Single Participant object coresponds to single participant in Loadero.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .resource import (
    LoaderoResourceParams,
    LoaderoResource,
    DuplicateResourceBodyParams,
    from_dict_as_new,
    FilterKey,
    QueryParams,
)
from .classificator import (
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
)
from .pagination import PagedResponse


class ParticipantFilterKey(FilterKey):
    """ParticipantFilterKey is an enum of all filter keys for participant read
    all API operation."""

    NAME = "filter_name"
    COUNT_FROM = "filter_count_from"
    COUNT_TO = "filter_count_to"
    COMPUTE_UNIT = "filter_compute_unit"
    HAS_GROUP = "filter_has_group"
    RECORD_AUDIO = "filter_record_audio"
    BROWSER = "filter_browser"
    NETWORK = "filter_network"
    LOCATION = "filter_location"
    MEDIATYPE = "filter_media_type"
    VIDEOFEED = "filter_video_feed"
    AUDIOFEED = "filter_audio_feed"


class ParticipantParams(LoaderoResourceParams):
    """ParticipantParams describes single Loadero participant resources
    attributes.
    ParticipantParams has a builder pattern for Participant resource read and
    write attributes.
    """

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

        self._created = None
        self._updated = None

    @property
    def created(self) -> datetime:
        """Time when participant was created.

        Returns:
            datetime: Time when participant was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when particpant was last updated.

        Returns:
            datetime: Time when participant was last updated.
        """

        return self._updated

    def with_id(self, participant_id: int) -> ParticipantParams:
        """Set participant id.

        Args:
            participant_id (int): Participant id.

        Returns:
            ParticipantParams: Participant params with participant id set.
        """

        self.participant_id = participant_id
        return self

    def in_test(self, test_id: int) -> ParticipantParams:
        """Set parent test id.

        Args:
            test_id (int): Test id.

        Returns:
            ParticipantParams: Participant params with parent test id set.
        """

        self.test_id = test_id
        return self

    def with_name(self, name: str) -> ParticipantParams:
        """Set participant name.

        Args:
            name (str): Participant name.

        Returns:
            ParticipantParams: Participant params with participant name set.
        """

        self.name = name
        return self

    def with_count(self, count: int) -> ParticipantParams:
        """Set participant count.

        Args:
            count (int): Participant count.

        Returns:
            ParticipantParams: Participant params with participant count set.
        """

        self.count = count
        return self

    def with_compute_unit(self, compute_unit: ComputeUnit) -> ParticipantParams:
        """Set participant compute unit.

        Args:
            compute_unit (ComputeUnit): Compute unit.

        Returns:
            ParticipantParams: Participant params with set compute unit.
        """

        self.compute_unit = compute_unit
        return self

    def in_group(self, group_id: int) -> ParticipantParams:
        """Set participant parent group id.

        Args:
            group_id (int): Group id.

        Returns:
            ParticipantParams: Participant params with set parent group id.s
        """

        self.group_id = group_id
        return self

    def with_record_audio(self, record_audio: bool) -> ParticipantParams:
        """Set participant record audio flag.

        Args:
            record_audio (bool): Participant record audio flag.

        Returns:
            ParticipantParams: Participant params with set record audio flag.
        """

        self.record_audio = record_audio
        return self

    def with_audio_feed(self, audio_feed: AudioFeed) -> ParticipantParams:
        """Set participant audio feed.

        Args:
            audio_feed (AudioFeed): Participant audio feed.

        Returns:
            ParticipantParams: Participant params with set audio feed.
        """

        self.audio_feed = audio_feed
        return self

    def with_browser(self, browser: Browser) -> ParticipantParams:
        """Set participant browser.

        Args:
            browser (Browser): Browser.

        Returns:
            ParticipantParams: Participant params with set browser.
        """

        self.browser = browser
        return self

    def with_location(self, location: Location) -> ParticipantParams:
        """Set participant location.

        Args:
            location (Location): Location.

        Returns:
            ParticipantParams: Participant params with set location.
        """

        self.location = location
        return self

    def with_network(self, network: Network) -> ParticipantParams:
        """Set participant network.

        Args:
            network (Network): Network.

        Returns:
            ParticipantParams: Participant params with set network.
        """

        self.network = network
        return self

    def with_video_feed(self, video_feed: VideoFeed) -> ParticipantParams:
        """Set participant video feed.

        Args:
            video_feed (VideoFeed): Video feed.

        Returns:
            ParticipantParams: Participant params with set video feed.
        """

        self.video_feed = video_feed
        return self


class Participant(LoaderoResource):
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
        self.params = params or ParticipantParams()

        if participant_id is not None:
            self.params.participant_id = participant_id

        if test_id is not None:
            self.params.test_id = test_id

        super().__init__(self.params)

    def create(self) -> Participant:
        """Creates new participant with given data.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            Participant: Created participant resource.
        """

        ParticipantAPI.create(self.params)

        return self

    def read(self) -> Participant:
        """Reads information about an existing participant.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Participant: Read participant resource.
        """

        ParticipantAPI.read(self.params)

        return self

    def update(self) -> Participant:
        """Updates particpant with given parameters.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            Participant: Updated participant resource.
        """

        ParticipantAPI.update(self.params)

        return self

    def delete(self) -> None:
        """Deletes and existing participant.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        ParticipantAPI.delete(self.params)

    def duplicate(self, name: str) -> Participant:
        """Duplicates and existing participant.

        Args:
            name (str): New name for the duplicate participant.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Participant: Duplicate instance of participant.
        """

        return Participant(
            params=ParticipantAPI.duplicate(
                ParticipantParams(
                    participant_id=self.params.participant_id,
                    test_id=self.params.test_id,
                ),
                name,
            )
        )


class ParticipantAPI:
    """ParticipantAPI defines Loadero API operations for participant
    resources.
    """

    @staticmethod
    def create(params: ParticipantParams) -> ParticipantParams:
        """Create a new participant resource.

        Args:
            params (ParticipantParams): Describes the participant resource to
                be created.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            ParticipantParams: Created participant resource.
        """

        ParticipantAPI.__validate_identifiers(params, False)

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
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            ParticipantParams: Read participant resource.
        """

        ParticipantAPI.__validate_identifiers(params)

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
            ValueError: If resource params do not sufficiently identify
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            ParticipantParams: Updated participant resource.
        """

        ParticipantAPI.__validate_identifiers(params)

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
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        ParticipantAPI.__validate_identifiers(params)

        APIClient().delete(
            ParticipantAPI().route(params.test_id, params.participant_id)
        )

    @staticmethod
    def duplicate(params: ParticipantParams, name: str) -> ParticipantParams:
        """Duplicate an existing participant resource.

        Args:
            params (ParticipantParams): Describes the participant resource to
                duplicate and the name of duplicate participant resource.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            ParticipantParams: Duplicate participant resource.
        """

        ParticipantAPI.__validate_identifiers(params)

        return from_dict_as_new(ParticipantParams)(
            APIClient().post(
                ParticipantAPI().route(params.test_id, params.participant_id)
                + "copy/",
                DuplicateResourceBodyParams(name=name).to_dict(),
            )
        )

    @staticmethod
    def read_all(
        test_id: int,
        group_id: int or None = None,
        query_params: QueryParams or None = None,
    ) -> PagedResponse:
        """Real all participant resources.

        Args:
            test_id (int): Parent test resource id.
            group_id (int, optional): Parent group resource id. Defaults to
                None. If omitted all participants in parent test will be read.
            query_params (QueryParams, optional): Describes query parameters.

        Returns:
            PagedResponse: Paged response of participant resources.
        """

        qp = None
        if query_params is not None:
            qp = query_params.parse()

        return PagedResponse(ParticipantParams).from_dict(
            APIClient().get(
                ParticipantAPI.route(test_id, group_id=group_id),
                query_params=qp,
            )
        )

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

        r = APIClient().project_route + f"tests/{test_id}/participants/"

        if group_id is not None:
            r = (
                APIClient().project_route
                + f"tests/{test_id}/groups/{group_id}/participants/"
            )

        if participant_id is not None:
            r += f"{participant_id}/"

        return r

    @staticmethod
    def __validate_identifiers(params: ParticipantParams, single: bool = True):
        """Validate participant identifiers.

        Args:
            params (ParticipantParams): Participant resource params.
            single (bool, optional): Indicates if the resource identifiers
                should be validated as pointing to a single resource (True) or
                to all assert resources belinging to test resource.
                Defaults to True.

        Raises:
            ValueError: ParticipantParams.test_id must be a valid int
            ValueError: ParticipantParams.participant_id must be a valid int
        """

        if params.test_id is None:
            raise ValueError("ParticipantParams.test_id must be a valid int")

        if single and params.participant_id is None:
            raise ValueError(
                "ParticipantParams.participant_id must be a valid int"
            )
