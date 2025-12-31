# CyberSource.EnrollmentApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enroll_card**](EnrollmentApi.md#enroll_card) | **POST** /acp/v1/tokens | Enroll a card


# **enroll_card**
> AgenticCardEnrollmentResponse200 enroll_card(agentic_card_enrollment_request)

Enroll a card

Enroll a card for tokenization during the customer's account registration or when the customer starts a new purchase intent.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.EnrollmentApi()
agentic_card_enrollment_request = CyberSource.AgenticCardEnrollmentRequest() # AgenticCardEnrollmentRequest | 

try: 
    # Enroll a card
    api_response = api_instance.enroll_card(agentic_card_enrollment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentApi->enroll_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentic_card_enrollment_request** | [**AgenticCardEnrollmentRequest**](AgenticCardEnrollmentRequest.md)|  | 

### Return type

[**AgenticCardEnrollmentResponse200**](AgenticCardEnrollmentResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

