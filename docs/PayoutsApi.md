# CyberSource.PayoutsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oct_create_payment**](PayoutsApi.md#oct_create_payment) | **POST** /pts/v2/payouts | Process a Payout


# **oct_create_payment**
> PtsV2PayoutsPost201Response oct_create_payment(oct_create_payment_request)

Process a Payout

Send funds from a selected funding source to a designated credit/debit card account or a prepaid card using an Original Credit Transaction (OCT). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PayoutsApi()
oct_create_payment_request = CyberSource.OctCreatePaymentRequest() # OctCreatePaymentRequest | 

try: 
    # Process a Payout
    api_response = api_instance.oct_create_payment(oct_create_payment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayoutsApi->oct_create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oct_create_payment_request** | [**OctCreatePaymentRequest**](OctCreatePaymentRequest.md)|  | 

### Return type

[**PtsV2PayoutsPost201Response**](PtsV2PayoutsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

