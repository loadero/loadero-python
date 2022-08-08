"""Loadero file resource.

File resource is seperated into three parts
    - FileParams class describes file attributes
    - FileAPI class groups file related API calls
    - File class combines FileParams and FileAPI

Single File object coresponds to single file in Loadero.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser

from .pagination import PagedResponse
from ..api_client import APIClient
from .resource import (
    FilterKey,
    LoaderoResourceParams,
    LoaderoResource,
    QueryParams,
)
from .classificator import FileType


class FileFilterKey(FilterKey):
    """FileFilterKey is an enum of all filter keys for file read all API
    operation."""

    FILE_TYPE = "filter_file_type"


class FileParams(LoaderoResourceParams):
    """FileParams represents Loadero file parameters."""

    def __init__(
        self,
        file_id: int or None = None,
        file_type: FileType or None = None,
        content: str or None = None,
        password: str or None = None,
    ):
        super().__init__(
            attribute_map={
                "id": "file_id",
                "created": "_created",
                "updated": "_updated",
                "file_type": "file_type",
                "content": "content",
                "password": "password",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "file_type": FileType.from_dict,
            },
            body_attributes=[
                "content",
                "file_type",
                "password",
            ],
            required_body_attributes=[
                "content",
                "file_type",
            ],
        )

        self.file_id = file_id
        self.file_type = file_type
        self.content = content
        self.password = password

        self._created = None
        self._updated = None

    @property
    def created(self) -> datetime:
        """Time when file was created.

        Returns:
            datetime: Time when resource was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when file was last updated.

        Returns:
            datetime: Time when file was last updated.
        """

        return self._updated


class File(LoaderoResource):
    """File allows to perform CRUD manipulatons on a single Loadero file
    resource.
    APIClient must be previously initialized with a valid Loadero access token.
    The target Loadero file resource is determined by FileParams.
    """

    def __init__(
        self, file_id: int or None = None, params: FileParams or None = None
    ):
        self.params = params or FileParams()

        if file_id is not None:
            self.params.file_id = file_id

        super().__init__(self.params)

    def create(self) -> File:
        """Creates a new file.

        Raises:
            APIException: If API call fails.

        Returns:
            File: Created file resource.
        """

        FileAPI.create(self.params)
        return self

    def read(self) -> File:
        """Reads information about an existing file.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            File: Read file resource.
        """

        FileAPI.read(self.params)
        return self

    def update(self) -> File:
        """Update information about an existing file.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.

        Returns:
            File: Updated file resource.
        """

        FileAPI.update(self.params)
        return self

    def delete(self) -> None:
        """Delete an existing file.

        Raises:
            ValueError: If resource params do not sufficiently identify
                resource.
            APIException: If API call fails.
        """

        FileAPI.delete(self.params)


class FileAPI:
    """FileAPI defines Loadero API operations for file resources."""

    @staticmethod
    def create(params: FileParams) -> FileParams:
        """Create a new file resource.

        Args:
            params (FileParams): Describes the file resource to create.

        Raises:
            APIException: If API call fails.

        Returns:
            FileParams: Created file resource params.
        """

        return params.from_dict(
            APIClient().post(FileAPI.route(), params.to_dict())
        )

    @staticmethod
    def read(params: FileParams) -> FileParams:
        """Read an existing file resource.

        Args:
            params (FileParams): Describes the file resource to read.

        Raises:
            Exception: FileParams.file_id was not defined.
            APIException: If API call fails.

        Returns:
            FileParams: Read file resource params.
        """

        FileAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(FileAPI().route(params.file_id))
        )

    @staticmethod
    def update(params: FileParams) -> FileParams:
        """Update an existing file resource.

        Args:
            params (FileParams): Describes the file and the changes to apply.

        Raises:
            Exception: FileParams.file_id was not defined.
            APIException: If API call fails.

        Returns:
            FileParams: Read file resource.
        """

        FileAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().put(FileAPI.route(params.file_id), params.to_dict())
        )

    @staticmethod
    def delete(params: FileParams) -> None:
        """Delete an existing file resource.

        Args:
            params (FileParams): Describes the file to delete.

        Raises:
            Exception: FileParams.file_id was not defined.
            APIException: If API call fails.

        Returns:
            FileParams: Read file resource.
        """

        FileAPI.__validate_identifiers(params)

        APIClient().delete(FileAPI.route(params.file_id))

    @staticmethod
    def read_all(query_params: QueryParams or None = None) -> PagedResponse:
        """Read all files in project.

        Args:
            query_params (QueryParams, optional): Describes query parameters.

        Raises:
            APIException: If API call fails.

        Returns:
            PagedResponse: Paged response of file resources.
        """

        qp = None
        if query_params is not None:
            qp = query_params.parse()

        return PagedResponse(FileParams).from_dict(
            APIClient().get(FileAPI.route(), qp)
        )

    @staticmethod
    def route(file_id: int or None = None) -> str:
        """Build file resource url route.

        Args:
            file_id (int, optional): File resource id. Defaults to None. If
                omitted the route will point to all file resources

        Returns:
            str: Route to file resource.
        """

        r = APIClient().project_route + "files/"

        if file_id is not None:
            r += f"{file_id}/"

        return r

    @staticmethod
    def __validate_identifiers(params: FileParams, single: bool = True):
        """Validate file resource identifiers.

        Args:
            params (FileParams): File params.
            single (bool, optional): Indicates if the resource identifiers
                should be validated as pointing to a single resource.
                Defaults to True.
        Raises:
            ValueError: FileParams.file_id must be a valid int.
        """

        if single and params.file_id is None:
            raise ValueError("FileParams.file_id must be a valid int")
