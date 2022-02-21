# coding: utf-8

"""
    Loadero group resource
"""

from __future__ import annotations
from ..api_client import ApiClient


class GroupParams:

    """Group Params"""

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
        if group_id is not None:
            self.group_id = group_id

        if name is not None:
            self.name = name

        if count is not None:
            self.count = count

        if test_id is not None:
            self.test_id_path = test_id

        if project_id is not None:
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
    GROUP
    """

    params = None

    def __init__(
        self,
        group_id: int or None = None,
        params: GroupParams or None = None,
    ) -> None:
        if params is not None:
            self.params = params

        if group_id is not None:
            if self.params is None:
                self.params = GroupParams()

            self.params.group_id = group_id

    def create(self, api_client: ApiClient) -> Group:
        """create operation"""

        api_client.call_api(self.params)

        return self

    def read(self, api_client: ApiClient) -> Group:
        """create operation"""

        api_client.call_api(self.params)

        return self

    def update(self, api_client: ApiClient) -> Group:
        """create operation"""

        api_client.call_api(self.params)

        return self

    def delete(self, api_client: ApiClient) -> Group:
        """create operation"""

        api_client.call_api(self.params)

        return self

    def duplicate(self, api_client: ApiClient) -> Group:
        """create operation"""

        api_client.call_api(self.params)

        return self
