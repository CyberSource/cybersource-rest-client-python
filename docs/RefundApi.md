# CyberSource.RefundApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refund_capture**](RefundApi.md#refund_capture) | **POST** /pts/v2/captures/{id}/refunds | Refund a Capture
[**refund_payment**](RefundApi.md#refund_payment) | **POST** /pts/v2/payments/{id}/refunds | Refund a Payment


# **refund_capture**
> PtsV2PaymentsRefundPost201Response refund_capture(refund_capture_request, id)

Refund a Capture

Refund a capture API is only used, if you have requested Capture independenlty using [/pts/v2/payments/{id}/captures](https://developer.cybersource.com/api-reference-assets/index.html#payments_capture) API call Include the capture ID in the POST request to refund the captured amount. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.RefundApi()
refund_capture_request = CyberSource.RefundCaptureRequest() # RefundCaptureRequest | 
id = 'id_example' # str | The capture ID. This ID is returned from a previous capture request.

try: 
    # Refund a Capture
    api_response = api_instance.refund_capture(refund_capture_request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundApi->refund_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_capture_request** | [**RefundCaptureRequest**](RefundCaptureRequest.md)|  | 
 **id** | **str**| The capture ID. This ID is returned from a previous capture request. | 

### Return type

[**PtsV2PaymentsRefundPost201Response**](PtsV2PaymentsRefundPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_payment**
> PtsV2PaymentsRefundPost201Response refund_payment(refund_payment_request, id)

Refund a Payment

Refund a Payment API is only used, if you have requested Authorization and Capture together in [/pts/v2/payments](https://developer.cybersource.com/api-reference-assets/index.html#payments_payments) API call.  Include the payment ID in the POST request to refund the payment amount. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.RefundApi()
refund_payment_request = CyberSource.RefundPaymentRequest() # RefundPaymentRequest | 
id = 'id_example' # str | The payment ID. This ID is returned from a previous payment request.

try: 
    # Refund a Payment
    api_response = api_instance.refund_payment(refund_payment_request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundApi->refund_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_payment_request** | [**RefundPaymentRequest**](RefundPaymentRequest.md)|  | 
 **id** | **str**| The payment ID. This ID is returned from a previous payment request. | 

### Return type

[**PtsV2PaymentsRefundPost201Response**](PtsV2PaymentsRefundPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

