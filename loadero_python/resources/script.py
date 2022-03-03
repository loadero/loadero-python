# coding: utf-8

"""
Loadero script resource.
Script resource can be created by either suppling the scripts contents directly
or by supplying a filename from which to load the script.
"""

from __future__ import annotations


class Script:
    """
    Script describes a single Loadero test Script.
    Script can be created from str data or loaded from file.
    """

    _data = None

    def __init__(
        self, content: str or None = None, script_file: str or None = None
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

        if content is not None:
            self._data = content
        elif script_file is not None:
            self._load_from_file(script_file)

    def from_file(self, script_file: str) -> Script:
        """Loads Loadero script from file.

        Args:
            script_file (str): file path to script file

        Returns:
            Script: script loaded from file
        """

        return self._load_from_file(script_file)

    def from_data(self, content: str) -> Script:
        """Loads Loadero script from provided str data.

        Args:
            content (str): script

        Returns:
            Script: script loaded from data
        """
        self._data = content

        return self

    def _load_from_file(self, script_file: str) -> Script:
        with open(script_file, "r") as f:
            self._data = f.read()

        return self

    @property
    def script(self) -> str:
        return self._data
