# coding: utf-8

"""
    Loadero Controller

    This application serves main Loadero's endpoints that can be used to manipulate test data and other services  # noqa: E501

    OpenAPI spec version: {{ .Version }}
    Contact: support@loadero.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RunparticipantApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def read_all_test_run_participants(self, run_id, test_id, project_id, **kwargs):  # noqa: E501
        """Get all existing test run participants for run  # noqa: E501

        This endpoint retrieves all test run participant info.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_all_test_run_participants(run_id, test_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int run_id: (required)
        :param int test_id: (required)
        :param int project_id: (required)
        :param int limit:
        :param int offset:
        :param str describe:
        :param str filter_browser:
        :param str filter_network:
        :param str filter_location:
        :param str filter_media_type:
        :param str filter_video_feed:
        :param str filter_audio_feed:
        :param str filter_name:
        :param str filter_num_from:
        :param str filter_num_to:
        :param str filter_group_name:
        :param str filter_group_num_from:
        :param str filter_group_num_to:
        :param str filter_record_audio:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_all_test_run_participants_with_http_info(run_id, test_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_all_test_run_participants_with_http_info(run_id, test_id, project_id, **kwargs)  # noqa: E501
            return data

    def read_all_test_run_participants_with_http_info(self, run_id, test_id, project_id, **kwargs):  # noqa: E501
        """Get all existing test run participants for run  # noqa: E501

        This endpoint retrieves all test run participant info.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_all_test_run_participants_with_http_info(run_id, test_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int run_id: (required)
        :param int test_id: (required)
        :param int project_id: (required)
        :param int limit:
        :param int offset:
        :param str describe:
        :param str filter_browser:
        :param str filter_network:
        :param str filter_location:
        :param str filter_media_type:
        :param str filter_video_feed:
        :param str filter_audio_feed:
        :param str filter_name:
        :param str filter_num_from:
        :param str filter_num_to:
        :param str filter_group_name:
        :param str filter_group_num_from:
        :param str filter_group_num_to:
        :param str filter_record_audio:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['run_id', 'test_id', 'project_id', 'limit', 'offset', 'describe', 'filter_browser', 'filter_network', 'filter_location', 'filter_media_type', 'filter_video_feed', 'filter_audio_feed', 'filter_name', 'filter_num_from', 'filter_num_to', 'filter_group_name', 'filter_group_num_from', 'filter_group_num_to', 'filter_record_audio']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_all_test_run_participants" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'run_id' is set
        if ('run_id' not in params or
                params['run_id'] is None):
            raise ValueError("Missing the required parameter `run_id` when calling `read_all_test_run_participants`")  # noqa: E501
        # verify the required parameter 'test_id' is set
        if ('test_id' not in params or
                params['test_id'] is None):
            raise ValueError("Missing the required parameter `test_id` when calling `read_all_test_run_participants`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `read_all_test_run_participants`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'run_id' in params:
            path_params['runID'] = params['run_id']  # noqa: E501
        if 'test_id' in params:
            path_params['testID'] = params['test_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'describe' in params:
            query_params.append(('describe', params['describe']))  # noqa: E501
        if 'filter_browser' in params:
            query_params.append(('filter_browser', params['filter_browser']))  # noqa: E501
        if 'filter_network' in params:
            query_params.append(('filter_network', params['filter_network']))  # noqa: E501
        if 'filter_location' in params:
            query_params.append(('filter_location', params['filter_location']))  # noqa: E501
        if 'filter_media_type' in params:
            query_params.append(('filter_media_type', params['filter_media_type']))  # noqa: E501
        if 'filter_video_feed' in params:
            query_params.append(('filter_video_feed', params['filter_video_feed']))  # noqa: E501
        if 'filter_audio_feed' in params:
            query_params.append(('filter_audio_feed', params['filter_audio_feed']))  # noqa: E501
        if 'filter_name' in params:
            query_params.append(('filter_name', params['filter_name']))  # noqa: E501
        if 'filter_num_from' in params:
            query_params.append(('filter_num_from', params['filter_num_from']))  # noqa: E501
        if 'filter_num_to' in params:
            query_params.append(('filter_num_to', params['filter_num_to']))  # noqa: E501
        if 'filter_group_name' in params:
            query_params.append(('filter_group_name', params['filter_group_name']))  # noqa: E501
        if 'filter_group_num_from' in params:
            query_params.append(('filter_group_num_from', params['filter_group_num_from']))  # noqa: E501
        if 'filter_group_num_to' in params:
            query_params.append(('filter_group_num_to', params['filter_group_num_to']))  # noqa: E501
        if 'filter_record_audio' in params:
            query_params.append(('filter_record_audio', params['filter_record_audio']))  # noqa: E501

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
            '/projects/{projectID}/tests/{testID}/runs/{runID}/participants/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_test_run_participant(self, run_participant_id, run_id, test_id, project_id, **kwargs):  # noqa: E501
        """Get existing test run participant  # noqa: E501

        This endpoint retrieves test run participant info. Run, run participant must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_test_run_participant(run_participant_id, run_id, test_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int run_participant_id: (required)
        :param int run_id: (required)
        :param int test_id: (required)
        :param int project_id: (required)
        :param str describe:
        :return: RunParticipantBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_test_run_participant_with_http_info(run_participant_id, run_id, test_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_test_run_participant_with_http_info(run_participant_id, run_id, test_id, project_id, **kwargs)  # noqa: E501
            return data

    def read_test_run_participant_with_http_info(self, run_participant_id, run_id, test_id, project_id, **kwargs):  # noqa: E501
        """Get existing test run participant  # noqa: E501

        This endpoint retrieves test run participant info. Run, run participant must be previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_test_run_participant_with_http_info(run_participant_id, run_id, test_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int run_participant_id: (required)
        :param int run_id: (required)
        :param int test_id: (required)
        :param int project_id: (required)
        :param str describe:
        :return: RunParticipantBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['run_participant_id', 'run_id', 'test_id', 'project_id', 'describe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_test_run_participant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'run_participant_id' is set
        if ('run_participant_id' not in params or
                params['run_participant_id'] is None):
            raise ValueError("Missing the required parameter `run_participant_id` when calling `read_test_run_participant`")  # noqa: E501
        # verify the required parameter 'run_id' is set
        if ('run_id' not in params or
                params['run_id'] is None):
            raise ValueError("Missing the required parameter `run_id` when calling `read_test_run_participant`")  # noqa: E501
        # verify the required parameter 'test_id' is set
        if ('test_id' not in params or
                params['test_id'] is None):
            raise ValueError("Missing the required parameter `test_id` when calling `read_test_run_participant`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `read_test_run_participant`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'run_participant_id' in params:
            path_params['runParticipantID'] = params['run_participant_id']  # noqa: E501
        if 'run_id' in params:
            path_params['runID'] = params['run_id']  # noqa: E501
        if 'test_id' in params:
            path_params['testID'] = params['test_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501

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
            '/projects/{projectID}/tests/{testID}/runs/{runID}/participants/{runParticipantID}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunParticipantBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
