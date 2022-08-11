"""Loadero assert resource.
Assert resource is seperated into three parts
    - AssertPreconditionParams class describes assert preconditions attributes
    - AssertPreconditionAPI class that groups all API operations with assert
        preconditions attributes.
    - AssertPrecondition class combines AssertPreconditionParams and
        AssertPreconditionAPI.

Single AssertPrecondition object coresponds to a single assert precondition in
Loadero.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser

from ..api_client import APIClient
from .resource import (
    FilterKey,
    LoaderoResourceParams,
    LoaderoResource,
    QueryParams,
)
from .classificator import Operator, Property
from .pagination import PagedResponse


class AssertPreconditionFilterKey(FilterKey):
    """AssertPreconditionFilterKey is an enum of all filter keys for assert
    precondition read all API operation."""

    FILTER_PROPERTY = "filter_property"
    FILTER_OPERATOR = "filter_operator"
    FILTER_EXPECTED = "filter_expected"


class AssertPreconditionParams(LoaderoResourceParams):
    """AssertPreconditionParams describes single Loadero assert precondition
    resources attributes.
    AssertPreconditionParams has a builder pattern for write
    attributes.
    """

    def __init__(
        self,
        assert_precondition_id: int or None = None,
        assert_id: int or None = None,
        test_id: int or None = None,
        expected: str or None = None,
        operator: Operator or None = None,
        precondition_property: Property or None = None,
    ) -> None:
        super().__init__(
            attribute_map={
                "id": "assert_precondition_id",
                "assert_id": "assert_id",
                "test_id": "test_id",
                "expected": "expected",
                "operator": "operator",
                "property": "precondition_property",
                "created": "_created",
                "updated": "_updated",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "operator": Operator.from_dict,
                "property": Property.from_dict,
            },
            body_attributes=["expected", "operator", "property"],
            required_body_attributes=["expected", "operator", "property"],
        )

        self.assert_precondition_id = assert_precondition_id
        self.assert_id = assert_id
        self.test_id = test_id
        self.expected = expected
        self.operator = operator
        self.precondition_property = precondition_property

        self._created = None
        self._updated = None

    @property
    def created(self) -> datetime:
        """Time when resource was created.

        Returns:
            datetime: Time when resource was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when resource was last updated.

        Returns:
            datetime: Time when resource was last updated.
        """

        return self._updated

    def with_id(self, assert_precondition_id: int) -> AssertPreconditionParams:
        """Set assert precondition id.

        Args:
            assert_precondition_id (int): Assert precondition id.

        Returns:
            AssertPreconditionParams: Resource params with set id.
        """

        self.assert_precondition_id = assert_precondition_id
        return self

    def for_assert(self, assert_id: int) -> AssertPreconditionParams:
        """Set parent assert resource id.

        Args:
            assert_id (int): Assert resource id.

        Returns:
            AssertPreconditionParams: Resource params with set parent assert id.
        """

        self.assert_id = assert_id
        return self

    def in_test(self, test_id: int) -> AssertPreconditionParams:
        """Set parent test resource id.

        Args:
            test_id (int): Test resource id.

        Returns:
            AssertPreconditionParams: Resource params with set parent test
                resource id.
        """

        self.test_id = test_id
        return self

    def with_expected(self, expected: str) -> AssertPreconditionParams:
        """Set precondition expected value.

        Args:
            expected (str): Precondition expected value.

        Returns:
            AssertPreconditionParams: Resource params with set expected value.
        """

        self.expected = expected
        return self

    def with_operator(self, operator: Operator) -> AssertPreconditionParams:
        """Set precondition operator.

        Args:
            operator (Operator): Precondition operator.

        Returns:
            AssertPreconditionParams: Resource params with set operator.
        """

        self.operator = operator
        return self

    def with_property(
        self, precondition_property: Property
    ) -> AssertPreconditionParams:
        """Set precondition property.

        Args:
            precondition_property (Property): Precondition property.

        Returns:
            AssertPreconditionParams: Resource params with set property.
        """

        self.precondition_property = precondition_property
        return self


class AssertPrecondition(LoaderoResource):
    """
    AssertPrecondition class allows to perform CRUD operations on Loadero
    assert precondition resources. APIClient must be previously initialized
    with a valid Loadero access token.
    """

    params = None

    def __init__(
        self,
        test_id: int or None = None,
        assert_id: int or None = None,
        assert_precondition_id: int or None = None,
        params: AssertPreconditionParams or None = None,
    ) -> None:
        self.params = params or AssertPreconditionParams()

        if test_id is not None:
            self.params.test_id = test_id

        if assert_id is not None:
            self.params.assert_id = assert_id

        if assert_precondition_id is not None:
            self.params.assert_precondition_id = assert_precondition_id

        super().__init__(self.params)

    def create(self) -> AssertPrecondition:
        """Creates new assert precondition with given data.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            AssertPrecondition: Created assert precondition resource.
        """

        AssertPreconditionAPI.create(self.params)

        return self

    def read(self) -> AssertPrecondition:
        """Reads information about an existing assert precondition.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            AssertPrecondition: Read assert precondition resource.
        """

        AssertPreconditionAPI.read(self.params)

        return self

    def update(self) -> AssertPrecondition:
        """Updates assert precondition with given parameters.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            AssertPrecondition: Updated assert precondition resource.
        """

        self.params = AssertPreconditionAPI.update(self.params)

        return self

    def delete(self) -> AssertPrecondition:
        """Deletes and existing assert precondition.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        AssertPreconditionAPI.delete(self.params)

        return self


class AssertPreconditionAPI:
    """AssertPreconditionAPI defines Loadero API operations for assert
    precondition resources.
    """

    @staticmethod
    def create(params: AssertPreconditionParams) -> AssertPreconditionParams:
        """Create a new assert precondition resource.

        Args:
            params (AssertPreconditionParams): Describes the assert
                precondition resource to be created.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            AssertPreconditionParams: Created assert precondition resource.
        """

        AssertPreconditionAPI.__validate_identifiers(params, False)

        return params.from_dict(
            APIClient().post(
                AssertPreconditionAPI.route(params.test_id, params.assert_id),
                params.to_dict(),
            )
        )

    @staticmethod
    def read(params: AssertPreconditionParams) -> AssertPreconditionParams:
        """Read an existing assert precondition resource.

        Args:
            params (AssertPreconditionParams): Describes the assert
                precondition resource to be read.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            AssertPreconditionParams: Read assert precondition resource.
        """

        AssertPreconditionAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(
                AssertPreconditionAPI.route(
                    params.test_id,
                    params.assert_id,
                    params.assert_precondition_id,
                ),
            )
        )

    @staticmethod
    def update(params: AssertPreconditionParams) -> AssertPreconditionParams:
        """Update an existing assert precondition resource.

        Args:
            params (AssertPreconditionParams): Describes the assert
                precondition resource to update.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            AssertPreconditionParams: Updated assert precondition resource.
        """

        AssertPreconditionAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().put(
                AssertPreconditionAPI.route(
                    params.test_id,
                    params.assert_id,
                    params.assert_precondition_id,
                ),
                params.to_dict(),
            )
        )

    @staticmethod
    def delete(params: AssertPreconditionParams) -> None:
        """Delete an existing assert precondition resource.

        Args:
            params (AssertPreconditionParams): Describes the assert
                precondition resource to delete.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        AssertPreconditionAPI.__validate_identifiers(params)

        APIClient().delete(
            AssertPreconditionAPI.route(
                params.test_id, params.assert_id, params.assert_precondition_id
            )
        )

    @staticmethod
    def read_all(
        test_id: int, assert_id: int, query_params: QueryParams or None = None
    ) -> PagedResponse:
        """Read all assert precondition resources of assert.

        Args:
            test_id (int): Test resource id.
            assert_id (int): Parent assert resource id.
            query_params (QueryParams, optional): Describes query parameters.

        Raises:
            APIException: If API call fails.

        Returns:
            PagedResponse: Paged response of assert precondition resources.
        """

        qp = None
        if query_params is not None:
            qp = query_params.parse()

        pr = PagedResponse(AssertPreconditionParams).from_dict(
            APIClient().get(
                AssertPreconditionAPI.route(test_id, assert_id), query_params=qp
            )
        )

        for ap in pr.results:
            ap.test_id = test_id

        return pr

    @staticmethod
    def route(
        test_id: int, assert_id: int, assert_precondition_id: int or None = None
    ) -> str:
        """Build assert precondition resource url route.

        Args:
            test_id (int): Test resource id.
            assert_id (int): Assert resource id.
            assert_precondition_id (int, optional): Assert precondition
                resource id. Defaults to None. If omitted the route will point
                to all assert preconditions of assert.


        Returns:
            str: Route to assert precondition resource/s.
        """

        r = (
            APIClient().project_route
            + f"tests/{test_id}/asserts/{assert_id}/preconditions/"
        )

        if assert_precondition_id is not None:
            r += f"{assert_precondition_id}/"

        return r

    @staticmethod
    def __validate_identifiers(
        params: AssertPreconditionParams, single: bool = True
    ):
        """Validate assert precondition resource identifiers.

        Args:
            params (AssertPreconditionParams): Assert precondition params.
            single (bool, optional): Indicates if the resource identifiers
                should be validated as pointing to a single resource (True) or
                to all precondition resources belonging to assert resource.
                Defaults to True.

        Raises:
            ValueError: AssertPreconditionParams.test_id must be a valid int
            ValueError: AssertPreconditionParams.assert_id must be a valid int
            ValueError: AssertPreconditionParams.assert_precondition_id must be
                a valid int
        """

        if params.test_id is None:
            raise ValueError(
                "AssertPreconditionParams.test_id must be a valid int"
            )

        if params.assert_id is None:
            raise ValueError(
                "AssertPreconditionParams.assert_id must be a valid int"
            )

        if single and params.assert_precondition_id is None:
            raise ValueError(
                "AssertPreconditionParams.assert_precondition_id "
                "must be a valid int"
            )
