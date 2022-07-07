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

from .assert_precondition import AssertPrecondition, AssertPreconditionAPI
from ..api_client import APIClient
from .resource import (
    LoaderoResourceParams,
    convert_params_list,
    from_dict_as_list,
)
from .metric_path import MetricPath
from .classificator import Operator


class AssertParams(LoaderoResourceParams):
    """
    AssertParams represents Loadero assert resource attributes.
    AssertParams has a builder pattern for assert resources read and write
    attributes.
    """

    def __init__(
        self,
        assert_id: int or None = None,
        test_id: int or None = None,
        path: MetricPath or None = None,
        operator: Operator or None = None,
        expected: str or None = None,
    ) -> None:
        super().__init__(
            attribute_map={
                "id": "assert_id",
                "test_id": "test_id",
                "created": "_created",
                "updated": "_updated",
                "expected": "expected",
                "operator": "operator",
                "path": "path",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "operator": Operator.from_dict,
                "path": MetricPath.from_dict,
            },
            body_attributes=["expected", "operator", "path"],
            required_body_attributes=["expected", "operator", "path"],
        )

        self.assert_id = assert_id
        self.test_id = test_id
        self.path = path
        self.operator = operator
        self.expected = expected

        self._created = None
        self._updated = None

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

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            Assert: Created assert resource.
        """

        AssertAPI.create(self.params)

        return self

    def read(self) -> Assert:
        """Reads information about an existing assert.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Assert: Read assert resource.
        """

        AssertAPI.read(self.params)

        return self

    def update(self) -> Assert:
        """Updates assert with given parameters.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            Assert: Updated assert resource.
        """

        AssertAPI.update(self.params)

        return self

    def delete(self) -> None:
        """Deletes and existing assert.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        AssertAPI.delete(self.params)

    def duplicate(self) -> Assert:
        """Duplicates and existing assert.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Assert: Duplicate instance of assert.
        """

        dp = AssertParams(
            assert_id=self.params.assert_id,
            test_id=self.params.test_id,
        )

        dupl = Assert(params=AssertAPI.duplicate(dp))

        return dupl

    def preconditions(self) -> list[AssertPrecondition]:
        """Read all preconditions of assert.

        Raises:
            ValueError: Assert.params.test_id must be a valid int
            ValueError: Assert.params.assert_id must be a valid int
            APIException: If API call fails.

        Returns:
            list[AssertPrecondition]: List of all preconditions of assert
        """

        if self.params.test_id is None:
            raise ValueError("Assert.params.test_id must be a valid int")

        if self.params.assert_id is None:
            raise ValueError("Assert.params.assert_id must be a valid int")

        return convert_params_list(
            AssertPrecondition,
            AssertPreconditionAPI.read_all(
                self.params.test_id, self.params.assert_id
            ),
        )


class AssertAPI:
    """AssertAPI defines Loadero API operations for assert resources."""

    @staticmethod
    def create(params: AssertParams) -> AssertParams:
        """Create a new assert resource.

        Args:
            params (AssertParams): Describes the assert resource to be created.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            AssertParams: Created assert resource.
        """

        AssertAPI.__validate_identifiers(params, False)

        return params.from_dict(
            APIClient().post(AssertAPI.route(params.test_id), params.to_dict())
        )

    @staticmethod
    def read(params: AssertParams) -> AssertParams:
        """Read an existing assert resource.

        Args:
            params (AssertParams): Describes the assert resource to read.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            AssertParams: Read assert resource.
        """

        AssertAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(AssertAPI.route(params.test_id, params.assert_id))
        )

    @staticmethod
    def update(params: AssertParams) -> AssertParams:
        """Update an existing assert resource.

        Args:
            params (AssertParams): Describes the assert resource to update.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            AssertParams: Updated assert resource.
        """

        AssertAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().put(
                AssertAPI.route(params.test_id, params.assert_id),
                params.to_dict(),
            )
        )

    @staticmethod
    def delete(params: AssertParams) -> None:
        """Delete an existing assert resource.

        Args:
            params (AssertParams): Describes the assert resource to delete.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        AssertAPI.__validate_identifiers(params)

        APIClient().delete(AssertAPI.route(params.test_id, params.assert_id))

    @staticmethod
    def duplicate(params: AssertParams) -> AssertParams:
        """Duplicate an existing assert resource.

        Args:
            params (AssertParams): Describe the assert resource to duplicate and
            the name of duplicate assert resource.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            AssertParams: Duplicate assert resource.
        """

        AssertAPI.__validate_identifiers(params)

        dupl = AssertParams()

        return dupl.from_dict(
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

        Raises:
            APIException: If API call fails.

        Returns:
            list[AssertParams]: List of all assert resources in test.
        """

        resp = APIClient().get(AssertAPI.route(test_id))

        if "results" not in resp or resp["results"] is None:
            return []

        return from_dict_as_list(AssertParams)(resp["results"])

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

    @staticmethod
    def __validate_identifiers(params: AssertParams, single: bool = True):
        """Validate assert resource identifiers.

        Args:
            params (AssertParams): Assert resource params.
            single (bool, optional): Indicates if the resource identifiers
                should be validated as pointing to a single resource (True) or
                to all assert resources belinging to test resource.
                Defaults to True.

        Raises:
            Exception: AssertParams.test_id must be a valid int
            Exception: AssertParams.assert_id must be a valid int
        """

        if params.test_id is None:
            raise Exception("AssertParams.test_id must be a valid int")

        if single and params.assert_id is None:
            raise Exception("AssertParams.assert_id must be a valid int")
