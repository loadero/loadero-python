# coding: utf-8

"""
Loadero script resource.
"""

from __future__ import annotations


class Script:
    """
    Script describes a single Loadero test Script.
    Script can be created from str data or loaded from file.
    """

    _data = None

    def __init__(
        self, script_data: str or None = None, script_file: str or None = None
    ) -> None:
        if script_data is not None:
            self._data = script_data
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

    def from_data(self, script_data: str) -> Script:
        """Loads Loadero script from provides str data.

        Args:
            script_data (str): script

        Returns:
            Script: script loaded from data
        """
        self._data = script_data

        return self

    def _load_from_file(self, script_file: str) -> Script:
        with open(script_file, "r") as f:
            self._data = f.read()

        return self

    @property
    def script(self) -> str:
        return self._data
