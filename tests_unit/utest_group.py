"""Group resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member
# pylint: disable=unused-variable


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.group import Group, GroupParams, GroupAPI
from . import common


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE)

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(common.GROUP_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
        body=json.dumps(common.GROUP_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
        body=json.dumps(common.GROUP_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # delete
    httpretty.register_uri(
        httpretty.DELETE,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
    )

    # duplicate
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/groups/\d*/copy/$"
        ),
        body=json.dumps(common.GROUP_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all
    pg = common.PAGED_RESPONSE.copy()
    pg["results"] = [common.GROUP_JSON, common.GROUP_JSON]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all participants in group
    pg = common.PAGED_RESPONSE.copy()
    pg["results"] = [common.PARTICIPANT_JSON, common.PARTICIPANT_JSON]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/groups/\d*/participants/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestGroupParams:
    @staticmethod
    def utest_str():
        assert (
            str(GroupParams().from_dict(common.GROUP_JSON))
            == """{
    "id": 34421,
    "name": "pytest_group",
    "count": 8,
    "test_id": 12734,
    "total_cu_count": 1234,
    "participant_count": 331,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00"
}"""
        )

    @staticmethod
    def utest_created():
        g = GroupParams()
        g.__dict__["_created"] = common.CREATED_TIME
        assert g.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        g = GroupParams()
        g.__dict__["_updated"] = common.UPDATED_TIME
        assert g.updated == common.UPDATED_TIME

    @staticmethod
    def utest_participant_count():
        g = GroupParams()
        g.__dict__["_participant_count"] = 3
        assert g.participant_count == 3

    @staticmethod
    def utest_total_cu_count():
        g = GroupParams()
        g.__dict__["_total_cu_count"] = 4
        assert g.total_cu_count == 4

    @staticmethod
    def utest_builder_id():
        g = GroupParams()
        g.with_id(5)
        assert g.group_id == 5

    @staticmethod
    def utest_builder_name():
        g = GroupParams()
        g.with_name("group")
        assert g.name == "group"

    @staticmethod
    def utest_builder_count():
        g = GroupParams()
        g.with_count(5)
        assert g.count == 5

    @staticmethod
    def utest_builder_test_id():
        g = GroupParams()
        g.in_test(5)
        assert g.test_id == 5


@pytest.mark.usefixtures("mock")
class UTestGroup:
    @staticmethod
    def utest_create():
        common.check_group_params(
            Group(
                params=GroupParams(
                    name="pytest_group", count=8, test_id=common.TEST_ID
                )
            )
            .create()
            .params
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "count": 8,
            "name": "pytest_group",
        }

    @staticmethod
    def utest_read():
        common.check_group_params(
            Group(group_id=common.GROUP_ID, test_id=common.TEST_ID)
            .read()
            .params
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        common.check_group_params(
            Group(
                params=GroupParams(
                    group_id=common.GROUP_ID,
                    test_id=common.TEST_ID,
                    name="pytest group",
                    count=4,
                )
            )
            .update()
            .params
        )

        assert httpretty.last_request().method == httpretty.PUT
        assert httpretty.last_request().parsed_body == {
            "count": 4,
            "name": "pytest group",
        }

    @staticmethod
    def utest_delete():
        Group(
            params=GroupParams(group_id=common.GROUP_ID, test_id=common.TEST_ID)
        ).delete()

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_duplicate():
        common.check_group_params(
            Group(
                params=GroupParams(
                    group_id=common.GROUP_ID, test_id=common.TEST_ID
                )
            )
            .duplicate("duplicate pytest group name")
            .params
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "name": "duplicate pytest group name"
        }

    @staticmethod
    def utest_participants():
        resp = Group(
            params=GroupParams(group_id=common.GROUP_ID, test_id=common.TEST_ID)
        ).participants()

        assert len(resp) == 2

        for ret in resp:
            common.check_participant_params(ret.params)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body


@pytest.mark.usefixtures("mock")
class UTestGroupAPI:
    @staticmethod
    def utest_create():
        common.check_group_params(
            GroupAPI.create(
                GroupParams(
                    name="pytest_group", count=8, test_id=common.TEST_ID
                )
            )
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "count": 8,
            "name": "pytest_group",
        }

    @staticmethod
    def utest_read():
        common.check_group_params(
            GroupAPI.read(
                GroupParams(
                    test_id=common.TEST_ID,
                    group_id=common.GROUP_ID,
                )
            )
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_update():
        common.check_group_params(
            GroupAPI.update(
                GroupParams(
                    group_id=common.GROUP_ID,
                    test_id=common.TEST_ID,
                    name="updated pytest group name",
                    count=1,
                )
            )
        )

        assert httpretty.last_request().method == httpretty.PUT
        assert httpretty.last_request().parsed_body == {
            "count": 1,
            "name": "updated pytest group name",
        }

    @staticmethod
    def utest_delete():
        assert (
            GroupAPI.delete(
                GroupParams(test_id=common.TEST_ID, group_id=common.GROUP_ID)
            )
            is None
        )

        assert httpretty.last_request().method == httpretty.DELETE
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_duplicate():
        common.check_group_params(
            GroupAPI.duplicate(
                GroupParams(
                    group_id=common.GROUP_ID,
                    test_id=common.TEST_ID,
                ),
                "duplicate pytest group name",
            )
        )

        assert httpretty.last_request().method == httpretty.POST
        assert httpretty.last_request().parsed_body == {
            "name": "duplicate pytest group name"
        }

    @staticmethod
    def utest_read_all():
        resp = GroupAPI.read_all(common.TEST_ID)

        assert len(resp) == 2

        for ret in resp:
            common.check_group_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_no_results():
        pg = common.PAGED_RESPONSE.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
            ),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        resp = GroupAPI.read_all(common.TEST_ID)

        assert len(resp) == 0
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_route():
        assert (
            GroupAPI.route(common.TEST_ID, common.GROUP_ID)
            == "projects/538591/tests/12734/groups/34421/"
        )
        assert (
            GroupAPI.route(common.TEST_ID)
            == "projects/538591/tests/12734/groups/"
        )

    @staticmethod
    def utest_validate_identifiers():
        with pytest.raises(ValueError):
            GroupAPI.create(GroupParams())

        with pytest.raises(ValueError):
            GroupAPI.read(GroupParams())

        with pytest.raises(ValueError):
            GroupAPI.read(GroupParams(test_id=common.TEST_ID))

        with pytest.raises(ValueError):
            GroupAPI.update(GroupParams())

        with pytest.raises(ValueError):
            GroupAPI.update(GroupParams(test_id=common.TEST_ID))

        with pytest.raises(ValueError):
            GroupAPI.delete(GroupParams())

        with pytest.raises(ValueError):
            GroupAPI.delete(GroupParams(test_id=common.TEST_ID))

        with pytest.raises(ValueError):
            GroupAPI.duplicate(GroupParams(), "")

        with pytest.raises(ValueError):
            GroupAPI.duplicate(GroupParams(test_id=common.TEST_ID), "")
