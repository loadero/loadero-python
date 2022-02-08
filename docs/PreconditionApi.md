# swagger_client.PreconditionApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_precondition**](PreconditionApi.md#create_precondition) | **POST** /projects/{projectID}/tests/{testID}/asserts/{assertID}/preconditions/ | Create new assert precondition
[**delete_precondition**](PreconditionApi.md#delete_precondition) | **DELETE** /projects/{projectID}/tests/{testID}/asserts/{assertID}/preconditions/{preconditionID}/ | Delete existing assert precondition
[**read_all_preconditions**](PreconditionApi.md#read_all_preconditions) | **GET** /projects/{projectID}/tests/{testID}/asserts/{assertID}/preconditions/ | Get all existing assert preconditions for assert
[**read_precondition**](PreconditionApi.md#read_precondition) | **GET** /projects/{projectID}/tests/{testID}/asserts/{assertID}/preconditions/{preconditionID}/ | Read assert precondition info
[**update_precondition**](PreconditionApi.md#update_precondition) | **PUT** /projects/{projectID}/tests/{testID}/asserts/{assertID}/preconditions/{preconditionID}/ | Update existing assert precondition

# **create_precondition**
> AssertPrecondition create_precondition(project_id, test_id, assert_id, body=body, describe=describe)

Create new assert precondition

This endpoint creates new assert precondition with given data.

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
api_instance = swagger_client.PreconditionApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
assert_id = 789 # int | 
body = swagger_client.AssertPrecondition() # AssertPrecondition |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Create new assert precondition
    api_response = api_instance.create_precondition(project_id, test_id, assert_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreconditionApi->create_precondition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **assert_id** | **int**|  | 
 **body** | [**AssertPrecondition**](AssertPrecondition.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**AssertPrecondition**](AssertPrecondition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_precondition**
> delete_precondition(precondition_id, project_id, test_id, assert_id)

Delete existing assert precondition

This endpoint deletes assert precondition. Assert and precondition must be previously created

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
api_instance = swagger_client.PreconditionApi(swagger_client.ApiClient(configuration))
precondition_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
assert_id = 789 # int | 

try:
    # Delete existing assert precondition
    api_instance.delete_precondition(precondition_id, project_id, test_id, assert_id)
except ApiException as e:
    print("Exception when calling PreconditionApi->delete_precondition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **precondition_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **assert_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_preconditions**
> InlineResponse2006 read_all_preconditions(project_id, test_id, assert_id, limit=limit, offset=offset, describe=describe, filter_property=filter_property, filter_operator=filter_operator, filter_expected=filter_expected)

Get all existing assert preconditions for assert

This endpoint retrieves all assert precodndition info. Assert must be previously created

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
api_instance = swagger_client.PreconditionApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
assert_id = 789 # int | 
limit = 789 # int |  (optional)
offset = 789 # int |  (optional)
describe = 'describe_example' # str |  (optional)
filter_property = 'filter_property_example' # str |  (optional)
filter_operator = 'filter_operator_example' # str |  (optional)
filter_expected = 'filter_expected_example' # str |  (optional)

try:
    # Get all existing assert preconditions for assert
    api_response = api_instance.read_all_preconditions(project_id, test_id, assert_id, limit=limit, offset=offset, describe=describe, filter_property=filter_property, filter_operator=filter_operator, filter_expected=filter_expected)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreconditionApi->read_all_preconditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **assert_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **describe** | **str**|  | [optional] 
 **filter_property** | **str**|  | [optional] 
 **filter_operator** | **str**|  | [optional] 
 **filter_expected** | **str**|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_precondition**
> AssertPrecondition read_precondition(precondition_id, project_id, test_id, assert_id, describe=describe)

Read assert precondition info

This endpoint retrieves assert precondition info. Assert and precondition must be previously created

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
api_instance = swagger_client.PreconditionApi(swagger_client.ApiClient(configuration))
precondition_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
assert_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Read assert precondition info
    api_response = api_instance.read_precondition(precondition_id, project_id, test_id, assert_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreconditionApi->read_precondition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **precondition_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **assert_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**AssertPrecondition**](AssertPrecondition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_precondition**
> AssertPrecondition update_precondition(precondition_id, project_id, test_id, assert_id, body=body, describe=describe)

Update existing assert precondition

This endpoint updates assert precondition with given properties. Assert and precondition must be previously created

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
api_instance = swagger_client.PreconditionApi(swagger_client.ApiClient(configuration))
precondition_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
assert_id = 789 # int | 
body = swagger_client.AssertPrecondition() # AssertPrecondition |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Update existing assert precondition
    api_response = api_instance.update_precondition(precondition_id, project_id, test_id, assert_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreconditionApi->update_precondition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **precondition_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **assert_id** | **int**|  | 
 **body** | [**AssertPrecondition**](AssertPrecondition.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**AssertPrecondition**](AssertPrecondition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

