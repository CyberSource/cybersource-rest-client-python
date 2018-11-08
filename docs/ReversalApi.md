# CyberSource.ReversalApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_reversal**](ReversalApi.md#auth_reversal) | **POST** /pts/v2/payments/{id}/reversals | Process an Authorization Reversal


# **auth_reversal**
> PtsV2PaymentsReversalsPost201Response auth_reversal(id, auth_reversal_request)

Process an Authorization Reversal

Include the payment ID in the POST request to reverse the payment amount.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReversalApi()
id = 'id_example' # str | The payment ID returned from a previous payment request.
auth_reversal_request = CyberSource.AuthReversalRequest() # AuthReversalRequest | 

try: 
    # Process an Authorization Reversal
    api_response = api_instance.auth_reversal(id, auth_reversal_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReversalApi->auth_reversal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The payment ID returned from a previous payment request. | 
 **auth_reversal_request** | [**AuthReversalRequest**](AuthReversalRequest.md)|  | 

### Return type

[**PtsV2PaymentsReversalsPost201Response**](PtsV2PaymentsReversalsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

