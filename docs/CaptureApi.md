# CyberSource.CaptureApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_payment**](CaptureApi.md#capture_payment) | **POST** /pts/v2/payments/{id}/captures | Capture a Payment


# **capture_payment**
> PtsV2PaymentsCapturesPost201Response capture_payment(capture_payment_request, id)

Capture a Payment

Include the payment ID in the POST request to capture the payment amount.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CaptureApi()
capture_payment_request = CyberSource.CapturePaymentRequest() # CapturePaymentRequest | 
id = 'id_example' # str | The payment ID returned from a previous payment request. This ID links the capture to the payment. 

try: 
    # Capture a Payment
    api_response = api_instance.capture_payment(capture_payment_request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureApi->capture_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capture_payment_request** | [**CapturePaymentRequest**](CapturePaymentRequest.md)|  | 
 **id** | **str**| The payment ID returned from a previous payment request. This ID links the capture to the payment.  | 

### Return type

[**PtsV2PaymentsCapturesPost201Response**](PtsV2PaymentsCapturesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

