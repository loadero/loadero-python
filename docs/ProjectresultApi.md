# swagger_client.ProjectresultApi

All URIs are relative to *http://api.loadero.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_all_project_results**](ProjectresultApi.md#read_all_project_results) | **GET** /projects/{projectID}/runs/{runID}/results/ | Read all project run results
[**read_project_result**](ProjectresultApi.md#read_project_result) | **GET** /projects/{projectID}/runs/{runID}/results/{resultID}/ | Read single project run result
[**read_project_result_statistics**](ProjectresultApi.md#read_project_result_statistics) | **GET** /projects/{projectID}/runs/{runID}/results/statistics/ | Read all project result statistics

# **read_all_project_results**
> InlineResponse2002 read_all_project_results(run_id, project_id, limit=limit, offset=offset, describe=describe, filter_browser=filter_browser, filter_network=filter_network, filter_location=filter_location, filter_media_type=filter_media_type, filter_video_feed=filter_video_feed, filter_audio_feed=filter_audio_feed, filter_name=filter_name, filter_num_from=filter_num_from, filter_num_to=filter_num_to, filter_group_name=filter_group_name, filter_group_num_from=filter_group_num_from, filter_group_num_to=filter_group_num_to, filter_record_audio=filter_record_audio, filter_start_from=filter_start_from, filter_start_to=filter_start_to, filter_end_from=filter_end_from, filter_end_to=filter_end_to, filter_status=filter_status, filter_selenium_result=filter_selenium_result, filter_done=filter_done)

Read all project run results

This endpoint retrieves all project run results. Project, run must be previously created and run has to be finished in order to get results

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
api_instance = swagger_client.ProjectresultApi(swagger_client.ApiClient(configuration))
run_id = 789 # int | 
project_id = 789 # int | 
limit = 789 # int |  (optional)
offset = 789 # int |  (optional)
describe = 'describe_example' # str |  (optional)
filter_browser = 'filter_browser_example' # str |  (optional)
filter_network = 'filter_network_example' # str |  (optional)
filter_location = 'filter_location_example' # str |  (optional)
filter_media_type = 'filter_media_type_example' # str |  (optional)
filter_video_feed = 'filter_video_feed_example' # str |  (optional)
filter_audio_feed = 'filter_audio_feed_example' # str |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_num_from = 'filter_num_from_example' # str |  (optional)
filter_num_to = 'filter_num_to_example' # str |  (optional)
filter_group_name = 'filter_group_name_example' # str |  (optional)
filter_group_num_from = 'filter_group_num_from_example' # str |  (optional)
filter_group_num_to = 'filter_group_num_to_example' # str |  (optional)
filter_record_audio = 'filter_record_audio_example' # str |  (optional)
filter_start_from = 'filter_start_from_example' # str |  (optional)
filter_start_to = 'filter_start_to_example' # str |  (optional)
filter_end_from = 'filter_end_from_example' # str |  (optional)
filter_end_to = 'filter_end_to_example' # str |  (optional)
filter_status = 'filter_status_example' # str |  (optional)
filter_selenium_result = 'filter_selenium_result_example' # str |  (optional)
filter_done = 'filter_done_example' # str |  (optional)

try:
    # Read all project run results
    api_response = api_instance.read_all_project_results(run_id, project_id, limit=limit, offset=offset, describe=describe, filter_browser=filter_browser, filter_network=filter_network, filter_location=filter_location, filter_media_type=filter_media_type, filter_video_feed=filter_video_feed, filter_audio_feed=filter_audio_feed, filter_name=filter_name, filter_num_from=filter_num_from, filter_num_to=filter_num_to, filter_group_name=filter_group_name, filter_group_num_from=filter_group_num_from, filter_group_num_to=filter_group_num_to, filter_record_audio=filter_record_audio, filter_start_from=filter_start_from, filter_start_to=filter_start_to, filter_end_from=filter_end_from, filter_end_to=filter_end_to, filter_status=filter_status, filter_selenium_result=filter_selenium_result, filter_done=filter_done)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectresultApi->read_all_project_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  | 
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **describe** | **str**|  | [optional] 
 **filter_browser** | **str**|  | [optional] 
 **filter_network** | **str**|  | [optional] 
 **filter_location** | **str**|  | [optional] 
 **filter_media_type** | **str**|  | [optional] 
 **filter_video_feed** | **str**|  | [optional] 
 **filter_audio_feed** | **str**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_num_from** | **str**|  | [optional] 
 **filter_num_to** | **str**|  | [optional] 
 **filter_group_name** | **str**|  | [optional] 
 **filter_group_num_from** | **str**|  | [optional] 
 **filter_group_num_to** | **str**|  | [optional] 
 **filter_record_audio** | **str**|  | [optional] 
 **filter_start_from** | **str**|  | [optional] 
 **filter_start_to** | **str**|  | [optional] 
 **filter_end_from** | **str**|  | [optional] 
 **filter_end_to** | **str**|  | [optional] 
 **filter_status** | **str**|  | [optional] 
 **filter_selenium_result** | **str**|  | [optional] 
 **filter_done** | **str**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_result**
> ExtendedResult read_project_result(result_id, run_id, project_id, describe=describe)

Read single project run result

This endpoint retrieves single project run result info. Project, run and result must be previously created

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
api_instance = swagger_client.ProjectresultApi(swagger_client.ApiClient(configuration))
result_id = 789 # int | 
run_id = 789 # int | 
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Read single project run result
    api_response = api_instance.read_project_result(result_id, run_id, project_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectresultApi->read_project_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **int**|  | 
 **run_id** | **int**|  | 
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**ExtendedResult**](ExtendedResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_result_statistics**
> InlineResponse2003 read_project_result_statistics(run_id, project_id, describe=describe)

Read all project result statistics

This endpoint retrieves all project result statisctics. Project and run must be previously created

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
api_instance = swagger_client.ProjectresultApi(swagger_client.ApiClient(configuration))
run_id = 789 # int | 
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Read all project result statistics
    api_response = api_instance.read_project_result_statistics(run_id, project_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectresultApi->read_project_result_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  | 
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

