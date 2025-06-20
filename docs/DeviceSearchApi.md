# CyberSource.DeviceSearchApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_search_query**](DeviceSearchApi.md#post_search_query) | **POST** /dms/v2/devices/search | Retrieve List of Devices for a given search query V2
[**post_search_query_v3**](DeviceSearchApi.md#post_search_query_v3) | **POST** /dms/v3/devices/search | Retrieve List of Devices for a given search query


# **post_search_query**
> InlineResponse2005 post_search_query(post_device_search_request)

Retrieve List of Devices for a given search query V2

Retrieves list of terminals in paginated format.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DeviceSearchApi()
post_device_search_request = CyberSource.PostDeviceSearchRequest() # PostDeviceSearchRequest | 

try: 
    # Retrieve List of Devices for a given search query V2
    api_response = api_instance.post_search_query(post_device_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSearchApi->post_search_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_device_search_request** | [**PostDeviceSearchRequest**](PostDeviceSearchRequest.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_query_v3**
> InlineResponse2007 post_search_query_v3(post_device_search_request_v3)

Retrieve List of Devices for a given search query

Search for devices matching a given search query.  The search query supports serialNumber, readerId, terminalId, status, statusChangeReason or organizationId  Matching results are paginated. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DeviceSearchApi()
post_device_search_request_v3 = CyberSource.PostDeviceSearchRequestV3() # PostDeviceSearchRequestV3 | 

try: 
    # Retrieve List of Devices for a given search query
    api_response = api_instance.post_search_query_v3(post_device_search_request_v3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSearchApi->post_search_query_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_device_search_request_v3** | [**PostDeviceSearchRequestV3**](PostDeviceSearchRequestV3.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

