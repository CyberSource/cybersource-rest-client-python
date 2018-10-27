# CyberSource.PaymentApi

All URIs are relative to *https://api.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment**](PaymentApi.md#create_payment) | **POST** /v2/payments/ | Process a Payment
[**get_payment**](PaymentApi.md#get_payment) | **GET** /v2/payments/{id} | Retrieve a Payment


# **create_payment**
> InlineResponse201 create_payment(create_payment_request)

Process a Payment

Authorize the payment for the transaction. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentApi()
create_payment_request = CyberSource.CreatePaymentRequest() # CreatePaymentRequest | 

try: 
    # Process a Payment
    api_response = api_instance.create_payment(create_payment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_request** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment**
> InlineResponse2002 get_payment(id)

Retrieve a Payment

Include the payment ID in the GET request to retrieve the payment details.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentApi()
id = 'id_example' # str | The payment ID returned from a previous payment request. 

try: 
    # Retrieve a Payment
    api_response = api_instance.get_payment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The payment ID returned from a previous payment request.  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

