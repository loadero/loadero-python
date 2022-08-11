"""Loadero group resource.

Group resource is seperated into three parts
    - GroupParams class describes groups attributes
    - GroupAPI class groups all API operations related to groups.
    - Group class combined GroupParams and GroupAPI

Single group object coresponds to single group in Loadero.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .resource import (
    FilterKey,
    LoaderoResourceParams,
    LoaderoResource,
    DuplicateResourceBodyParams,
    convert_params_list,
    from_dict_as_new,
)
from .participant import Participant, ParticipantAPI
from .pagination import PagedResponse, PaginationParams
from .resource import QueryParams


class GroupFilterKey(FilterKey):
    """GroupFilterKey is an enum of all filter keys for group read all API
    operation."""

    NAME = "filter_name"
    COUNT_FROM = "filter_count_from"
    COUNT_TO = "filter_count_to"


class GroupParams(LoaderoResourceParams):
    """GroupParams represents Loadero group resource attributes.
    GroupParams has a builder pattern for group resources read and write
    attributes.
    """

    def __init__(
        self,
        group_id: int or None = None,
        name: str or None = None,
        count: int or None = None,
        test_id: int or None = None,
    ) -> None:
        super().__init__(
            attribute_map={
                "id": "group_id",
                "count": "count",
                "name": "name",
                "test_id": "test_id",
                "created": "_created",
                "updated": "_updated",
                "total_cu_count": "_total_cu_count",
                "participant_count": "_participant_count",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
            },
            body_attributes=[
                "count",
                "name",
            ],
            required_body_attributes=[
                "count",
                "name",
            ],
        )

        self.group_id = group_id
        self.name = name
        self.count = count
        self.test_id = test_id

        self._total_cu_count = None
        self._participant_count = None
        self._created = None
        self._updated = None

    @property
    def created(self) -> datetime or None:
        """Time when group was created.

        Returns:
            datetime: Time when group was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when group was last updated.

        Returns:
            datetime: Time when group was last updated.
        """
        return self._updated

    @property
    def total_cu_count(self) -> int:
        """Total compute unit count in group.

        Returns:
            int: Total compute unit count in group.
        """

        return self._total_cu_count

    @property
    def participant_count(self) -> int:
        """Participant count in group.

        Returns:
            int: Participant count in group.
        """

        return self._participant_count

    def with_id(self, group_id: int) -> GroupParams:
        """Set group id.

        Args:
            group_id (int): Group id.

        Returns:
            GroupParams: Group params with set group id.
        """

        self.group_id = group_id
        return self

    def with_name(self, name: str) -> GroupParams:
        """Set group name.

        Args:
            name (str): Group name.

        Returns:
            GroupParams: Group params with set group name.
        """

        self.name = name
        return self

    def with_count(self, count: int) -> GroupParams:
        """Set group count.

        Args:
            count (int): Group count.

        Returns:
            GroupParams: Group params with set group count.
        """

        self.count = count
        return self

    def in_test(self, tid: int) -> GroupParams:
        """Set parent test id.

        Args:
            tid (int): Test id.

        Returns:
            GroupParams: Group params with set parent test id.
        """

        self.test_id = tid
        return self


class Group(LoaderoResource):
    """Group class allows to perform CRUD operations on a single Loadero group
    resource.
    APIClient must be previously initialized with a valid Loadero access token.
    The target Loadero group resource is determined by GroupParams.
    """

    def __init__(
        self,
        group_id: int or None = None,
        test_id: int or None = None,
        params: GroupParams or None = None,
    ) -> None:
        self.params = params or GroupParams()

        if group_id is not None:
            self.params.group_id = group_id

        if test_id is not None:
            self.params.test_id = test_id

        super().__init__(self.params)

    def create(self) -> Group:
        """Creates new group with given data.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            Group: Created group resource.
        """

        GroupAPI.create(self.params)

        return self

    def read(self) -> Group:
        """Reads information about an existing group.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            Group: Read group resource.
        """

        GroupAPI.read(self.params)

        return self

    def update(self) -> Group:
        """Updates group with given parameters.

        Returns:
            Group: Updated group resource.
        """

        GroupAPI.update(self.params)

        return self

    def delete(self) -> None:
        """Deletes and existing group."""

        GroupAPI.delete(self.params)

    def duplicate(self, name: str) -> Group:
        """Duplicates and existing group.

        Args:
            name (str): New name for the duplicate group.

        Returns:
            Group: Duplicate instance of group.
        """

        return Group(params=GroupAPI.duplicate(self.params, name))

    def participants(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[Participant], PaginationParams, dict[any, any]]:
        """Read all participants in group.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            ValueError: Test.params.test_id must be a valid int.
            APIException: If API call fails.

        Returns:
            list[Participant]: List of participants in group.
        """

        if self.params.test_id is None:
            raise ValueError("Group.params.test_id must be a valid int")

        if self.params.group_id is None:
            raise ValueError("Group.params.group_id must be a valid int")

        resp = ParticipantAPI.read_all(
            self.params.test_id,
            group_id=self.params.group_id,
            query_params=query_params,
        )

        return (
            convert_params_list(Participant, resp.results),
            resp.pagination,
            resp.filter,
        )


class GroupAPI:
    """GroupAPI defines Loadero API operations for group resources."""

    @staticmethod
    def create(params: GroupParams) -> GroupParams:
        """Create a new group resource.

        Args:
            params (GroupParams): Describes the group resource to be created.

        Raises:
            ValueError: If resource params do not sufficiently identify parent
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            GroupParams: Created group resource.
        """

        GroupAPI.__validate_identifiers(params, False)

        return params.from_dict(
            APIClient().post(GroupAPI.route(params.test_id), params.to_dict())
        )

    @staticmethod
    def read(params: GroupParams) -> GroupParams:
        """Read an existing group resource.

        Args:
            params (GroupParams): Describes the group resource to read.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            GroupParams: Read group resource.
        """

        GroupAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(GroupAPI.route(params.test_id, params.group_id))
        )

    @staticmethod
    def update(params: GroupParams) -> GroupParams:
        """Update an existing group resource.

        Args:
            params (GroupParams): Describes the group resource to update.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource or resource params required attributes are None.
            APIException: If API call fails.

        Returns:
            GroupParams: Updated group resource.
        """

        GroupAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().put(
                GroupAPI.route(params.test_id, params.group_id),
                params.to_dict(),
            )
        )

    @staticmethod
    def delete(params: GroupParams) -> None:
        """Delete an existing group resource.

        Args:
            params (GroupParams): Describes the group resource to delete.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        GroupAPI.__validate_identifiers(params)

        APIClient().delete(GroupAPI.route(params.test_id, params.group_id))

    @staticmethod
    def duplicate(params: GroupParams, name: str) -> GroupParams:
        """Duplicate an existing group resource.

        Args:
            params (GroupParams): Identified the group resource to duplicate.
            name (str): Name of the duplicate group.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            GroupParams: Duplicate group resource.
        """

        GroupAPI.__validate_identifiers(params)

        return from_dict_as_new(GroupParams)(
            APIClient().post(
                GroupAPI.route(params.test_id, params.group_id) + "copy/",
                DuplicateResourceBodyParams(name=name).to_dict(),
            )
        )

    @staticmethod
    def read_all(
        test_id: int, query_params: QueryParams or None = None
    ) -> PagedResponse:
        """Read all group resources.

        Args:
            test_id (int): Parent test resource id.
            query_params (QueryParams, optional): Describes query parameters.

        Returns:
            PagedResponse: Paged response of group resources.
        """

        qp = None
        if query_params is not None:
            qp = query_params.parse()

        return PagedResponse(GroupParams).from_dict(
            APIClient().get(GroupAPI.route(test_id), query_params=qp)
        )

    @staticmethod
    def route(test_id: int, group_id: int or None = None) -> str:
        """Build group resource url route.

        Args:
            test_id (int): Test resource id.
            group_id (int, optional): Group resource id. Defaults to None. If
                omitted the route will point to all group resources.

        Returns:
            str: Route to group resource/s.
        """
        r = APIClient().project_route + f"tests/{test_id}/groups/"

        if group_id is not None:
            r += f"{group_id}/"

        return r

    @staticmethod
    def __validate_identifiers(
        params: GroupParams, single: bool = True
    ) -> None:
        """Validate group resource identifiers.

        Args:
            params (GroupParams): Group resource params.
            single (bool, optional): Indicates if the resource identifiers
                should be validated as pointing to a single resource (True) or
                to all assert resources belinging to test resource.
                Defaults to True.

        Raises:
            ValueError: GroupParams.test_id must be a valid int
            ValueError: GroupParams.group_id must be a valid int
        """

        if params.test_id is None:
            raise ValueError("GroupParams.test_id must be a valid int")

        if single and params.group_id is None:
            raise ValueError("GroupParams.group_id must be a valid int")
