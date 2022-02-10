# swagger_client.ProjectrunparticipantApi

All URIs are relative to *http://api.loadero.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_all_project_run_participants**](ProjectrunparticipantApi.md#read_all_project_run_participants) | **GET** /projects/{projectID}/runs/{runID}/participants/ | Get all existing project run participants for run
[**read_project_run_participant**](ProjectrunparticipantApi.md#read_project_run_participant) | **GET** /projects/{projectID}/runs/{runID}/participants/{runParticipantID}/ | Get existing project run participant

# **read_all_project_run_participants**
> InlineResponse2001 read_all_project_run_participants(run_id, project_id, limit=limit, offset=offset, describe=describe, filter_browser=filter_browser, filter_network=filter_network, filter_location=filter_location, filter_media_type=filter_media_type, filter_video_feed=filter_video_feed, filter_audio_feed=filter_audio_feed, filter_name=filter_name, filter_num_from=filter_num_from, filter_num_to=filter_num_to, filter_group_name=filter_group_name, filter_group_num_from=filter_group_num_from, filter_group_num_to=filter_group_num_to, filter_record_audio=filter_record_audio)

Get all existing project run participants for run

This endpoint retrieves all project run participant info.

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
api_instance = swagger_client.ProjectrunparticipantApi(swagger_client.ApiClient(configuration))
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

try:
    # Get all existing project run participants for run
    api_response = api_instance.read_all_project_run_participants(run_id, project_id, limit=limit, offset=offset, describe=describe, filter_browser=filter_browser, filter_network=filter_network, filter_location=filter_location, filter_media_type=filter_media_type, filter_video_feed=filter_video_feed, filter_audio_feed=filter_audio_feed, filter_name=filter_name, filter_num_from=filter_num_from, filter_num_to=filter_num_to, filter_group_name=filter_group_name, filter_group_num_from=filter_group_num_from, filter_group_num_to=filter_group_num_to, filter_record_audio=filter_record_audio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectrunparticipantApi->read_all_project_run_participants: %s\n" % e)
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

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_run_participant**
> RunParticipantBody read_project_run_participant(run_participant_id, run_id, project_id)

Get existing project run participant

This endpoint retrieves project run participant info. Run, run participant must be previously created

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
api_instance = swagger_client.ProjectrunparticipantApi(swagger_client.ApiClient(configuration))
run_participant_id = 789 # int | 
run_id = 789 # int | 
project_id = 789 # int | 

try:
    # Get existing project run participant
    api_response = api_instance.read_project_run_participant(run_participant_id, run_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectrunparticipantApi->read_project_run_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_participant_id** | **int**|  | 
 **run_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**RunParticipantBody**](RunParticipantBody.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

