"""Loadero result resource.
Result resource is seperated into three parts
    - ResultParams class describes result attributes
    - ResultAPI group all API operations for result resource
    - Result class combines ResultParams and ResultAPI

Single result object coresponds to single result in Loadero.
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
    from_dict_as_list,
    from_dict_as_new,
)
from .metric_path import MetricPath, MetricBasePath
from .classificator import (
    MetricStatus,
    Operator,
    AssertStatus,
    ResultStatus,
    MosAlgorithm,
)
from .run_participant import RunParticipantParams
from .pagination import PagedResponse


class ResultFilterKey(FilterKey):
    """ResultFilterKey is an enum of all filter keys for result read all API
    operation."""

    START_FROM = "filter_start_from"
    START_TO = "filter_start_to"
    END_FROM = "filter_end_from"
    END_TO = "filter_end_to"
    STATUS = "filter_status"
    SELENIUM_RESULT = "filter_selenium_result"
    MOS_STATUS = "filter_mos_status"


class ResultLogParams(LoaderoResourceParams):
    """ResultLogParams describes Loadero result log resource attributes."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "id": "_result_log_id",
                "created": "_created",
                "result_id": "_result_id",
                "webrtc": "_webrtc",
                "selenium": "_selenium",
                "browser": "_browser",
                "rru": "_rru",
                "allure_report": "_allure_report",
            },
            custom_deserializers={
                "created": parser.parse,
            },
        )

        self._result_log_id = None
        self._created = None
        self._result_id = None
        self._webrtc = None
        self._selenium = None
        self._browser = None
        self._rru = None
        self._allure_report = None

    @property
    def result_log_id(self) -> int:
        """Result log id.

        Returns:
            int: Result log id.
        """

        return self._result_log_id

    @property
    def created(self) -> datetime:
        """Time when result log  was created.

        Returns:
            datetime: Time when result log was created.
        """

        return self._created

    @property
    def result_id(self) -> int:
        """Result id that the result log belongs to.

        Returns:
            int: Result id.
        """

        return self._result_id

    @property
    def webrtc(self) -> str:
        """WebRTC log URL.

        Returns:
            str: WebRTC log URL.
        """

        return self._webrtc

    @property
    def selenium(self) -> str:
        """Selenium log URL.

        Returns:
            str: Selenium log URL.
        """

        return self._selenium

    @property
    def browser(self) -> str:
        """Browser log URL.

        Returns:
            str: Browser log URL.
        """

        return self._browser

    @property
    def rru(self) -> str:
        """Result resource usage log URL.

        Returns:
            str: Result resource usage log URL.
        """

        return self._rru

    @property
    def allure_report(self) -> str:
        """Allure report URL.

        Returns:
            str: Allure report URL.
        """

        return self._allure_report


class ResultAssertParams(LoaderoResourceParams):
    """ResultAssert describes Loadero result assert resource attributes."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "id": "_result_assert_id",
                "created": "_created",
                "path": "_path",
                "operator": "_operator",
                "expected": "_expected",
                "result_id": "_result_id",
                "run_assert_id": "_run_assert_id",
                "message": "_message",
                "actual": "_actual",
                "status": "_status",
            },
            custom_deserializers={
                "created": parser.parse,
                "operator": Operator.from_dict,
                "path": MetricPath.from_dict,
                "status": AssertStatus.from_dict,
            },
        )

        self._result_assert_id = None
        self._created = None
        self._path = None
        self._operator = None
        self._expected = None
        self._result_id = None
        self._run_assert_id = None
        self._message = None
        self._actual = None
        self._status = None

    @property
    def result_assert_id(self) -> int:
        """Result assert id.

        Returns:
            int: Result assert id.
        """

        return self._result_assert_id

    @property
    def created(self) -> datetime:
        """Time when result assert was created.

        Returns:
            datetime: Time when result assert was created.
        """

        return self._created

    @property
    def path(self) -> MetricPath:
        """Metric pats of result assert.

        Returns:
            MetricPath: Metric path.
        """

        return self._path

    @property
    def operator(self) -> Operator:
        """Operator of result assert.

        Returns:
            Operator: Operator.
        """

        return self._operator

    @property
    def expected(self) -> str:
        """Expected value of result assert.

        Returns:
            str: Expected value.
        """

        return self._expected

    @property
    def result_id(self) -> int:
        """Result id that the result assert belongs to.

        Returns:
            int: Result id.
        """

        return self._result_id

    @property
    def run_assert_id(self) -> int:
        """Run assert id that the result assert belongs to.

        Returns:
            int: Run assert id.
        """

        return self._run_assert_id

    @property
    def message(self) -> str:
        """Result assert message.

        Returns:
            str: Result assert message.
        """

        return self._message

    @property
    def actual(self) -> str:
        """Actual value of result assert.

        Returns:
            str: Actual value.
        """

        return self._actual

    @property
    def status(self) -> AssertStatus:
        """Result assert status.

        Returns:
            AssertStatus: Result assert status.
        """

        return self._status


class ArtifactInfoParams(LoaderoResourceParams):
    """ArtifactInfoParams describes Loadero artifact resources."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "error": "_error",
                "paths": "_paths",
            },
        )

        self._error = None
        self._paths = None

    @property
    def error(self) -> str:
        """Artifact error message.

        Returns:
            str: Artifact error message.
        """

        return self._error

    @property
    def paths(self) -> list[str]:
        """URLs of artifact files.

        Returns:
            list[str]: URLs of artifact files.
        """

        return self._paths


class ArtifactsInfoParams(LoaderoResourceParams):
    """
    ArtifactsInfoParams describes Loadero artifacts of a single test run.
    """

    def __init__(self):
        super().__init__(
            attribute_map={
                "audio": "_audio",
                "downloads": "_downloads",
                "screenshots": "_screenshots",
                "video": "_video",
            },
            custom_deserializers={
                "audio": from_dict_as_new(ArtifactInfoParams),
                "downloads": from_dict_as_new(ArtifactInfoParams),
                "screenshots": from_dict_as_new(ArtifactInfoParams),
                "video": from_dict_as_new(ArtifactInfoParams),
            },
        )

        self._audio = None
        self._downloads = None
        self._screenshots = None
        self._video = None

    @property
    def audio(self) -> ArtifactInfoParams:
        """Audio artifacts.

        Returns:
            ArtifactInfoParams: Audio artifacts.
        """

        return self._audio

    @property
    def downloads(self) -> ArtifactInfoParams:
        """Downloads artifacts.

        Returns:
            ArtifactInfoParams: Downloads artifacts.
        """

        return self._downloads

    @property
    def screenshots(self) -> ArtifactInfoParams:
        """Screenshots artifacts.

        Returns:
            ArtifactInfoParams: Screenshots artifacts.
        """

        return self._screenshots

    @property
    def video(self) -> ArtifactInfoParams:
        """Video artifacts.

        Returns:
            ArtifactInfoParams: Video artifacts.
        """

        return self._video


class MetricParams(LoaderoResourceParams):
    """
    MetricParams describes single result metric of a Loadero test run.
    """

    def __init__(self):
        super().__init__(
            attribute_map={
                "id": "_metric_id",
                "created": "_created",
                "data_count": "_data_count",
                "metric_path": "_metric_path",
                "value": "_value",
                "total": "_total",
                "minimum": "_minimum",
                "maximum": "_maximum",
                "average": "_average",
                "stddev": "_stddev",
                "rstddev": "_rstddev",
                "perc_1st": "_perc_1st",
                "perc_5th": "_perc_5th",
                "perc_25th": "_perc_25th",
                "perc_50th": "_perc_50th",
                "perc_75th": "_perc_75th",
                "perc_95th": "_perc_95th",
                "perc_99th": "_perc_99th",
            },
            custom_deserializers={
                "created": parser.parse,
                "metric_path": MetricBasePath.from_dict,
            },
        )

        self._metric_id = None
        self._created = None
        self._data_count = None
        self._metric_path = None
        self._value = None
        self._total = None
        self._minimum = None
        self._maximum = None
        self._average = None
        self._stddev = None
        self._rstddev = None
        self._perc_1st = None
        self._perc_5th = None
        self._perc_25th = None
        self._perc_50th = None
        self._perc_75th = None
        self._perc_95th = None
        self._perc_99th = None

    @property
    def metric_id(self) -> int:
        """Metric id.

        Returns:
            int: Metric id.
        """

        return self._metric_id

    @property
    def created(self) -> datetime:
        """Time when metric was created.

        Returns:
            datetime: Time when metric was created.
        """

        return self._created

    @property
    def data_count(self) -> int:
        """Number of data points of metric.

        Returns:
            int: Number of data points of metric.
        """

        return self._data_count

    @property
    def metric_path(self) -> MetricBasePath:
        """Metric base path of metric.

        Returns:
            MetricBasePath: Metric base path of metric.
        """

        return self._metric_path

    @property
    def value(self) -> str:
        """Value of metric.

        Returns:
            str: Value of metric.
        """

        return self._value

    @property
    def total(self) -> float:
        """Total value of all data points of metric.

        Returns:
            float: Total value of all data points of metric.
        """

        return self._total

    @property
    def minimum(self) -> float:
        """Minimum value of all data points of metric.

        Returns:
            float: Minimum value of all data points of metric.
        """

        return self._minimum

    @property
    def maximum(self) -> float:
        """Maximum value of all data points of metric.

        Returns:
            float: Maximum value of all data points of metric.
        """

        return self._maximum

    @property
    def average(self) -> float:
        """Average value of all data points of metric.

        Returns:
            float: Average value of all data points of metric.
        """

        return self._average

    @property
    def stddev(self) -> float:
        """Standard deviation of all data points of metric.

        Returns:
            float: Standard deviation of all data points of metric.
        """

        return self._stddev

    @property
    def rstddev(self) -> float:
        """Relative standard deviation of all data points of metric.

        Returns:
            float: Relative standard deviation of all data points of metric.
        """

        return self._rstddev

    @property
    def perc_1st(self) -> float:
        """1st percentile of all data points of metric.

        Returns:
            float: 1st percentile of all data points of metric.
        """

        return self._perc_1st

    @property
    def perc_5th(self) -> float:
        """5th percentile of all data points of metric.

        Returns:
            float: 5th percentile of all data points of metric.
        """

        return self._perc_5th

    @property
    def perc_25th(self) -> float:
        """25th percentile of all data points of metric.

        Returns:
            float: 25th percentile of all data points of metric.
        """

        return self._perc_25th

    @property
    def perc_50th(self) -> float:
        """50th percentile of all data points of metric.

        Returns:
            float: 50th percentile of all data points of metric.
        """

        return self._perc_50th

    @property
    def perc_75th(self) -> float:
        """75th percentile of all data points of metric.

        Returns:
            float: 75th percentile of all data points of metric.
        """

        return self._perc_75th

    @property
    def perc_95th(self) -> float:
        """95th percentile of all data points of metric.

        Returns:
            float: 95th percentile of all data points of metric.
        """

        return self._perc_95th

    @property
    def perc_99th(self) -> float:
        """99th percentile of all data points of metric.

        Returns:
            float: 99th percentile of all data points of metric.
        """

        return self._perc_99th


class MetricsParams(LoaderoResourceParams):
    """MetricsParams groups all result metrics of a Loadero test run."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "machine": "_machine",
                "webrtc": "_webrtc",
            },
            custom_deserializers={
                "machine": MetricsParams.__from_dict_metric_list,
                "webrtc": MetricsParams.__from_dict_metric_list,
            },
        )

        self._machine = None
        self._webrtc = None

    @property
    def machine(self) -> dict[MetricBasePath, MetricParams]:
        """Machine metrics.

        Returns:
            dict[MetricBasePath, MetricParams]: Machine metrics.
        """

        return self._machine

    @property
    def webrtc(self) -> dict[MetricBasePath, MetricParams]:
        """Webrtc metrics.

        Returns:
            dict[MetricBasePath, MetricParams]: Webrtc metrics.
        """

        return self._webrtc

    @staticmethod
    def __from_dict_metric_list(
        json_dict: dict[str, any]
    ) -> dict[MetricBasePath, MetricParams]:
        """Serializes metric list from JSON.

        Args:
            json_value (dict[str, any]): JSON dictionary.

        Returns:
            dict[MetricPath, MetricParams]: Mapping of metric paths to metric.
        """

        metric_list = {}

        for k, v in json_dict.items():
            m = MetricParams()
            metric_list[MetricBasePath.from_dict(k)] = m.from_dict(v)

        return metric_list


class ResultMOSParams(LoaderoResourceParams):
    """ResultMOSParams describes a single MOS result."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "id": "_result_mos_id",
                "created": "_created",
                "result_id": "_result_id",
                "algorithm": "_algorithm",
                "score": "_score",
                "start": "_start",
                "end": "_end",
            },
            custom_deserializers={
                "created": parser.parse,
                "algorithm": MosAlgorithm.from_dict,
                "start": parser.parse,
                "end": parser.parse,
            },
        )

        self._result_mos_id = None
        self._created = None
        self._result_id = None
        self._algorithm = None
        self._score = None
        self._start = None
        self._end = None

    @property
    def result_mos_id(self) -> int:
        """Result MOS ID.

        Returns:
            int: Result MOS ID.
        """

        return self._result_mos_id

    @property
    def created(self) -> datetime:
        """Time when mos result was created.

        Returns:
            datetime: Time when mos result was created.
        """

        return self._created

    @property
    def result_id(self) -> int:
        """Result id that the mos result belongs to.

        Returns:
            int: Result id that the mos result belongs to.
        """

        return self._result_id

    @property
    def algorithm(self) -> MosAlgorithm:
        """Algorithm used to calculate MOS.

        Returns:
            MosAlgorithm: Algorithm used to calculate MOS.
        """

        return self._algorithm

    @property
    def score(self) -> str:
        """Mean opinion score.

        Returns:
            str: Mean opinion score.
        """

        return self._score

    @property
    def start(self) -> datetime:
        """Start time of audio fragment.

        Returns:
            datetime: Start time of audio fragment.
        """

        return self._start

    @property
    def end(self) -> datetime:
        """End time of audio fragment.

        Returns:
            datetime: End time of audio fragment.
        """

        return self._end


class MeanOpinionScoresParams(LoaderoResourceParams):
    """MeanOpinionScoresParams groups all MOS evaluations results."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "visqol": "_visqol",
            },
            custom_deserializers={
                "visqol": from_dict_as_list(ResultMOSParams),
            },
        )

        self._visqol = None

    @property
    def visqol(self) -> list[ResultMOSParams]:
        """Mean opinion scores calculated using Visqol algorithm.

        Returns:
            list[ResultMOSParams]: Mean opinion scores calculated using Visqol
                algorithm.
        """

        return self._visqol


class ResultTimecardParams(LoaderoResourceParams):
    """ResultTimecardParams describes a single timecard result."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "id": "_result_timecard_id",
                "created": "_created",
                "result_id": "_result_id",
                "name": "_name",
                "start": "_start",
                "end": "_end",
            },
            custom_deserializers={
                "created": parser.parse,
            },
        )

        self._result_timecard_id = None
        self._created = None
        self._result_id = None
        self._name = None
        self._start = None
        self._end = None

    @property
    def result_timecard_id(self) -> int:
        """Result timecard ID.

        Returns:
            int: Result timecard ID.
        """

        return self._result_timecard_id

    @property
    def created(self) -> datetime:
        """Time when result timecard was created.

        Returns:
            datetime: Time when result timecard was created.
        """

        return self._created

    @property
    def result_id(self) -> int:
        """Result id that the timecard result belongs to.

        Returns:
            int: Result id that the timecard result belongs to.
        """

        return self._result_id

    @property
    def name(self) -> str:
        """Name of the timecard.

        Returns:
            str: Name of the timecard.
        """

        return self._name

    @property
    def start(self) -> int:
        """Start time of timecard as Unix timestamp in milliseconds.

        Returns:
            int: Start time of timecard as Unix timestamp in milliseconds.
        """

        return self._start

    @property
    def end(self) -> int:
        """End time of timecard as Unix timestamp in milliseconds.

        Returns:
            int: End time of timecard as Unix timestamp in milliseconds.
        """

        return self._end


class DataSyncParams(LoaderoResourceParams):
    """DataSyncParams groups all datasync results result."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "result_timecards": "_result_timecards",
            },
            custom_deserializers={
                "result_timecards": from_dict_as_list(ResultTimecardParams),
            },
        )

        self._result_timecards = None

    @property
    def result_timecards(self) -> list[ResultTimecardParams]:
        """List of timecards created duding test.

        Returns:
            list[ResultTimecardParams]: List of timecards created duding test.
        """

        return self._result_timecards


class ResultParams(LoaderoResourceParams):
    """ResultParams represents Loadero result resource attributes."""

    def __init__(
        self, result_id: int or None = None, run_id: int or None = None
    ):
        super().__init__(
            attribute_map={
                "id": "result_id",
                "created": "_created",
                "updated": "_updated",
                "start": "_start",
                "end": "_end",
                "status": "_status",
                "selenium_result": "_selenium_result",
                "mos_status": "_mos_status",
                "participant_details": "_participant_details",
                "log_paths": "_log_paths",
                "asserts": "_asserts",
                "artifacts": "_artifacts",
                "metrics": "_metrics",
                "mos": "_mos",
                "data_sync": "_data_sync",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "start": parser.parse,
                "end": parser.parse,
                "status": ResultStatus.from_dict,
                "selenium_result": ResultStatus.from_dict,
                "mos_status": MetricStatus.from_dict,
                "participant_details": from_dict_as_new(RunParticipantParams),
                "log_paths": from_dict_as_new(ResultLogParams),
                "asserts": from_dict_as_list(ResultAssertParams),
                "artifacts": from_dict_as_new(ArtifactsInfoParams),
                "metrics": from_dict_as_new(MetricsParams),
                "mos": from_dict_as_new(MeanOpinionScoresParams),
                "data_sync": from_dict_as_new(DataSyncParams),
            },
        )

        self.result_id = result_id
        self.run_id = run_id
        self._created = None
        self._updated = None
        self._start = None
        self._end = None
        self._status = None
        self._selenium_result = None
        self._mos_status = None
        self._participant_details = None
        self._log_paths = None
        self._asserts = None
        self._artifacts = None
        self._metrics = None
        self._mos = None
        self._data_sync = None

    @property
    def created(self) -> datetime:
        """Time when result was created.

        Returns:
            datetime: Time when result was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when result was last updated.

        Returns:
            datetime: Time when result was last updated.
        """

        return self._updated

    @property
    def start(self) -> datetime:
        """Test particpiant execution start time.

        Returns:
            datetime: Test  particpiant execution start time.
        """

        return self._start

    @property
    def end(self) -> datetime:
        """Test particpiant execution end time.

        Returns:
            datetime: Test particpiant execution end time.
        """

        return self._end

    @property
    def status(self) -> ResultStatus:
        """Test particpiant execution status.

        Returns:
            ResultStatus: Test particpiant execution status.
        """

        return self._status

    @property
    def selenium_result(self) -> ResultStatus:
        """Test script execution result of particpiant.

        Returns:
            ResultStatus: Test script execution result of particpiant.
        """

        return self._selenium_result

    @property
    def mos_status(self) -> MetricStatus:
        """Mean opinion score calculation status.

        Returns:
            MetricStatus: Mean opinion score calculation status.
        """

        return self._mos_status

    @property
    def participant_details(self) -> RunParticipantParams:
        """Participant details.

        Returns:
            RunParticipantParams: Participant details.
        """

        return self._participant_details

    @property
    def log_paths(self) -> ResultLogParams:
        """Log paths.

        Returns:
            ResultLogParams: Log paths.
        """

        return self._log_paths

    @property
    def asserts(self) -> list[ResultAssertParams]:
        """Assert results for participant.

        Returns:
            list[ResultAssertParams]: Assert results for participant.
        """

        return self._asserts

    @property
    def artifacts(self) -> ArtifactsInfoParams:
        """Artifacts created by participant.

        Returns:
            ArtifactsInfoParams: Artifacts created by participant.
        """

        return self._artifacts

    @property
    def metrics(self) -> MetricsParams:
        """Metrics results of participant.

        Returns:
            MetricsParams: Metrics results of participant.
        """

        return self._metrics

    @property
    def mos(self) -> MeanOpinionScoresParams:
        """Mean opinion score results of participant.

        Returns:
            MeanOpinionScoresParams: Mean opinion score results of participant.
        """

        return self._mos

    @property
    def data_sync(self) -> DataSyncParams:
        """Data collected with datasync wy participant.

        Returns:
            DataSyncParams: Data collected with datasync wy participant.
        """

        return self._data_sync


class Result(LoaderoResource):
    """Result class allows to perform read operation of Loadero result resource.
    APIClient must be previously initialized with a valid Loadero access token.
    """

    def __init__(
        self,
        run_id: int or None = None,
        result_id: int or None = None,
        params: ResultParams or None = None,
    ):
        self.params = params or ResultParams()

        if run_id is not None:
            self.params.run_id = run_id

        if result_id is not None:
            self.params.result_id = result_id

        super().__init__(self.params)

    def read(self) -> Result:
        """Reads a existing result.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Result: Read result resource.
        """

        ResultAPI.read(self.params)

        return self


class ResultAPI:
    """ResultAPI defines Loadero API operations for result resources."""

    @staticmethod
    def read(params: ResultParams) -> ResultParams:
        """Read an existing result resource.

        Args:
            params (ResultParams): Describes the result resource to read.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            ResultParams: Read Result resource params.
        """

        ResultAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(ResultAPI.route(params.run_id, params.result_id))
        )

    @staticmethod
    def read_all(
        run_id: int,
        query_params: QueryParams or None = None,
    ) -> PagedResponse:
        """Read all result resources for run.

        Args:
            run_id (int): Parent run resource id.
            query_params (QueryParams, optional): Describes query parameters.

        Raises:
            APIException: If API call fails.

        Returns:
            PagedResponse: Paged response of result resources.
        """

        qp = None
        if query_params is not None:
            qp = query_params.parse()

        return PagedResponse(ResultParams).from_dict(
            APIClient().get(ResultAPI.route(run_id), query_params=qp)
        )

    @staticmethod
    def route(run_id: int, result_id: int or None = None) -> str:
        """Build result url route.

        Args:
            run_id (int): Run resource id.
            result_id (int, optional): Result resource id. Defaults to None. If
                omitted, the route will point to all result resources of parent
                run resource.

        Returns:
            str: Route to result resource/s.
        """

        r = APIClient().project_route + f"runs/{run_id}/results/"

        if result_id is not None:
            r += f"{result_id}/"

        return r

    @staticmethod
    def __validate_identifiers(params: ResultParams):
        """Validate result params identifiers.

        Args:
            params (ResultParams): Result params.

        Raises:
            ValueError: Result result_id must be a valid int
            ValueError: Result run_id must be a valid int
        """

        if params.result_id is None:
            raise ValueError("Result result_id must be a valid int")

        if params.run_id is None:
            raise ValueError("Result run_id must be a valid int")
