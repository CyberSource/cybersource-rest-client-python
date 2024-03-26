# CyberSource.UnifiedCheckoutCaptureContextApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_unified_checkout_capture_context**](UnifiedCheckoutCaptureContextApi.md#generate_unified_checkout_capture_context) | **POST** /up/v1/capture-contexts | Generate Unified Checkout Capture Context


# **generate_unified_checkout_capture_context**
> str generate_unified_checkout_capture_context(generate_unified_checkout_capture_context_request)

Generate Unified Checkout Capture Context

Unified Checkout is a powerful product within the Digital Acceptance Suite. Unified Checkout is designed to assist merchants with the adoption and inclusion of digital payments within their payment acceptance page. With Unified Checkout Integration you can add digital payment methods to create familiar, convenient and seamless payment experiences that are designed to reduce checkout friction and increase conversions. Click to Pay Drop-in UI is built on the Unified Checkout platform. For more information about Unified Checkout, see the [Unified Checkout Developer Guides Page](https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.html). For examples on how to integrate Unified Checkout within your webpage please see our [GitHub Unified Checkout Samples](https://github.com/CyberSource/cybersource-unified-checkout-sample-java). For more information about Click to Pay drop in UI, see the [Click to Pay Drop-in UI Developer Guides Page](https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-intro.html). Generate Unified Checkout Capture Context Generate a one-time use capture context used for the invocation of Unified Checkout. The Request wil contain all of the parameters for how Unified Checkout will operate within a client webpage. The resulting payload will be a JWT signed object that can be used to initiate Unified Checkout or Click to Pay Drop-in UI within a web page

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

