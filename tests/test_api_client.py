"""API client tests"""

import pytest
import httpretty
from loadero_python.api_client import APIClient
from . import identifiers


# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=missing-class-docstring


@pytest.fixture
def api():
    httpretty.enable(allow_net_connect=False, verbose=True)
    APIClient(
        project_id=identifiers.project_id,
        access_token=identifiers.access_token,
        api_base=identifiers.api_base,
    )

    yield


class TestAPIClient:
    def test_init_no_args(self):
        with pytest.raises(Exception):
            APIClient()

    def test_init_no_access_token(self):
        with pytest.raises(Exception):
            APIClient(project_id=identifiers.project_id)

    def test_init_no_project_id(self):
        with pytest.raises(Exception):
            APIClient(access_token=identifiers.access_token)

    def test_init_valid(self):
        APIClient(
            project_id=identifiers.project_id,
            access_token=identifiers.access_token,
            api_base=identifiers.api_base,
        )

        APIClient()

    def test_api_client_api_base(self, api):
        assert APIClient().api_base == identifiers.api_base

    def test_api_client_access_token(self, api):
        assert APIClient().access_token == identifiers.access_token

    def test_api_client_project_id(self, api):
        assert APIClient().project_id == identifiers.project_id

    def test_api_client_headers(self, api):
        assert APIClient().headers == {
            "Authorization": "LoaderoAuth " + identifiers.access_token,
            "Content-Type": "application/json",
        }


class TestAPIClientGet:
    def test_valid(self, api):
        httpretty.register_uri(
            httpretty.GET,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body='{"hello":"world"}',
        )

        assert APIClient().get("route/") == {"hello": "world"}

        assert dict(httpretty.last_request().headers) == {
            "Accept-Encoding": "identity",
            "Authorization": "LoaderoAuth LOADERO_PROJECT_ACCESS_TOKEN",
            "Content-Type": "application/json",
            "Host": "mock.loadero.api",
            "User-Agent": "python-urllib3/1.26.9",
        }

    def test_invalid_headers(self, api):
        httpretty.register_uri(
            httpretty.GET,
            identifiers.api_base + "route/",
        )

        with pytest.raises(Exception):
            APIClient().get("route/")

    def test_non_success_resp(self, api):
        httpretty.register_uri(
            httpretty.GET,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().get("route/")

    def test_empty_response(self, api):
        httpretty.register_uri(
            httpretty.GET,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().get("route/") is None


class TestAPIClientPost:
    def test_valid(self, api):
        httpretty.register_uri(
            httpretty.POST,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body='{"api":"resp"}',
        )

        assert APIClient().post("route/", {"hello": "world"}) == {"api": "resp"}

        assert dict(httpretty.last_request().headers) == {
            "Accept-Encoding": "identity",
            "Authorization": "LoaderoAuth LOADERO_PROJECT_ACCESS_TOKEN",
            "Content-Type": "application/json",
            "Host": "mock.loadero.api",
            "User-Agent": "python-urllib3/1.26.9",
            "Content-Length": "18",
        }

        assert httpretty.last_request().body == b'{"hello": "world"}'

    def test_invalid_headers(self, api):
        httpretty.register_uri(
            httpretty.POST,
            identifiers.api_base + "route/",
        )

        with pytest.raises(Exception):
            APIClient().post("route/", {"hello": "world"})

    def test_non_success_resp(self, api):
        httpretty.register_uri(
            httpretty.POST,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().post("route/", {"hello": "world"})

    def test_empty_response(self, api):
        httpretty.register_uri(
            httpretty.POST,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().post("route/", {"hello": "world"}) is None


class TestAPIPut:
    def test_valid(self, api):
        httpretty.register_uri(
            httpretty.PUT,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body='{"api":"resp"}',
        )

        assert APIClient().put("route/", {"hello": "world"}) == {"api": "resp"}

        assert dict(httpretty.last_request().headers) == {
            "Accept-Encoding": "identity",
            "Authorization": "LoaderoAuth LOADERO_PROJECT_ACCESS_TOKEN",
            "Content-Type": "application/json",
            "Host": "mock.loadero.api",
            "User-Agent": "python-urllib3/1.26.9",
            "Content-Length": "18",
        }

        assert httpretty.last_request().body == b'{"hello": "world"}'

    def test_invalid_uri(self, api):
        httpretty.register_uri(
            httpretty.PUT,
            identifiers.api_base + "route/",
        )

        with pytest.raises(Exception):
            APIClient().put("route/", {"hello": "world"})

    def test_non_success_resp(self, api):
        httpretty.register_uri(
            httpretty.PUT,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().put("route/", {"hello": "world"})

    def test_empty_response(self, api):
        httpretty.register_uri(
            httpretty.PUT,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            body="",
        )

        assert APIClient().put("route/", {"hello": "world"}) is None


class TestAPIDelete:
    def test_valid(self, api):
        httpretty.register_uri(
            httpretty.DELETE,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
        )

        assert APIClient().delete("route/") is None

        assert dict(httpretty.last_request().headers) == {
            "Accept-Encoding": "identity",
            "Authorization": "LoaderoAuth LOADERO_PROJECT_ACCESS_TOKEN",
            "Content-Type": "application/json",
            "Host": "mock.loadero.api",
            "User-Agent": "python-urllib3/1.26.9",
        }

    def test_non_success_resp(self, api):
        httpretty.register_uri(
            httpretty.DELETE,
            identifiers.api_base + "route/",
            forcing_headers={"Content-Type": "application/json"},
            status=500,
        )

        with pytest.raises(Exception):
            APIClient().delete("route/")
