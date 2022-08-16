"""
Loadero run resource.
Run resources is seperated into three parts:
    RunParams class that describes runs attributes
    RunAPI class implements run resources API operations
    Runs class that in combination with RunParams and RunAPI allows to manage a
        single run resources instance.
"""

from __future__ import annotations
from time import sleep
from datetime import datetime
from dateutil import parser
from .pagination import PagedResponse, PaginationParams
from ..api_client import APIClient
from .resource import (
    FilterKey,
    LoaderoResourceParams,
    LoaderoResource,
    QueryParams,
    convert_params_list,
)
from .classificator import (
    RunStatus,
    MetricStatus,
    TestMode,
    IncrementStrategy,
)
from .result import Result, ResultAPI


class RunFilterKey(FilterKey):
    """RunFilterKey is an enum of all filter keys for run read all API
    operation."""

    NAME = "filter_test_name"
    INCREMENT_STRATEGY = "filter_increment_strategy"
    STATUS = "filter_status"
    METRIC_STATUS = "filter_metric_status"
    TEST_MODE = "filter_test_mode"
    MOS_STATUS = "filter_mos_status"
    START_INTERVAL_FROM = "filter_start_interval_from"
    START_INTERVAL_TO = "filter_start_interval_to"
    PARTICIPANT_TIMEOUT_FROM = "filter_participant_timeout_from"
    PARTICIPANT_TIMEOUT_TO = "filter_participant_timeout_to"
    STARTED_FROM = "filter_started_from"
    STARTED_TO = "filter_started_to"
    FINISHED_FROM = "filter_finished_from"
    FINISHED_TO = "filter_finished_to"
    EXECUTION_STARTED_FROM = "filter_execution_started_from"
    EXECUTION_STARTED_TO = "filter_execution_started_to"
    EXECUTION_FINISHED_FROM = "filter_execution_finished_from"
    EXECUTION_FINISHED_TO = "filter_execution_finished_to"
    MOS_TEST = "filter_mos_test"
    STARTED = "filter_started"
    FINISHED = "filter_finished"


class RunParams(LoaderoResourceParams):
    """
    RunParams represents Loadero run resource attributes.
    """

    def __init__(
        self, run_id: int or None = None, test_id: int or None = None
    ) -> None:
        super().__init__(
            attribute_map={
                "id": "run_id",
                "test_id": "test_id",
                "created": "_created",
                "updated": "_updated",
                "status": "_status",
                "metric_status": "_metric_status",
                "test_mode": "_test_mode",
                "increment_strategy": "_increment_strategy",
                "mos_status": "_mos_status",
                "processing_started": "_processing_started",
                "processing_finished": "_processing_finished",
                "execution_started": "_execution_started",
                "execution_finished": "_execution_finished",
                "script_file_id": "_script_file_id",
                "test_name": "_test_name",
                "start_interval": "_start_interval",
                "participant_timeout": "_participant_timeout",
                "launching_account_id": "_launching_account_id",
                "success_rate": "_success_rate",
                "total_cu_count": "_total_cu_count",
                "group_count": "_group_count",
                "participant_count": "_participant_count",
                "mos_test": "_mos_test",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "status": RunStatus.from_dict,
                "metric_status": MetricStatus.from_dict,
                "test_mode": TestMode.from_dict,
                "increment_strategy": IncrementStrategy.from_dict,
                "mos_status": MetricStatus.from_dict,
                "processing_started": parser.parse,
                "processing_finished": parser.parse,
                "execution_started": parser.parse,
                "execution_finished": parser.parse,
            },
        )

        self.run_id = run_id
        self.test_id = test_id

        self._created = None
        self._updated = None

        self._status = None
        self._metric_status = None
        self._test_mode = None
        self._increment_strategy = None
        self._mos_status = None
        self._processing_started = None
        self._processing_finished = None
        self._execution_started = None
        self._execution_finished = None
        self._script_file_id = None
        self._test_name = None
        self._start_interval = None
        self._participant_timeout = None
        self._launching_account_id = None
        self._success_rate = None
        self._total_cu_count = None
        self._group_count = None
        self._participant_count = None
        self._mos_test = None

    @property
    def created(self) -> datetime:
        """Time when run was created.

        Returns:
            datetime: Time when run was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when run was last updated.

        Returns:
            datetime: Time when run was last updated.
        """

        return self._updated

    @property
    def status(self) -> RunStatus:
        """Status of the run.

        Returns:
            RunStatus: Status of the run.
        """

        return self._status

    @property
    def metric_status(self) -> MetricStatus:
        """Status of metric calculation for the run.

        Returns:
            MetricStatus: Status of metric calculation for the run.
        """

        return self._metric_status

    @property
    def test_mode(self) -> TestMode:
        """Test mode of the run.

        Returns:
            TestMode: Test mode of the run.
        """

        return self._test_mode

    @property
    def increment_strategy(self) -> IncrementStrategy:
        """Increment strategy of the run.

        Returns:
            IncrementStrategy: Increment strategy of the run.
        """

        return self._increment_strategy

    @property
    def mos_status(self) -> MetricStatus:
        """Status of mean opinion score calculation for the run.

        Returns:
            MetricStatus: Status of mean opinion score calculation for the run.
        """

        return self._mos_status

    @property
    def processing_started(self) -> datetime:
        """Time when processing of the run started.

        Returns:
            datetime: Time when processing of the run started.
        """

        return self._processing_started

    @property
    def processing_finished(self) -> datetime:
        """Time when processing of the run finished.

        Returns:
            datetime: Time when processing of the run finished.
        """

        return self._processing_finished

    @property
    def execution_started(self) -> datetime:
        """Time when test script execution of the run started.

        Returns:
            datetime: Time when test script execution of the run started.
        """

        return self._execution_started

    @property
    def execution_finished(self) -> datetime:
        """Time when test script execution of the run finished.

        Returns:
            datetime: Time when test script execution of the run finished.
        """

        return self._execution_finished

    @property
    def script_file_id(self) -> int:
        """ID of the script file used for the run.

        Returns:
            int: ID of the script file used for the run.
        """

        return self._script_file_id

    @property
    def test_name(self) -> str:
        """Name of the test being run.

        Returns:
            str: Name of the test being run.
        """

        return self._test_name

    @property
    def start_interval(self) -> int:
        """Start interval of the test.

        Returns:
            int: Start interval of the test.
        """

        return self._start_interval

    @property
    def participant_timeout(self) -> int:
        """Timeout for participants in the test.

        Returns:
            int: Timeout for participants in the test.
        """

        return self._participant_timeout

    # TODO: consider removing this property, because project tokens cant do
    # anything with this data.

    @property
    def launching_account_id(self) -> int:
        """ID of the account that launched the test.

        Returns:
            int: ID of the account that launched the test.
        """

        return self._launching_account_id

    @property
    def success_rate(self) -> float:
        """Fraction of participants that finished the test successfully over
        the total number of participants.

        Returns:
            float: Success rate of the test run.
        """

        return self._success_rate

    @property
    def total_cu_count(self) -> float:
        """Total compute units used by the test run.

        Returns:
            float: Total compute units used by the test run.
        """

        return self._total_cu_count

    @property
    def group_count(self) -> int:
        """Number of groups in the test.

        Returns:
            int: Number of groups in the test.
        """

        return self._group_count

    @property
    def participant_count(self) -> int:
        """Number of participants in the test.

        Returns:
            int: Number of participants in the test.
        """

        return self._participant_count

    @property
    def mos_test(self) -> bool:
        """Whether the test run is a MOS test run.

        Returns:
            bool: Whether the test run is a MOS test run.
        """

        return self._mos_test

    # param builder

    def with_id(self, run_id: int) -> RunParams:
        """Set the ID of the run.

        Args:
            run_id (int): ID of the run.

        Returns:
            RunParams: Run params with set run id.
        """

        self.run_id = run_id
        return self

    def in_test(self, test_id: int) -> RunParams:
        """Set the ID of the test.

        Args:
            test_id (int): ID of the test.

        Returns:
            RunParams: Run params with set test id.
        """

        self.test_id = test_id
        return self


class Run(LoaderoResource):
    """Run class allows to create, read and stop runs.
    APIClient must be previously initialized with a valid Loadero access token.
    The target Loadero run resource is determined by RunParams.
    """

    def __init__(
        self,
        run_id: int or None = None,
        test_id: int or None = None,
        params: RunParams or None = None,
    ) -> None:
        self.params = params or RunParams()

        if run_id is not None:
            self.params.run_id = run_id

        if test_id is not None:
            self.params.test_id = test_id

        super().__init__(self.params)

    def create(self) -> Run:
        """Creates new run with given data.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource.
            APIException: If API call fails.

        Returns:
            Run: Created run resource.
        """

        RunAPI.create(self.params)

        return self

    def read(self) -> Run:
        """Read an existing run resource.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Run: Read run resource.
        """

        RunAPI.read(self.params)

        return self

    def stop(self) -> Run:
        """Stop an active run. To stop a run need only to specify the test_id
        and run_id in resource params.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Run: Stopped run resource.
        """

        RunAPI.stop(self.params)

        return self

    def poll(
        self, interval: float = 15.0, timeout: float = 12 * 60 * 60
    ) -> Run:
        """Polls run status until it is finished.

        Args:
            interval (float, optional): Poll interval in seconds.
                Defaults to 15.0.
            timeout (float, optional): Poll timeout in seconds. Defaults to
                12*60*60 (12h).

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
            TimeoutError: Run poll timeout exceeded

        Returns:
            Run: Finished run resource.
        """

        t = 0

        poll_stop_statuses = [
            RunStatus.RS_ABORTED,
            RunStatus.RS_AWS_ERROR,
            RunStatus.RS_DB_ERROR,
            RunStatus.RS_INSUFFICIENT_RESOURCES,
            RunStatus.RS_NO_USERS,
            RunStatus.RS_SERVER_ERROR,
            RunStatus.RS_TIMEOUT_EXCEEDED,
            RunStatus.RS_DONE,
        ]

        while t < timeout:
            self.read()

            if self.params.status in poll_stop_statuses:
                break

            sleep(interval)
            t += interval

        if t >= timeout:
            raise TimeoutError("Run poll timeout exceeded")

        return self

    def results(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[Result], PaginationParams, dict[any, any]]:
        """Get all results of the run.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            APIException: If API call fails.
            ValueError: Run.params.run_id must be a valid int

        Returns:
            list[Result]: List of all results of the run.
            PaginationParams: Pagination parameters of request.
            dict[any, any]: Filters applied to in request.
        """

        if self.params.run_id is None:
            raise ValueError("Run.params.run_id must be a valid int")

        resp = ResultAPI.read_all(self.params.run_id, query_params=query_params)

        return (
            convert_params_list(Result, resp.results),
            resp.pagination,
            resp.filter,
        )


class RunAPI:
    """RunAPI defines Loadero API operations for run resources."""

    @staticmethod
    def create(params: RunParams) -> RunParams:
        """Creates and launches a new test run.

        Args:
            params (RunParams): Describes the run resource to be created. Only
                the RunParams.test_id field is required.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource.
            APIException: If API call fails.

        Returns:
            RunParams: Created run resource.
        """

        RunAPI.__validate_identifiers(params, False, False)

        return params.from_dict(
            APIClient().post(RunAPI.route(params.test_id), None)
        )

    @staticmethod
    def read(params: RunParams) -> RunParams:
        """Read an existing run resource.

        Args:
            params (RunParams): Describes the run resource to read.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            RunParams: Read run resource.
        """

        RunAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(RunAPI.route(run_id=params.run_id))
        )

    @staticmethod
    def read_all(
        test_id: int or None = None,
        query_params: QueryParams or None = None,
    ) -> PagedResponse:
        """Read all run resources.

        Args:
            test_id (int, optional): Parent test resource id. Defaults to None.
                If omitted all runs in project will be read.
            query_params (QueryParams, optional): Describes query parameters.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource.
            APIException: If API call fails.

        Returns:
            PagedResponse: Paged response of run resources.
        """

        qp = None
        if query_params is not None:
            qp = query_params.parse()

        return PagedResponse(RunParams).from_dict(
            APIClient().get(RunAPI.route(test_id=test_id), query_params=qp)
        )

    @staticmethod
    def stop(params: RunParams) -> None:
        """Stop an active test run.

        Args:
            params (RunParams): Describes the run resource to stop.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        RunAPI.__validate_identifiers(params, True, False)

        APIClient().post(
            RunAPI.route(test_id=params.test_id, run_id=params.run_id)
            + "stop/",
            None,
        )

    @staticmethod
    def route(test_id: int or None = None, run_id: int or None = None) -> str:
        """Build run resource url route.

        Args:
            test_id (int, optional): Test resource id. Defaults to None. If
                omitted route will point to all runs in project.
            run_id (int, optional): Run resource id. Defaults to None. If
                omitted the route will point to all run resources that belong
                to parent resource, either test or project.

        Returns:
            str: Route to run resource/s.
        """

        r = APIClient().project_route

        if test_id is not None:
            r += f"tests/{test_id}/"

        r += "runs/"

        if run_id is not None:
            r += f"{run_id}/"

        return r

    @staticmethod
    def __validate_identifiers(
        params: RunParams, single: bool = True, project_run: bool = True
    ) -> None:
        """Validate run resource identifiers.

        Args:
            params (RunParams): Run params.
            single (bool, optional): Indicates if the resource identifiers
                should be validated as pointing to a single resource.
                Defaults to True.
            project_run (bool, optional): Indicates if the resource identifiers
                should include a valid test id. Defaults to True.

        Raises:
            ValueError: RunParams.run_id must be a valid int.
            ValueError: RunParams.test_id must be a valid int.
        """

        if single and params.run_id is None:
            raise ValueError("RunParams.run_id must be a valid int")

        if not project_run and params.test_id is None:
            raise ValueError("RunParams.test_id must be a valid int")
