# coding: utf-8

"""
Loadero test resource.
Test resource is seperated into two parts - TestParams class that describes test
attributes and Test class that in combination with TestParams and APIClient
allows to perform CRUD operations on Loadero test resources.
"""

from __future__ import annotations
from copy import deepcopy
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .script import Script
from .resource import (
    LoaderoResource,
    to_json,
    from_json,
    to_string,
    convert_params_list,
)
from .classificator import TestMode, IncrementStrategy
from .group import Group, GroupAPI
from .participant import Participant, ParticipantAPI
from .assert_resource import Assert, AssertAPI


class TestParams(LoaderoResource):
    """
    TestParams represents Loadero test parameters.
    TestParams has a builder method pattern for test resources read and write
    attributes.
    """

    # Describes python object attribute name mapping to Loadero resources
    # JSON field names.
    __attribute_map = {
        "test_id": "id",
        "name": "name",
        "start_interval": "start_interval",
        "participant_timeout": "participant_timeout",
        "mode": "mode",
        "increment_strategy": "increment_strategy",
        "mos_test": "mos_test",
        "script": "script",
        "_created": "created",
        "_updated": "updated",
        "_group_count": "group_count",
        "_participant_count": "participant_count",
        "_script_file_id": "script_file_id",
        "_deleted": "deleted",
    }

    # Describes a mapping from Loadero resources JSON field names to custom
    # deserialization functions.
    __custom_deserializers = {
        "created": parser.parse,
        "updated": parser.parse,
        "mode": TestMode.from_json,
        "increment_strategy": IncrementStrategy.from_json,
    }

    # Describes Loadero resources JSON field names that are required for CRUD
    # operations.
    __body_attributes = [
        "name",
        "start_interval",
        "participant_timeout",
        "mode",
        "increment_strategy",
        "mos_test",  # optional
        "script",  # optional
    ]

    test_id = None

    name = None
    start_interval = None
    participant_timeout = None
    mode = None
    increment_strategy = None
    script = None
    mos_test = None

    _created = None
    _updated = None
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
        self.test_id = test_id
        self.name = name
        self.start_interval = start_interval
        self.participant_timeout = participant_timeout
        self.mode = mode
        self.increment_strategy = increment_strategy
        self.mos_test = mos_test
        self.script = script

    def __str__(self) -> str:
        return to_string(self.__dict__, self.__attribute_map)

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
        self.script = sc

        return self

    # serializers

    def to_json(
        self, body_attributes: list[str] or None = None
    ) -> dict[str, any]:
        """Serializes test resource to JSON.

        Args:
            body_attributes (list[str] or None, optional): String list of JSON
                field names that will be serialized. Defaults to None, then
                the default body attributed for test resource are used.

        Returns:
            dict[str, any]: JSON dictionary.
        """

        if body_attributes is None:
            body_attributes = self.__body_attributes

        return to_json(self.__dict__, self.__attribute_map, body_attributes)

    def from_json(self, json_value: dict[str, any]) -> TestParams:
        """Serializes test resource from JSON.

        Args:
            json_value (dict[str, any]): JSON dictionary.

        Returns:
            TestParams: Serialized test resource.
        """

        from_json(
            self.__dict__,
            json_value,
            self.__attribute_map,
            self.__custom_deserializers,
        )

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

        dp = TestParams(test_id=self.params.test_id, name=name)

        t = Test(params=TestAPI.duplicate(dp))

        return t

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

        scp = deepcopy(params.script)

        ret = params.from_json(
            APIClient().post(TestAPI().route(), params.to_json())
        )

        ret.script = scp

        return ret

    @staticmethod
    def read(params: TestParams) -> TestParams:
        """Read an existing test resource.

        Args:
            params (TestParams): Describes the test resource to read.

        Raises:
            Exception: TestParams.test_id was not defined.

        Returns:
            TestParams: Read test resource.
        """

        if params.test_id is None:
            raise Exception("TestParams.test_id must be a valid int")

        ret = params.from_json(APIClient().get(TestAPI().route(params.test_id)))

        # pylint: disable=protected-access
        ret.script = Script(script_id=ret._script_file_id)

        ret.script.read()

        return ret

    @staticmethod
    def update(params: TestParams) -> TestParams:
        """Update an existing test resource.

        Args:
            params (TestParams): Describe the test resource to update.

        Raises:
            Exception: TestParams.test_id was not defined.

        Returns:
            TestParams: Updated test resource.
        """

        if params.test_id is None:
            raise Exception("TestParams.test_id must be a valid int")

        scp = deepcopy(params.script)

        ret = params.from_json(
            APIClient().put(TestAPI().route(params.test_id), params.to_json())
        )

        ret.script = scp

        return ret

    @staticmethod
    def delete(params: TestParams) -> TestParams:
        """Delete an existing test resource.

        Args:
            params (TestParams): Describes the test resource to delete.

        Raises:
            Exception: TestParams.test_id was not defined.

        Returns:
            TestParams: Deleted test resource.
        """

        if params.test_id is None:
            raise Exception("TestParams.test_id must be a valid int")

        APIClient().delete(TestAPI().route(params.test_id))

        params.__dict__["_deleted"] = True

        return params

    @staticmethod
    def duplicate(params: TestParams) -> TestParams:
        """Created a duplicate test resource from an existing test resource.

        Args:
            params (TestParams): Describe the test resources to duplicate and
                the name of the duplicate test resource.

        Raises:
            Exception: TestParams.test_id was not defined.

        Returns:
            TestParams: Duplicated test resource.
        """

        if params.test_id is None:
            raise Exception("TestParams.test_id must be a valid int")

        dupl = TestParams()

        dupl = dupl.from_json(
            APIClient().post(
                TestAPI().route(params.test_id) + "copy/",
                params.to_json(["name"]),
            )
        )

        # pylint: disable=protected-access
        dupl.script = Script(script_id=dupl._script_file_id)

        dupl.script.read()

        return dupl

    @staticmethod
    def read_all() -> list[TestParams]:
        """Read all test resources.

        Returns:
            list[TestParams]: List of all test resources in project.
        """

        resp = APIClient().get(TestAPI.route())

        if "results" not in resp or resp["results"] is None:
            return []

        resources = []
        for r in resp["results"]:
            resource = TestParams()
            resources.append(resource.from_json(r))

        return resources

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
