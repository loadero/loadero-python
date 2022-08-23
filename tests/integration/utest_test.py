"""Test resource integration tests.
"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-variable

import os
import pytest
from loadero_python.api_client import APIClient
from loadero_python.resources.classificator import Browser
from loadero_python.resources.participant import ParticipantFilterKey
from loadero_python.resources.project import Project
from loadero_python.resources.resource import QueryParams


@pytest.fixture(scope="module")
def api_client():
    APIClient(
        project_id=int(os.environ.get("PROJECT_ID")),
        access_token=os.environ.get("ACCESS_TOKEN"),
        api_base=os.environ.get("API_BASE"),
    )

    yield


@pytest.mark.usefixtures("api_client")
class UTestTest:
    @staticmethod
    def utest_participants():
        tests, _, _ = Project().tests()
        test = tests[0]

        participants, pagination, filters = test.participants()

        assert len(participants) == 2

        assert pagination.limit == 0
        assert pagination.offset == 0
        assert pagination.page == 1
        assert pagination.total_pages == 1
        assert pagination.total_items == 2

        assert not filters

        participants, pagination, filters = test.participants(
            QueryParams().limit(1)
        )

        assert len(participants) == 1

        assert pagination.limit == 1
        assert pagination.offset == 0
        assert pagination.page == 1
        assert pagination.total_pages == 2
        assert pagination.total_items == 2

        assert not filters

        participants, pagination, filters = test.participants(
            QueryParams().filter(
                ParticipantFilterKey.BROWSER, Browser.B_CHROMELATEST
            )
        )

        assert len(participants) == 1

        assert pagination.limit == 0
        assert pagination.offset == 0
        assert pagination.page == 1
        assert pagination.total_pages == 1
        assert pagination.total_items == 1

        assert filters == {"profile": {"browser": ["chromeLatest"]}}

        participants, pagination, filters = test.participants(
            QueryParams().filter(
                ParticipantFilterKey.BROWSER, Browser.B_FIREFOXLATEST
            )
        )

        assert len(participants) == 1

        assert pagination.limit == 0
        assert pagination.offset == 0
        assert pagination.page == 1
        assert pagination.total_pages == 1
        assert pagination.total_items == 1

        assert filters == {"profile": {"browser": ["firefoxLatest"]}}

        participants, pagination, filters = test.participants(
            QueryParams().filter(
                ParticipantFilterKey.BROWSER,
                Browser.B_CHROMELATEST,
                Browser.B_FIREFOXLATEST,
            )
        )

        assert len(participants) == 2

        assert pagination.limit == 0
        assert pagination.offset == 0
        assert pagination.page == 1
        assert pagination.total_pages == 1
        assert pagination.total_items == 2

        assert filters == {
            "profile": {"browser": ["chromeLatest", "firefoxLatest"]}
        }
