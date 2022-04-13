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
    def file_type(self) -> str or None:  # TODO: change to classificator
        return self._file_type

    @property
    def content(self) -> datetime or None:
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
    """
    Script describes a single Loadero test Script.
    Script can be created from str data or loaded from file.
    """

    # _data = None
    _content = None
    _params = None

    def __init__(
        self,
        script_id: int or None = None,
        content: str or None = None,
        script_file: str or None = None,
    ) -> None:
        """Creates a new Script object.
        If no arguments are provided then a new empty Script object is
        created.
        If content is provided then a new Script object is initalized with the
        provided content.
        If script_file is provided then a new Script object is initalized with
        script content loaded from file specified by script_file.
        If both arguments are provided then script_file argument is ignored and
        a new Script object is created with the provided content.

        Args:
            content (str or None): Defaults to None.
            script_file (str or None): Defaults to None.
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
            return "empty script"

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
    def route(file_id: int) -> str:
        """Build file resource url route.

        Args:
            file_id (int): File resource id.

        Returns:
            str: Route to file resource.
        """
        return APIClient().project_url + f"files/{file_id}/"
