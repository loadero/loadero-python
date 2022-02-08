# swagger_client.ParticipantsApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_participant**](ParticipantsApi.md#create_participant) | **POST** /projects/{projectID}/tests/{testID}/participants/ | Create new participant.
[**delete_participant**](ParticipantsApi.md#delete_participant) | **DELETE** /projects/{projectID}/tests/{testID}/participants/{participantID}/ | Delete existing participant.
[**duplicate_participant**](ParticipantsApi.md#duplicate_participant) | **POST** /projects/{projectID}/tests/{testID}/participants/{participantID}/copy/ | Duplicate existing participant
[**read_all_participants**](ParticipantsApi.md#read_all_participants) | **GET** /projects/{projectID}/tests/{testID}/participants/ | Get all existing participants for test.
[**read_participant**](ParticipantsApi.md#read_participant) | **GET** /projects/{projectID}/tests/{testID}/participants/{participantID}/ | Get existing participant.
[**update_participant**](ParticipantsApi.md#update_participant) | **PUT** /projects/{projectID}/tests/{testID}/participants/{participantID}/ | Update existing participant.

# **create_participant**
> Participant create_participant(project_id, test_id, body=body, describe=describe)

Create new participant.

This endpoint creates new participant with given properties.

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
api_instance = swagger_client.ParticipantsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
body = swagger_client.Participant() # Participant |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Create new participant.
    api_response = api_instance.create_participant(project_id, test_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParticipantsApi->create_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **body** | [**Participant**](Participant.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Participant**](Participant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_participant**
> delete_participant(participant_id, project_id, test_id)

Delete existing participant.

This endpoint deletes participant.

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
api_instance = swagger_client.ParticipantsApi(swagger_client.ApiClient(configuration))
participant_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 

try:
    # Delete existing participant.
    api_instance.delete_participant(participant_id, project_id, test_id)
except ApiException as e:
    print("Exception when calling ParticipantsApi->delete_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_participant**
> Participant duplicate_participant(participant_id, project_id, test_id, body=body, describe=describe)

Duplicate existing participant

This endpoint duplicates given participant. If no copy name is provided an \"Copy of\" prefix will be applied to the participant name. Group and participant must be previously created.

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
api_instance = swagger_client.ParticipantsApi(swagger_client.ApiClient(configuration))
participant_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
body = swagger_client.ParticipantIDCopyBody() # ParticipantIDCopyBody |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Duplicate existing participant
    api_response = api_instance.duplicate_participant(participant_id, project_id, test_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParticipantsApi->duplicate_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **body** | [**ParticipantIDCopyBody**](ParticipantIDCopyBody.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Participant**](Participant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_participants**
> InlineResponse2008 read_all_participants(project_id, test_id, limit=limit, offset=offset, describe=describe, filter_browser=filter_browser, filter_network=filter_network, filter_location=filter_location, filter_media_type=filter_media_type, filter_video_feed=filter_video_feed, filter_audio_feed=filter_audio_feed, filter_name=filter_name, filter_count_from=filter_count_from, filter_count_to=filter_count_to, filter_compute_unit=filter_compute_unit, filter_has_group=filter_has_group, filter_record_audio=filter_record_audio)

Get all existing participants for test.

This endpoint retrieves all participant info.

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
api_instance = swagger_client.ParticipantsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
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
    # Get all existing participants for test.
    api_response = api_instance.read_all_participants(project_id, test_id, limit=limit, offset=offset, describe=describe, filter_browser=filter_browser, filter_network=filter_network, filter_location=filter_location, filter_media_type=filter_media_type, filter_video_feed=filter_video_feed, filter_audio_feed=filter_audio_feed, filter_name=filter_name, filter_count_from=filter_count_from, filter_count_to=filter_count_to, filter_compute_unit=filter_compute_unit, filter_has_group=filter_has_group, filter_record_audio=filter_record_audio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParticipantsApi->read_all_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
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

# **read_participant**
> Participant read_participant(participant_id, project_id, test_id, describe=describe)

Get existing participant.

This endpoint retrieves participant info.

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
api_instance = swagger_client.ParticipantsApi(swagger_client.ApiClient(configuration))
participant_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Get existing participant.
    api_response = api_instance.read_participant(participant_id, project_id, test_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParticipantsApi->read_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**Participant**](Participant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_participant**
> Participant update_participant(participant_id, project_id, test_id, body=body, describe=describe)

Update existing participant.

This endpoint updates participant with given properties.

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
api_instance = swagger_client.ParticipantsApi(swagger_client.ApiClient(configuration))
participant_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
body = swagger_client.Participant() # Participant |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Update existing participant.
    api_response = api_instance.update_participant(participant_id, project_id, test_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParticipantsApi->update_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **body** | [**Participant**](Participant.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Participant**](Participant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

