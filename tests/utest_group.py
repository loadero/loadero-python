"""Group resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.group import Group, GroupParams, GroupAPI
from loadero_python.resources.classificator import (
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
)
from . import common


@pytest.fixture(scope="module")
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.project_id, common.access_token, common.api_base)

    # create
    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(common.group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
        body=json.dumps(common.group_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # update
    upd = common.group_json.copy()
    upd["count"] = 1
    upd["name"] = "updated pytest group name"

    httpretty.register_uri(
        httpretty.PUT,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/\d*/$"
        ),
        body=json.dumps(upd),
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
    dupl = common.group_json.copy()
    dupl["id"] += 1
    dupl["name"] = "duplicate pytest group name"

    httpretty.register_uri(
        httpretty.POST,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/groups/\d*/copy/$"
        ),
        body=json.dumps(dupl),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all
    gpg = common.paged_response.copy()
    g1 = common.group_json.copy()
    g1["id"] += 1

    g2 = common.group_json.copy()
    g2["id"] += 2

    gpg["results"] = [g1, g2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
        ),
        body=json.dumps(gpg),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all participants in group
    ppg = common.paged_response.copy()
    p1 = common.participant_json.copy()
    p1["id"] += 1

    p2 = common.participant_json.copy()
    p2["id"] += 2

    ppg["results"] = [p1, p2]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/"
            r"projects/\d*/tests/\d*/groups/\d*/participants/$"
        ),
        body=json.dumps(ppg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


class UTestGroupParams:
    def utest_str(self):
        g = GroupParams()
        dupl = common.group_json.copy()
        g.from_dict(dupl)

        assert (
            str(g)
            == """{
    "id": 34421,
    "name": "pytest_group",
    "count": 8,
    "test_id": 12734,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00"
}"""
        )

    def utest_created(self):
        g = GroupParams()
        g.__dict__["_created"] = common.created_time
        assert g.created == common.created_time

    def utest_updated(self):
        g = GroupParams()
        g.__dict__["_updated"] = common.updated_time
        assert g.updated == common.updated_time

    def utest_participant_count(self):
        g = GroupParams()
        g.__dict__["_participant_count"] = 3
        assert g.participant_count == 3

    def utest_total_cu_count(self):
        g = GroupParams()
        g.__dict__["_total_cu_count"] = 4
        assert g.total_cu_count == 4

    def utest_builder_id(self):
        g = GroupParams()
        g.with_id(5)
        assert g.group_id == 5

    def utest_builder_name(self):
        g = GroupParams()
        g.with_name("group")
        assert g.name == "group"

    def utest_builder_count(self):
        g = GroupParams()
        g.with_count(5)
        assert g.count == 5

    def utest_builder_test_id(self):
        g = GroupParams()
        g.in_test(5)
        assert g.test_id == 5


@pytest.mark.usefixtures("mock")
class UTestGroup:
    def utest_create(self):
        g = Group(
            params=GroupParams(
                name="pytest_group", count=8, test_id=common.test_id
            )
        )

        g.create()

        assert g.params.test_id == common.test_id
        assert g.params.group_id == common.group_id
        assert g.params.created == common.created_time
        assert g.params.updated == common.updated_time
        assert g.params.name == "pytest_group"
        assert g.params.count == 8
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty

        assert httpretty.last_request().parsed_body == {
            "count": 8,
            "name": "pytest_group",
        }

    def utest_read(self):
        g = Group(group_id=common.group_id, test_id=common.test_id)

        g.read()

        assert g.params.test_id == common.test_id
        assert g.params.group_id == common.group_id
        assert g.params.created == common.created_time
        assert g.params.updated == common.updated_time
        assert g.params.name == "pytest_group"
        assert g.params.count == 8
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty

        assert not httpretty.last_request().parsed_body

    def utest_update(self):
        g = Group(
            params=GroupParams(group_id=common.group_id, test_id=common.test_id)
        )

        g.params.count = 1
        g.params.name = "updated pytest group name"

        g.update()

        assert g.params.test_id == common.test_id
        assert g.params.group_id == common.group_id
        assert g.params.created == common.created_time
        assert g.params.updated == common.updated_time
        assert g.params.name == "updated pytest group name"
        assert g.params.count == 1
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty

        assert httpretty.last_request().parsed_body == {
            "count": 1,
            "name": "updated pytest group name",
        }

    def utest_delete(self):
        g = Group(
            params=GroupParams(group_id=common.group_id, test_id=common.test_id)
        )

        g.delete()

        assert g.params.name is None
        assert g.params.count is None
        assert g.params.test_id == common.test_id
        assert g.params.group_id == common.group_id
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty
        assert g.params.created is None
        assert g.params.updated is None

        assert not httpretty.last_request().parsed_body

    def utest_duplicate(self):
        g = Group(
            params=GroupParams(group_id=common.group_id, test_id=common.test_id)
        )

        dupl = g.duplicate("duplicate pytest group name")

        assert g.params.name is None
        assert g.params.count is None
        assert g.params.test_id == common.test_id
        assert g.params.group_id == common.group_id
        assert g.params.participant_count is None  # omit empty
        assert g.params.total_cu_count is None  # omit empty
        assert g.params.created is None
        assert g.params.updated is None

        assert dupl.params.name == "duplicate pytest group name"
        assert dupl.params.count == 8
        assert dupl.params.test_id == common.test_id
        assert dupl.params.group_id == common.group_id + 1
        assert dupl.params.participant_count is None  # omit empty
        assert dupl.params.total_cu_count is None  # omit empty
        assert dupl.params.created is not None
        assert dupl.params.updated is not None

        assert httpretty.last_request().parsed_body == {
            "name": "duplicate pytest group name"
        }

    def utest_participants(self):
        g = Group(
            params=GroupParams(group_id=common.group_id, test_id=common.test_id)
        )

        resp = g.participants()

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.params.participant_id == common.participant_id + i + 1
            assert ret.params.group_id == common.group_id
            assert ret.params.test_id == common.test_id
            assert ret.params.created == common.created_time
            assert ret.params.updated == common.updated_time
            assert ret.params.count == 3
            assert ret.params.record_audio is False
            assert ret.params.name == "pytest participant"
            assert ret.params.compute_unit is ComputeUnit.CU_G4
            assert ret.params.audio_feed is AudioFeed.AF_SILENCE
            assert ret.params.browser is Browser.B_CHROMELATEST
            assert ret.params.location is Location.L_EU_CENTRAL_1
            assert ret.params.network is Network.N_4G
            assert ret.params.video_feed is VideoFeed.VF_480P_15FPS


@pytest.mark.usefixtures("mock")
class UTestGroupAPI:
    def utest_create(self):
        ret = GroupAPI.create(
            GroupParams(name="pytest_group", count=8, test_id=common.test_id)
        )

        assert ret.name == "pytest_group"
        assert ret.count == 8
        assert ret.test_id == common.test_id
        assert ret.group_id == common.group_id
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time

        assert httpretty.last_request().parsed_body == {
            "count": 8,
            "name": "pytest_group",
        }

    def utest_create_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.create(GroupParams(name="pytest_group", count=8))

    def utest_read(self):
        ret = GroupAPI.read(
            GroupParams(
                test_id=common.test_id,
                group_id=common.group_id,
            )
        )

        assert ret.name == "pytest_group"
        assert ret.count == 8
        assert ret.test_id == common.test_id
        assert ret.group_id == common.group_id
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time

        assert not httpretty.last_request().parsed_body

    def utest_read_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.read(
                GroupParams(
                    name="pytest_group", count=8, test_id=common.test_id
                )
            )

        with pytest.raises(Exception):
            GroupAPI.read(GroupParams(name="pytest_group", count=8, group_id=1))

    def utest_update(self):
        ret = GroupAPI.update(
            GroupParams(
                group_id=common.group_id,
                test_id=common.test_id,
                name="updated pytest group name",
                count=1,
            )
        )

        assert ret.name == "updated pytest group name"
        assert ret.count == 1
        assert ret.test_id == common.test_id
        assert ret.group_id == common.group_id
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time

        assert httpretty.last_request().parsed_body == {
            "count": 1,
            "name": "updated pytest group name",
        }

    def utest_update_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.update(
                GroupParams(
                    name="pytest_group", count=8, test_id=common.test_id
                )
            )

        with pytest.raises(Exception):
            GroupAPI.update(
                GroupParams(name="pytest_group", count=8, group_id=1)
            )

    def utest_delete(self):
        ret = GroupAPI.delete(
            GroupParams(test_id=common.test_id, group_id=common.group_id)
        )

        assert ret is None

        assert not httpretty.last_request().parsed_body

    def utest_delete_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.delete(
                GroupParams(
                    name="pytest_group", count=8, test_id=common.test_id
                )
            )

        with pytest.raises(Exception):
            GroupAPI.delete(
                GroupParams(name="pytest_group", count=8, group_id=1)
            )

    def utest_duplicate(self):
        ret = GroupAPI.duplicate(
            GroupParams(
                group_id=common.group_id,
                test_id=common.test_id,
                name="duplicate pytest group name",
            )
        )

        assert ret.name == "duplicate pytest group name"
        assert ret.count == 8
        assert ret.test_id == common.test_id
        assert ret.group_id == common.group_id + 1
        assert ret.participant_count is None  # omit empty
        assert ret.total_cu_count is None  # omit empty
        assert ret.created == common.created_time
        assert ret.updated == common.updated_time

        assert httpretty.last_request().parsed_body == {
            "name": "duplicate pytest group name"
        }

    def utest_duplicate_invalid_params(self):
        with pytest.raises(Exception):
            GroupAPI.duplicate(
                GroupParams(
                    name="pytest_group", count=8, test_id=common.test_id
                )
            )

        with pytest.raises(Exception):
            GroupAPI.duplicate(
                GroupParams(name="pytest_group", count=8, group_id=1)
            )

    def utest_read_all(self):
        resp = GroupAPI.read_all(common.test_id)

        assert len(resp) == 2

        for i, ret in enumerate(resp):
            assert ret.group_id == common.group_id + i + 1
            assert ret.name == "pytest_group"
            assert ret.count == 8
            assert ret.test_id == common.test_id
            assert ret.participant_count is None  # omit empty
            assert ret.total_cu_count is None  # omit empty
            assert ret.created == common.created_time
            assert ret.updated == common.updated_time

        assert not httpretty.last_request().parsed_body

    def utest_read_all_no_results(self):
        pg = common.paged_response.copy()
        pg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                r"^http://mock\.loadero\.api/v2/projects/\d*/tests/\d*/groups/$"
            ),
            body=json.dumps(pg),
            forcing_headers={"Content-Type": "application/json"},
        )

        resp = GroupAPI.read_all(common.test_id)

        assert len(resp) == 0
        assert not httpretty.last_request().parsed_body

    def utest_route(self):
        assert (
            GroupAPI.route(common.test_id, common.group_id)
            == "http://mock.loadero.api"
            "/v2/projects/538591/tests/12734/groups/34421/"
        )
        assert (
            GroupAPI.route(common.test_id)
            == "http://mock.loadero.api/v2/projects/538591/tests/12734/groups/"
        )
