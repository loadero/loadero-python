"""Pagination resource tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from loadero_python.resources.assert_resource import AssertParams
from loadero_python.resources.pagination import PagedResponse, PaginationParams
from . import common


class UTestPaginationParams:
    @staticmethod
    def utest_attributes():
        common.check_pagination_params(
            PaginationParams().from_dict(common.PAGINATION_JSON)
        )


class UTestPagedResponse:
    @staticmethod
    def utest_attributes():
        prj = common.PAGED_RESPONSE_JSON.copy()
        prj["results"] = [common.ASSERT_JSON, common.ASSERT_JSON]

        pr = PagedResponse(AssertParams).from_dict(prj)

        common.check_pagination_params(pr.pagination)
        assert pr.filter == common.FILTER_JSON

        for a in pr.results:
            common.check_assert_params(a)
