# coding: utf-8

"""
Loadero group resource.
Group resource is seperated into two parts - GroupParams class that describes
groups attributes and Group class that in combination with GroupParams and
APIClient allows to perform CRUD operations on Loadero group resources.
"""

from __future__ import annotations
from ..api_client import APIClient


class GroupParams:
    """
    GroupParams represents Loadero group resource attributes.
    GroupParams has a builder patter for group resources read and write
    attributes.
    """

    # Describes python object attribute name mapping to Loadero resources
    # JSON field names.
    attribute_map = {
        "group_id": "id",
        "count": "count",
        "name": "name",
        "_test_id_path": "test_id",
        "_created": "created",
        "_updated": "updated",
        "_total_cu_count": "total_cu_count",
        "_participant_count": "participant_count",
    }

    body_attributes = {
        "count": "count",
        "name": "name",
    }

    # id. read as path, update as body
    group_id = None

    # required
    count = None
    name = None

    # route paths
    _project_id_path = None
    _test_id_path = None

    # read only
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
        self.test_id_path = test_id
        self.project_id_path = project_id

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
        return self._project_id_path

    @property
    def test_id(self) -> int:
        return self._test_id_path

    def with_id(self, group_id: int) -> GroupParams:
        self.group_id = group_id

        return self

    def with_name(self, name: str) -> GroupParams:
        self.name = name

        return self

    def with_count(self, count: int) -> GroupParams:
        self.count = count

        return self

    def in_project(self, pid: int) -> GroupParams:
        self._project_id_path = pid

        return self

    def in_test(self, tid: int) -> GroupParams:
        self._test_id_path = tid

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
            if self.params is None:
                self.params = GroupParams()

            self.params.group_id = group_id

    def create(self, api_client: APIClient) -> Group:
        """Creates new group with given data.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Group: created group resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def read(self, api_client: APIClient) -> Group:
        """Reads information about an existing group.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Group: retrived group resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def update(self, api_client: APIClient) -> Group:
        """Updates group with given parameters.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Group: updated group resource
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self

    def delete(self, api_client: APIClient) -> None:
        """Deletes and existing group.

        Args:
            api_client (APIClient): initalized instance of API client
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

    def duplicate(self, api_client: APIClient) -> Group:
        """Duplicates and existing group.

        Args:
            api_client (APIClient): initalized instance of API client

        Returns:
            Group: duplicate instance of group
        """

        # TODO: finnish when API client implementation is finished

        api_client.call_api(self.params)

        return self
