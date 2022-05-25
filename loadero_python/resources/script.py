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
from .resource import LoaderoResource, from_json
from .classificator import FileType


class FileParams(LoaderoResource):
    """FileParams represents Loadero file parameters."""

    __attribute_map = {
        "file_id": "id",
        "_created": "created",
        "_updated": "updated",
        "_file_type": "file_type",
        "_content": "content",
    }

    # Describes a mapping from Loadero resources JSON field names to custom
    __custom_deserializers = {
        "created": parser.parse,
        "updated": parser.parse,
        "file_type": FileType.from_json,
    }

    file_id = None
    _created = None
    _updated = None
    _file_type = None
    _content = None

    def __init__(self, file_id: int or None = None):
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

    def from_json(self, json_value: dict[str, any]) -> FileParams:
        """Serializes file resource from JSON.

        Args:
            json_value (dict[str, any]): JSON dictionary.

        Returns:
            TestParams: Serialized file resource.
        """

        from_json(
            self.__dict__,
            json_value,
            self.__attribute_map,
            self.__custom_deserializers,
        )

        return self


class Script(LoaderoResource):
    """Script describes a single Loadero test script."""

    _content = None
    _params = None

    def __init__(
        self,
        script_id: int or None = None,
        content: str or None = None,
        script_file: str or None = None,
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

        if script_id is not None:
            self._params = FileParams(script_id)

            return

        if content is not None:
            self.from_content(content)

            return

        if script_file is not None:
            self.from_file(script_file)

    def __str__(self) -> str:
        if self._content is None:
            return "<empty script>"

        return self._content

    @property
    def content(self) -> str:
        """Contents of script.

        Returns:
            str: Contents of a script loaded by user or read from Loadero API.
        """

        if self._params is not None:
            return self._params.content

        if self._content is not None:
            return self._content

        return ""

    def from_file(self, script_file: str) -> Script:
        """Loads Loadero script from file.

        Args:
            script_file (str): file path to script file

        Returns:
            Script: script loaded from file
        """

        with open(script_file, "r") as f:
            self._content = f.read()

        return self

    def from_content(self, content: str) -> Script:
        """Loads Loadero script from provided str data.

        Args:
            content (str): script

        Returns:
            Script: script loaded from data
        """
        self._content = content

        return self

    def to_json(self) -> str:
        return self.content

    def read(self) -> Script:
        self._params = FileAPI().read(self._params)

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

        Returns:
            FileParams: Read file resource.
        """

        if params.file_id is None:
            raise Exception("FileParams.file_id must be a valid int")

        return params.from_json(
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

        resources = []
        for r in resp["results"]:
            resource = FileParams()
            resources.append(resource.from_json(r))

        return resources

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
