# swagger_client.RunApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_run**](RunApi.md#create_test_run) | **POST** /projects/{projectID}/tests/{testID}/runs/ | Create and launch new test run
[**read_all_test_runs**](RunApi.md#read_all_test_runs) | **GET** /projects/{projectID}/tests/{testID}/runs/ | Get all existing test runs for test
[**read_test_run**](RunApi.md#read_test_run) | **GET** /projects/{projectID}/tests/{testID}/runs/{runID}/ | Read test run info
[**stop_test_run**](RunApi.md#stop_test_run) | **POST** /projects/{projectID}/tests/{testID}/runs/{runID}/stop/ | Stop test run

# **create_test_run**
> Run create_test_run(test_id, project_id, describe=describe)

Create and launch new test run

This endpoint starts test execution. Project and test must be previously created

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
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
test_id = 789 # int | 
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Create and launch new test run
    api_response = api_instance.create_test_run(test_id, project_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->create_test_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **int**|  | 
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_test_runs**
> InlineResponse200 read_all_test_runs(test_id, project_id, limit=limit, offset=offset, describe=describe, filter_test_name=filter_test_name, filter_started_from=filter_started_from, filter_started_to=filter_started_to, filter_finished_from=filter_finished_from, filter_finished_to=filter_finished_to, filter_execution_started_from=filter_execution_started_from, filter_execution_started_to=filter_execution_started_to, filter_execution_finished_from=filter_execution_finished_from, filter_execution_finished_to=filter_execution_finished_to, filter_increment_strategy=filter_increment_strategy, filter_status=filter_status, filter_metric_status=filter_metric_status, filter_test_mode=filter_test_mode, filter_start_interval_from=filter_start_interval_from, filter_start_interval_to=filter_start_interval_to, filter_participant_timeout_from=filter_participant_timeout_from, filter_participant_timeout_to=filter_participant_timeout_to, filter_active=filter_active, mos_test=mos_test)

Get all existing test runs for test

This endpoint retrieves all test run info. Project and test must be previously created

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
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
test_id = 789 # int | 
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
    # Get all existing test runs for test
    api_response = api_instance.read_all_test_runs(test_id, project_id, limit=limit, offset=offset, describe=describe, filter_test_name=filter_test_name, filter_started_from=filter_started_from, filter_started_to=filter_started_to, filter_finished_from=filter_finished_from, filter_finished_to=filter_finished_to, filter_execution_started_from=filter_execution_started_from, filter_execution_started_to=filter_execution_started_to, filter_execution_finished_from=filter_execution_finished_from, filter_execution_finished_to=filter_execution_finished_to, filter_increment_strategy=filter_increment_strategy, filter_status=filter_status, filter_metric_status=filter_metric_status, filter_test_mode=filter_test_mode, filter_start_interval_from=filter_start_interval_from, filter_start_interval_to=filter_start_interval_to, filter_participant_timeout_from=filter_participant_timeout_from, filter_participant_timeout_to=filter_participant_timeout_to, filter_active=filter_active, mos_test=mos_test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->read_all_test_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **int**|  | 
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

# **read_test_run**
> RunBody read_test_run(run_id, test_id, project_id, describe=describe)

Read test run info

This endpoint retrieves test run info. Project, test and run must be previously created

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
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
run_id = 789 # int | 
test_id = 789 # int | 
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Read test run info
    api_response = api_instance.read_test_run(run_id, test_id, project_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->read_test_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  | 
 **test_id** | **int**|  | 
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**RunBody**](RunBody.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_test_run**
> stop_test_run(run_id, test_id, project_id)

Stop test run

This endpoint stops test run. Project, test and run must be previously created. Test run needs to be in progress.

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
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
run_id = 789 # int | 
test_id = 789 # int | 
project_id = 789 # int | 

try:
    # Stop test run
    api_instance.stop_test_run(run_id, test_id, project_id)
except ApiException as e:
    print("Exception when calling RunApi->stop_test_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  | 
 **test_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

