# coding: utf-8

"""
Loadero test resource.
Test resource is seperated into two parts - TestParams class that describes test
attributes and Test class that in combination with TestParams and APIClient
allows to perform CRUD operations on Loadero test resources.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .script import Script
from .resource import (
    LoaderoResourceParams,
    DuplicateResourceBodyParams,
    from_dict_as_list,
    convert_params_list,
)
from .classificator import TestMode, IncrementStrategy
from .group import Group, GroupAPI
from .participant import Participant, ParticipantAPI
from .assert_resource import Assert, AssertAPI
from .run import Run


class TestParams(LoaderoResourceParams):
    """
    TestParams represents Loadero test parameters.
    TestParams has a builder method pattern for test resources read and write
    attributes.
    """

    test_id = None

    name = None
    start_interval = None
    participant_timeout = None
    mode = None
    increment_strategy = None
    mos_test = None

    _created = None
    _updated = None
    _script = None
    _script_file_id = None
    _group_count = None
    _participant_count = None
    _deleted = None

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

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    @property
    def group_count(self) -> int:
        return self._group_count

    @property
    def participant_count(self) -> int:
        return self._participant_count

    @property
    def deleted(self) -> bool:
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
        self._script = script

    # parameter builder

    def with_id(self, tid) -> TestParams:
        self.test_id = tid

        return self

    def with_name(self, name: str) -> TestParams:
        self.name = name

        return self

    def with_start_interval(self, si: int) -> TestParams:
        self.start_interval = si

        return self

    def with_participant_timeout(self, pt: int) -> TestParams:
        self.participant_timeout = pt

        return self

    def with_mode(self, m: TestMode) -> TestParams:
        self.mode = m

        return self

    def with_increment_strategy(self, inc: IncrementStrategy) -> TestParams:
        self.increment_strategy = inc

        return self

    def with_mos_test(self, mt: bool) -> TestParams:
        self.mos_test = mt

        return self

    def with_script(self, sc: Script) -> TestParams:
        self._script = sc

        return self


class Test:
    """
    Test class allows to perform CRUD operations on Loadero test resources.
    APIClient must be previously initialized with a valid Loadero access token.
    The target Loadero test resource is determined by TestParams.
    """

    params = None

    def __init__(
        self, test_id: int or None = None, params: TestParams or None = None
    ) -> None:
        if params is not None:
            self.params = params
        else:
            self.params = TestParams()

        if test_id is not None:
            self.params.test_id = test_id

    def create(self) -> Test:
        """Creates new test with given data.

        Returns:
            Test: Created test resource.
        """

        TestAPI.create(self.params)

        return self

    def read(self) -> Test:
        """Reads information about an existing test.

        Returns:
            Test: Read test resource.
        """

        TestAPI.read(self.params)

        self.params.script.read()

        return self

    def update(self) -> Test:
        """Updates test with given parameters.

        Returns:
            Test: Updated test resource.
        """

        TestAPI.update(self.params)

        return self

    def delete(self) -> Test:
        """Deletes and existing test.

        Returns:
            Test: Deleted test resource.
        """

        TestAPI.delete(self.params)

        return self

    def duplicate(self, name: str) -> Test:
        """Duplicates and existing test.

        Args:
            name (str): New name for the duplicate test.

        Returns:
            Test: Duplicate test resource.
        """

        dupl = Test(params=TestAPI.duplicate(self.params, name))
        dupl.params.script.read()

        return dupl

    def launch(self) -> Run:
        """Launches test.

        Returns:
            Run: Launched test run.
        """

        r = Run(test_id=self.params.test_id)
        r.create()

        return r

    def groups(self) -> list[Group]:
        """Read all groups in test.

        Returns:
            list[Group]: List of groups in test.
        """

        return convert_params_list(
            Group, GroupAPI.read_all(self.params.test_id)
        )

    def participants(self) -> list[Participant]:
        """Read all participants in test.

        Returns:
            list[Participant]: List of participants in test.
        """

        return convert_params_list(
            Participant,
            ParticipantAPI.read_all(self.params.test_id),
        )

    def asserts(self) -> list[Assert]:
        """Read all asserts in test.

        Returns:
            list[Assert]: List of asserts in test.
        """

        return convert_params_list(
            Assert,
            AssertAPI.read_all(self.params.test_id),
        )


class TestAPI:
    """TestAPI defines Loadero API operations for test resources."""

    @staticmethod
    def create(params: TestParams) -> TestParams:
        """Create a new test resource.

        Args:
            params (TestParams): Describes the test resource to be created.

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
    def read_all() -> list[TestParams]:
        """Read all test resources.

        Returns:
            list[TestParams]: List of all test resources in project.
        """

        resp = APIClient().get(TestAPI.route())

        if "results" not in resp or resp["results"] is None:
            return []

        return from_dict_as_list(TestParams)(resp["results"])

    @staticmethod
    def route(test_id: int or None = None) -> str:
        """Build test resource url route.

        Args:
            test_id (int, optional): Test resource id. Defaults to None. If
                omitted the route will point to all test resources.

        Returns:
            str: Route to test resource/s.
        """
        r = APIClient().project_url + "tests/"

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
