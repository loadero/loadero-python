"""Loadero resource pagination.

Pagination describes and provides a way to manage large read all operation
responses
"""

from .resource import LoaderoResourceParams, from_dict_as_list, from_dict_as_new


class PaginationParams(LoaderoResourceParams):
    """PaginationParams describes Loadero pagination attributes."""

    def __init__(self):
        super().__init__(
            attribute_map={
                "limit": "_limit",
                "offset": "_offset",
                "page": "_page",
                "total_pages": "_total_pages",
                "total_items": "_total_items",
            }
        )

        self._limit = None
        self._offset = None
        self._page = None
        self._total_pages = None
        self._total_items = None

    @property
    def limit(self) -> int:
        """Maximum number of items to returned per page.

        Returns:
            int: Maximum number of items to returned per page.
        """

        return self._limit

    @property
    def offset(self) -> int:
        """Offset of the first item to in page.

        Returns:
            int: Offset of the first item to return.
        """

        return self._offset

    @property
    def page(self) -> int:
        """Index of the returned page.

        Returns:
            int: Index of the returned page.
        """

        return self._page

    @property
    def total_pages(self) -> int:
        """Total number of pages.

        Returns:
            int: Total number of pages.
        """

        return self._total_pages

    @property
    def total_items(self) -> int:
        """Total number of items.

        Returns:
            int: Total number of items.
        """

        return self._total_items


class PagedResponse(LoaderoResourceParams):
    """PagedResponse is a generic representation of Loadero read all
    responses."""

    def __init__(self, resource_params_class: type):
        super().__init__(
            attribute_map={
                "pagination": "_pagination",
                "results": "_results",
                "filter": "_filter",
            },
            custom_deserializers={
                "pagination": from_dict_as_new(PaginationParams),
                "results": from_dict_as_list(resource_params_class),
            },
        )

        self._pagination = None
        self._results = None
        self._filter = None

    @property
    def pagination(self) -> PaginationParams:
        """Pagination information of request results.

        Returns:
            PaginationParams: Pagination params.
        """

        return self._pagination

    @property
    def results(self) -> list[LoaderoResourceParams]:
        """Request results.

        Returns:
            list[LoaderoResourceParams]: Results.
        """

        if self._results is None:
            return []

        return self._results

    @property
    def filter(self) -> dict[any, any]:
        """Filters applied in request. Filter keys and values are NOT parsed to
        their python types.

        Returns:
            dict[any, any]: Filters.
        """

        return self._filter
