# CyberSource.DeviceSearchApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_search_query_v3**](DeviceSearchApi.md#post_search_query_v3) | **POST** /dms/v3/devices/search | Retrieve List of Devices for a given search query V3


# **post_search_query_v3**
> InlineResponse2006 post_search_query_v3(post_device_search_request_v3)

Retrieve List of Devices for a given search query V3

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
    # Retrieve List of Devices for a given search query V3
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

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

