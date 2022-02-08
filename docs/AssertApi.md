# swagger_client.AssertApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_assert**](AssertApi.md#create_assert) | **POST** /projects/{projectID}/tests/{testID}/asserts/ | Create new assert
[**delete_assert**](AssertApi.md#delete_assert) | **DELETE** /projects/{projectID}/tests/{testID}/asserts/{assertID}/ | Delete existing assert
[**duplicate_assert**](AssertApi.md#duplicate_assert) | **POST** /projects/{projectID}/tests/{testID}/asserts/{assertID}/copy/ | Duplicate existing assert
[**read_all_asserts**](AssertApi.md#read_all_asserts) | **GET** /projects/{projectID}/tests/{testID}/asserts/ | Get all existing asserts for test
[**read_assert**](AssertApi.md#read_assert) | **GET** /projects/{projectID}/tests/{testID}/asserts/{assertID}/ | Read assert info
[**update_assert**](AssertApi.md#update_assert) | **PUT** /projects/{projectID}/tests/{testID}/asserts/{assertID}/ | Update existing assert

# **create_assert**
> ModelAssert create_assert(project_id, test_id, body=body, describe=describe)

Create new assert

This endpoint creates new assert with given data.

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
api_instance = swagger_client.AssertApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
body = swagger_client.ModelAssert() # ModelAssert |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Create new assert
    api_response = api_instance.create_assert(project_id, test_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssertApi->create_assert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **body** | [**ModelAssert**](ModelAssert.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**ModelAssert**](ModelAssert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assert**
> delete_assert(assert_id, project_id, test_id)

Delete existing assert

This endpoint deletes assert. Test and assert must be previously created

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
api_instance = swagger_client.AssertApi(swagger_client.ApiClient(configuration))
assert_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 

try:
    # Delete existing assert
    api_instance.delete_assert(assert_id, project_id, test_id)
except ApiException as e:
    print("Exception when calling AssertApi->delete_assert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assert_id** | **int**|  | 
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

# **duplicate_assert**
> ModelAssert duplicate_assert(assert_id, project_id, test_id, describe=describe)

Duplicate existing assert

This endpoint duplicates given assert. Test and assert must be previously created.

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
api_instance = swagger_client.AssertApi(swagger_client.ApiClient(configuration))
assert_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Duplicate existing assert
    api_response = api_instance.duplicate_assert(assert_id, project_id, test_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssertApi->duplicate_assert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assert_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**ModelAssert**](ModelAssert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_asserts**
> InlineResponse2005 read_all_asserts(project_id, test_id, limit=limit, offset=offset, describe=describe, filter_path=filter_path, filter_operator=filter_operator, filter_expected=filter_expected)

Get all existing asserts for test

This endpoint retrieves all assert info. Test must be previously created

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
api_instance = swagger_client.AssertApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
test_id = 789 # int | 
limit = 789 # int |  (optional)
offset = 789 # int |  (optional)
describe = 'describe_example' # str |  (optional)
filter_path = 'filter_path_example' # str |  (optional)
filter_operator = 'filter_operator_example' # str |  (optional)
filter_expected = 'filter_expected_example' # str |  (optional)

try:
    # Get all existing asserts for test
    api_response = api_instance.read_all_asserts(project_id, test_id, limit=limit, offset=offset, describe=describe, filter_path=filter_path, filter_operator=filter_operator, filter_expected=filter_expected)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssertApi->read_all_asserts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **describe** | **str**|  | [optional] 
 **filter_path** | **str**|  | [optional] 
 **filter_operator** | **str**|  | [optional] 
 **filter_expected** | **str**|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_assert**
> ModelAssert read_assert(assert_id, project_id, test_id, describe=describe)

Read assert info

This endpoint retrieves assert info. Test and assert must be previously created

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
api_instance = swagger_client.AssertApi(swagger_client.ApiClient(configuration))
assert_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Read assert info
    api_response = api_instance.read_assert(assert_id, project_id, test_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssertApi->read_assert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assert_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**ModelAssert**](ModelAssert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assert**
> ModelAssert update_assert(assert_id, project_id, test_id, body=body, describe=describe)

Update existing assert

This endpoint updates assert with given properties. Test and assert must be previously created

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
api_instance = swagger_client.AssertApi(swagger_client.ApiClient(configuration))
assert_id = 789 # int | 
project_id = 789 # int | 
test_id = 789 # int | 
body = swagger_client.ModelAssert() # ModelAssert |  (optional)
describe = 'describe_example' # str |  (optional)

try:
    # Update existing assert
    api_response = api_instance.update_assert(assert_id, project_id, test_id, body=body, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssertApi->update_assert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assert_id** | **int**|  | 
 **project_id** | **int**|  | 
 **test_id** | **int**|  | 
 **body** | [**ModelAssert**](ModelAssert.md)|  | [optional] 
 **describe** | **str**|  | [optional] 

### Return type

[**ModelAssert**](ModelAssert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

