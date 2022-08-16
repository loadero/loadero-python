"""API client to access Loadero API"""

from __future__ import annotations

import json
import threading
import time
from urllib.parse import urljoin
import urllib3


class APIException(Exception):
    """APIException indicates that Loadero API returned an error. This can
    indicate that an invalid request was made or that an internal error
    occurred in the Loadero servers.
    """


# TODO: ADD RATE LIMIT


class APIClient:
    """API client to access Loadero API"""

    __max_pool_size = 4
    __timeout = urllib3.Timeout(total=30.0)
    # __http = None
    __auth_header = {}

    __initalized = False
    __project_id = None
    __access_token = None
    __api_base = None

    __instance = None
    __lock = threading.Lock()
    __last_request_time = None
    __average_rps = 4

    def __init__(
        self,
        project_id: int or None = None,
        access_token: str or None = None,
        api_base: str = "https://api.loadero.com/v2/",
        rate_limit: bool = True,
    ) -> None:
        if self.__initalized and project_id is None and access_token is None:
            return

        if project_id is None:
            raise Exception(
                "APIClient singleton first must be initalized with project id."
            )

        if access_token is None:
            raise Exception(
                "APIClient singleton first must be "
                "initalized with access token."
            )

        self.__project_id = project_id
        self.__access_token = access_token
        self.__api_base = api_base
        self.__do_rate_limit = rate_limit

        self.__auth_header["Authorization"] = (
            "LoaderoAuth " + self.__access_token
        )

        self.__http = urllib3.PoolManager(
            maxsize=APIClient.__max_pool_size,
            timeout=APIClient.__timeout,
            block=True,
        )

        self.__initalized = True

    def __new__(cls, *_, **__):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = super(APIClient, cls).__new__(cls)

        return cls.__instance

    def __rate_limit(self) -> None:
        if not self.__do_rate_limit:
            return

        if self.__last_request_time is None:
            self.__last_request_time = time.time()
            return

        dt = time.time() - self.__last_request_time

        if dt < 1.0 / self.__average_rps:
            time.sleep((1.0 / self.__average_rps) - dt)

        self.__last_request_time = time.time()

    def get(
        self, route: str, query_params: list[tuple[str, any]] or None = None
    ) -> dict or None:
        """Sends a HTTP GET request to Loadero API.

        Args:
            route (str): Loadero API route.

        Raises:
            APIException: When Loadero API returns non application/json content
                response. This should never happen.
            APIException: When Loadero API request fails. Either because of
                client error or server error.

        Returns:
            dict or None: API JSON response decoded as dictionary or None if
                request returned nothing.
        """

        self.__rate_limit()

        resp = self.__http.request(
            method="GET",
            url=urljoin(self.api_base, route),
            headers=self._build_headers(),
            fields=query_params,
        )

        if "application/json" not in resp.headers["Content-Type"]:
            raise APIException(
                "Loadero API returned content type other that "
                f"'application/json': {resp.headers['Content-Type']}"
            )

        if resp.status // 100 != 2:
            raise APIException(f"Loadero API request failed: {resp.data}")

        if len(resp.data) == 0:
            return None

        return json.loads(resp.data)

    def post(self, route: str, body: dict) -> dict or None:
        """Sends a HTTP POST request to Loadero API.

        Args:
            route (str): Loadero API route.
            body (dict): Request JSON body decoded as dictionary.

        Raises:
            APIException: When Loadero API returns non application/json content
                response. This should never happen.
            APIException: When Loadero API request fails. Either because of
                client error or server error.

        Returns:
            dict or None: API JSON response decoded as dictionary or None if
                request returned nothing.
        """

        self.__rate_limit()

        encoded_body = ""
        if body is not None:
            encoded_body = json.dumps(body)

        resp = self.__http.request(
            method="POST",
            url=urljoin(self.api_base, route),
            body=encoded_body,
            headers=self._build_headers({"Content-Type": "application/json"}),
        )

        if resp.status // 100 != 2:
            raise APIException(f"Loadero API request failed: {resp.data}")

        if len(resp.data) == 0:
            return None

        if "application/json" not in resp.headers["Content-Type"]:
            raise APIException(
                "Loadero API returned content type other that "
                f"'application/json': {resp.headers['Content-Type']}"
            )

        return json.loads(resp.data)

    def put(self, route: str, body: dict):
        """Sends a HTTP PUT request to Loadero API.

        Args:
            route (str): Loadero API route.
            body (dict): Request JSON body decoded as dictionary.

        Raises:
            APIException: When Loadero API returns non application/json content
                response. This should never happen.
            APIException: When Loadero API request fails. Either because of
                client error or server error.

        Returns:
            dict or None: API JSON response decoded as dictionary or None if
                request returned nothing.
        """

        self.__rate_limit()

        encoded_body = json.dumps(body)

        resp = self.__http.request(
            method="PUT",
            url=urljoin(self.api_base, route),
            body=encoded_body,
            headers=self._build_headers({"Content-Type": "application/json"}),
        )

        if "application/json" not in resp.headers["Content-Type"]:
            raise APIException(
                "Loadero API returned content type other that "
                f"'application/json': {resp.headers['Content-Type']}"
            )

        if resp.status // 100 != 2:
            raise APIException(f"Loadero API request failed: {resp.data}")

        if len(resp.data) == 0:
            return None

        return json.loads(resp.data)

    def delete(self, route: str) -> None:
        """Sends a HTTP DELETE request to Loadero API.

        Args:
            route (str): Loadero API route.

        Raises:
            APIException: When Loadero API returns non application/json content
                response. This should never happen.
            APIException: When Loadero API request fails. Either because of
                client error or server error.
        """

        self.__rate_limit()

        resp = self.__http.request(
            method="DELETE",
            url=urljoin(self.api_base, route),
            headers=self._build_headers(),
        )

        if resp.status // 100 != 2:
            raise APIException(f"Loadero API request failed: {resp.data}")

    def _build_headers(
        self, headers: dict[str, str] or None = None
    ) -> dict[str, str]:
        """Adds authentication headers common for all requests to request
        specifc headers.

        Args:
            headers (dict[str, str] optional): Request specific headers.
                Defaults to None. If omitted only auth headers are added.

        Returns:
            dict[str, str]: Combination of auth and request specific headers.
        """

        h = {}

        for k, v in self.__auth_header.items():
            h[k] = v

        if headers is None:
            return h

        for k, v in headers.items():
            h[k] = v

        return h

    @property
    def api_base(self) -> str:
        """Returns Loadero API base URL.

        Returns:
            str: Loadero API base URL.
        """

        return self.__api_base

    @property
    def project_route(self) -> str:
        """Returns Loadero API URL to the project that APIClient is configured
        for.

        Returns:
            str: Loadero API URL to the project that APIClient is configured
                for.
        """

        return f"projects/{self.project_id}/"

    @property
    def access_token(self) -> str:
        """Returns Loadero API access token of project.

        Returns:
            str: Loadero API access token of project.
        """

        return self.__access_token

    @property
    def project_id(self) -> int:
        """Returns project ID that the APIClient is configured for.

        Returns:
            int: Project ID that the APIClient is configured for.
        """

        return self.__project_id

    @property
    def auth_header(self) -> dict[str, str]:
        """Returns Loadero API authentication header used for all requests.

        Returns:
            dict[str, str]: Loadero API authentication header used for all
                requests.
        """

        return self.__auth_header
