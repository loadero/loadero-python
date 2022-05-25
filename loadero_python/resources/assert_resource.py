# coding: utf-8

"""
Loadero assert resource.
Assert resource is seperated into two parts - AssertParams class that describes
assert attributes and Assert class that in combination with AssertParams and
APIClient allows to perform CRUD operations on Loadero assert resources.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .resource import LoaderoResource, to_json, from_json, to_string
from .metric_path import MetricPath
from .classificator import Operator


class AssertParams(LoaderoResource):
    """
    AssertParams represents Loadero assert resource attributes.
    AssertParams has a builder pattern for assert resources read and write
    attributes.
    """

    # Describes python object attribute name mapping to Loadero resources
    # JSON field names.
    __attribute_map = {
        "assert_id": "id",
        "test_id": "test_id",
        "_created": "created",
        "_updated": "updated",
        "expected": "expected",
        "operator": "operator",
        "path": "path",
    }

    # Describes Loadero resources JSON field names that are required for CRUD
    # operations.
    __body_attributes = ["expected", "operator", "path"]

    # Describes a mapping from Loadero resources JSON field names to custom
    # deserialization functions.
    __custom_deserializers = {
        "created": parser.parse,
        "updated": parser.parse,
        "operator": Operator.from_json,
        "path": MetricPath.from_json,
    }

    assert_id = None
    test_id = None

    path = None
    operator = None
    expected = None

    _created = None
    _updated = None

    def __init__(
        self,
        assert_id: int or None = None,
        test_id: int or None = None,
        path: MetricPath or None = None,
        operator: Operator or None = None,
        expected: str or None = None,
    ) -> None:
        self.assert_id = assert_id
        self.test_id = test_id
        self.path = path
        self.operator = operator
        self.expected = expected

    def __str__(self) -> str:
        return to_string(self.__dict__, self.__attribute_map)

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    def with_id(self, assert_id: int) -> AssertParams:
        self.assert_id = assert_id

        return self

    def in_test(self, test_id: int) -> AssertParams:
        self.test_id = test_id

        return self

    def with_path(self, path: MetricPath) -> AssertParams:
        self.path = path

        return self

    def with_operator(self, operator: Operator) -> AssertParams:
        self.operator = operator

        return self

    def with_expected(self, expected: str) -> AssertParams:
        self.expected = expected

        return self

    def to_json(
        self, body_attributes: list[str] or None = None
    ) -> dict[str, any]:
        """Serializes assert resource to JSON.

        Args:
            body_attributes (list[str] or None, optional): String list of JSON
                field names that will be serialized. Defaults to None, then
                the default body attributes for assert resource are used.

        Returns:
            dict[str, any]: JSON dictionary.
        """
        if body_attributes is None:
            body_attributes = self.__body_attributes

        return to_json(self.__dict__, self.__attribute_map, body_attributes)

    def from_json(self, json_value: dict[str, any]) -> AssertParams:
        """Serializes assert resource from JSON.

        Args:
            json_value (dict[str, any]): JSON dictionary.

        Returns:
            AssertParams: Serialized assert resource.
        """

        from_json(
            self.__dict__,
            json_value,
            self.__attribute_map,
            self.__custom_deserializers,
        )

        return self


class Assert:
    """
    Assert class allows to perform CRUD operations on Loadero assert resources.
    APIClient must be previously initialized with a valid Loadero access token.
    The target Loadero assert resource is determined by AssertParams.
    """

    params = None

    def __init__(
        self,
        assert_id: int or None = None,
        test_id: int or None = None,
        params: AssertParams or None = None,
    ) -> None:
        if params is not None:
            self.params = params
        else:
            self.params = AssertParams()

        if assert_id is not None:
            self.params.assert_id = assert_id

        if test_id is not None:
            self.params.test_id = test_id

    def create(self) -> Assert:
        """Creates new assert with given data.

        Returns:
            Assert: Created assert resource.
        """

        AssertAPI.create(self.params)

        return self

    def read(self) -> Assert:
        """Reads information about an existing assert.

        Returns:
            Assert: Read assert resource.
        """

        AssertAPI.read(self.params)

        return self

    def update(self) -> Assert:
        """Updates assert with given parameters.

        Returns:
            Assert: Updated assert resource.
        """

        AssertAPI.update(self.params)

        return self

    def delete(self) -> None:
        """Deletes and existing assert."""

        AssertAPI.delete(self.params)

    def duplicate(self) -> Assert:
        """Duplicates and existing assert.

        Returns:
            Assert: Duplicate instance of assert.
        """

        dp = AssertParams(
            assert_id=self.params.assert_id,
            test_id=self.params.test_id,
        )

        dupl = Assert(params=AssertAPI.duplicate(dp))

        return dupl


class AssertAPI:
    """AssertAPI defines Loadero API operations for assert resources."""

    @staticmethod
    def create(params: AssertParams) -> AssertParams:
        """Create a new assert resource.

        Args:
            params (AssertParams): Describes the assert resource to be created.

        Raises:
            Exception: AssertParams.test_id was not defined.

        Returns:
            AssertParams: Created assert resource.
        """

        if params.test_id is None:
            raise Exception("AssertParams.test_id must be a valid int")

        return params.from_json(
            APIClient().post(AssertAPI.route(params.test_id), params.to_json())
        )

    @staticmethod
    def read(params: AssertParams) -> AssertParams:
        """Read an existing assert resource.

        Args:
            params (AssertParams): Describes the assert resource to read.

        Raises:
            Exception: AssertParams.test_id was not defined.
            Exception: AssertParams.assert_id was not defined.

        Returns:
            AssertParams: Read assert resource.
        """

        if params.test_id is None:
            raise Exception("AssertParams.test_id must be a valid int")

        if params.assert_id is None:
            raise Exception("AssertParams.assert_id must be a valid int")

        return params.from_json(
            APIClient().get(AssertAPI.route(params.test_id, params.assert_id))
        )

    @staticmethod
    def update(params: AssertParams) -> AssertParams:
        """Update an existing assert resource.

        Args:
            params (AssertParams): Describes the assert resource to update.

        Raises:
            Exception: AssertParams.test_id was not defined.
            Exception: AssertParams.assert_id was not defined.

        Returns:
            AssertParams: Updated assert resource.
        """

        if params.test_id is None:
            raise Exception("AssertParams.test_id must be a valid int")

        if params.assert_id is None:
            raise Exception("AssertParams.assert_id must be a valid int")

        return params.from_json(
            APIClient().put(
                AssertAPI.route(params.test_id, params.assert_id),
                params.to_json(),
            )
        )

    @staticmethod
    def delete(params: AssertParams) -> None:
        """Delete an existing assert resource.

        Args:
            params (AssertParams): Describes the assert resource to delete.

        Raises:
            Exception: AssertParams.test_id was not defined.
            Exception: AssertParams.assert_id was not defined.
        """

        if params.test_id is None:
            raise Exception("AssertParams.test_id must be a valid int")

        if params.assert_id is None:
            raise Exception("AssertParams.assert_id must be a valid int")

        APIClient().delete(AssertAPI.route(params.test_id, params.assert_id))

    @staticmethod
    def duplicate(params: AssertParams) -> AssertParams:
        """Duplicate an existing assert resource.

        Args:
            params (AssertParams): Describe the assert resource to duplicate and
            the name of duplicate assert resource.

        Raises:
            Exception: AssertParams.test_id was not defined.
            Exception: AssertParams.assert_id was not defined.

        Returns:
            AssertParams: Duplicate assert resource.
        """

        if params.test_id is None:
            raise Exception("AssertParams.test_id must be a valid int")

        if params.assert_id is None:
            raise Exception("AssertParams.assert_id must be a valid int")

        dupl = AssertParams()

        return dupl.from_json(
            APIClient().post(
                AssertAPI.route(params.test_id, params.assert_id) + "copy/",
                None,
            )
        )

    @staticmethod
    def read_all(test_id: int) -> list[AssertParams]:
        """Read all assert resources.

        Args:
            test_id (int): Parent test resource id.

        Returns:
            list[AssertParams]: List of all assert resources in test.
        """
        resp = APIClient().get(AssertAPI.route(test_id))

        if "results" not in resp or resp["results"] is None:
            return []

        resources = []
        for r in resp["results"]:
            resource = AssertParams()
            resources.append(resource.from_json(r))

        return resources

    @staticmethod
    def route(test_id: int, assert_id: int or None = None) -> str:
        """Build assert resource url route.

        Args:
            test_id (int): Test resource id.
            assert_id (int, optional): Assert resource id. Defaults to None. If
                omitted the route will point to all assert resources.

        Returns:
            str: Route to assert resource/s.
        """
        r = APIClient().project_url + f"tests/{test_id}/asserts/"

        if assert_id is not None:
            r += f"{assert_id}/"

        return r
