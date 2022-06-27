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
from .resource import LoaderoResourceParams, from_dict_as_list
from .classificator import Operator, Property


class AssertPreconditionParams(LoaderoResourceParams):
    """
    AssertPreconditionParams represents Loadero assert precondition resource
    attributes. AssertPreconditionParams has a builder pattern for write
    attributes.
    """

    assert_precondition_id = None
    assert_id = None
    test_id = None

    expected = None
    operator = None
    precondition_property = None

    _created = None
    _updated = None

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

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    def with_id(self, assert_precondition_id: int) -> AssertPreconditionParams:
        self.assert_precondition_id = assert_precondition_id

        return self

    def for_assert(self, assert_id: int) -> AssertPreconditionParams:
        self.assert_id = assert_id

        return self

    def in_test(self, test_id: int) -> AssertPreconditionParams:
        self.test_id = test_id

        return self

    def with_expected(self, expected: str) -> AssertPreconditionParams:
        self.expected = expected

        return self

    def with_operator(self, operator: Operator) -> AssertPreconditionParams:
        self.operator = operator

        return self

    # pylint: disable=missing-function-docstring
    def with_property(
        self, precondition_property: Property
    ) -> AssertPreconditionParams:
        self.precondition_property = precondition_property

        return self


class AssertPrecondition:
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
        if params is not None:
            self.params = params
        else:
            self.params = AssertPreconditionParams()

        if test_id is not None:
            self.params.test_id = test_id

        if assert_id is not None:
            self.params.assert_id = assert_id

        if assert_precondition_id is not None:
            self.params.assert_precondition_id = assert_precondition_id

    def create(self) -> AssertPrecondition:
        """Creates new assert precondition with given data.

        Returns:
            AssertPrecondition: Created assert precondition resource.
        """

        AssertPreconditionAPI.create(self.params)

        return self

    def read(self) -> AssertPrecondition:
        """Reads information about an existing assert precondition.

        Returns:
            AssertPrecondition: Read assert precondition resource.
        """

        AssertPreconditionAPI.read(self.params)

        return self

    def update(self) -> AssertPrecondition:
        """Updates assert precondition with given parameters.

        Returns:
            AssertPrecondition: Updated assert precondition resource.
        """

        self.params = AssertPreconditionAPI.update(self.params)

        return self

    def delete(self) -> AssertPrecondition:
        """Deletes and existing assert precondition."""

        AssertPreconditionAPI.delete(self.params)

        return self


class AssertPreconditionAPI:
    """
    AssertPreconditionAPI defines Loadero API operations for assert
    precondition resources.
    """

    @staticmethod
    def create(params: AssertPreconditionParams) -> AssertPreconditionParams:
        """Create a new assert precondition resource.

        Args:
            params (AssertPreconditionParams): Describes the assert
                precondition resource to be created.

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
        """

        AssertPreconditionAPI.__validate_identifiers(params)

        APIClient().delete(
            AssertPreconditionAPI.route(
                params.test_id, params.assert_id, params.assert_precondition_id
            )
        )

    @staticmethod
    def read_all(
        test_id: int, assert_id: int
    ) -> list[AssertPreconditionParams]:
        """Read all assert precondition resources of assert.

        Args:
            test_id (int): Test resource id.
            assert_id (int): Parent assert resource id.

        Returns:
            list[AssertPreconditionParams]: List of all assert precondition
                resources for assert.
        """

        resp = APIClient().get(AssertPreconditionAPI.route(test_id, assert_id))

        if "results" not in resp or resp["results"] is None:
            return []

        res = from_dict_as_list(AssertPreconditionParams)(resp["results"])

        for r in res:
            r.test_id = test_id

        return res

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
            APIClient().project_url
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
