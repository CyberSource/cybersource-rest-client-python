# CyberSource.RefundApi

All URIs are relative to *https://api.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_refund**](RefundApi.md#get_refund) | **GET** /v2/refunds/{id} | Retrieve a Refund
[**refund_capture**](RefundApi.md#refund_capture) | **POST** /v2/captures/{id}/refunds | Refund a Capture
[**refund_payment**](RefundApi.md#refund_payment) | **POST** /v2/payments/{id}/refunds | Refund a Payment


# **get_refund**
> InlineResponse2005 get_refund(id)

Retrieve a Refund

Include the refund ID in the GET request to to retrieve the refund details.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.RefundApi()
id = 'id_example' # str | The refund ID. This ID is returned from a previous refund request.

try: 
    # Retrieve a Refund
    api_response = api_instance.get_refund(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundApi->get_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The refund ID. This ID is returned from a previous refund request. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_capture**
> InlineResponse2013 refund_capture(refund_capture_request, id)

Refund a Capture

Include the capture ID in the POST request to refund the captured amount. 

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

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_payment**
> InlineResponse2013 refund_payment(refund_payment_request, id)

Refund a Payment

Include the payment ID in the POST request to refund the payment amount. 

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

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

