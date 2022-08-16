"""Loadero project resource.

Project resource is seperated into three parts
    - ProjectParams class describes projects attributes
    - ProjectAPI class groups all API operations related to projects.
    - Project class combines ProjectParams and ProjectAPI.

Single Project object coresponds to single project in Loadero.
"""

from __future__ import annotations
from datetime import datetime
from dateutil import parser

from .pagination import PaginationParams
from ..api_client import APIClient
from .resource import (
    LoaderoResourceParams,
    LoaderoResource,
    QueryParams,
    from_dict_as_new,
    convert_params_list,
)
from .classificator import (
    MemberRole,
    Language,
    Location,
    ComputeUnit,
    Browser,
    PaymentPlan,
    PaymentStatus,
    TestDuration,
)
from .test import Test, TestAPI
from .file import File, FileAPI
from .run import Run, RunAPI


class PlanLimitsParams(LoaderoResourceParams):
    """PlanLimitsParams describes Loadero subscription plan limitations."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "plan_duration": "_plan_duration",
                "max_test_duration": "_max_test_duration",
                "included_test_duration": "_included_test_duration",
                "max_test_cu": "_max_test_cu",
                "max_monthly_cu": "_max_monthly_cu",
                "included_compute_units": "_included_compute_units",
                "mos_enabled": "_mos_enabled",
                "locations": "_locations",
                "compute_units": "_compute_units",
                "browsers": "_browsers",
                "api_access": "_api_access",
                "aws_access": "_aws_access",
                "session_recording_access": "_session_recording_access",
                "assert_preconditions_access": "_assert_preconditions_access",
            },
            custom_deserializers={
                "locations": lambda x: list(map(Location.from_dict, x)),
                "compute_units": lambda x: list(map(ComputeUnit.from_dict, x)),
                "browsers": lambda x: list(map(Browser.from_dict, x)),
            },
        )

        self._plan_duration = None
        self._max_test_duration = None
        self._included_test_duration = None
        self._max_test_cu = None
        self._max_monthly_cu = None
        self._included_compute_units = None
        self._mos_enabled = None
        self._locations = None
        self._compute_units = None
        self._browsers = None
        self._api_access = None
        self._aws_access = None
        self._session_recording_access = None
        self._assert_preconditions_access = None

    # TODO: create a parser for duration.
    @property
    def plan_duration(self) -> str:
        """Plan duration.

        Returns:
            str: Plan duration.
        """

        return self._plan_duration

    @property
    def max_test_duration(self) -> str:
        """Maximum allowed test duration.

        Returns:
            str: Maximum allowed test duration.
        """

        return self._max_test_duration

    @property
    def included_test_duration(self) -> str:
        """Included test duration.

        Returns:
            str: Included test duration.
        """

        return self._included_test_duration

    @property
    def max_test_cu(self) -> int:
        """Maximum allowed test compute unit.

        Returns:
            int: Maximum allowed test compute unit.
        """

        return self._max_test_cu

    @property
    def max_monthly_cu(self) -> int:
        """Maximum allowed compute unit usage per month.

        Returns:
            int: Maximum allowed compute unit usage per month.
        """

        return self._max_monthly_cu

    @property
    def included_compute_units(self) -> int:
        """Included compute units.

        Returns:
            int: Included compute units.
        """

        return self._included_compute_units

    @property
    def mos_enabled(self) -> bool:
        """Are mean opinion score tests enabled.

        Returns:
            bool: Are mean opinion score tests enabled.
        """

        return self._mos_enabled

    @property
    def locations(self) -> list[Location]:
        """Allowed test locations.

        Returns:
            list[Location]: Allowed test locations.
        """

        return self._locations

    @property
    def compute_units(self) -> list[ComputeUnit]:
        """Allowed compute units.

        Returns:
            list[ComputeUnit]: Allowed compute units.
        """

        return self._compute_units

    @property
    def browsers(self) -> list[Browser]:
        """Allowed browsers.

        Returns:
            list[Browser]: Allowed browsers.
        """

        return self._browsers

    @property
    def api_access(self) -> bool:
        """Is API access allowed.

        Returns:
            bool: Is API access allowed.
        """

        return self._api_access

    @property
    def aws_access(self) -> bool:
        """Is AWS access allowed.

        Returns:
            bool: Is AWS access allowed.
        """

        return self._aws_access

    @property
    def session_recording_access(self) -> bool:
        """Is session recording access allowed.

        Returns:
            bool: Is session recording access allowed.
        """

        return self._session_recording_access

    @property
    def assert_preconditions_access(self) -> bool:
        """Is assert preconditions access allowed.

        Returns:
            bool: Is assert preconditions access allowed.
        """

        return self._assert_preconditions_access


class SubscriptionSettingsParams(LoaderoResourceParams):
    """SubscriptionSettingsParams describes Loadero subscription settings."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "max_participant_cu": "_max_participant_cu",
                "max_test_duration": "_max_test_duration",
                "max_monthly_cu": "_max_monthly_cu",
                "max_test_cu": "_max_test_cu",
                "mos_enabled": "_mos_enabled",
            },
            custom_deserializers={
                "max_participant_cu": ComputeUnit.from_dict,
                "max_test_duration": TestDuration.from_dict,
            },
        )

        self._max_participant_cu = None
        self._max_test_duration = None
        self._max_monthly_cu = None
        self._max_test_cu = None
        self._mos_enabled = None

    @property
    def max_participant_cu(self) -> ComputeUnit:
        """Maximum allowed compute unit for a participant.

        Returns:
            ComputeUnit: Maximum allowed compute unit for a participant.
        """

        return self._max_participant_cu

    @property
    def max_test_duration(self) -> TestDuration:
        """Maximum allowed test duration.

        Returns:
            TestDuration: Maximum allowed test duration.
        """

        return self._max_test_duration

    @property
    def max_monthly_cu(self) -> int:
        """Maximum allowed compute unit usage per month.

        Returns:
            int: Maximum allowed compute unit usage per month.
        """

        return self._max_monthly_cu

    @property
    def max_test_cu(self) -> int:
        """Maximum allowed compute unit usage per test.

        Returns:
            int: Maximum allowed compute unit usage per test.
        """

        return self._max_test_cu

    @property
    def mos_enabled(self) -> bool:
        """Are mean opinion score tests enabled.

        Returns:
            bool: Are mean opinion score tests enabled.
        """

        return self._mos_enabled


class SubscriptionParams(LoaderoResourceParams):
    """SubscriptionParams describes Loadero subscription."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "subscription_id": "_subscription_id",
                "created": "_created",
                "updated": "_updated",
                "payment_plan": "_payment_plan",
                "activation_date": "_activation_date",
                "payment_status": "_payment_status",
                "billing_email": "_billing_email",
                "settings": "_settings",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "payment_plan": PaymentPlan.from_dict,
                "activation_date": parser.parse,
                "payment_status": PaymentStatus.from_dict,
                "settings": from_dict_as_new(SubscriptionSettingsParams),
            },
        )

        self._subscription_id = None
        self._created = None
        self._updated = None
        self._payment_plan = None
        self._activation_date = None
        self._payment_status = None
        self._billing_email = None
        self._settings = None

    @property
    def subscription_id(self) -> str:
        """Subscription ID.

        Returns:
            str: Subscription ID.
        """

        return self._subscription_id

    @property
    def created(self) -> datetime:
        """Time when subscription was created.

        Returns:
            datetime: Time when subscription was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when subscription was last updated.

        Returns:
            datetime: Time when subscription was last updated.
        """

        return self._updated

    @property
    def payment_plan(self) -> PaymentPlan:
        """Payment plan of subscription.

        Returns:
            PaymentPlan: Payment plan of subscription.
        """

        return self._payment_plan

    @property
    def activation_date(self) -> datetime:
        """Time when subscription was activated.

        Returns:
            datetime: Time when subscription was activated.
        """

        return self._activation_date

    @property
    def payment_status(self) -> PaymentStatus:
        """Payment status of subscription.

        Returns:
            PaymentStatus: Payment status of subscription.
        """

        return self._payment_status

    @property
    def billing_email(self) -> str:
        """Billing email of subscription.

        Returns:
            str: Billing email of subscription.
        """

        return self._billing_email

    @property
    def settings(self) -> SubscriptionSettingsParams:
        """Subscription settings.

        Returns:
            SubscriptionSettingsParams: Subscription settings.
        """

        return self._settings


class ProjectComputeUnitUsageParams(LoaderoResourceParams):
    """ProjectComputeUnitUsageParams describes compute unit usage for a single
    project.
    """

    def __init__(self):
        super().__init__(
            attribute_map={
                "included": "_included",
                "used": "_used",
            },
        )

        self._included = None
        self._used = None

    @property
    def included(self) -> int:
        """Compute unit included in the project.

        Returns:
            int: Compute unit included in the project.
        """

        return self._included

    @property
    def used(self) -> int:
        """Compute unit used in the project.

        Returns:
            int: Compute unit used in the project.
        """

        return self._used


class ProjectParams(LoaderoResourceParams):
    """ProjectParams represents Loadero project resource attributes."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "id": "_project_id",
                "created": "_created",
                "updated": "_updated",
                "name": "_name",
                "trial_expired": "_trial_expired",
                "member_count": "_member_count",
                "account_role": "_account_role",
                "language": "_language",
                "aws_info_id": "_aws_info_id",
                "subscription_id": "_subscription_id",
                "plan_limits": "_plan_limits",
                "subscription": "_subscription",
                "compute_unit_usage": "_compute_unit_usage",
            },
            custom_deserializers={
                "created": parser.parse,
                "updated": parser.parse,
                "account_role": MemberRole.from_dict,
                "language": Language.from_dict,
                "plan_limits": from_dict_as_new(PlanLimitsParams),
                "subscription": from_dict_as_new(SubscriptionParams),
                "compute_unit_usage": from_dict_as_new(
                    ProjectComputeUnitUsageParams
                ),
            },
        )

        self._project_id = None
        self._created = None
        self._updated = None
        self._name = None
        self._trial_expired = None
        self._member_count = None
        self._account_role = None
        self._language = None
        self._aws_info_id = None
        self._subscription_id = None
        self._plan_limits = None
        self._subscription = None
        self._compute_unit_usage = None

    @property
    def project_id(self) -> str:
        """Project ID.

        Returns:
            str: Project ID.
        """

        return self._project_id

    @property
    def created(self) -> datetime:
        """Time when project was created.

        Returns:
            datetime: Time when project was created.
        """

        return self._created

    @property
    def updated(self) -> datetime:
        """Time when project was last updated.

        Returns:
            datetime: Time when project was last updated.
        """

        return self._updated

    @property
    def name(self) -> str:
        """Project name.

        Returns:
            str: Project name.
        """

        return self._name

    @property
    def trial_expired(self) -> bool:
        """Whether project trial period has expired.

        Returns:
            bool: Whether project trial period has expired.
        """

        return self._trial_expired

    @property
    def member_count(self) -> int:
        """Number of members in the project.

        Returns:
            int: Number of members in the project.
        """

        return self._member_count

    @property
    def account_role(self) -> MemberRole:
        """Account role in the project.

        Returns:
            MemberRole: Account role in the project.
        """

        return self._account_role

    @property
    def language(self) -> Language:
        """Test script programming language.

        Returns:
            Language: Test script programming language.
        """

        return self._language

    @property
    def aws_info_id(self) -> str:
        """AWS info ID.

        Returns:
            str: AWS info ID.
        """

        return self._aws_info_id

    @property
    def subscription_id(self) -> str:
        """Subscription ID.

        Returns:
            str: Subscription ID.
        """

        return self._subscription_id

    @property
    def plan_limits(self) -> PlanLimitsParams:
        """Plan limits.

        Returns:
            PlanLimitsParams: Plan limits.
        """

        return self._plan_limits

    @property
    def subscription(self) -> SubscriptionParams:
        """Subscription.

        Returns:
            SubscriptionParams: Subscription.
        """

        return self._subscription

    @property
    def compute_unit_usage(self) -> ProjectComputeUnitUsageParams:
        """Compute unit usage statistics.

        Returns:
            ProjectComputeUnitUsageParams: Compute unit usage statistics.
        """

        return self._compute_unit_usage


class Project(LoaderoResource):
    """Project class allows read information about the project that the API
    client is configured for. APIClient must be previously initialized with a
    valid Loadero access token.
    """

    def __init__(self):
        self.params = ProjectParams()
        super().__init__(self.params)

    def read(self) -> Project:
        """Reads information about project.

        Raises:
            APIException: If API call fails.

        Returns:
            Assert: Read assert resource.
        """

        self.params = ProjectAPI.read()
        return self

    # pylint: disable=no-self-use
    def tests(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[Test], PaginationParams, dict[any, any]]:
        """Read all tests in the project.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            APIException: If API call fails.

        Returns:
            list[Test]: List of tests.
            PaginationParams: Pagination parameters of request.
            dict[any, any]: Filters applied to in request.
        """

        resp = TestAPI.read_all(query_params=query_params)

        return (
            convert_params_list(Test, resp.results),
            resp.pagination,
            resp.filter,
        )

    # pylint: disable=no-self-use
    def files(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[File], PaginationParams, dict[any, any]]:
        """Read all files in the project.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            APIException: If API call fails.

        Returns:
            list[File]: List of files.
            PaginationParams: Pagination parameters of request.
            dict[any, any]: Filters applied to in request.
        """

        resp = FileAPI.read_all(query_params=query_params)

        return (
            convert_params_list(File, resp.results),
            resp.pagination,
            resp.filter,
        )

    # pylint: disable=no-self-use
    def runs(
        self, query_params: QueryParams or None = None
    ) -> tuple[list[Run], PaginationParams, dict[any, any]]:
        """Read all runs in the project.

        Args:
            query_params (QueryParams, optional): Describes query parameters

        Raises:
            APIException: If API call fails.

        Returns:
            list[Run]: List of runs.
            PaginationParams: Pagination parameters of request.
            dict[any, any]: Filters applied to in request.
        """

        resp = RunAPI.read_all(query_params=query_params)

        return (
            convert_params_list(Run, resp.results),
            resp.pagination,
            resp.filter,
        )


class ProjectAPI:
    """ProjectAPI defines Loadero API operations for project resource."""

    @staticmethod
    def read() -> ProjectParams:
        """Read an existing project resource that the API Client is configured
        too

        Raises:
            APIException: If API call fails.

        Returns:
            ProjectParams: Read project resource params.
        """

        return from_dict_as_new(ProjectParams)(
            APIClient().get(APIClient().project_route)
        )
