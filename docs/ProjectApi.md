# swagger_client.ProjectApi

All URIs are relative to *http://api.loadero.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_project**](ProjectApi.md#read_project) | **GET** /projects/{projectID}/ | Get existing project

# **read_project**
> FullProject read_project(project_id, describe=describe)

Get existing project

This endpoint retrieves project info. Project must be previously created

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | 
describe = 'describe_example' # str |  (optional)

try:
    # Get existing project
    api_response = api_instance.read_project(project_id, describe=describe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->read_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **describe** | **str**|  | [optional] 

### Return type

[**FullProject**](FullProject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

