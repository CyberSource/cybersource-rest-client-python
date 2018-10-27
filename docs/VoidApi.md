# CyberSource.VoidApi

All URIs are relative to *https://api.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_void**](VoidApi.md#get_void) | **GET** /v2/voids/{id} | Retrieve A Void
[**void_capture**](VoidApi.md#void_capture) | **POST** /v2/captures/{id}/voids | Void a Capture
[**void_credit**](VoidApi.md#void_credit) | **POST** /v2/credits/{id}/voids | Void a Credit
[**void_payment**](VoidApi.md#void_payment) | **POST** /v2/payments/{id}/voids | Void a Payment
[**void_refund**](VoidApi.md#void_refund) | **POST** /v2/refunds/{id}/voids | Void a Refund


# **get_void**
> InlineResponse2015 get_void(id)

Retrieve A Void

Include the void ID in the GET request to retrieve the void details.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.VoidApi()
id = 'id_example' # str | The void ID returned from a previous void request.

try: 
    # Retrieve A Void
    api_response = api_instance.get_void(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoidApi->get_void: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The void ID returned from a previous void request. | 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_capture**
> InlineResponse2015 void_capture(void_capture_request, id)

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

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_credit**
> InlineResponse2015 void_credit(void_credit_request, id)

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

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_payment**
> InlineResponse2015 void_payment(void_payment_request, id)

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

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_refund**
> InlineResponse2015 void_refund(void_refund_request, id)

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

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

