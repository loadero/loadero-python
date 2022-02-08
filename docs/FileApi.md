# swagger_client.FileApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_file**](FileApi.md#read_file) | **GET** /projects/{projectID}/files/{fileID}/ | Read file info.

# **read_file**
> File read_file(file_id, project_id, describe=describe)

Read file info.

This endpoint retrieves file info.

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
api_instance = swagger_client.FileApi(swagger_client.ApiClient(configuration))
file_id = 789 # int | 
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Read file info.
    api_response = api_instance.read_file(file_id, project_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->read_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**File**](File.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

