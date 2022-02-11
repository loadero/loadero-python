# coding: utf-8

"""
    Loadero Controller

    This application serves main Loadero's endpoints that can be used to manipulate test data and other services  # noqa: E501

    OpenAPI spec version: v0.38.0
    Contact: support@loadero.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AssertApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_assert(self, project_id, test_id, **kwargs):  # noqa: E501
        """Create new assert  # noqa: E501

        This endpoint creates new assert with given data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_assert(project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: (required)
        :param int test_id: (required)
        :param ModelAssert body:
        :param str describe:
        :return: ModelAssert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_assert_with_http_info(project_id, test_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_assert_with_http_info(project_id, test_id, **kwargs)  # noqa: E501
            return data

    def create_assert_with_http_info(self, project_id, test_id, **kwargs):  # noqa: E501
        """Create new assert  # noqa: E501

        This endpoint creates new assert with given data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_assert_with_http_info(project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: (required)
        :param int test_id: (required)
        :param ModelAssert body:
        :param str describe:
        :return: ModelAssert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'test_id', 'body', 'describe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_assert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `create_assert`")  # noqa: E501
        # verify the required parameter 'test_id' is set
        if ('test_id' not in params or
                params['test_id'] is None):
            raise ValueError("Missing the required parameter `test_id` when calling `create_assert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'test_id' in params:
            path_params['testID'] = params['test_id']  # noqa: E501

        query_params = []
        if 'describe' in params:
            query_params.append(('describe', params['describe']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tests/{testID}/asserts/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelAssert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_assert(self, assert_id, project_id, test_id, **kwargs):  # noqa: E501
        """Delete existing assert  # noqa: E501

        This endpoint deletes assert. Test and assert must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_assert(assert_id, project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assert_id: (required)
        :param int project_id: (required)
        :param int test_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_assert_with_http_info(assert_id, project_id, test_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_assert_with_http_info(assert_id, project_id, test_id, **kwargs)  # noqa: E501
            return data

    def delete_assert_with_http_info(self, assert_id, project_id, test_id, **kwargs):  # noqa: E501
        """Delete existing assert  # noqa: E501

        This endpoint deletes assert. Test and assert must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_assert_with_http_info(assert_id, project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assert_id: (required)
        :param int project_id: (required)
        :param int test_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assert_id', 'project_id', 'test_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_assert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assert_id' is set
        if ('assert_id' not in params or
                params['assert_id'] is None):
            raise ValueError("Missing the required parameter `assert_id` when calling `delete_assert`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `delete_assert`")  # noqa: E501
        # verify the required parameter 'test_id' is set
        if ('test_id' not in params or
                params['test_id'] is None):
            raise ValueError("Missing the required parameter `test_id` when calling `delete_assert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assert_id' in params:
            path_params['assertID'] = params['assert_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'test_id' in params:
            path_params['testID'] = params['test_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tests/{testID}/asserts/{assertID}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def duplicate_assert(self, assert_id, project_id, test_id, **kwargs):  # noqa: E501
        """Duplicate existing assert  # noqa: E501

        This endpoint duplicates given assert. Test and assert must be previously created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.duplicate_assert(assert_id, project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assert_id: (required)
        :param int project_id: (required)
        :param int test_id: (required)
        :param str describe:
        :return: ModelAssert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.duplicate_assert_with_http_info(assert_id, project_id, test_id, **kwargs)  # noqa: E501
        else:
            (data) = self.duplicate_assert_with_http_info(assert_id, project_id, test_id, **kwargs)  # noqa: E501
            return data

    def duplicate_assert_with_http_info(self, assert_id, project_id, test_id, **kwargs):  # noqa: E501
        """Duplicate existing assert  # noqa: E501

        This endpoint duplicates given assert. Test and assert must be previously created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.duplicate_assert_with_http_info(assert_id, project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assert_id: (required)
        :param int project_id: (required)
        :param int test_id: (required)
        :param str describe:
        :return: ModelAssert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assert_id', 'project_id', 'test_id', 'describe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method duplicate_assert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assert_id' is set
        if ('assert_id' not in params or
                params['assert_id'] is None):
            raise ValueError("Missing the required parameter `assert_id` when calling `duplicate_assert`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `duplicate_assert`")  # noqa: E501
        # verify the required parameter 'test_id' is set
        if ('test_id' not in params or
                params['test_id'] is None):
            raise ValueError("Missing the required parameter `test_id` when calling `duplicate_assert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assert_id' in params:
            path_params['assertID'] = params['assert_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'test_id' in params:
            path_params['testID'] = params['test_id']  # noqa: E501

        query_params = []
        if 'describe' in params:
            query_params.append(('describe', params['describe']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tests/{testID}/asserts/{assertID}/copy/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelAssert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_all_asserts(self, project_id, test_id, **kwargs):  # noqa: E501
        """Get all existing asserts for test  # noqa: E501

        This endpoint retrieves all assert info. Test must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_all_asserts(project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: (required)
        :param int test_id: (required)
        :param int limit:
        :param int offset:
        :param str describe:
        :param str filter_path:
        :param str filter_operator:
        :param str filter_expected:
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_all_asserts_with_http_info(project_id, test_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_all_asserts_with_http_info(project_id, test_id, **kwargs)  # noqa: E501
            return data

    def read_all_asserts_with_http_info(self, project_id, test_id, **kwargs):  # noqa: E501
        """Get all existing asserts for test  # noqa: E501

        This endpoint retrieves all assert info. Test must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_all_asserts_with_http_info(project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: (required)
        :param int test_id: (required)
        :param int limit:
        :param int offset:
        :param str describe:
        :param str filter_path:
        :param str filter_operator:
        :param str filter_expected:
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'test_id', 'limit', 'offset', 'describe', 'filter_path', 'filter_operator', 'filter_expected']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_all_asserts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `read_all_asserts`")  # noqa: E501
        # verify the required parameter 'test_id' is set
        if ('test_id' not in params or
                params['test_id'] is None):
            raise ValueError("Missing the required parameter `test_id` when calling `read_all_asserts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'test_id' in params:
            path_params['testID'] = params['test_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'describe' in params:
            query_params.append(('describe', params['describe']))  # noqa: E501
        if 'filter_path' in params:
            query_params.append(('filter_path', params['filter_path']))  # noqa: E501
        if 'filter_operator' in params:
            query_params.append(('filter_operator', params['filter_operator']))  # noqa: E501
        if 'filter_expected' in params:
            query_params.append(('filter_expected', params['filter_expected']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tests/{testID}/asserts/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_assert(self, assert_id, project_id, test_id, **kwargs):  # noqa: E501
        """Read assert info  # noqa: E501

        This endpoint retrieves assert info. Test and assert must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_assert(assert_id, project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assert_id: (required)
        :param int project_id: (required)
        :param int test_id: (required)
        :param str describe:
        :return: ModelAssert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_assert_with_http_info(assert_id, project_id, test_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_assert_with_http_info(assert_id, project_id, test_id, **kwargs)  # noqa: E501
            return data

    def read_assert_with_http_info(self, assert_id, project_id, test_id, **kwargs):  # noqa: E501
        """Read assert info  # noqa: E501

        This endpoint retrieves assert info. Test and assert must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_assert_with_http_info(assert_id, project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assert_id: (required)
        :param int project_id: (required)
        :param int test_id: (required)
        :param str describe:
        :return: ModelAssert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assert_id', 'project_id', 'test_id', 'describe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_assert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assert_id' is set
        if ('assert_id' not in params or
                params['assert_id'] is None):
            raise ValueError("Missing the required parameter `assert_id` when calling `read_assert`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `read_assert`")  # noqa: E501
        # verify the required parameter 'test_id' is set
        if ('test_id' not in params or
                params['test_id'] is None):
            raise ValueError("Missing the required parameter `test_id` when calling `read_assert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assert_id' in params:
            path_params['assertID'] = params['assert_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'test_id' in params:
            path_params['testID'] = params['test_id']  # noqa: E501

        query_params = []
        if 'describe' in params:
            query_params.append(('describe', params['describe']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tests/{testID}/asserts/{assertID}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelAssert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_assert(self, assert_id, project_id, test_id, **kwargs):  # noqa: E501
        """Update existing assert  # noqa: E501

        This endpoint updates assert with given properties. Test and assert must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_assert(assert_id, project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assert_id: (required)
        :param int project_id: (required)
        :param int test_id: (required)
        :param ModelAssert body:
        :param str describe:
        :return: ModelAssert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_assert_with_http_info(assert_id, project_id, test_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_assert_with_http_info(assert_id, project_id, test_id, **kwargs)  # noqa: E501
            return data

    def update_assert_with_http_info(self, assert_id, project_id, test_id, **kwargs):  # noqa: E501
        """Update existing assert  # noqa: E501

        This endpoint updates assert with given properties. Test and assert must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_assert_with_http_info(assert_id, project_id, test_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assert_id: (required)
        :param int project_id: (required)
        :param int test_id: (required)
        :param ModelAssert body:
        :param str describe:
        :return: ModelAssert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assert_id', 'project_id', 'test_id', 'body', 'describe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_assert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assert_id' is set
        if ('assert_id' not in params or
                params['assert_id'] is None):
            raise ValueError("Missing the required parameter `assert_id` when calling `update_assert`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `update_assert`")  # noqa: E501
        # verify the required parameter 'test_id' is set
        if ('test_id' not in params or
                params['test_id'] is None):
            raise ValueError("Missing the required parameter `test_id` when calling `update_assert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assert_id' in params:
            path_params['assertID'] = params['assert_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'test_id' in params:
            path_params['testID'] = params['test_id']  # noqa: E501

        query_params = []
        if 'describe' in params:
            query_params.append(('describe', params['describe']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tests/{testID}/asserts/{assertID}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelAssert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)