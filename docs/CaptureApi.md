# CyberSource.CaptureApi

All URIs are relative to *https://api.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_payment**](CaptureApi.md#capture_payment) | **POST** /v2/payments/{id}/captures | Capture a Payment
[**get_capture**](CaptureApi.md#get_capture) | **GET** /v2/captures/{id} | Retrieve a Capture


# **capture_payment**
> InlineResponse2012 capture_payment(capture_payment_request, id)

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

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capture**
> InlineResponse2004 get_capture(id)

Retrieve a Capture

Include the capture ID in the GET request to retrieve the capture details. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CaptureApi()
id = 'id_example' # str | The capture ID returned from a previous capture request. 

try: 
    # Retrieve a Capture
    api_response = api_instance.get_capture(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureApi->get_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The capture ID returned from a previous capture request.  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

