# CyberSource.MicroformIntegrationApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_capture_context**](MicroformIntegrationApi.md#generate_capture_context) | **POST** /microform/v2/sessions | Generate Capture Context


# **generate_capture_context**
> str generate_capture_context(generate_capture_context_request)

Generate Capture Context

This API is used to generate the Capture Context data structure for the Microform Integration.  Microform is a browser-based acceptance solution that allows a seller to capture payment information is a secure manner from their website.  For more information about Flex Microform transactions, see the [Flex Developer Guides Page](https://developer.cybersource.com/api/developer-guides/dita-flex/SAFlexibleToken.html). For examples on how to integrate Flex Microform within your webpage please see our [GitHub Flex Samples](https://github.com/CyberSource?q=flex&type=&language=) This API is a server-to-server API to generate the capture context that can be used to initiate instance of microform on a acceptance page.  The capture context is a digitally signed JWT that provides authentication, one-time keys, and the target origin to the Microform Integration application. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MicroformIntegrationApi()
generate_capture_context_request = CyberSource.GenerateCaptureContextRequest() # GenerateCaptureContextRequest | 

try: 
    # Generate Capture Context
    api_response = api_instance.generate_capture_context(generate_capture_context_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MicroformIntegrationApi->generate_capture_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_capture_context_request** | [**GenerateCaptureContextRequest**](GenerateCaptureContextRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/jwt

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

