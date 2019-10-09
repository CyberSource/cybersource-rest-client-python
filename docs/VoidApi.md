# CyberSource.VoidApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**void_capture**](VoidApi.md#void_capture) | **POST** /pts/v2/captures/{id}/voids | Void a Capture
[**void_credit**](VoidApi.md#void_credit) | **POST** /pts/v2/credits/{id}/voids | Void a Credit
[**void_payment**](VoidApi.md#void_payment) | **POST** /pts/v2/payments/{id}/voids | Void a Payment
[**void_refund**](VoidApi.md#void_refund) | **POST** /pts/v2/refunds/{id}/voids | Void a Refund


# **void_capture**
> PtsV2PaymentsVoidsPost201Response void_capture(void_capture_request, id)

Void a Capture

Include the capture ID in the POST request to cancel the capture.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.VoidApi()
void_capture_request = CyberSource.VoidCaptureRequest() # VoidCaptureRequest | 
id = 'id_example' # str | The capture ID returned from a previous capture request.

try: 
    # Void a Capture
    api_response = api_instance.void_capture(void_capture_request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoidApi->void_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **void_capture_request** | [**VoidCaptureRequest**](VoidCaptureRequest.md)|  | 
 **id** | **str**| The capture ID returned from a previous capture request. | 

### Return type

[**PtsV2PaymentsVoidsPost201Response**](PtsV2PaymentsVoidsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_credit**
> PtsV2PaymentsVoidsPost201Response void_credit(void_credit_request, id)

Void a Credit

Include the credit ID in the POST request to cancel the credit.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.VoidApi()
void_credit_request = CyberSource.VoidCreditRequest() # VoidCreditRequest | 
id = 'id_example' # str | The credit ID returned from a previous credit request.

try: 
    # Void a Credit
    api_response = api_instance.void_credit(void_credit_request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoidApi->void_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **void_credit_request** | [**VoidCreditRequest**](VoidCreditRequest.md)|  | 
 **id** | **str**| The credit ID returned from a previous credit request. | 

### Return type

[**PtsV2PaymentsVoidsPost201Response**](PtsV2PaymentsVoidsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_payment**
> PtsV2PaymentsVoidsPost201Response void_payment(void_payment_request, id)

Void a Payment

Include the payment ID in the POST request to cancel the payment.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.VoidApi()
void_payment_request = CyberSource.VoidPaymentRequest() # VoidPaymentRequest | 
id = 'id_example' # str | The payment ID returned from a previous payment request.

try: 
    # Void a Payment
    api_response = api_instance.void_payment(void_payment_request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoidApi->void_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **void_payment_request** | [**VoidPaymentRequest**](VoidPaymentRequest.md)|  | 
 **id** | **str**| The payment ID returned from a previous payment request. | 

### Return type

[**PtsV2PaymentsVoidsPost201Response**](PtsV2PaymentsVoidsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_refund**
> PtsV2PaymentsVoidsPost201Response void_refund(void_refund_request, id)

Void a Refund

Include the refund ID in the POST request to cancel the refund.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.VoidApi()
void_refund_request = CyberSource.VoidRefundRequest() # VoidRefundRequest | 
id = 'id_example' # str | The refund ID returned from a previous refund request.

try: 
    # Void a Refund
    api_response = api_instance.void_refund(void_refund_request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoidApi->void_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **void_refund_request** | [**VoidRefundRequest**](VoidRefundRequest.md)|  | 
 **id** | **str**| The refund ID returned from a previous refund request. | 

### Return type

[**PtsV2PaymentsVoidsPost201Response**](PtsV2PaymentsVoidsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

