# swagger_client.TestApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test**](TestApi.md#create_test) | **POST** /projects/{projectID}/tests/ | Create new test
[**delete_test**](TestApi.md#delete_test) | **DELETE** /projects/{projectID}/tests/{testID}/ | Delete existing test
[**duplicate_test**](TestApi.md#duplicate_test) | **POST** /projects/{projectID}/tests/{testID}/copy/ | Duplicate existing test
[**read_all_tests**](TestApi.md#read_all_tests) | **GET** /projects/{projectID}/tests/ | Get all existing tests for project
[**read_test**](TestApi.md#read_test) | **GET** /projects/{projectID}/tests/{testID}/ | Read test info
[**update_test**](TestApi.md#update_test) | **PUT** /projects/{projectID}/tests/{testID}/ | Update existing test

# **create_test**
> Test create_test(name, start_interval, participant_timeout, mode, increment_strategy, script, project_id, describe=describe, id=id, created=created, updated=updated, project_id=project_id, script_file_id=script_file_id, deleted=deleted, group_count=group_count, participant_count=participant_count)

Create new test

This endpoint creates new test with given data.

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
api_instance = swagger_client.TestApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
start_interval = 789 # int | 
participant_timeout = 789 # int | 
mode = 'mode_example' # str | 
increment_strategy = 'increment_strategy_example' # str | 
script = 'script_example' # str | 
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)
id = 789 # int | readonly: true (optional)
created = '2013-10-20T19:20:30+01:00' # datetime | readonly: true (optional)
updated = '2013-10-20T19:20:30+01:00' # datetime | readonly: true (optional)
project_id = 789 # int | readonly: true (optional)
script_file_id = 789 # int | readonly: true (optional)
deleted = true # bool | readonly: true (optional)
group_count = 789 # int | readonly: true (optional)
participant_count = 789 # int | readonly: true (optional)

try:
    # Create new test
    api_response = api_instance.create_test(name, start_interval, participant_timeout, mode, increment_strategy, script, project_id, describe=describe, id=id, created=created, updated=updated, project_id=project_id, script_file_id=script_file_id, deleted=deleted, group_count=group_count, participant_count=participant_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->create_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **start_interval** | **int**|  | 
 **participant_timeout** | **int**|  | 
 **mode** | **str**|  | 
 **increment_strategy** | **str**|  | 
 **script** | **str**|  | 
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 
 **id** | **int**| readonly: true | [optional] 
 **created** | **datetime**| readonly: true | [optional] 
 **updated** | **datetime**| readonly: true | [optional] 
 **project_id** | **int**| readonly: true | [optional] 
 **script_file_id** | **int**| readonly: true | [optional] 
 **deleted** | **bool**| readonly: true | [optional] 
 **group_count** | **int**| readonly: true | [optional] 
 **participant_count** | **int**| readonly: true | [optional] 

### Return type

[**Test**](Test.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test**
> delete_test(test_id, project_id)

Delete existing test

This endpoint deletes test. Project and test must be previously created

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
api_instance = swagger_client.TestApi(swagger_client.ApiClient(configuration))
test_id = 789 # int | 
project_id = 789 # int | 

try:
    # Delete existing test
    api_instance.delete_test(test_id, project_id)
except ApiException as e:
    print("Exception when calling TestApi->delete_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **duplicate_test**
> Test duplicate_test(test_id, project_id, body=body, describe=describe)

Duplicate existing test

This endpoint duplicates given test. If no copy name is provided an \"Copy of\" prefix will be applied to the test name. Project and test must be previously created.

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
api_instance = swagger_client.TestApi(swagger_client.ApiClient(configuration))
test_id = 789 # int | 
project_id = 789 # int | 
body = swagger_client.TestIDCopyBody() # TestIDCopyBody |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Duplicate existing test
    api_response = api_instance.duplicate_test(test_id, project_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->duplicate_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**TestIDCopyBody**](TestIDCopyBody.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Test**](Test.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_tests**
> InlineResponse2004 read_all_tests(project_id, limit=limit, offset=offset, describe=describe, filter_name=filter_name, filter_test_mode=filter_test_mode, filter_increment_strategy=filter_increment_strategy, filter_start_interval_from=filter_start_interval_from, filter_start_interval_to=filter_start_interval_to, filter_participant_timeout_from=filter_participant_timeout_from, filter_participant_timeout_to=filter_participant_timeout_to)

Get all existing tests for project

This endpoint retrieves all test info. Project must be previously created

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
api_instance = swagger_client.TestApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
limit = 789 # int |  (optional)
offset = 789 # int |  (optional)
describe = 'describe_example' # str |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_test_mode = 'filter_test_mode_example' # str |  (optional)
filter_increment_strategy = 'filter_increment_strategy_example' # str |  (optional)
filter_start_interval_from = 'filter_start_interval_from_example' # str |  (optional)
filter_start_interval_to = 'filter_start_interval_to_example' # str |  (optional)
filter_participant_timeout_from = 'filter_participant_timeout_from_example' # str |  (optional)
filter_participant_timeout_to = 'filter_participant_timeout_to_example' # str |  (optional)

try:
    # Get all existing tests for project
    api_response = api_instance.read_all_tests(project_id, limit=limit, offset=offset, describe=describe, filter_name=filter_name, filter_test_mode=filter_test_mode, filter_increment_strategy=filter_increment_strategy, filter_start_interval_from=filter_start_interval_from, filter_start_interval_to=filter_start_interval_to, filter_participant_timeout_from=filter_participant_timeout_from, filter_participant_timeout_to=filter_participant_timeout_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->read_all_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **describe** | **str**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_test_mode** | **str**|  | [optional] 
 **filter_increment_strategy** | **str**|  | [optional] 
 **filter_start_interval_from** | **str**|  | [optional] 
 **filter_start_interval_to** | **str**|  | [optional] 
 **filter_participant_timeout_from** | **str**|  | [optional] 
 **filter_participant_timeout_to** | **str**|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_test**
> Test read_test(test_id, project_id, describe=describe)

Read test info

This endpoint retrieves test info. Project and test must be previously created

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
api_instance = swagger_client.TestApi(swagger_client.ApiClient(configuration))
test_id = 789 # int | 
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Read test info
    api_response = api_instance.read_test(test_id, project_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->read_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **int**|  | 
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**Test**](Test.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test**
> Test update_test(name, start_interval, participant_timeout, mode, increment_strategy, script, test_id, project_id, describe=describe, id=id, created=created, updated=updated, project_id=project_id, script_file_id=script_file_id, deleted=deleted, group_count=group_count, participant_count=participant_count)

Update existing test

This endpoint updates test with given properties. Project and test must be previously created

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
api_instance = swagger_client.TestApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
start_interval = 789 # int | 
participant_timeout = 789 # int | 
mode = 'mode_example' # str | 
increment_strategy = 'increment_strategy_example' # str | 
script = 'script_example' # str | 
test_id = 789 # int | 
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)
id = 789 # int | readonly: true (optional)
created = '2013-10-20T19:20:30+01:00' # datetime | readonly: true (optional)
updated = '2013-10-20T19:20:30+01:00' # datetime | readonly: true (optional)
project_id = 789 # int | readonly: true (optional)
script_file_id = 789 # int | readonly: true (optional)
deleted = true # bool | readonly: true (optional)
group_count = 789 # int | readonly: true (optional)
participant_count = 789 # int | readonly: true (optional)

try:
    # Update existing test
    api_response = api_instance.update_test(name, start_interval, participant_timeout, mode, increment_strategy, script, test_id, project_id, describe=describe, id=id, created=created, updated=updated, project_id=project_id, script_file_id=script_file_id, deleted=deleted, group_count=group_count, participant_count=participant_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->update_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **start_interval** | **int**|  | 
 **participant_timeout** | **int**|  | 
 **mode** | **str**|  | 
 **increment_strategy** | **str**|  | 
 **script** | **str**|  | 
 **test_id** | **int**|  | 
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 
 **id** | **int**| readonly: true | [optional] 
 **created** | **datetime**| readonly: true | [optional] 
 **updated** | **datetime**| readonly: true | [optional] 
 **project_id** | **int**| readonly: true | [optional] 
 **script_file_id** | **int**| readonly: true | [optional] 
 **deleted** | **bool**| readonly: true | [optional] 
 **group_count** | **int**| readonly: true | [optional] 
 **participant_count** | **int**| readonly: true | [optional] 

### Return type

[**Test**](Test.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

