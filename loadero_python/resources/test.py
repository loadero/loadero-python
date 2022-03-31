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
from .resource import LoaderoResource, to_json, from_json, to_string


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
        "__project_id": "project_id",
        "name": "name",
        "script_file_id": "script_file_id",
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
        "_deleted": "deleted",
    }

    # Describes a mapping from Loadero resources JSON field names to custom
    # deserialization functions.
    __custom_deserializers = {
        "script": Script.from_json,
        "created": parser.parse,
        "updated": parser.parse,
    }

    # Describes Loadero resources JSON field names that are required for CRUD
    # operations.
    __body_attributes = [
        "name",
        "start_interval",
        "participant_timeout",
        "mode",
        "increment_strategy",
        "mos_test",
        "script",
    ]

    test_id = None

    name = None
    start_interval = None
    participant_timeout = None
    mode = None  # classificator
    increment_strategy = None  # classificator
    script = None
    mos_test = None

    _created = None
    _updated = None
    _script_file_id = None
    _project_id = None
    _group_count = None
    _participant_count = None
    _deleted = None

    def __init__(
        self,
        test_id: int or None = None,
        name: str or None = None,
        start_interval: int or None = None,
        participant_timeout: int or None = None,
        mode: str or None = None,  # classificator
        increment_strategy: str or None = None,  # classificator
        mos_test: bool or None = None,
        script: Script or None = None,
        project_id: int or None = None,
    ) -> None:
        self.test_id = test_id
        self._project_id_path = project_id
        self.name = name
        self.script = script
        self.start_interval = start_interval
        self.name = name
        self.participant_timeout = participant_timeout
        self.mode = mode
        self.increment_strategy = increment_strategy
        self.mos_test = mos_test

    def __str__(self) -> str:
        return to_string(self.__dict__, self.__attribute_map)

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    @property
    def script_file_id(self) -> int:
        return self._script_file_id

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
    def project_id(self) -> bool:
        return self._project_id

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

    # TODO: change to classificator.
    def with_mode(self, m: str) -> TestParams:
        self.mode = m

        return self

    # TODO: change to classificator.
    def with_increment_strategy(self, inc: str) -> TestParams:
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
            body_attributes (list[str]orNone, optional): String list of JSON
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

    def duplicate(self) -> Test:
        """Duplicates and existing test.


        Returns:
            Test: Duplicate test resource.
        """
        t = Test(params=TestAPI.duplicate(self.params))

        return t


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

        return params.from_json(
            APIClient().post(
                f"projects/{APIClient().project_id}/tests/",
                params.to_json(),
            )
        )

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

        return params.from_json(
            APIClient().get(
                f"projects/{APIClient().project_id}/tests/{params.test_id}/"
            )
        )

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

        return params.from_json(
            APIClient().put(
                f"projects/{APIClient().project_id}/tests/{params.test_id}/",
                params.to_json(),
            )
        )

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

        APIClient().delete(
            f"projects/{APIClient().project_id}/tests/{params.test_id}/",
        )

        params.__dict__["__deleted"] = True

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

        return dupl.from_json(
            APIClient().post(
                f"projects/{APIClient().project_id}"
                f"/tests/{params.test_id}/copy/",
                params.to_json(["name"]),
            )
        )

    @staticmethod
    def read_all() -> list[TestParams]:
        # TODO: implement.
        pass
