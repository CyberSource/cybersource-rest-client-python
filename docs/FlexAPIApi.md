# CyberSource.FlexAPIApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_flex_api_capture_context**](FlexAPIApi.md#generate_flex_api_capture_context) | **POST** /flex/v2/sessions | Establish a Payment Session with a Capture Context


# **generate_flex_api_capture_context**
> str generate_flex_api_capture_context(generate_flex_api_capture_context_request)

Establish a Payment Session with a Capture Context

To establish a payment session, include the API fields you plan to use in that session in the body of the request.  The system then returns a JSON Web Token (JWT) that includes the capture context.   To determine which fields to include in your capture context, identify the personal information that you wish to isolate from the payment session.  **Capture Context Fields**<br> When making a session request, any fields that you request to be added to the capture context are required by default.  However, you can choose to make a field optional by setting the required parameter to false. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.FlexAPIApi()
generate_flex_api_capture_context_request = CyberSource.GenerateFlexAPICaptureContextRequest() # GenerateFlexAPICaptureContextRequest | 

try: 
    # Establish a Payment Session with a Capture Context
    api_response = api_instance.generate_flex_api_capture_context(generate_flex_api_capture_context_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlexAPIApi->generate_flex_api_capture_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_flex_api_capture_context_request** | [**GenerateFlexAPICaptureContextRequest**](GenerateFlexAPICaptureContextRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/jwt

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

