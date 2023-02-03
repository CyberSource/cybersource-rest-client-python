# CyberSource.TransientTokenDataApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_for_transient_token**](TransientTokenDataApi.md#get_transaction_for_transient_token) | **GET** /up/v1/payment-details/{transientToken} | Get Transient Token Data


# **get_transaction_for_transient_token**
> get_transaction_for_transient_token(transient_token)

Get Transient Token Data

Retrieve the data captured by Unfied Checkout. This API is used to retrieve the detailed data represented by the Transient Token. This API will not return PCI payment data (PAN). Include the Request ID in the GET request to retrieve the transaction details.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TransientTokenDataApi()
transient_token = 'transient_token_example' # str | Transient Token returned by the Unified Checkout application. 

try: 
    # Get Transient Token Data
    api_instance.get_transaction_for_transient_token(transient_token)
except ApiException as e:
    print("Exception when calling TransientTokenDataApi->get_transaction_for_transient_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transient_token** | **str**| Transient Token returned by the Unified Checkout application.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
