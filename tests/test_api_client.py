"""API client tests"""

import os
import pytest
import httpretty
from loadero_python.api_client import APIClient


# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name


access_token = os.environ.get("ACCESS_TOKEN", default="LOADERO_ACCESS_TOKEN")
api_base = os.environ.get("API_BASE", default="http://mock.loadero.api/v2/")
project_id = int(os.environ.get("PROJECT_ID", default="45"))


@pytest.fixture
def api():
    httpretty.enable(allow_net_connect=False, verbose=True)
    APIClient(
        project_id=project_id, access_token=access_token, api_base=api_base
    )

    yield

    httpretty.disable()


def test_api_client_init():
    with pytest.raises(Exception):
        APIClient()

    with pytest.raises(Exception):
        APIClient(project_id=project_id)

    APIClient(
        project_id=project_id, access_token=access_token, api_base=api_base
    )


def test_api_client_get(api):
    # invalid headers
    httpretty.register_uri(
        httpretty.GET,
        api_base + "route/",
    )

    with pytest.raises(Exception):
        APIClient().get("route/")

    # non 200 status
    httpretty.register_uri(
        httpretty.GET,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        status=500,
    )

    with pytest.raises(Exception):
        APIClient().get("route/")

    # empty resp
    httpretty.register_uri(
        httpretty.GET,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        body="",
    )

    assert APIClient().get("route/") is None

    # valid
    httpretty.register_uri(
        httpretty.GET,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        body='{"hello":"world"}',
    )

    assert APIClient().get("route/") == {"hello": "world"}


def test_api_client_post(api):
    # invalid headers
    httpretty.register_uri(
        httpretty.POST,
        api_base + "route/",
    )

    with pytest.raises(Exception):
        APIClient().post("route/", {"hello": "world"})

    # non 200 status
    httpretty.register_uri(
        httpretty.POST,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        status=500,
    )

    with pytest.raises(Exception):
        APIClient().post("route/", {"hello": "world"})

    # empty resp
    httpretty.register_uri(
        httpretty.POST,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        body="",
    )

    assert APIClient().post("route/", {"hello": "world"}) is None

    # valid
    httpretty.register_uri(
        httpretty.POST,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        body='{"hello":"world"}',
    )

    assert APIClient().post("route/", {"hello": "world"}) == {"hello": "world"}


def test_api_client_put(api):
    # invalid headers
    httpretty.register_uri(
        httpretty.PUT,
        api_base + "route/",
    )

    with pytest.raises(Exception):
        APIClient().put("route/", {"hello": "world"})

    # non 200 status
    httpretty.register_uri(
        httpretty.PUT,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        status=500,
    )

    with pytest.raises(Exception):
        APIClient().put("route/", {"hello": "world"})

    # empty resp
    httpretty.register_uri(
        httpretty.PUT,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        body="",
    )

    assert APIClient().put("route/", {"hello": "world"}) is None

    # valid
    httpretty.register_uri(
        httpretty.PUT,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        body='{"hello":"world"}',
    )

    assert APIClient().put("route/", {"hello": "world"}) == {"hello": "world"}


def test_api_client_delete(api):
    # non 200 status
    httpretty.register_uri(
        httpretty.DELETE,
        api_base + "route/",
        forcing_headers={"Content-Type": "application/json"},
        status=500,
    )

    with pytest.raises(Exception):
        APIClient().delete("route/")


def test_api_client_api_base(api):
    assert APIClient().api_base == api_base


def test_api_client_access_token(api):
    assert APIClient().access_token == access_token


def test_api_client_project_id(api):
    assert APIClient().project_id == project_id


def test_api_client_headers(api):
    assert APIClient().headers == {
        "Authorization": "LoaderoAuth " + access_token,
        "Content-Type": "application/json",
    }
