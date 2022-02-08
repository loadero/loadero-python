# swagger_client.GroupparticipantsApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_participant**](GroupparticipantsApi.md#create_group_participant) | **POST** /projects/{projectID}/tests/{testID}/groups/{groupID}/participants/ | Create new group participant.
[**delete_group_participant**](GroupparticipantsApi.md#delete_group_participant) | **DELETE** /projects/{projectID}/tests/{testID}/groups/{groupID}/participants/{participantID}/ | Delete existing group participant.
[**duplicate_group_participant**](GroupparticipantsApi.md#duplicate_group_participant) | **POST** /projects/{projectID}/tests/{testID}/groups/{groupID}/participants/{participantID}/copy/ | Duplicate existing group participant.
[**read_all_group_participants**](GroupparticipantsApi.md#read_all_group_participants) | **GET** /projects/{projectID}/tests/{testID}/groups/{groupID}/participants/ | Get all existing group participants for group.
[**read_group_participant**](GroupparticipantsApi.md#read_group_participant) | **GET** /projects/{projectID}/tests/{testID}/groups/{groupID}/participants/{participantID}/ | Get existing group participant.
[**update_group_participant**](GroupparticipantsApi.md#update_group_participant) | **PUT** /projects/{projectID}/tests/{testID}/groups/{groupID}/participants/{participantID}/ | Update existing group participant.

# **create_group_participant**
> Participant create_group_participant(project_id, test_id, group_id, body=body, describe=describe)

Create new group participant.

This endpoint creates new group participant with given properties.

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
api_instance = swagger_client.GroupparticipantsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
group_id = 789 # int | 
body = swagger_client.GroupParticipant() # GroupParticipant |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Create new group participant.
    api_response = api_instance.create_group_participant(project_id, test_id, group_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupparticipantsApi->create_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **group_id** | **int**|  | 
 **body** | [**GroupParticipant**](GroupParticipant.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Participant**](Participant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_participant**
> delete_group_participant(participant_id, project_id, test_id, group_id)

Delete existing group participant.

This endpoint deletes group participant.

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
api_instance = swagger_client.GroupparticipantsApi(swagger_client.ApiClient(configuration))
participant_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
group_id = 789 # int | 

try:
    # Delete existing group participant.
    api_instance.delete_group_participant(participant_id, project_id, test_id, group_id)
except ApiException as e:
    print("Exception when calling GroupparticipantsApi->delete_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **group_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_group_participant**
> Participant duplicate_group_participant(participant_id, project_id, test_id, group_id, describe=describe)

Duplicate existing group participant.

This endpoint duplicates given group participant. If no copy name is provided an \"Copy of\" prefix will be applied to the participant name.

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
api_instance = swagger_client.GroupparticipantsApi(swagger_client.ApiClient(configuration))
participant_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
group_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Duplicate existing group participant.
    api_response = api_instance.duplicate_group_participant(participant_id, project_id, test_id, group_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupparticipantsApi->duplicate_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **group_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**Participant**](Participant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_group_participants**
> InlineResponse2008 read_all_group_participants(project_id, test_id, group_id, limit=limit, offset=offset, describe=describe, filter_browser=filter_browser, filter_network=filter_network, filter_location=filter_location, filter_media_type=filter_media_type, filter_video_feed=filter_video_feed, filter_audio_feed=filter_audio_feed, filter_name=filter_name, filter_count_from=filter_count_from, filter_count_to=filter_count_to, filter_compute_unit=filter_compute_unit, filter_has_group=filter_has_group, filter_record_audio=filter_record_audio)

Get all existing group participants for group.

This endpoint retrieves all group participant info.

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
api_instance = swagger_client.GroupparticipantsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
group_id = 789 # int | 
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
filter_count_from = 'filter_count_from_example' # str |  (optional)
filter_count_to = 'filter_count_to_example' # str |  (optional)
filter_compute_unit = 'filter_compute_unit_example' # str |  (optional)
filter_has_group = 'filter_has_group_example' # str |  (optional)
filter_record_audio = 'filter_record_audio_example' # str |  (optional)

try:
    # Get all existing group participants for group.
    api_response = api_instance.read_all_group_participants(project_id, test_id, group_id, limit=limit, offset=offset, describe=describe, filter_browser=filter_browser, filter_network=filter_network, filter_location=filter_location, filter_media_type=filter_media_type, filter_video_feed=filter_video_feed, filter_audio_feed=filter_audio_feed, filter_name=filter_name, filter_count_from=filter_count_from, filter_count_to=filter_count_to, filter_compute_unit=filter_compute_unit, filter_has_group=filter_has_group, filter_record_audio=filter_record_audio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupparticipantsApi->read_all_group_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **group_id** | **int**|  | 
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
 **filter_count_from** | **str**|  | [optional] 
 **filter_count_to** | **str**|  | [optional] 
 **filter_compute_unit** | **str**|  | [optional] 
 **filter_has_group** | **str**|  | [optional] 
 **filter_record_audio** | **str**|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_group_participant**
> Participant read_group_participant(participant_id, project_id, test_id, group_id, describe=describe)

Get existing group participant.

This endpoint retrieves group participant info.

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
api_instance = swagger_client.GroupparticipantsApi(swagger_client.ApiClient(configuration))
participant_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
group_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Get existing group participant.
    api_response = api_instance.read_group_participant(participant_id, project_id, test_id, group_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupparticipantsApi->read_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **group_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**Participant**](Participant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_participant**
> Participant update_group_participant(participant_id, project_id, test_id, group_id, body=body, describe=describe)

Update existing group participant.

This endpoint updates group participant with given properties.

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
api_instance = swagger_client.GroupparticipantsApi(swagger_client.ApiClient(configuration))
participant_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
group_id = 789 # int | 
body = swagger_client.GroupParticipant() # GroupParticipant |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Update existing group participant.
    api_response = api_instance.update_group_participant(participant_id, project_id, test_id, group_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupparticipantsApi->update_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **group_id** | **int**|  | 
 **body** | [**GroupParticipant**](GroupParticipant.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Participant**](Participant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

