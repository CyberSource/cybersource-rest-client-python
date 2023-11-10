# CyberSource.UnifiedCheckoutCaptureContextApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_unified_checkout_capture_context**](UnifiedCheckoutCaptureContextApi.md#generate_unified_checkout_capture_context) | **POST** /up/v1/capture-contexts | Generate Unified Checkout Capture Context


# **generate_unified_checkout_capture_context**
> str generate_unified_checkout_capture_context(generate_unified_checkout_capture_context_request)

Generate Unified Checkout Capture Context

Generate a one-time use capture context used for the invocation of Unified Checkout. The Request wil contain all of the parameters for how Unified Checkout will operate within a client webpage. The resulting payload will be a JWT signed object that can be used to initiate Unified Checkout within a merchant web page

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.UnifiedCheckoutCaptureContextApi()
generate_unified_checkout_capture_context_request = CyberSource.GenerateUnifiedCheckoutCaptureContextRequest() # GenerateUnifiedCheckoutCaptureContextRequest | 

try: 
    # Generate Unified Checkout Capture Context
    api_response = api_instance.generate_unified_checkout_capture_context(generate_unified_checkout_capture_context_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnifiedCheckoutCaptureContextApi->generate_unified_checkout_capture_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_unified_checkout_capture_context_request** | [**GenerateUnifiedCheckoutCaptureContextRequest**](GenerateUnifiedCheckoutCaptureContextRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/jwt

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

