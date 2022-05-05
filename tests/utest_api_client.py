"""API client tests"""


# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=missing-class-docstring


import pytest
import httpretty
from loadero_python.api_client import APIClient
from . import identifiers


def dict_includes(want: dict, got: dict) -> None:
    for k, v in want.items():
        assert v == got[k]


@pytest.fixture
def api():
    httpretty.enable(allow_net_connect=False, verbose=True)
    APIClient(
        project_id=identifiers.project_id,
        access_token=identifiers.access_token,
        api_base=identifiers.api_base,
    )

    yield

    httpretty.disable()


class UTestAPIClient:
    def utest_init_no_args(self):
        with pytest.raises(Exception):
            APIClient()

    def utest_init_no_access_token(self):
        with pytest.raises(Exception):
            APIClient(project_id=identifiers.project_id)

    def utest_init_no_project_id(self):
        with pytest.raises(Exception):
            APIClient(access_token=identifiers.access_token)

    def utest_init_valid(self):
        APIClient(
            project_id=identifiers.project_id,
            access_token=identifiers.access_token,
            api_base=identifiers.api_base,
        )

        APIClient()

    def utest_repeated_init(self):
        APIClient(
            project_id=432532334,
            access_token="changed_token",
            api_base="changer_api_base",
        )

        assert APIClient().api_base == "changer_api_base"
        assert APIClient().access_token == "changed_token"
        assert APIClient().project_id == 432532334

        APIClient(
            project_id=identifiers.project_id,
            access_token=identifiers.access_token,
            api_base=identifiers.api_base,
        )

        assert APIClient().api_base == identifiers.api_base
        assert APIClient().access_token == identifiers.access_token
        assert APIClient().project_id == identifiers.project_id

    def utest_api_client_api_base(self, api):
        assert APIClient().api_base == identifiers.api_base

    def utest_api_client_access_token(self, api):
        assert APIClient().access_token == identifiers.access_token

    def utest_api_client_project_id(self, api):
        assert APIClient().project_id == identifiers.project_id

    def utest_api_client_auth_header(self, api):
        dict_includes(
            {"Authorization": "LoaderoAuth " + identifiers.access_token},
            APIClient().auth_header,
        )


class UTestAPIClientGet:
    def utest_valid(self, api):
        httpretty.register_uri(
            httpretty.GET,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body='{"hello":"world"}',
        )

        assert APIClient().get("route/") == {"hello": "world"}

        dict_includes(
            {
                "Accept-Encoding": "identity",
                "Authorization": "LoaderoAuth LOADERO_PROJECT_ACCESS_TOKEN",
                "Host": "mock.loadero.api",
            },
            dict(httpretty.last_request().headers),
        )

    def utest_invalid_headers(self, api):
        httpretty.register_uri(
            httpretty.GET,
            identifiers.api_base + "route/",
        )

        with pytest.raises(Exception):
            APIClient().get("route/")

    def utest_non_success_resp(self, api):
        httpretty.register_uri(
            httpretty.GET,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().get("route/")

    def utest_empty_response(self, api):
        httpretty.register_uri(
            httpretty.GET,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().get("route/") is None


class UTestAPIClientPost:
    def utest_valid(self, api):
        httpretty.register_uri(
            httpretty.POST,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body='{"api":"resp"}',
        )

        assert APIClient().post("route/", {"hello": "world"}) == {"api": "resp"}

        dict_includes(
            {
                "Accept-Encoding": "identity",
                "Authorization": "LoaderoAuth LOADERO_PROJECT_ACCESS_TOKEN",
                "Content-Type": "application/json",
                "Host": "mock.loadero.api",
            },
            dict(httpretty.last_request().headers),
        )

        assert httpretty.last_request().body == b'{"hello": "world"}'

    def utest_invalid_headers(self, api):
        httpretty.register_uri(
            httpretty.POST,
            identifiers.api_base + "route/",
        )

        with pytest.raises(Exception):
            APIClient().post("route/", {"hello": "world"})

    def utest_non_success_resp(self, api):
        httpretty.register_uri(
            httpretty.POST,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().post("route/", {"hello": "world"})

    def utest_empty_response(self, api):
        httpretty.register_uri(
            httpretty.POST,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().post("route/", {"hello": "world"}) is None


class UTestAPIPut:
    def utest_valid(self, api):
        httpretty.register_uri(
            httpretty.PUT,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body='{"api":"resp"}',
        )

        assert APIClient().put("route/", {"hello": "world"}) == {"api": "resp"}

        dict_includes(
            {
                "Accept-Encoding": "identity",
                "Authorization": "LoaderoAuth LOADERO_PROJECT_ACCESS_TOKEN",
                "Content-Type": "application/json",
                "Host": "mock.loadero.api",
            },
            dict(httpretty.last_request().headers),
        )

        assert httpretty.last_request().body == b'{"hello": "world"}'

    def utest_invalid_headers(self, api):
        httpretty.register_uri(
            httpretty.PUT,
            identifiers.api_base + "route/",
        )

        with pytest.raises(Exception):
            APIClient().put("route/", {"hello": "world"})

    def utest_non_success_resp(self, api):
        httpretty.register_uri(
            httpretty.PUT,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().put("route/", {"hello": "world"})

    def utest_empty_response(self, api):
        httpretty.register_uri(
            httpretty.PUT,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().put("route/", {"hello": "world"}) is None


class UTestAPIDelete:
    def utest_valid(self, api):
        httpretty.register_uri(
            httpretty.DELETE,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
        )

        assert APIClient().delete("route/") is None

        dict_includes(
            {
                "Accept-Encoding": "identity",
                "Authorization": "LoaderoAuth LOADERO_PROJECT_ACCESS_TOKEN",
                "Host": "mock.loadero.api",
            },
            dict(httpretty.last_request().headers),
        )

    def utest_non_success_resp(self, api):
        httpretty.register_uri(
            httpretty.DELETE,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().delete("route/")
