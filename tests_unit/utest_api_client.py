"""API client tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-variable


import time
import pytest
import httpretty
from loadero_python.api_client import APIClient
from . import common


def dict_includes(want: dict, got: dict) -> None:
    for k, v in want.items():
        assert v == got[k]


@pytest.fixture(scope="class")
def api():
    httpretty.enable(allow_net_connect=False, verbose=True)

    APIClient(
        project_id=common.PROJECT_ID,
        access_token=common.ACCESS_TOKEN,
        api_base=common.API_BASE,
        rate_limit=False,
    )

    yield

    httpretty.disable()


@pytest.fixture(scope="function")
def reset():
    httpretty.reset()
    yield


@pytest.mark.usefixtures("api", "reset")
class UTestAPIClient:
    @staticmethod
    def utest_init_no_access_token():
        with pytest.raises(Exception):
            APIClient(project_id=common.PROJECT_ID)

    @staticmethod
    def utest_init_no_project_id():
        with pytest.raises(Exception):
            APIClient(access_token=common.ACCESS_TOKEN)

    @staticmethod
    def utest_init_valid():
        APIClient(
            project_id=common.PROJECT_ID,
            access_token=common.ACCESS_TOKEN,
            api_base=common.API_BASE,
        )

        APIClient()

    @staticmethod
    def utest_repeated_init():
        APIClient(
            project_id=432532334,
            access_token="changed_token",
            api_base="changer_api_base",
        )

        assert APIClient().api_base == "changer_api_base"
        assert APIClient().access_token == "changed_token"
        assert APIClient().project_id == 432532334

        APIClient(
            project_id=common.PROJECT_ID,
            access_token=common.ACCESS_TOKEN,
            api_base=common.API_BASE,
        )

        assert APIClient().api_base == common.API_BASE
        assert APIClient().access_token == common.ACCESS_TOKEN
        assert APIClient().project_id == common.PROJECT_ID

    @staticmethod
    def utest_api_client_api_base():
        assert APIClient().api_base == common.API_BASE

    @staticmethod
    def utest_api_client_access_token():
        assert APIClient().access_token == common.ACCESS_TOKEN

    @staticmethod
    def utest_api_client_project_id():
        assert APIClient().project_id == common.PROJECT_ID

    @staticmethod
    def utest_api_client_auth_header():
        dict_includes(
            {"Authorization": "LoaderoAuth " + common.ACCESS_TOKEN},
            APIClient().auth_header,
        )


@pytest.mark.usefixtures("api", "reset")
class UTestAPIClientGet:
    @staticmethod
    def utest_valid():
        httpretty.register_uri(
            httpretty.GET,
            common.API_BASE + "route/",
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

    @staticmethod
    def utest_invalid_headers():
        httpretty.register_uri(
            httpretty.GET,
            common.API_BASE + "route/",
        )

        with pytest.raises(Exception):
            APIClient().get("route/")

    @staticmethod
    def utest_non_success_resp():
        httpretty.register_uri(
            httpretty.GET,
            common.API_BASE + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().get("route/")

    @staticmethod
    def utest_empty_response():
        httpretty.register_uri(
            httpretty.GET,
            common.API_BASE + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().get("route/") is None


@pytest.mark.usefixtures("api", "reset")
class UTestAPIClientPost:
    @staticmethod
    def utest_valid():
        httpretty.register_uri(
            httpretty.POST,
            common.API_BASE + "route/",
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

    @staticmethod
    def utest_invalid_headers():
        httpretty.register_uri(
            httpretty.POST,
            common.API_BASE + "route/",
        )

        with pytest.raises(Exception):
            APIClient().post("route/", {"hello": "world"})

    @staticmethod
    def utest_non_success_resp():
        httpretty.register_uri(
            httpretty.POST,
            common.API_BASE + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().post("route/", {"hello": "world"})

    @staticmethod
    def utest_empty_response():
        httpretty.register_uri(
            httpretty.POST,
            common.API_BASE + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().post("route/", {"hello": "world"}) is None


@pytest.mark.usefixtures("api", "reset")
class UTestAPIPut:
    @staticmethod
    def utest_valid():
        httpretty.register_uri(
            httpretty.PUT,
            common.API_BASE + "route/",
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

    @staticmethod
    def utest_invalid_headers():
        httpretty.register_uri(
            httpretty.PUT,
            common.API_BASE + "route/",
        )

        with pytest.raises(Exception):
            APIClient().put("route/", {"hello": "world"})

    @staticmethod
    def utest_non_success_resp():
        httpretty.register_uri(
            httpretty.PUT,
            common.API_BASE + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().put("route/", {"hello": "world"})

    @staticmethod
    def utest_empty_response():
        httpretty.register_uri(
            httpretty.PUT,
            common.API_BASE + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().put("route/", {"hello": "world"}) is None


@pytest.mark.usefixtures("api", "reset")
class UTestAPIDelete:
    @staticmethod
    def utest_valid():
        httpretty.register_uri(
            httpretty.DELETE,
            common.API_BASE + "route/",
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

    @staticmethod
    def utest_non_success_resp():
        httpretty.register_uri(
            httpretty.DELETE,
            common.API_BASE + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().delete("route/")


@pytest.mark.usefixtures("api", "reset")
def utest_ratelimit():
    httpretty.register_uri(
        httpretty.GET,
        common.API_BASE + "route/",
        forcing_headers={"Content-Type": "application/json"},
        body='{"hello":"world"}',
    )

    APIClient(
        project_id=common.PROJECT_ID,
        access_token=common.ACCESS_TOKEN,
        api_base=common.API_BASE,
        rate_limit=True,
    )

    start_time = time.time()

    APIClient().get("route/")
    APIClient().get("route/")
    APIClient().get("route/")
    APIClient().get("route/")
    APIClient().get("route/")

    assert time.time() - start_time > 1
