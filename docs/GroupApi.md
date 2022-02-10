# swagger_client.GroupApi

All URIs are relative to *http://api.loadero.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupApi.md#create_group) | **POST** /projects/{projectID}/tests/{testID}/groups/ | Create new group.
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /projects/{projectID}/tests/{testID}/groups/{groupID}/ | Delete existing group.
[**duplicate_group**](GroupApi.md#duplicate_group) | **POST** /projects/{projectID}/tests/{testID}/groups/{groupID}/copy/ | Duplicate existing group.
[**read_all_groups**](GroupApi.md#read_all_groups) | **GET** /projects/{projectID}/tests/{testID}/groups/ | Get all existing groups for test.
[**read_group**](GroupApi.md#read_group) | **GET** /projects/{projectID}/tests/{testID}/groups/{groupID}/ | Get existing group.
[**update_group**](GroupApi.md#update_group) | **PUT** /projects/{projectID}/tests/{testID}/groups/{groupID}/ | Update existing group.

# **create_group**
> Group create_group(project_id, test_id, body=body, describe=describe)

Create new group.

This endpoint creates new group with given data.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
body = swagger_client.Group() # Group |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Create new group.
    api_response = api_instance.create_group(project_id, test_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **body** | [**Group**](Group.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id, project_id, test_id)

Delete existing group.

This endpoint deletes group.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 

try:
    # Delete existing group.
    api_instance.delete_group(group_id, project_id, test_id)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
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

# **duplicate_group**
> Group duplicate_group(group_id, project_id, test_id, body=body, describe=describe)

Duplicate existing group.

This endpoint duplicates given group. If no copy name is provided an \"Copy of\" prefix will be applied to the group name.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
body = swagger_client.GroupIDCopyBody() # GroupIDCopyBody |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Duplicate existing group.
    api_response = api_instance.duplicate_group(group_id, project_id, test_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->duplicate_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **body** | [**GroupIDCopyBody**](GroupIDCopyBody.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_groups**
> InlineResponse2007 read_all_groups(project_id, test_id, limit=limit, offset=offset, describe=describe, filter_name=filter_name, filter_count_from=filter_count_from, filter_count_to=filter_count_to)

Get all existing groups for test.

This endpoint retrieves all group info.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
limit = 789 # int |  (optional)
offset = 789 # int |  (optional)
describe = 'describe_example' # str |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_count_from = 'filter_count_from_example' # str |  (optional)
filter_count_to = 'filter_count_to_example' # str |  (optional)

try:
    # Get all existing groups for test.
    api_response = api_instance.read_all_groups(project_id, test_id, limit=limit, offset=offset, describe=describe, filter_name=filter_name, filter_count_from=filter_count_from, filter_count_to=filter_count_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->read_all_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **describe** | **str**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_count_from** | **str**|  | [optional] 
 **filter_count_to** | **str**|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_group**
> Group read_group(group_id, project_id, test_id, describe=describe)

Get existing group.

This endpoint retrieves group info.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Get existing group.
    api_response = api_instance.read_group(group_id, project_id, test_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->read_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(group_id, project_id, test_id, body=body, describe=describe)

Update existing group.

This endpoint updates group with given properties.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
body = swagger_client.Group() # Group |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Update existing group.
    api_response = api_instance.update_group(group_id, project_id, test_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **body** | [**Group**](Group.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

