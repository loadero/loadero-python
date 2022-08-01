"""Loadero run participant resource.
Run participant resources is seperated into three parts
    - RunParticipantParams class describes run participant attributes
    - RunParticipantAPI class groups all API operations related to run
        participant.
    - RunParticipant class combined RunParticipantParams and RunParticipantAPI.

Single RunParticipant object coresponds to single run participant in Loadero.
"""


from __future__ import annotations
from datetime import datetime
from dateutil import parser
from .resource import LoaderoResourceParams
from .classificator import (
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
)


class RunParticipantParams(LoaderoResourceParams):
    """
    RunParticipantParams represents Loadero RunParticipant resource attributes.
    """

    def __init__(self, run_participant_id: int or None = None) -> None:
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
                "run_id": "_run_id",
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

        self._run_id = None
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
    def run_id(self) -> int:
        """Run id that the participant belongs to.

        Returns:
            int: Run id that the participant belongs to.
        """

        return self._run_id

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


class RunParticipant:
    """Not implemented."""


class RunParticipantAPI:
    """Not implemented."""
