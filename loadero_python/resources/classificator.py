"""Loadero classificator constants."""

from __future__ import annotations
from enum import Enum
from .resource import LoaderoResource


# This file is generated automatically by generate-constants/generate.py script.


class Artifact(LoaderoResource, Enum):
    """
    Artifact enumerates Loadero classificator constants for
    artifact classificator type.
    """

    A_AUDIO = "audio"

    A_DOWNLOADS = "downloads"

    A_SCREENSHOT = "screenshot"

    A_VIDEO = "video"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> Artifact:
        return Artifact(jv)

    def to_json(self) -> str:
        return self.value


class AssertStatus(LoaderoResource, Enum):
    """
    AssertStatus enumerates Loadero classificator constants for
    assert_status classificator type.
    """

    AS_FAIL = "fail"

    AS_PASS = "pass"

    AS_SKIPPED = "skipped"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> AssertStatus:
        return AssertStatus(jv)

    def to_json(self) -> str:
        return self.value


class AudioFeed(LoaderoResource, Enum):
    """
    AudioFeed enumerates Loadero classificator constants for
    audio_feed classificator type.
    """

    AF_128KBPS = "128kbps"

    AF_DEFAULT = "default"

    AF_DTMF = "dtmf"

    AF_NEG_20DB = "-20db"

    AF_NEG_30DB = "-30db"

    AF_NEG_50DB = "-50db"

    AF_SILENCE = "silence"

    AF_VISQOL_SPEECH = "visqol-speech"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> AudioFeed:
        return AudioFeed(jv)

    def to_json(self) -> str:
        return self.value


class AwsStatus(LoaderoResource, Enum):
    """
    AwsStatus enumerates Loadero classificator constants for
    aws_status classificator type.
    """

    AS_CLEARING = "clearing"

    AS_FAILED = "failed"

    AS_INACTIVE = "inactive"

    AS_INITIALIZING = "initializing"

    AS_PENDING = "pending"

    AS_READY = "ready"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> AwsStatus:
        return AwsStatus(jv)

    def to_json(self) -> str:
        return self.value


class Browser(LoaderoResource, Enum):
    """
    Browser enumerates Loadero classificator constants for
    browser classificator type.
    """

    B_CHROMELATEST = "chromeLatest"

    B_FIREFOXLATEST = "firefoxLatest"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> Browser:
        return Browser(jv)

    def to_json(self) -> str:
        return self.value


class ComputeUnit(LoaderoResource, Enum):
    """
    ComputeUnit enumerates Loadero classificator constants for
    compute_unit classificator type.
    """

    CU_G0_5 = "g0.5"

    CU_G1 = "g1"

    CU_G2 = "g2"

    CU_G4 = "g4"

    CU_G6 = "g6"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> ComputeUnit:
        return ComputeUnit(jv)

    def to_json(self) -> str:
        return self.value


class FileType(LoaderoResource, Enum):
    """
    FileType enumerates Loadero classificator constants for
    file_type classificator type.
    """

    FT_FT_TEST_1 = "ft_test_1"

    FT_FT_TEST_2 = "ft_test_2"

    FT_RUN_SCRIPT = "run_script"

    FT_RUN_SSL_CERTIFICATE = "run-ssl-certificate"

    FT_SSL_CERTIFICATE = "ssl-certificate"

    FT_TEST_SCRIPT = "test_script"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> FileType:
        return FileType(jv)

    def to_json(self) -> str:
        return self.value


class IncrementStrategy(LoaderoResource, Enum):
    """
    IncrementStrategy enumerates Loadero classificator constants for
    increment_strategy classificator type.
    """

    IS_LINEAR = "linear"

    IS_LINEAR_GROUP = "linear_group"

    IS_RANDOM = "random"

    IS_RANDOM_GROUP = "random_group"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> IncrementStrategy:
        return IncrementStrategy(jv)

    def to_json(self) -> str:
        return self.value


class Language(LoaderoResource, Enum):
    """
    Language enumerates Loadero classificator constants for
    language classificator type.
    """

    L_JAVA = "java"

    L_JAVASCRIPT = "javascript"

    L_PYTHON = "python"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> Language:
        return Language(jv)

    def to_json(self) -> str:
        return self.value


class Location(LoaderoResource, Enum):
    """
    Location enumerates Loadero classificator constants for
    location classificator type.
    """

    L_AP_EAST_1 = "ap-east-1"

    L_AP_NORTHEAST_1 = "ap-northeast-1"

    L_AP_NORTHEAST_2 = "ap-northeast-2"

    L_AP_SOUTHEAST_2 = "ap-southeast-2"

    L_AP_SOUTH_1 = "ap-south-1"

    L_EU_CENTRAL_1 = "eu-central-1"

    L_EU_WEST_1 = "eu-west-1"

    L_EU_WEST_3 = "eu-west-3"

    L_SA_EAST_1 = "sa-east-1"

    L_US_EAST_1 = "us-east-1"

    L_US_EAST_2 = "us-east-2"

    L_US_WEST_2 = "us-west-2"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> Location:
        return Location(jv)

    def to_json(self) -> str:
        return self.value


class MediaType(LoaderoResource, Enum):
    """
    MediaType enumerates Loadero classificator constants for
    media_type classificator type.
    """

    MT_1080PAV = "1080pAV"

    MT_1080P_20DB = "1080p-20db"

    MT_1080P_30DB = "1080p-30db"

    MT_1080P_50DB = "1080p-50db"

    MT_240PAV = "240pAV"

    MT_240P_50DB = "240p-50db"

    MT_360PAV = "360pAV"

    MT_360P_50DB = "360p-50db"

    MT_480PAV = "480pAV"

    MT_480P_50DB = "480p-50db"

    MT_720PAV = "720pAV"

    MT_720P_50DB = "720p-50db"

    MT_720P_MARKED = "720p-marked"

    MT_CUSTOM = "custom"

    MT_DEFAULT = "default"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> MediaType:
        return MediaType(jv)

    def to_json(self) -> str:
        return self.value


class MemberRole(LoaderoResource, Enum):
    """
    MemberRole enumerates Loadero classificator constants for
    member_role classificator type.
    """

    MR_ADMINISTRATOR = "administrator"

    MR_DEVELOPER = "developer"

    MR_VISITOR = "visitor"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> MemberRole:
        return MemberRole(jv)

    def to_json(self) -> str:
        return self.value


class MetricKey(LoaderoResource, Enum):
    """
    MetricKey enumerates Loadero classificator constants for
    metric_key classificator type.
    """

    MK_1ST = "1st"

    MK_25TH = "25th"

    MK_50TH = "50th"

    MK_5TH = "5th"

    MK_75TH = "75th"

    MK_95TH = "95th"

    MK_99TH = "99th"

    MK_AUDIO = "audio"

    MK_AVAILABLE = "available"

    MK_AVG = "avg"

    MK_BITRATE = "bitrate"

    MK_BYTES = "bytes"

    MK_CODEC = "codec"

    MK_CONNECTIONS = "connections"

    MK_CPU = "cpu"

    MK_ERRORS = "errors"

    MK_FPS = "fps"

    MK_FRAMEHEIGHT = "frameHeight"

    MK_FRAMEWIDTH = "frameWidth"

    MK_IN = "in"

    MK_JITTER = "jitter"

    MK_JITTERBUFFER = "jitterBuffer"

    MK_LEVEL = "level"

    MK_MACHINE = "machine"

    MK_MAX = "max"

    MK_MIN = "min"

    MK_NETWORK = "network"

    MK_OUT = "out"

    MK_PACKETS = "packets"

    MK_PACKETSLOST = "packetsLost"

    MK_PERCENT = "percent"

    MK_RAM = "ram"

    MK_RSTDDEV = "rstddev"

    MK_RTT = "rtt"

    MK_STDDEV = "stddev"

    MK_TOTAL = "total"

    MK_USED = "used"

    MK_VIDEO = "video"

    MK_WEBRTC = "webrtc"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> MetricKey:
        return MetricKey(jv)

    def to_json(self) -> str:
        return self.value


class MetricStatus(LoaderoResource, Enum):
    """
    MetricStatus enumerates Loadero classificator constants for
    metric_status classificator type.
    """

    MS_AVAILABLE = "available"

    MS_CALCULATING = "calculating"

    MS_CALCULATION_ERROR = "calculation-error"

    MS_CALCULATION_TIMEOUT = "calculation-timeout"

    MS_NONE = "none"

    MS_REQUESTED = "requested"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> MetricStatus:
        return MetricStatus(jv)

    def to_json(self) -> str:
        return self.value


class MosAlgorithm(LoaderoResource, Enum):
    """
    MosAlgorithm enumerates Loadero classificator constants for
    mos_algorithm classificator type.
    """

    MA_VISQOL = "visqol"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> MosAlgorithm:
        return MosAlgorithm(jv)

    def to_json(self) -> str:
        return self.value


class Network(LoaderoResource, Enum):
    """
    Network enumerates Loadero classificator constants for
    network classificator type.
    """

    N_100PACKET = "100packet"

    N_10PACKET = "10packet"

    N_20PACKET = "20packet"

    N_3G = "3g"

    N_4G = "4g"

    N_50PACKET = "50packet"

    N_5PACKET = "5packet"

    N_ASYMMETRIC = "asymmetric"

    N_DEFAULT = "default"

    N_EDGE = "edge"

    N_GPRS = "gprs"

    N_HSDPA = "hsdpa"

    N_JITTER = "jitter"

    N_LATENCY = "latency"

    N_SATELLITE = "satellite"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> Network:
        return Network(jv)

    def to_json(self) -> str:
        return self.value


class NodeStatus(LoaderoResource, Enum):
    """
    NodeStatus enumerates Loadero classificator constants for
    node_status classificator type.
    """

    NS_FAILED = "failed"

    NS_PENDING = "pending"

    NS_RUNNING = "running"

    NS_STOPPED = "stopped"

    NS_TERMINATING = "terminating"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> NodeStatus:
        return NodeStatus(jv)

    def to_json(self) -> str:
        return self.value


class Operator(LoaderoResource, Enum):
    """
    Operator enumerates Loadero classificator constants for
    operator classificator type.
    """

    O_EQ = "eq"

    O_GT = "gt"

    O_GTE = "gte"

    O_LT = "lt"

    O_LTE = "lte"

    O_NEQ = "neq"

    O_REGEX = "regex"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> Operator:
        return Operator(jv)

    def to_json(self) -> str:
        return self.value


class PaymentPlan(LoaderoResource, Enum):
    """
    PaymentPlan enumerates Loadero classificator constants for
    payment_plan classificator type.
    """

    PP_ENTERPRISE = "enterprise"

    PP_MONTHLY = "monthly"

    PP_SINGLE_BASIC = "single_basic"

    PP_SINGLE_PRO = "single_pro"

    PP_YEARLY = "yearly"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> PaymentPlan:
        return PaymentPlan(jv)

    def to_json(self) -> str:
        return self.value


class PaymentStatus(LoaderoResource, Enum):
    """
    PaymentStatus enumerates Loadero classificator constants for
    payment_status classificator type.
    """

    PS_CANCELLED = "cancelled"

    PS_DECLINED = "declined"

    PS_DRAFT = "draft"

    PS_PROCESSING = "processing"

    PS_SKIP_RENEWAL = "skip_renewal"

    PS_SUCCESS = "success"

    PS_VAT_INVALID = "vat_invalid"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> PaymentStatus:
        return PaymentStatus(jv)

    def to_json(self) -> str:
        return self.value


class Property(LoaderoResource, Enum):
    """
    Property enumerates Loadero classificator constants for
    property classificator type.
    """

    P_AUDIO_FEED = "audio_feed"

    P_BROWSER = "browser"

    P_COMPUTE_UNIT = "compute_unit"

    P_GROUP_NAME = "group_name"

    P_GROUP_NUM = "group_num"

    P_LOCATION = "location"

    P_MEDIA_TYPE = "media_type"

    P_NETWORK = "network"

    P_PARTICIPANT_NAME = "participant_name"

    P_PARTICIPANT_NUM = "participant_num"

    P_VIDEO_FEED = "video_feed"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> Property:
        return Property(jv)

    def to_json(self) -> str:
        return self.value


class ResultStatus(LoaderoResource, Enum):
    """
    ResultStatus enumerates Loadero classificator constants for
    result_status classificator type.
    """

    RS_ABORTED = "aborted"

    RS_FAIL = "fail"

    RS_PASS = "pass"

    RS_TIMEOUT = "timeout"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> ResultStatus:
        return ResultStatus(jv)

    def to_json(self) -> str:
        return self.value


class RunStatus(LoaderoResource, Enum):
    """
    RunStatus enumerates Loadero classificator constants for
    run_status classificator type.
    """

    RS_ABORTED = "aborted"

    RS_AWS_ERROR = "aws-error"

    RS_COLLECTING_RESULTS = "collecting-results"

    RS_DB_ERROR = "db-error"

    RS_DONE = "done"

    RS_INITIALIZING = "initializing"

    RS_INSUFFICIENT_RESOURCES = "insufficient-resources"

    RS_NO_USERS = "no-users"

    RS_PENDING = "pending"

    RS_RUNNING = "running"

    RS_SERVER_ERROR = "server-error"

    RS_STOPPING = "stopping"

    RS_TIMEOUT_EXCEEDED = "timeout-exceeded"

    RS_WAITING_RESULTS = "waiting-results"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> RunStatus:
        return RunStatus(jv)

    def to_json(self) -> str:
        return self.value


class TestDuration(LoaderoResource, Enum):
    """
    TestDuration enumerates Loadero classificator constants for
    test_duration classificator type.
    """

    TD_15M = "15m"

    TD_1H = "1h"

    TD_24H = "24h"

    TD_2H = "2h"

    TD_45M = "45m"

    TD_4H = "4h"

    TD_8H = "8h"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> TestDuration:
        return TestDuration(jv)

    def to_json(self) -> str:
        return self.value


class TestMode(LoaderoResource, Enum):
    """
    TestMode enumerates Loadero classificator constants for
    test_mode classificator type.
    """

    TM_LOAD = "load"

    TM_PERFORMANCE = "performance"

    TM_SESSION_RECORD = "session-record"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> TestMode:
        return TestMode(jv)

    def to_json(self) -> str:
        return self.value


class VideoFeed(LoaderoResource, Enum):
    """
    VideoFeed enumerates Loadero classificator constants for
    video_feed classificator type.
    """

    VF_1080P = "1080p"

    VF_1080P_15FPS = "1080p-15fps"

    VF_1080P_30FPS = "1080p-30fps"

    VF_1080P_5FPS = "1080p-5fps"

    VF_1080P_MARKED_CENTER = "1080p-marked-center"

    VF_1080P_MARKED_TOP_LEFT = "1080p-marked-top-left"

    VF_1080P_MEETING = "1080p-meeting"

    VF_240P = "240p"

    VF_240P_15FPS = "240p-15fps"

    VF_240P_30FPS = "240p-30fps"

    VF_240P_5FPS = "240p-5fps"

    VF_240P_MARKED_TOP_LEFT = "240p-marked-top-left"

    VF_240P_MEETING = "240p-meeting"

    VF_360P = "360p"

    VF_360P_15FPS = "360p-15fps"

    VF_360P_30FPS = "360p-30fps"

    VF_360P_5FPS = "360p-5fps"

    VF_360P_MARKED_TOP_LEFT = "360p-marked-top-left"

    VF_360P_MEETING = "360p-meeting"

    VF_480P = "480p"

    VF_480P_15FPS = "480p-15fps"

    VF_480P_30FPS = "480p-30fps"

    VF_480P_5FPS = "480p-5fps"

    VF_480P_MARKED_TOP_LEFT = "480p-marked-top-left"

    VF_480P_MEETING = "480p-meeting"

    VF_720P = "720p"

    VF_720P_15FPS = "720p-15fps"

    VF_720P_30FPS = "720p-30fps"

    VF_720P_5FPS = "720p-5fps"

    VF_720P_MARKED = "720p-marked"

    VF_720P_MARKED_TOP_LEFT = "720p-marked-top-left"

    VF_720P_MEETING = "720p-meeting"

    VF_DEFAULT = "default"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> VideoFeed:
        return VideoFeed(jv)

    def to_json(self) -> str:
        return self.value
