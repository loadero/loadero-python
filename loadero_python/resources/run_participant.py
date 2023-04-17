"""Loadero run participant resource.

Run participant resources is seperated into three parts
    RunParticipantParams class describes run participant attributes

    RunParticipantAPI class groups all API operations related to run
    participant.

    RunParticipant class combined RunParticipantParams and RunParticipantAPI.

Single RunParticipant object coresponds to single run participant in Loadero.
"""


from __future__ import annotations
from datetime import datetime
from dateutil import parser

from ..api_client import APIClient
from .resource import (
    FilterKey,
    LoaderoResourceParams,
    LoaderoResource,
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


class RunParticipantFilterKey(FilterKey):
    """RunParticipantFilterKey is an enum of all filter keys for run participant
    read all API operation.
    """

    NAME = "filter_name"
    NUM_FROM = "filter_num_from"
    NUM_TO = "filter_num_to"
    GROUP_NAME = "filter_group_name"
    GROUP_NUM_FROM = "filter_group_num_from"
    GROUP_NUM_TO = "filter_group_num_to"
    RECORD_AUDIO = "filter_record_audio"
    BROWSER = "filter_browser"
    NETWORK = "filter_network"
    LOCATION = "filter_location"
    MEDIA_TYPE = "filter_media_type"
    VIDEO_FEED = "filter_video_feed"
    AUDIO_FEED = "filter_audio_feed"


class RunParticipantParams(LoaderoResourceParams):
    """RunParticipantParams represents Loadero RunParticipant resource
    attributes.
    """

    def __init__(
        self, run_participant_id: int or None = None, run_id: int or None = None
    ) -> None:
        """Creates a new RunParticipantParams instance that will contain single
        run participant resources attributes.

        Args:
            run_participant_id (int, optional): Existing run participant
            resources ID. Defaults to None.

            run_id (int, optional): Existing run resources ID. Defaults to None.
        """

        super().__init__(
            attribute_map={
                "id": "run_participant_id",
                "created": "_created",
                "updated": "_updated",
                "participant_num": "_participant_num",
                "participant_name": "_participant_name",
                "group_num": "_group_num",
                "group_name": "_group_name",
                "compute_unit": "_compute_unit",
                "audio_feed": "_audio_feed",
                "browser": "_browser",
                "location": "_location",
                "network": "_network",
                "video_feed": "_video_feed",
                "run_id": "run_id",
                "record_audio": "_record_audio",
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
        )

        self.run_participant_id = run_participant_id
        self.run_id = run_id

        self._created = None
        self._updated = None
        self._participant_num = None
        self._participant_name = None
        self._group_num = None
        self._group_name = None
        self._compute_unit = None

        self._audio_feed = None
        self._browser = None
        self._location = None
        self._network = None
        self._video_feed = None

        self._record_audio = None

    @property
    def created(self) -> datetime:
        """Time when run participant was created.

        Returns:
            datetime: Time when run participant was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when run participant was last updated.

        Returns:
            datetime: Time when run participant was last updated.
        """

        return self._updated

    @property
    def participant_num(self) -> int:
        """Participants number in group.

        Returns:
            int: Participants number in group.
        """

        return self._participant_num

    @property
    def participant_name(self) -> str:
        """Participants name.

        Returns:
            str: Participants name.
        """

        return self._participant_name

    @property
    def group_num(self) -> int:
        """Group number in test that the participant is in.

        Returns:
            int: Group number in test that the participant is in.
        """

        return self._group_num

    @property
    def group_name(self) -> int:
        """Name of the group that the participant is in.

        Returns:
            int: Name of the group that the participant is in.
        """

        return self._group_name

    @property
    def compute_unit(self) -> ComputeUnit:
        """Compute unit of participant.

        Returns:
            ComputeUnit: Compute unit of participant.
        """

        return self._compute_unit

    @property
    def audio_feed(self) -> AudioFeed:
        """Audio feed of participant.

        Returns:
            AudioFeed: Audio feed of participant.
        """

        return self._audio_feed

    @property
    def browser(self) -> Browser:
        """Browser of participant.

        Returns:
            Browser: Browser of participant.
        """

        return self._browser

    @property
    def location(self) -> Location:
        """Location of participant.

        Returns:
            Location: Location of participant.
        """

        return self._location

    @property
    def network(self) -> Network:
        """Network of participant.

        Returns:
            Network: Network of participant.
        """

        return self._network

    @property
    def video_feed(self) -> VideoFeed:
        """Video feed of participant.

        Returns:
            VideoFeed: Video feed of participant.
        """

        return self._video_feed

    @property
    def record_audio(self) -> bool:
        """Flag indicating whether audio was recorded.

        Returns:
            bool: Flag indicating whether audio was recorded.
        """

        return self._record_audio

    # builder

    def with_id(self, run_participant_id: int) -> RunParticipantParams:
        """Set run participant id.

        Args:
            run_participant_id (int): Run participant id.

        Returns:
            RunParticipantParams: Run participant params with set id.
        """

        self.run_participant_id = run_participant_id
        return self


class RunParticipant(LoaderoResource):
    """RunParticipant class allows to perform read operations on Loadero run
    participant resources.

    APIClient must be previously initialized with a valid Loadero access token.

    The target Loadero run participant resource is determined by
    RunParticipantParams.
    """

    def __init__(
        self,
        run_participant_id: int or None = None,
        run_id: int or None = None,
        params: RunParticipantParams or None = None,
    ) -> None:
        """Creates a new instance of RunParticipant that allows to perform read
        operations on a single run participant resource.

        The resources attribute data is stored in params field that is an
        instance of RunParticipantParams.

        Args:
            run_participant_id (int, optional): Existing run_participant
            resources ID. Defaults to None.

            run_id (int, optional): Existing run resources ID. Defaults to None.

            params (RunParticipantParams, optional): Instance of
            RunParticipantParams that describes the run participant resource.
            Defaults to None.
        """

        self.params = params or RunParticipantParams()

        if run_participant_id is not None:
            self.params.run_participant_id = run_participant_id

        if run_id is not None:
            self.params.run_id = run_id

        super().__init__(self.params)

    def read(self) -> RunParticipant:
        """Reads information about an existing run participant.

        Required attributes of params field that need to be populated, otherwise
        the method will raise an exception:

        - run_participant_id
        - run_id

        Raises:
            ValueError: If resource params do not sufficiently identify
            resource.

            APIException: If API call fails.

        Returns:
            Test: Read run participants resource.
        """

        RunParticipantAPI.read(self.params)

        return self


class RunParticipantAPI:
    """RunParticipantAPI defines Loadero API operations for run participant
    resources.
    """

    @staticmethod
    def read(params: RunParticipantParams) -> RunParticipantParams:
        """Read an existing run participant resource.

        Args:
            params (RunParticipantParams): Describes run participant resource to
            read.

        Returns:
            RunParticipantParams: Read run participant resource.
        """

        RunParticipantAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(
                RunParticipantAPI.route(
                    params.run_id, params.run_participant_id
                )
            )
        )

    @staticmethod
    def read_all(
        run_id: int, query_params: QueryParams or None = None
    ) -> PagedResponse:
        """Read all run participant resources.

        Args:
            run_id (int): Parent run resource id.
            query_params (QueryParams, optional): Describes query parameters.

        Raises:
            APIException: If API call fails.

        Returns:
            PagedResponse: Paged response of run participant resources.
        """

        qp = None
        if query_params is not None:
            qp = query_params.parse()

        return PagedResponse(RunParticipantParams).from_dict(
            APIClient().get(RunParticipantAPI.route(run_id), query_params=qp)
        )

    @staticmethod
    def route(run_id: int, run_particpant_id: int or None = None) -> str:
        """Build run participant resource route

        Args:
            run_id (int): Run resource id.

            run_particpant_id (int or None, optional): Run participant resource
            id. Defaults to None. If omitted the route will point to all run
            participant resources.

        Returns:
            str: Route to run participant resource/s.
        """

        r = APIClient().project_route + f"runs/{run_id}/participants/"

        if run_particpant_id is not None:
            r += f"{run_particpant_id}/"

        return r

    @staticmethod
    def __validate_identifiers(
        params: RunParticipantParams, single: bool = True
    ):
        """Validate run participant resource identifiers.

        Args:
            params (TestParams): Run participant params.

            single (bool, optional): Indicates if the resource identifiers
            should be validated as pointing to a single resource.
            Defaults to True.

        Raises:
            ValueError: RunParticipantParams.run_participant_id must be a valid
            int.
            ValueError: RunParticipantParams.run_id must be a valid int.
        """

        if params.run_id is None:
            raise ValueError("RunParticipantParams.run_id must be a valid int.")

        if single and params.run_participant_id is None:
            raise ValueError(
                "RunParticipantParams.run_participant_id must be a valid int"
            )
