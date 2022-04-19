"""
    API client to access Loadero API
"""

import json
import threading
from urllib.parse import urljoin
import urllib3


class APIException(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """


class APIClient:
    """API client to access Loadero API"""

    # TODO: bring /project/id routes inside api client. + figure out what to do
    # about statics routes.

    __pool_size = 4
    __pool_manager = None
    # __headers = {}
    __auth_header = {}

    __initalized = False
    __project_id = None
    __access_token = None
    __api_base = None

    __instance = None
    __lock = threading.Lock()

    def __init__(
        self,
        project_id: int or None = None,
        access_token: str or None = None,
        api_base: str = "https://api.loadero.com/v2/",
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

        self.__auth_header["Authorization"] = (
            "LoaderoAuth " + self.__access_token
        )

        # self.__headers["Authorization"] = "LoaderoAuth " + self.__access_token
        self.__pool_manager = urllib3.PoolManager(num_pools=self.__pool_size)
        # headers=self.__headers,

        self.__initalized = True

    def __new__(cls, *_, **__):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = super(APIClient, cls).__new__(cls)

        return cls.__instance

    def get(self, route: str) -> dict or None:
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

        resp = self.__pool_manager.request(
            method="GET",
            url=urljoin(self.api_base, route),
            headers=self._build_headers(),
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
        encoded_body = json.dumps(body)

        resp = self.__pool_manager.request(
            method="POST",
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

        encoded_body = json.dumps(body)

        resp = self.__pool_manager.request(
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

        resp = self.__pool_manager.request(
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
        return self.__api_base

    @property
    def project_url(self) -> str:
        return self.__api_base + f"projects/{self.project_id}/"

    @property
    def access_token(self) -> str:
        return self.__access_token

    @property
    def project_id(self) -> int:
        return self.__project_id

    @property
    def auth_header(self) -> dict[str, str]:
        return self.__auth_header
