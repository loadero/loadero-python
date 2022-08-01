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
from ..api_client import APIClient
from .resource import LoaderoResourceParams, LoaderoResource, from_dict_as_list
from .classificator import FileType


class FileParams(LoaderoResourceParams):
    """FileParams represents Loadero file parameters."""

    def __init__(self, file_id: int or None = None):
        super().__init__(
            attribute_map={
                "id": "file_id",
                "created": "_created",
                "updated": "_updated",
                "file_type": "_file_type",
                "content": "_content",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "file_type": FileType.from_dict,
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

        self.file_id = file_id

        self._created = None
        self._updated = None
        self._file_type = None
        self._content = None

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

    @property
    def file_type(self) -> FileType:
        """Files type.

        Returns:
            FileType: Files type.
        """

        return self._file_type

    @property
    def content(self) -> str:
        """Files content.

        Returns:
            str: Files content.
        """

        return self._content


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


class FileAPI:
    """FileAPI defines Loadero API operations for file resources."""

    @staticmethod
    def read(params: FileParams) -> FileParams:
        """Read an existing file resource.

        Args:
            params (FileParams): Describes the file resource to read.

        Raises:
            Exception: FileParams.file_id was not defined.
            APIException: If API call fails.

        Returns:
            FileParams: Read file resource.
        """

        FileAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(FileAPI().route(params.file_id))
        )

    @staticmethod
    def read_all() -> list[FileParams]:
        """Read all files in project.

        Raises:
            APIException: If API call fails.

        Returns:
            list[FileParams]: List of file resources in project.
        """

        resp = APIClient().get(FileAPI.route())

        if "results" not in resp or resp["results"] is None:
            return []

        return from_dict_as_list(FileParams)(resp["results"])

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
            raise Exception("FileParams.file_id must be a valid int")
