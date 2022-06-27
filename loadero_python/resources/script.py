# coding: utf-8

"""
Loadero script resource.
Script resource can be created by either suppling the scripts contents directly
or by supplying a filename from which to load the script.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser
from ..api_client import APIClient
from .resource import (
    LoaderoResourceParams,
    Serializable,
    from_dict_as_list,
)
from .classificator import FileType


class FileParams(LoaderoResourceParams):
    """FileParams represents Loadero file parameters."""

    file_id = None
    _created = None
    _updated = None
    _file_type = None
    _content = None

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

    @property
    def created(self) -> datetime or None:
        return self._created

    @property
    def updated(self) -> datetime or None:
        return self._updated

    @property
    def file_type(self) -> FileType or None:
        return self._file_type

    @property
    def content(self) -> str or None:
        return self._content


class Script(Serializable):
    """Script describes a single Loadero test script."""

    # _content = None
    # _params = FileParams()

    # content = ""
    # file_id = None

    def __init__(
        self,
        file_id: int or None = None,
        content: str or None = None,
        filepath: str or None = None,
    ) -> None:
        """Creates a new script or loads an existing script.

        Args:
            script_id (int, optional): File id of the script Loadero resource.
                Defaults to None.
            content (str, optional): Script file contents. Defaults to None.
            script_file (str, optional): File path to a script. Defaults to
                None.

        If more than one script content source is specified, then the loading
        priorities are: script_id - first, content - second,
        script_file - third.
        """

        self.file_id = file_id
        self.content = content

        if filepath is not None:
            self.from_file(filepath)

        # if script_id is not None:
        #     self._params.file_id = script_id

        #     return

        # if content is not None:
        #     self.from_content(content)

        #     return

        # if script_file is not None:
        #     self.from_file(script_file)

    def __str__(self) -> str:
        if self.content is None:
            return "<no script>"

        return self.content

    # @property
    # def file_id(self) -> int:
    #     return self._params.file_id

    # @file_id.setter
    # def file_id(self, file_id: int) -> None:
    #     self._params.file_id = file_id

    # @property
    # def content(self) -> str:
    #     """Contents of script.

    #     Returns:
    #         str: Contents of a script loaded by user or read from Loadero API.
    #     """

    #     if self._params.content is not None:
    #         return self._params.content

    #     if self._content is not None:
    #         return self._content

    #     return ""

    def from_file(self, filepath: str) -> Script:
        """Loads Loadero script from file.

        Args:
            filepath (str): file path to script file

        Returns:
            Script: script loaded from file
        """

        with open(filepath, "r") as f:
            self.content = f.read()

        return self

    # def from_content(self, content: str) -> Script:
    #     """Loads Loadero script from provided str data.

    #     Args:
    #         content (str): script

    #     Returns:
    #         Script: script loaded from data
    #     """
    #     self._content = content

    #     return self

    def to_dict(self) -> str:
        return self.content

    def to_dict_full(self) -> str:
        return self.to_dict()

    def from_dict(self, json_dict: dict[str, any]) -> Script:
        return self

    def read(self) -> Script:
        self.content = FileAPI().read(FileParams(self.file_id)).content

        return self


class FileAPI:
    """FileAPI defines Loadero API operations for file resources."""

    @staticmethod
    def read(params: FileParams) -> FileParams:
        """Read an existing file resource.

        Args:
            params (FileParams): Describes the file resource to read.


        Returns:
            FileParams: Read file resource.
        """

        FileAPI.__validate_identifiers(params)

        return params.from_dict(
            APIClient().get(FileAPI().route(params.file_id))
        )

    @staticmethod
    def read_all() -> list[FileParams]:
        """Read all files.

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

        r = APIClient().project_url + "files/"

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
