"""Loadero test resource.

Test resource is seperated into three parts
    - TestParams class describes test attributes
    - TestAPI class groups API operation with test resources.
    - Test class combines TestParams and TestAPI.

Single Test object coresponds to single test in Loadero.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .resource import (
    FilterKey,
    QueryParams,
    Serializable,
    LoaderoResourceParams,
    LoaderoResource,
    DuplicateResourceBodyParams,
    convert_params_list,
)
from .file import FileParams, FileAPI
from .classificator import TestMode, IncrementStrategy
from .group import Group, GroupAPI
from .participant import Participant, ParticipantAPI
from .assert_resource import Assert, AssertAPI
from .run import Run, RunAPI
from .pagination import PagedResponse, PaginationParams


class TestFilterKey(FilterKey):
    """TestFilterKey is an enum of all filter keys for test read all API
    operation."""

    NAME = "filter_name"
    TEST_MODE = "filter_test_mode"
    INCREMENT_STRATEGY = "filter_increment_strategy"
    START_INTERVAL_FROM = "filter_start_interval_from"
    START_INTERVAL_TO = "filter_start_interval_to"
    PARTICIPANT_TIMEOUT_FROM = "filter_participant_timeout_from"
    PARTICIPANT_TIMEOUT_TO = "filter_participant_timeout_to"


class Script(Serializable):
    """Script describes a single Loadero test script."""

    def __init__(
        self,
        file_id: int or None = None,
        content: str or None = None,
        filepath: str or None = None,
    ) -> None:
        """Creates a new script or loads an existing script.

        Args:
            file_id (int, optional): File id of the script Loadero resource.
                Defaults to None.
            content (str, optional): Script file contents. Defaults to None.
            filepath (str, optional): File path to a script. Defaults to
                None.

        If more than one script content source is specified, then the loading
        priorities are: file_id - first, content - second, filepath - third.
        """

        self.file_id = file_id
        self.content = content

        if filepath is not None:
            self.from_file(filepath)

    def __str__(self) -> str:
        if self.content is None:
            return "<no script>"

        return self.content

    def from_file(self, filepath: str) -> Script:
        """Loads Loadero script from file.

        Args:
            filepath (str): file path to script file

        Returns:
            Script: script loaded from file
        """

        with open(filepath, "r", encoding="utf-8") as f:
            self.content = f.read()

        return self

    def to_dict(self) -> str:
        """Returns script content as a string. Used for serialization.

        Returns:
            str: Script content.
        """

        return self.content

    def to_dict_full(self) -> str:
        """Returns script content as a string. Used for serialization.

        Returns:
            str: Script content.
        """

        return self.to_dict()

    def from_dict(self, json_dict: dict[str, any]) -> Script:
        """Loads script from a dictionary. Never used. Required for
            serialization.

        Args:
            json_dict (dict[str, any]): JSON parsed as dictionary.

        Returns:
            Script: Script loaded from dictionary.
        """

        return self

    def read(self) -> Script:
        """Reads script from Loadero API.

        Raises:
            ValueError: If file_id is not specified.
            APIException: If API call fails.

        Returns:
            Script: Script loaded from Loadero API.
        """

        self.content = FileAPI().read(FileParams(self.file_id)).content
        return self


class TestParams(LoaderoResourceParams):
    """
    TestParams represents Loadero test parameters.
    TestParams has a builder method pattern for test resources read and write
    attributes.
    """

    def __init__(
        self,
        test_id: int or None = None,
        name: str or None = None,
        start_interval: int or None = None,
        participant_timeout: int or None = None,
        mode: TestMode or None = None,
        increment_strategy: IncrementStrategy or None = None,
        mos_test: bool or None = None,
        script: Script or None = None,
    ) -> None:
        super().__init__(
            attribute_map={
                "id": "test_id",
                "name": "name",
                "start_interval": "start_interval",
                "participant_timeout": "participant_timeout",
                "mode": "mode",
                "increment_strategy": "increment_strategy",
                "mos_test": "mos_test",
                "script": "_script",
                "created": "_created",
                "updated": "_updated",
                "group_count": "_group_count",
                "participant_count": "_participant_count",
                "script_file_id": "_script_file_id",
                "deleted": "_deleted",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "mode": TestMode.from_dict,
                "increment_strategy": IncrementStrategy.from_dict,
            },
            body_attributes=[
                "name",
                "start_interval",
                "participant_timeout",
                "mode",
                "increment_strategy",
                "mos_test",
                "script",
            ],
            required_body_attributes=[
                "name",
                "start_interval",
                "participant_timeout",
                "mode",
                "increment_strategy",
            ],
        )

        self.test_id = test_id
        self.name = name
        self.start_interval = start_interval
        self.participant_timeout = participant_timeout
        self.mode = mode
        self.increment_strategy = increment_strategy
        self.mos_test = mos_test
        self._script = script

        self._created = None
        self._updated = None
        self._script_file_id = None
        self._group_count = None
        self._participant_count = None
        self._deleted = None

    @property
    def created(self) -> datetime:
        """Time when test was created.

        Returns:
            datetime: Time when test was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when test was last updated.

        Returns:
            datetime: Time when test was last updated.
        """

        return self._updated

    @property
    def group_count(self) -> int:
        """Number of groups in test.

        Returns:
            int: Number of groups in test.
        """

        return self._group_count

    @property
    def participant_count(self) -> int:
        """Number of participants in test.

        Returns:
            int: Number of participants in test.
        """

        return self._participant_count

    @property
    def deleted(self) -> bool:
        """Is test deleted.

        Returns:
            bool: Is test deleted.
        """

        return self._deleted

    @property
    def script(self) -> Script:
        """Retrive the test script.

        Returns:
            Script: Test script.
        """

        if self._script is None:
            self._script = Script()

        self._script.file_id = self._script_file_id

        return self._script

    @script.setter
    def script(self, script: Script):
        """Set the test script.

        Args:
            script (Script): Test script.
        """

        self._script = script

    # parameter builder

    def with_id(self, test_id: int) -> TestParams:
        """Set test id.

        Args:
            test_id (int): Test id.

        Returns:
            TestParams: TestParams with test id set.
        """

        self.test_id = test_id
        return self

    def with_name(self, name: str) -> TestParams:
        """Set test name.

        Args:
            name (str): Test name.

        Returns:
            TestParams: TestParams with test name set.
        """

        self.name = name
        return self

    def with_start_interval(self, start_interval: int) -> TestParams:
        """Set test start interval.

        Args:
            start_interval (int): Test start interval.

        Returns:
            TestParams: TestParams with test start interval set.
        """

        self.start_interval = start_interval
        return self

    def with_participant_timeout(self, participant_timeout: int) -> TestParams:
        """Set test participant timeout.

        Args:
            participant_timeout (int): Test participant timeout.

        Returns:
            TestParams: TestParams with test participant timeout set.
        """

        self.participant_timeout = participant_timeout
        return self

    def with_mode(self, test_mode: TestMode) -> TestParams:
        """Set test mode.

        Args:
            test_mode (TestMode): Test mode.

        Returns:
            TestParams: TestParams with test mode set.
        """

        self.mode = test_mode
        return self

    def with_increment_strategy(
        self, increment_strategy: IncrementStrategy
    ) -> TestParams:
        """Set test increment strategy.

        Args:
            increment_strategy (IncrementStrategy): Test increment strategy.

        Returns:
            TestParams: TestParams with test increment strategy set.
        """

        self.increment_strategy = increment_strategy
        return self

    def with_mos_test(self, mos_test: bool) -> TestParams:
        """Set test MOS test.

        Args:
            mos_test (bool): Test MOS test.

        Returns:
            TestParams: TestParams with test MOS test set.
        """

        self.mos_test = mos_test
        return self

    def with_script(self, script: Script) -> TestParams:
        """Set test script.

        Args:
            script (Script): The test script.

        Returns:
            TestParams: TestParams with test script set.
        """

        self._script = script
        return self


class Test(LoaderoResource):
    """Test class allows to perform CRUD operations on Loadero test resources.
    APIClient must be previously initialized with a valid Loadero access token.
    The target Loadero test resource is determined by TestParams.
    """

    def __init__(
        self, test_id: int or None = None, params: TestParams or None = None
    ) -> None:
        self.params = params or TestParams()

        if test_id is not None:
            self.params.test_id = test_id

        super().__init__(self.params)

    def create(self) -> Test:
        """Creates new test with given data.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            Test: Created test resource.
        """

        TestAPI.create(self.params)
        return self

    def read(self) -> Test:
        """Reads information about an existing test.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Test: Read test resource.
        """

        TestAPI.read(self.params).script.read()
        return self

    def update(self) -> Test:
        """Updates test with given parameters.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            Test: Updated test resource.
        """

        TestAPI.update(self.params)
        return self

    def delete(self) -> Test:
        """Deletes and existing test.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Test: Deleted test resource.
        """

        TestAPI.delete(self.params)
        return self

    def duplicate(self, name: str) -> Test:
        """Duplicates and existing test.

        Args:
            name (str): New name for the duplicate test.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Test: Duplicate test resource.
        """

        dupl = Test(params=TestAPI.duplicate(self.params, name))
        dupl.params.script.read()
        return dupl

    def launch(self) -> Run:
        """Launches test.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Run: Launched test run.
        """

        r = Run(test_id=self.params.test_id)
        r.create()
        return r

    def groups(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[Group], PaginationParams, dict[any, any]]:
        """Read all groups in test.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            ValueError: Test.params.test_id must be a valid int.
            APIException: If API call fails.

        Returns:
            list[Group]: List of groups in test.
            PaginationParams: Pagination parameters of request.
            dict[any, any]: Filters applied to in request.
        """

        if self.params.test_id is None:
            raise ValueError("Test.params.test_id must be a valid int")

        resp = GroupAPI.read_all(self.params.test_id, query_params=query_params)

        return (
            convert_params_list(Group, resp.results),
            resp.pagination,
            resp.filter,
        )

    def participants(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[Participant], PaginationParams, dict[any, any]]:
        """Read all participants in test.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            ValueError: Test.params.test_id must be a valid int.
            APIException: If API call fails.

        Returns:
            list[Participant]: List of participants in test.
            PaginationParams: Pagination parameters of request.
            dict[any, any]: Filters applied to in request.
        """

        if self.params.test_id is None:
            raise ValueError("Test.params.test_id must be a valid int")

        resp = ParticipantAPI.read_all(
            self.params.test_id, query_params=query_params
        )

        return (
            convert_params_list(Participant, resp.results),
            resp.pagination,
            resp.filter,
        )

    def asserts(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[Assert], PaginationParams, dict[any, any]]:
        """Read all asserts in test.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            ValueError: Test.params.test_id must be a valid int.
            APIException: If API call fails.

        Returns:
            list[Assert]: List of asserts in test.
            PaginationParams: Pagination parameters of request.
            dict[any, any]: Filters applied to in request.
        """

        if self.params.test_id is None:
            raise ValueError("Test.params.test_id must be a valid int")

        resp = AssertAPI.read_all(
            self.params.test_id, query_params=query_params
        )

        return (
            convert_params_list(Assert, resp.results),
            resp.pagination,
            resp.filter,
        )

    def runs(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[Run], PaginationParams, dict[any, any]]:
        """Read all runs in test.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            ValueError: Test.params.test_id must be a valid int.
            APIException: If API call fails.

        Returns:
            list[Assert]: List of asserts in test.
            PaginationParams: Pagination parameters of request.
            dict[any, any]: Filters applied to in request.
        """

        if self.params.test_id is None:
            raise ValueError("Test.params.test_id must be a valid int")

        resp = RunAPI.read_all(
            test_id=self.params.test_id, query_params=query_params
        )

        return (
            convert_params_list(Run, resp.results),
            resp.pagination,
            resp.filter,
        )


class TestAPI:
    """TestAPI defines Loadero API operations for test resources."""

    @staticmethod
    def create(params: TestParams) -> TestParams:
        """Create a new test resource.

        Args:
            params (TestParams): Describes the test resource to be created.
            APIException: If API call fails.

        Returns:
            TestParams: Created participant resource.
        """

        return params.from_dict(
            APIClient().post(TestAPI().route(), params.to_dict())
        )

    @staticmethod
    def read(params: TestParams) -> TestParams:
        """Read an existing test resource.

        Args:
            params (TestParams): Describes the test resource to read.

        Raises:
            Exception: TestParams.test_id was not defined.
            APIException: If API call fails.

        Returns:
            TestParams: Read test resource.
        """

        TestAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(TestAPI().route(params.test_id))
        )

    @staticmethod
    def update(params: TestParams) -> TestParams:
        """Update an existing test resource.

        Args:
            params (TestParams): Describe the test resource to update.

        Raises:
            Exception: TestParams.test_id was not defined.
            APIException: If API call fails.

        Returns:
            TestParams: Updated test resource.
        """

        TestAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().put(TestAPI().route(params.test_id), params.to_dict())
        )

    @staticmethod
    def delete(params: TestParams) -> TestParams:
        """Delete an existing test resource.

        Args:
            params (TestParams): Describes the test resource to delete.

        Raises:
            Exception: TestParams.test_id was not defined.
            APIException: If API call fails.


        Returns:
            TestParams: Deleted test resource.
        """

        TestAPI.__validate_identifiers(params)

        APIClient().delete(TestAPI().route(params.test_id))

        params.__dict__["_deleted"] = True

        return params

    @staticmethod
    def duplicate(params: TestParams, name: str) -> TestParams:
        """Created a duplicate test resource from an existing test resource.

        Args:
            params (TestParams): Describe the test resources to duplicate and
                the name of the duplicate test resource.

        Raises:
            Exception: TestParams.test_id was not defined.
            APIException: If API call fails.

        Returns:
            TestParams: Duplicated test resource.
        """

        TestAPI.__validate_identifiers(params)

        return TestParams().from_dict(
            APIClient().post(
                TestAPI().route(params.test_id) + "copy/",
                DuplicateResourceBodyParams(name=name).to_dict(),
            )
        )

    @staticmethod
    def read_all(
        query_params: QueryParams or None = None,
    ) -> PagedResponse:
        """Read all test resources.

        Raises:
            APIException: If API call fails.

        Returns:
            PagedResponse: Paged response of participant resources.
        """

        qp = None
        if query_params is not None:
            qp = query_params.parse()

        return PagedResponse(TestParams).from_dict(
            APIClient().get(TestAPI.route(), query_params=qp)
        )

    @staticmethod
    def route(test_id: int or None = None) -> str:
        """Build test resource url route.

        Args:
            test_id (int, optional): Test resource id. Defaults to None. If
                omitted the route will point to all test resources.

        Returns:
            str: Route to test resource/s.
        """
        r = APIClient().project_route + "tests/"

        if test_id is not None:
            r += f"{test_id}/"

        return r

    @staticmethod
    def __validate_identifiers(params: TestParams, single: bool = True):
        """Validate test resource identifiers.

        Args:
            params (TestParams): Test params.
            single (bool, optional): Indicates if the resource identifiers
                should be validated as pointing to a single resource.
                Defaults to True.

        Raises:
            ValueError: TestParams.test_id must be a valid int.
        """

        if single and params.test_id is None:
            raise ValueError("TestParams.test_id must be a valid int")
