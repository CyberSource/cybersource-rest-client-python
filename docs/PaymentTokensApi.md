# CyberSource.PaymentTokensApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_or_delete_payment_token**](PaymentTokensApi.md#retrieve_or_delete_payment_token) | **POST** /pts/v2/payment-tokens | Retrieve or Delete Payment Token


# **retrieve_or_delete_payment_token**
> InlineResponse201 retrieve_or_delete_payment_token(request)

Retrieve or Delete Payment Token

This API can be used in two flavours - for retrieval or deletion of vault id. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentTokensApi()
request = CyberSource.Request() # Request | 

try: 
    # Retrieve or Delete Payment Token
    api_response = api_instance.retrieve_or_delete_payment_token(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTokensApi->retrieve_or_delete_payment_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

