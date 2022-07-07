# coding: utf-8

"""
Loadero group resource.
Group resource is seperated into two parts - GroupParams class that describes
groups attributes and Group class that in combination with GroupParams and
APIClient allows to perform CRUD operations on Loadero group resources.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .resource import (
    LoaderoResourceParams,
    DuplicateResourceBodyParams,
    from_dict_as_list,
    convert_params_list,
)
from .participant import Participant, ParticipantAPI


class GroupParams(LoaderoResourceParams):
    """
    GroupParams represents Loadero group resource attributes.
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
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    @property
    def total_cu_count(self) -> int:
        return self._total_cu_count

    @property
    def participant_count(self) -> int:
        return self._participant_count

    def with_id(self, group_id: int) -> GroupParams:
        self.group_id = group_id

        return self

    def with_name(self, name: str) -> GroupParams:
        self.name = name

        return self

    def with_count(self, count: int) -> GroupParams:
        self.count = count

        return self

    def in_test(self, tid: int) -> GroupParams:
        self.test_id = tid

        return self


class Group:
    """
    Group class allows to perform CRUD operations on Loadero group resources.
    APIClient must be previously initialized with a valid Loadero access token.
    The target Loadero group resource is determined by GroupParams.
    """

    params = None

    def __init__(
        self,
        group_id: int or None = None,
        test_id: int or None = None,
        params: GroupParams or None = None,
    ) -> None:
        if params is not None:
            self.params = params
        else:
            self.params = GroupParams()

        if group_id is not None:
            self.params.group_id = group_id

        if test_id is not None:
            self.params.test_id = test_id

    def create(self) -> Group:
        """Creates new group with given data.

        Returns:
            Group: Created group resource.
        """

        GroupAPI.create(self.params)

        return self

    def read(self) -> Group:
        """Reads information about an existing group.

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

        dp = GroupParams(
            group_id=self.params.group_id,
            test_id=self.params.test_id,
            name=name,
        )

        dupl = Group(params=GroupAPI.duplicate(dp))

        return dupl

    def participants(self) -> list[Participant]:
        """Read all participants in group.

        Returns:
            list[Participant]: List of participants in group.
        """

        return convert_params_list(
            Participant,
            ParticipantAPI.read_all(
                self.params.test_id, group_id=self.params.group_id
            ),
        )


class GroupAPI:
    """GroupAPI defines Loadero API operations for group resources."""

    @staticmethod
    def create(params: GroupParams) -> GroupParams:
        """Create a new group resource.

        Args:
            params (GroupParams): Describes the group resource to be created.

        Raises:
            Exception: GroupParams.test_id was not defined.

        Returns:
            GroupParams: Created group resource.
        """

        if params.test_id is None:
            raise Exception("GroupParams.test_id must be a valid int")

        return params.from_dict(
            APIClient().post(GroupAPI.route(params.test_id), params.to_dict())
        )

    @staticmethod
    def read(params: GroupParams) -> GroupParams:
        """Read an existing group resource.

        Args:
            params (GroupParams): Describes the group resource to read.

        Raises:
            Exception: GroupParams.test_id was not defined.
            Exception: GroupParams.group_id was not defined.

        Returns:
            GroupParams: Read group resource.
        """

        if params.test_id is None:
            raise Exception("GroupParams.test_id must be a valid int")

        if params.group_id is None:
            raise Exception("GroupParams.group_id must be a valid int")

        return params.from_dict(
            APIClient().get(GroupAPI.route(params.test_id, params.group_id))
        )

    @staticmethod
    def update(params: GroupParams) -> GroupParams:
        """Update an existing group resource.

        Args:
            params (GroupParams): Describes the group resource to update.

        Raises:
            Exception: GroupParams.test_id was not defined.
            Exception: GroupParams.group_id was not defined.

        Returns:
            GroupParams: Updated group resource.
        """

        if params.test_id is None:
            raise Exception("GroupParams.test_id must be a valid int")

        if params.group_id is None:
            raise Exception("GroupParams.group_id must be a valid int")

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
            Exception: GroupParams.test_id was not defined.
            Exception: GroupParams.group_id was not defined.
        """

        if params.test_id is None:
            raise Exception("GroupParams.test_id must be a valid int")

        if params.group_id is None:
            raise Exception("GroupParams.group_id must be a valid int")

        APIClient().delete(GroupAPI.route(params.test_id, params.group_id))

    @staticmethod
    def duplicate(params: GroupParams) -> GroupParams:
        """Duplicate an existing group resource.

        Args:
            params (GroupParams): Describe the group resource to duplicate and
            the name of duplicate group resource.

        Raises:
            Exception: GroupParams.test_id was not defined.
            Exception: GroupParams.group_id was not defined.

        Returns:
            GroupParams: Duplicate group resource.
        """

        if params.test_id is None:
            raise Exception("GroupParams.test_id must be a valid int")

        if params.group_id is None:
            raise Exception("GroupParams.group_id must be a valid int")

        dupl = GroupParams()

        req = DuplicateResourceBodyParams(name=params.name)

        return dupl.from_dict(
            APIClient().post(
                GroupAPI.route(params.test_id, params.group_id) + "copy/",
                req.to_dict(),
            )
        )

    @staticmethod
    def read_all(test_id: int) -> list[GroupParams]:
        """Read all group resources.

        Args:
            test_id (int): Parent test resource id.

        Returns:
            list[GroupParams]: List of all group resources in test.
        """
        resp = APIClient().get(GroupAPI.route(test_id))

        if "results" not in resp or resp["results"] is None:
            return []

        return from_dict_as_list(GroupParams)(resp["results"])

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
        r = APIClient().project_url + f"tests/{test_id}/groups/"

        if group_id is not None:
            r += f"{group_id}/"

        return r

    # TODO: create __validate_identifiers method and apply it.
