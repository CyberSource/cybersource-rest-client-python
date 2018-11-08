# CyberSource.FlexTokenApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenize**](FlexTokenApi.md#tokenize) | **POST** /flex/v1/tokens/ | Flex Tokenize card


# **tokenize**
> FlexV1TokensPost200Response tokenize(tokenize_request=tokenize_request)

Flex Tokenize card

Returns a token representing the supplied card details. The token replaces card data and can be used as the Subscription ID in the CyberSource Simple Order API or SCMP API. This is an unauthenticated call that you should initiate from your customer’s device or browser.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.FlexTokenApi()
tokenize_request = CyberSource.TokenizeRequest() # TokenizeRequest |  (optional)

try: 
    # Flex Tokenize card
    api_response = api_instance.tokenize(tokenize_request=tokenize_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlexTokenApi->tokenize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenize_request** | [**TokenizeRequest**](TokenizeRequest.md)|  | [optional] 

### Return type

[**FlexV1TokensPost200Response**](FlexV1TokensPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

