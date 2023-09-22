# CyberSource.PaymentsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment**](PaymentsApi.md#create_payment) | **POST** /pts/v2/payments | Process a Payment
[**increment_auth**](PaymentsApi.md#increment_auth) | **PATCH** /pts/v2/payments/{id} | Increment an Authorization
[**refresh_payment_status**](PaymentsApi.md#refresh_payment_status) | **POST** /pts/v2/refresh-payment-status/{id} | Check a Payment Status


# **create_payment**
> PtsV2PaymentsPost201Response create_payment(create_payment_request)

Process a Payment

A payment authorizes the amount for the transaction. There are a number of supported payment features, such as E-commerce and Card Present - Credit Card/Debit Card, Echeck, e-Wallets, Level II/III Data, etc..  A payment response includes the status of the request. It also includes processor-specific information when the request is successful and errors if unsuccessful. See the [Payments Developer Guides Page](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.html).  Authorization can be requested with Capture, Decision Manager, Payer Authentication(3ds), and Token Creation. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentsApi()
create_payment_request = CyberSource.CreatePaymentRequest() # CreatePaymentRequest | 

try: 
    # Process a Payment
    api_response = api_instance.create_payment(create_payment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_request** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | 

### Return type

[**PtsV2PaymentsPost201Response**](PtsV2PaymentsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **increment_auth**
> PtsV2IncrementalAuthorizationPatch201Response increment_auth(id, increment_auth_request)

Increment an Authorization

Use this service to authorize additional charges in a lodging or autorental transaction. Include the ID returned from the original authorization in the PATCH request to add additional charges to that authorization. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentsApi()
id = 'id_example' # str | The ID returned from the original authorization request.
increment_auth_request = CyberSource.IncrementAuthRequest() # IncrementAuthRequest | 

try: 
    # Increment an Authorization
    api_response = api_instance.increment_auth(id, increment_auth_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->increment_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID returned from the original authorization request. | 
 **increment_auth_request** | [**IncrementAuthRequest**](IncrementAuthRequest.md)|  | 

### Return type

[**PtsV2IncrementalAuthorizationPatch201Response**](PtsV2IncrementalAuthorizationPatch201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_payment_status**
> PtsV2PaymentsPost201Response1 refresh_payment_status(id, refresh_payment_status_request)

Check a Payment Status

Checks and updates the payment status 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentsApi()
id = 'id_example' # str | The payment id whose status needs to be checked and updated.
refresh_payment_status_request = CyberSource.RefreshPaymentStatusRequest() # RefreshPaymentStatusRequest | 

try: 
    # Check a Payment Status
    api_response = api_instance.refresh_payment_status(id, refresh_payment_status_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->refresh_payment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The payment id whose status needs to be checked and updated. | 
 **refresh_payment_status_request** | [**RefreshPaymentStatusRequest**](RefreshPaymentStatusRequest.md)|  | 

### Return type

[**PtsV2PaymentsPost201Response1**](PtsV2PaymentsPost201Response1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

