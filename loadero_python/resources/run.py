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
from ..api_client import APIClient
from .resource import (
    LoaderoResourceParams,
    convert_params_list,
    from_dict_as_list,
)
from .classificator import (
    RunStatus,
    MetricStatus,
    TestMode,
    IncrementStrategy,
)
from .result import Result, ResultAPI


class RunParams(LoaderoResourceParams):
    """
    RunParams represents Loadero run resource attributes.
    """

    run_id = None
    test_id = None

    _created = None
    _updated = None

    _status = None
    _metric_status = None
    _test_mode = None
    _increment_strategy = None
    _mos_status = None
    _processing_started = None
    _processing_finished = None
    _execution_started = None
    _execution_finished = None
    _script_file_id = None
    _test_name = None
    _start_interval = None
    _participant_timeout = None
    _launching_account_id = None
    _success_rate = None
    _total_cu_count = None
    _group_count = None
    _participant_count = None
    _mos_test = None

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

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    @property
    def status(self) -> RunStatus:
        return self._status

    @property
    def metric_status(self) -> MetricStatus:
        return self._metric_status

    @property
    def test_mode(self) -> TestMode:
        return self._test_mode

    @property
    def increment_strategy(self) -> IncrementStrategy:
        return self._increment_strategy

    @property
    def mos_status(self) -> MetricStatus:
        return self._mos_status

    @property
    def processing_started(self) -> datetime:
        return self._processing_started

    @property
    def processing_finished(self) -> datetime:
        return self._processing_finished

    @property
    def execution_started(self) -> datetime:
        return self._execution_started

    @property
    def execution_finished(self) -> datetime:
        return self._execution_finished

    @property
    def script_file_id(self) -> int:
        return self._script_file_id

    @property
    def test_name(self) -> str:
        return self._test_name

    @property
    def start_interval(self) -> int:
        return self._start_interval

    @property
    def participant_timeout(self) -> int:
        return self._participant_timeout

    @property
    def launching_account_id(self) -> int:
        return self._launching_account_id

    @property
    def success_rate(self) -> float:
        return self._success_rate

    @property
    def total_cu_count(self) -> float:
        return self._total_cu_count

    @property
    def group_count(self) -> int:
        return self._group_count

    @property
    def participant_count(self) -> int:
        return self._participant_count

    @property
    def mos_test(self) -> bool:
        return self._mos_test

    # param builder

    def with_id(self, run_id: int) -> RunParams:
        self.run_id = run_id

        return self

    def in_test(self, test_id: int) -> RunParams:
        self.test_id = test_id

        return self


class Run:
    """
    Run class allows to create, read and stop runs.
    APIClient must be previously initialized with a valid Loadero access token.
    The target Loadero run resource is determined by RunParams.
    """

    params = None

    def __init__(
        self,
        run_id: int or None = None,
        test_id: int or None = None,
        params: RunParams or None = None,
    ) -> None:
        if params is not None:
            self.params = params
        else:
            self.params = RunParams()

        if run_id is not None:
            self.params.run_id = run_id

        if test_id is not None:
            self.params.test_id = test_id

    def create(self) -> Run:
        """Creates new run with given data.

        Returns:
            Run: Created run resource.
        """

        RunAPI.create(self.params)

        return self

    def read(self) -> Run:
        """Read an existing run resource.

        Returns:
            Run: Read run resource.
        """

        RunAPI.read(self.params)

        return self

    def stop(self) -> Run:
        """Stop an active run.

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

    def results(self) -> list[Result]:
        if not isinstance(self.params.run_id, int):
            raise ValueError("Run.params.run_id must be a valid int")

        return convert_params_list(
            Result, ResultAPI.read_all(self.params.run_id)
        )


class RunAPI:
    """RunAPI defines Loadero API operations for run resources."""

    @staticmethod
    def create(params: RunParams) -> RunParams:
        """Creates and launches a new test run.

        Args:
            params (RunParams): Describes the run resource to be created. Only
                the RunParams.test_id field is required.

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

        Returns:
            RunParams: Read run resource.
        """

        RunAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(RunAPI.route(run_id=params.run_id))
        )

    @staticmethod
    def read_all(test_id: int or None = None) -> list[RunParams]:
        """Read all run resources.

        Args:
            test_id (int, optional): Parent test resource id. Defaults to None.
                If omitted all runs in project will be read.

        Returns:
            list[RunParams]: List of all runs resource params in test or
                project.
        """

        resp = APIClient().get(RunAPI.route(test_id=test_id))

        if "results" not in resp or resp["results"] is None:
            return []

        return from_dict_as_list(RunParams)(resp["results"])

    @staticmethod
    def stop(params: RunParams) -> None:
        """Stop an active test run.

        Args:
            params (RunParams): Describes the run resource to stop.
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

        r = APIClient().project_url

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
