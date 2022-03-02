# coding: utf-8

"""
Loadero test resource.
Test resource is seperated into two parts - TestParams class that describes test
attributes and Test class that in combination with TestParams and APIClient
allows to perform CRUD operations on Loadero test resources.
"""

from __future__ import annotations
from ..api_client import APIClient
from .script import Script


class TestParams:
    """
    TestParams represents Loadero test parameters.
    TestParams has a builder method pattern for test resources read and write
    attributes.
    """

    # Describes python object attribute name mapping to Loadero resources
    # JSON field names.
    attribute_map = {
        "test_id": "id",
        "_project_id_path": "project_id",
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

    body_attributes = [
        "name",
        "start_interval",
        "participant_timeout",
        "mode",
        "increment_strategy",
        "mos_test",
        "script",
    ]

    # id
    test_id = None

    name = None
    start_interval = None
    participant_timeout = None
    mode = None  # classificator
    increment_strategy = None  # classificator
    script = None
    mos_test = None

    # route path
    _project_id_path = None

    # readonly attributes
    _created = None  # datetime
    _updated = None  # datetime
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

    # read only attribute getters

    @property
    def created(self):  # date time
        return self._created

    @property
    def updated(self):  # date time
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
        return self._project_id_path

    # parameter builder

    def with_id(self, tid) -> TestParams:
        self.test_id = tid

        return self

    def in_project(self, pid: int) -> TestParams:
        self._project_id_path = pid

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

    # to dict
    # from dict


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

    def create(self, api_client: APIClient) -> Test:
        """Creates new test with given data.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Test: created test resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def read(self, api_client: APIClient) -> Test:
        """Reads information about an existing test.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Test: retrived test resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def update(self, api_client: APIClient) -> Test:
        """Updates test with given parameters.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Test: updated test resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def delete(self, api_client: APIClient) -> Test:
        """Deletes and existing test.

        Args:
            api_client (APIClient): initalized instance of API client
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def duplicate(self, api_client: APIClient) -> Test:
        """Duplicates and existing test.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Test: duplicate instance of test
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self
