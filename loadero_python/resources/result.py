"""
Loadero result resource.
Result resource is seperated into two parts - ResultParams class that describes
result attributes and Result class that in combination with ResultParams and
APIClient allows to perform CRUD operations on Loadero Result resources.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .resource import (
    LoaderoResourceParams,
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


class ResultLogParams(LoaderoResourceParams):
    """
    ResultLogParams represents Loadero result log resource attributes.
    """

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
        return self._result_log_id

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def result_id(self) -> int:
        return self._result_id

    @property
    def webrtc(self) -> str:
        return self._webrtc

    @property
    def selenium(self) -> str:
        return self._selenium

    @property
    def browser(self) -> str:
        return self._browser

    @property
    def rru(self) -> str:
        return self._rru

    @property
    def allure_report(self) -> str:
        return self._allure_report


class ResultAssertParams(LoaderoResourceParams):
    """
    ResultAssert represents Loadero result assert resource attributes.
    """

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
        return self._result_assert_id

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def path(self) -> MetricPath:
        return self._path

    @property
    def operator(self) -> Operator:
        return self._operator

    @property
    def expected(self) -> str:
        return self._expected

    @property
    def result_id(self) -> int:
        return self._result_id

    @property
    def run_assert_id(self) -> int:
        return self._run_assert_id

    @property
    def message(self) -> str:
        return self._message

    @property
    def actual(self) -> str:
        return self._actual

    @property
    def status(self) -> AssertStatus:
        return self._status


class ArtifactInfoParams(LoaderoResourceParams):
    """
    ArtifactInfoParams describes Loadero artifact resources.
    """

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
        return self._error

    @property
    def paths(self) -> list[str]:
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
        return self._audio

    @property
    def downloads(self) -> ArtifactInfoParams:
        return self._downloads

    @property
    def screenshots(self) -> ArtifactInfoParams:
        return self._screenshots

    @property
    def video(self) -> ArtifactInfoParams:
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
        return self._metric_id

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def data_count(self) -> int:
        return self._data_count

    @property
    def metric_path(self) -> MetricBasePath:
        return self._metric_path

    @property
    def value(self) -> str:
        return self._value

    @property
    def total(self) -> float:
        return self._total

    @property
    def minimum(self) -> float:
        return self._minimum

    @property
    def maximum(self) -> float:
        return self._maximum

    @property
    def average(self) -> float:
        return self._average

    @property
    def stddev(self) -> float:
        return self._stddev

    @property
    def rstddev(self) -> float:
        return self._rstddev

    @property
    def perc_1st(self) -> float:
        return self._perc_1st

    @property
    def perc_5th(self) -> float:
        return self._perc_5th

    @property
    def perc_25th(self) -> float:
        return self._perc_25th

    @property
    def perc_50th(self) -> float:
        return self._perc_50th

    @property
    def perc_75th(self) -> float:
        return self._perc_75th

    @property
    def perc_95th(self) -> float:
        return self._perc_95th

    @property
    def perc_99th(self) -> float:
        return self._perc_99th


class MetricsParams(LoaderoResourceParams):
    """
    MetricsParams groups all result metrics of a Loadero test run.
    """

    def __init__(self):
        super().__init__(
            attribute_map={
                "machine": "_machine",
                "webrtc": "_webrtc",
            },
            custom_deserializers={
                "machine": self.__from_dict_metric_list,
                "webrtc": self.__from_dict_metric_list,
            },
        )

        self._machine = None
        self._webrtc = None

    @property
    def machine(self) -> dict[MetricBasePath, MetricParams]:
        return self._machine

    @property
    def webrtc(self) -> dict[MetricBasePath, MetricParams]:
        return self._webrtc

    def __from_dict_metric_list(
        self, json_dict: dict[str, any]
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
    """
    ResultMOSParams describes a single MOS result.
    """

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
        return self._result_mos_id

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def result_id(self) -> int:
        return self._result_id

    @property
    def algorithm(self) -> MosAlgorithm:
        return self._algorithm

    @property
    def score(self) -> str:
        return self._score

    @property
    def start(self) -> datetime:
        return self._start

    @property
    def end(self) -> datetime:
        return self._end


class MeanOpinionScoresParams(LoaderoResourceParams):
    """
    MeanOpinionScoresParams groups all MOS evaluations results.
    """

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
        return self._visqol


class ResultTimecardParams(LoaderoResourceParams):
    """
    ResultTimecardParams describes a single timecard result.
    """

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
        return self._result_timecard_id

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def result_id(self) -> int:
        return self._result_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end


class DataSyncParams(LoaderoResourceParams):
    """
    DataSyncParams groups all datasync results result.
    """

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
        return self._result_timecards


class ResultParams(LoaderoResourceParams):
    """
    ResultParams represents Loadero result resource attributes.
    """

    def __init__(self, result_id: int or None = None):
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
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    @property
    def start(self) -> datetime:
        return self._start

    @property
    def end(self) -> datetime:
        return self._end

    @property
    def status(self) -> ResultStatus:
        return self._status

    @property
    def selenium_result(self) -> ResultStatus:
        return self._selenium_result

    @property
    def mos_status(self) -> MetricStatus:
        return self._mos_status

    @property
    def participant_details(self) -> RunParticipantParams:
        return self._participant_details

    @property
    def log_paths(self) -> ResultLogParams:
        return self._log_paths

    @property
    def asserts(self) -> list[ResultAssertParams]:
        return self._asserts

    @property
    def artifacts(self) -> ArtifactsInfoParams:
        return self._artifacts

    @property
    def metrics(self) -> MetricsParams:
        return self._metrics

    @property
    def mos(self) -> MeanOpinionScoresParams:
        return self._mos

    @property
    def data_sync(self) -> DataSyncParams:
        return self._data_sync


class Result:
    """
    Result class allows to perform read operation of Loadero result resource.
    APIClient must be previously initialized with a valid Loadero
    access token.
    """

    params = None
    run_id = None  # TODO: move this field to ResultParams

    def __init__(
        self,
        run_id: int or None = None,
        result_id: int or None = None,
        params: ResultParams or None = None,
    ):
        if params is not None:
            self.params = params
        else:
            self.params = ResultParams()

        if run_id is not None:
            self.run_id = run_id

        if result_id is not None:
            self.params.result_id = result_id

    def read(self) -> Result:
        """Reads a existing result.

        Raises:
            ValueError: Run id is not set.
            ValueError: Result id is not set.

        Returns:
            Result: Read result resource.
        """
        if not isinstance(self.run_id, int):
            raise ValueError("Result run_id must be a valid int")

        if not isinstance(self.params.result_id, int):
            raise ValueError("Result result_id must be a valid int")

        self.params = ResultAPI.read(self.run_id, self.params.result_id)

        return self


class ResultAPI:
    """ResultAPI defines Loadero API operations for result resources."""

    # TODO: convert function signature to take ResultParams as argument
    @staticmethod
    def read(run_id: int, result_id: int) -> ResultParams:
        """Read an existing result resource.

        Args:
            run_id (int): Run resource id that the result belongs to.
            result_id (int): Result resource id.

        Raises:
            APIException: If API call fails.

        Returns:
            ResultParams: Read Result resource params.
        """

        return from_dict_as_new(ResultParams)(
            APIClient().get(ResultAPI.route(run_id, result_id))
        )

    @staticmethod
    def read_all(run_id: int) -> list[ResultParams]:
        """Read all result resources for run.

        Args:
            run_id (int): Parent run resource id.

        Raises:
            APIException: If API call fails.

        Returns:
            list[ResultParams]: List of all result resources in run.
        """

        resp = APIClient().get(ResultAPI.route(run_id))

        if "results" not in resp or resp["results"] is None:
            return []

        return from_dict_as_list(ResultParams)(resp["results"])

    @staticmethod
    def request_mos(run_id: int, result_id: int):  # TODO: implement
        raise Exception("not implemented")

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

        r = APIClient().project_url + f"runs/{run_id}/results/"

        if result_id is not None:
            r += f"{result_id}/"

        return r
