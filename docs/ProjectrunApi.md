# swagger_client.ProjectrunApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_all_project_runs**](ProjectrunApi.md#read_all_project_runs) | **GET** /projects/{projectID}/runs/ | Get all existing test runs for project
[**read_project_run**](ProjectrunApi.md#read_project_run) | **GET** /projects/{projectID}/runs/{runID}/ | Read project test run info

# **read_all_project_runs**
> InlineResponse200 read_all_project_runs(project_id, limit=limit, offset=offset, describe=describe, filter_test_name=filter_test_name, filter_started_from=filter_started_from, filter_started_to=filter_started_to, filter_finished_from=filter_finished_from, filter_finished_to=filter_finished_to, filter_execution_started_from=filter_execution_started_from, filter_execution_started_to=filter_execution_started_to, filter_execution_finished_from=filter_execution_finished_from, filter_execution_finished_to=filter_execution_finished_to, filter_increment_strategy=filter_increment_strategy, filter_status=filter_status, filter_metric_status=filter_metric_status, filter_test_mode=filter_test_mode, filter_start_interval_from=filter_start_interval_from, filter_start_interval_to=filter_start_interval_to, filter_participant_timeout_from=filter_participant_timeout_from, filter_participant_timeout_to=filter_participant_timeout_to, filter_active=filter_active, mos_test=mos_test)

Get all existing test runs for project

This endpoint retrieves all test run info. Project must be previously created

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProjectrunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
limit = 789 # int |  (optional)
offset = 789 # int |  (optional)
describe = 'describe_example' # str |  (optional)
filter_test_name = 'filter_test_name_example' # str |  (optional)
filter_started_from = 'filter_started_from_example' # str |  (optional)
filter_started_to = 'filter_started_to_example' # str |  (optional)
filter_finished_from = 'filter_finished_from_example' # str |  (optional)
filter_finished_to = 'filter_finished_to_example' # str |  (optional)
filter_execution_started_from = 'filter_execution_started_from_example' # str |  (optional)
filter_execution_started_to = 'filter_execution_started_to_example' # str |  (optional)
filter_execution_finished_from = 'filter_execution_finished_from_example' # str |  (optional)
filter_execution_finished_to = 'filter_execution_finished_to_example' # str |  (optional)
filter_increment_strategy = 'filter_increment_strategy_example' # str |  (optional)
filter_status = 'filter_status_example' # str |  (optional)
filter_metric_status = 'filter_metric_status_example' # str |  (optional)
filter_test_mode = 'filter_test_mode_example' # str |  (optional)
filter_start_interval_from = 'filter_start_interval_from_example' # str |  (optional)
filter_start_interval_to = 'filter_start_interval_to_example' # str |  (optional)
filter_participant_timeout_from = 'filter_participant_timeout_from_example' # str |  (optional)
filter_participant_timeout_to = 'filter_participant_timeout_to_example' # str |  (optional)
filter_active = 'filter_active_example' # str |  (optional)
mos_test = 'mos_test_example' # str |  (optional)

try:
    # Get all existing test runs for project
    api_response = api_instance.read_all_project_runs(project_id, limit=limit, offset=offset, describe=describe, filter_test_name=filter_test_name, filter_started_from=filter_started_from, filter_started_to=filter_started_to, filter_finished_from=filter_finished_from, filter_finished_to=filter_finished_to, filter_execution_started_from=filter_execution_started_from, filter_execution_started_to=filter_execution_started_to, filter_execution_finished_from=filter_execution_finished_from, filter_execution_finished_to=filter_execution_finished_to, filter_increment_strategy=filter_increment_strategy, filter_status=filter_status, filter_metric_status=filter_metric_status, filter_test_mode=filter_test_mode, filter_start_interval_from=filter_start_interval_from, filter_start_interval_to=filter_start_interval_to, filter_participant_timeout_from=filter_participant_timeout_from, filter_participant_timeout_to=filter_participant_timeout_to, filter_active=filter_active, mos_test=mos_test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectrunApi->read_all_project_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **describe** | **str**|  | [optional] 
 **filter_test_name** | **str**|  | [optional] 
 **filter_started_from** | **str**|  | [optional] 
 **filter_started_to** | **str**|  | [optional] 
 **filter_finished_from** | **str**|  | [optional] 
 **filter_finished_to** | **str**|  | [optional] 
 **filter_execution_started_from** | **str**|  | [optional] 
 **filter_execution_started_to** | **str**|  | [optional] 
 **filter_execution_finished_from** | **str**|  | [optional] 
 **filter_execution_finished_to** | **str**|  | [optional] 
 **filter_increment_strategy** | **str**|  | [optional] 
 **filter_status** | **str**|  | [optional] 
 **filter_metric_status** | **str**|  | [optional] 
 **filter_test_mode** | **str**|  | [optional] 
 **filter_start_interval_from** | **str**|  | [optional] 
 **filter_start_interval_to** | **str**|  | [optional] 
 **filter_participant_timeout_from** | **str**|  | [optional] 
 **filter_participant_timeout_to** | **str**|  | [optional] 
 **filter_active** | **str**|  | [optional] 
 **mos_test** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_run**
> RunBody read_project_run(project_id, run_id)

Read project test run info

This endpoint retrieves project test run info. Project and run must be previously created

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProjectrunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
run_id = 789 # int | 

try:
    # Read project test run info
    api_response = api_instance.read_project_run(project_id, run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectrunApi->read_project_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **run_id** | **int**|  | 

### Return type

[**RunBody**](RunBody.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

