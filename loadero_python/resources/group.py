# coding: utf-8

"""
Loadero group resource.
Group resource is seperated into two parts - GroupParams class that describes
groups attributes and Group class that in combination with GroupParams and
APIClient allows to perform CRUD operations on Loadero group resources.
"""

from __future__ import annotations
from dateutil import parser
from ..api_client import APIClient
from .resource import LoaderoResource, to_json, from_json, to_string


class GroupParams(LoaderoResource):
    """
    GroupParams represents Loadero group resource attributes.
    GroupParams has a builder patter for group resources read and write
    attributes.
    """

    # Describes python object attribute name mapping to Loadero resources
    # JSON field names.
    __attribute_map = {
        "group_id": "id",
        "count": "count",
        "name": "name",
        "_test_id": "test_id",
        "_created": "created",
        "_updated": "updated",
        "_total_cu_count": "total_cu_count",
        "_participant_count": "participant_count",
    }

    # Describes a mapping from Loadero resources JSON field names to custom
    # deserialization functions.
    __body_attributes = {
        "count": "count",
        "name": "name",
    }

    # Describes a mapping from Loadero resources JSON field names to custom
    # deserialization functions.
    __custom_deserializers = {
        "created": parser.parse,
        "updated": parser.parse,
    }

    group_id = None

    count = None
    name = None

    _project_id = None
    _test_id = None
    _total_cu_count = None
    _participant_count = None
    _created = None
    _updated = None

    def __init__(
        self,
        group_id: int or None = None,
        name: str or None = None,
        count: int or None = None,
        test_id: int or None = None,
        project_id: int or None = None,
    ) -> None:
        self.group_id = group_id
        self.name = name
        self.count = count
        self._test_id = test_id
        self.project_id_path = project_id

    def __str__(self) -> str:
        return to_string(self.__dict__, self.__attribute_map)

    @property
    def created(self):  # date time
        return self._created

    @property
    def updated(self):  # date time
        return self._updated

    @property
    def total_cu_count(self) -> int:
        return self._total_cu_count

    @property
    def participant_count(self) -> int:
        return self._participant_count

    @property
    def project_id(self) -> int:
        return self._project_id

    @property
    def test_id(self) -> int:
        return self._test_id

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
        self._test_id = tid

        return self

    def to_json(
        self, body_attributes: list[str] or None = None
    ) -> dict[str, any]:
        """Serializes group resource to JSON.

        Args:
            body_attributes (list[str]orNone, optional): String list of JSON
                field names that will be serialized. Defaults to None, then
                the default body attributed for group resource are used.

        Returns:
            dict[str, any]: JSON dictionary.
        """
        if body_attributes is None:
            body_attributes = self.__body_attributes

        return to_json(self.__dict__, self.__attribute_map, body_attributes)

    def from_json(self, json_value: dict[str, any]) -> GroupParams:
        """Serializes group resource from JSON.

        Args:
            json_value (dict[str, any]): JSON dictionary.

        Returns:
            GroupParams: Serialized group resource.
        """

        from_json(
            self.__dict__,
            json_value,
            self.__attribute_map,
            self.__custom_deserializers,
        )

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
        params: GroupParams or None = None,
    ) -> None:
        if params is not None:
            self.params = params
        else:
            self.params = GroupParams()

        if group_id is not None:
            self.params.group_id = group_id

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

    def duplicate(self) -> Group:
        """Duplicates and existing group.

        Returns:
            Group: Duplicate instance of group.
        """

        return Group(params=GroupAPI.duplicate(self.params))


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

        return params.from_json(
            APIClient().post(
                f"projects/{APIClient().project_id}"
                f"/tests/{params.test_id}/groups/",
                params.to_json(),
            )
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

        return params.from_json(
            APIClient().get(
                f"projects/{APIClient().project_id}"
                f"/tests/{params.test_id}/groups/{params.group_id}",
            )
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

        return params.from_json(
            APIClient().put(
                f"projects/{APIClient().project_id}"
                f"/tests/{params.test_id}/groups/{params.group_id}",
                params.to_json(),
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

        APIClient().delete(
            f"projects/{APIClient().project_id}"
            f"/tests/{params.test_id}/groups/{params.group_id}",
        )

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

        return dupl.from_json(
            APIClient().post(
                f"projects/{APIClient().project_id}"
                f"/tests/{params.test_id}/groups/{params.group_id}/copy/",
                params.to_json(["name"]),
            )
        )

    @staticmethod
    def read_all(test_id: int) -> list[GroupParams]:
        # TODO: implement.
        pass
