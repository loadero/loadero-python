# swagger_client.StaticApi

All URIs are relative to *http://{{ .Host }}/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_all_static_types**](StaticApi.md#read_all_static_types) | **GET** /statics/types/ | Read all static type info
[**read_all_statics**](StaticApi.md#read_all_statics) | **GET** /statics/ | Read all static resource info
[**read_metric_path**](StaticApi.md#read_metric_path) | **GET** /statics/metric_path/ | Read all metric path info
[**read_static_resource**](StaticApi.md#read_static_resource) | **GET** /statics/{resource}/ | Read all specified static resource info

# **read_all_static_types**
> list[str] read_all_static_types()

Read all static type info

This endpoint retrieves all static type info

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
api_instance = swagger_client.StaticApi(swagger_client.ApiClient(configuration))

try:
    # Read all static type info
    api_response = api_instance.read_all_static_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticApi->read_all_static_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_statics**
> dict(str, list[BaseClassificator]) read_all_statics()

Read all static resource info

This endpoint retrieves all static resource info

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
api_instance = swagger_client.StaticApi(swagger_client.ApiClient(configuration))

try:
    # Read all static resource info
    api_response = api_instance.read_all_statics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticApi->read_all_statics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, list[BaseClassificator])**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_metric_path**
> list[str] read_metric_path()

Read all metric path info

This endpoint retrieves all available metric paths

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
api_instance = swagger_client.StaticApi(swagger_client.ApiClient(configuration))

try:
    # Read all metric path info
    api_response = api_instance.read_metric_path()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticApi->read_metric_path: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_static_resource**
> list[BaseClassificator] read_static_resource(resource)

Read all specified static resource info

This endpoint retrieves all specified static resource info

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
api_instance = swagger_client.StaticApi(swagger_client.ApiClient(configuration))
resource = 'resource_example' # str | 

try:
    # Read all specified static resource info
    api_response = api_instance.read_static_resource(resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticApi->read_static_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 

### Return type

[**list[BaseClassificator]**](BaseClassificator.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

