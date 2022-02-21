# coding: utf-8

"""
    Loadero test resource
"""

from __future__ import annotations


class Script:

    """Loadero script resource"""

    _data = None

    def __init__(
        self, script_data: str or None = None, script_file: str or None = None
    ) -> None:
        if script_data is not None:
            self._data = script_data

        if script_file is not None:
            self._load_from_file(script_file)

    def from_file(self, script_file: str) -> Script:
        return self._load_from_file(script_file)

    def from_data(self, script_data: str) -> Script:
        self._data = script_data

        return self

    def _load_from_file(self, script_file: str) -> Script:
        with open(script_file, "r") as f:
            self._data = f.read()

        return self

    @property
    def script(self) -> str:
        return self._data
