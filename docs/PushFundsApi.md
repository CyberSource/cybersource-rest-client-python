# CyberSource.PushFundsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_push_funds_transfer**](PushFundsApi.md#create_push_funds_transfer) | **POST** /pts/v1/push-funds-transfer | Process a Push Funds Transfer


# **create_push_funds_transfer**
> PushFunds201Response create_push_funds_transfer(push_funds_request, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)

Process a Push Funds Transfer

Receive funds using an Original Credit Transaction (OCT). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PushFundsApi()
push_funds_request = CyberSource.PushFundsRequest() # PushFundsRequest | 
content_type = 'content_type_example' # str | 
x_requestid = 'x_requestid_example' # str | 
v_c_merchant_id = 'v_c_merchant_id_example' # str | 
v_c_permissions = 'v_c_permissions_example' # str | 
v_c_correlation_id = 'v_c_correlation_id_example' # str | 
v_c_organization_id = 'v_c_organization_id_example' # str | 

try: 
    # Process a Push Funds Transfer
    api_response = api_instance.create_push_funds_transfer(push_funds_request, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushFundsApi->create_push_funds_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_funds_request** | [**PushFundsRequest**](PushFundsRequest.md)|  | 
 **content_type** | **str**|  | 
 **x_requestid** | **str**|  | 
 **v_c_merchant_id** | **str**|  | 
 **v_c_permissions** | **str**|  | 
 **v_c_correlation_id** | **str**|  | 
 **v_c_organization_id** | **str**|  | 

### Return type

[**PushFunds201Response**](PushFunds201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

