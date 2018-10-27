# CyberSource.TokenizationApi

All URIs are relative to *https://api.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenize**](TokenizationApi.md#tokenize) | **POST** /payments/flex/v1/tokens/ | Tokenize card


# **tokenize**
> InlineResponse2001 tokenize(tokenize_request=tokenize_request)

Tokenize card

Returns a token representing the supplied card details. The token replaces card data and can be used as the Subscription ID in the CyberSource Simple Order API or SCMP API. This is an unauthenticated call that you should initiate from your customer’s device or browser.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TokenizationApi()
tokenize_request = CyberSource.TokenizeRequest() # TokenizeRequest |  (optional)

try: 
    # Tokenize card
    api_response = api_instance.tokenize(tokenize_request=tokenize_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->tokenize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenize_request** | [**TokenizeRequest**](TokenizeRequest.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

