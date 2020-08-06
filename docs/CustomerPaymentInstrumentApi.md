# CyberSource.CustomerPaymentInstrumentApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer_payment_instrument**](CustomerPaymentInstrumentApi.md#delete_customer_payment_instrument) | **DELETE** /tms/v2/customers/{customerTokenId}/payment-instruments/{paymentInstrumentTokenId} | Delete a Customer Payment Instrument
[**get_customer_payment_instrument**](CustomerPaymentInstrumentApi.md#get_customer_payment_instrument) | **GET** /tms/v2/customers/{customerTokenId}/payment-instruments/{paymentInstrumentTokenId} | Retrieve a Customer Payment Instrument
[**get_customer_payment_instruments_list**](CustomerPaymentInstrumentApi.md#get_customer_payment_instruments_list) | **GET** /tms/v2/customers/{customerTokenId}/payment-instruments | List Payment Instruments for a Customer
[**patch_customers_payment_instrument**](CustomerPaymentInstrumentApi.md#patch_customers_payment_instrument) | **PATCH** /tms/v2/customers/{customerTokenId}/payment-instruments/{paymentInstrumentTokenId} | Update a Customer Payment Instrument
[**post_customer_payment_instrument**](CustomerPaymentInstrumentApi.md#post_customer_payment_instrument) | **POST** /tms/v2/customers/{customerTokenId}/payment-instruments | Create a Customer Payment Instrument


# **delete_customer_payment_instrument**
> delete_customer_payment_instrument(customer_token_id, payment_instrument_token_id, profile_id=profile_id)

Delete a Customer Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
payment_instrument_token_id = 'payment_instrument_token_id_example' # str | The TokenId of a payment instrument.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete a Customer Payment Instrument
    api_instance.delete_customer_payment_instrument(customer_token_id, payment_instrument_token_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->delete_customer_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **payment_instrument_token_id** | **str**| The TokenId of a payment instrument. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_payment_instrument**
> Tmsv2customersEmbeddedDefaultPaymentInstrument get_customer_payment_instrument(customer_token_id, payment_instrument_token_id, profile_id=profile_id)

Retrieve a Customer Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
payment_instrument_token_id = 'payment_instrument_token_id_example' # str | The TokenId of a payment instrument.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve a Customer Payment Instrument
    api_response = api_instance.get_customer_payment_instrument(customer_token_id, payment_instrument_token_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->get_customer_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **payment_instrument_token_id** | **str**| The TokenId of a payment instrument. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrument**](Tmsv2customersEmbeddedDefaultPaymentInstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_payment_instruments_list**
> PaymentInstrumentListForCustomer get_customer_payment_instruments_list(customer_token_id, profile_id=profile_id, offset=offset, limit=limit)

List Payment Instruments for a Customer

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)
offset = 0 # int | Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. (optional) (default to 0)
limit = 20 # int | The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. (optional) (default to 20)

try: 
    # List Payment Instruments for a Customer
    api_response = api_instance.get_customer_payment_instruments_list(customer_token_id, profile_id=profile_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->get_customer_payment_instruments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 
 **offset** | **int**| Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. | [optional] [default to 0]
 **limit** | **int**| The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. | [optional] [default to 20]

### Return type

[**PaymentInstrumentListForCustomer**](PaymentInstrumentListForCustomer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_customers_payment_instrument**
> Tmsv2customersEmbeddedDefaultPaymentInstrument patch_customers_payment_instrument(customer_token_id, payment_instrument_token_id, patch_customer_payment_instrument_request, profile_id=profile_id, if_match=if_match)

Update a Customer Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
payment_instrument_token_id = 'payment_instrument_token_id_example' # str | The TokenId of a payment instrument.
patch_customer_payment_instrument_request = CyberSource.PatchCustomerPaymentInstrumentRequest() # PatchCustomerPaymentInstrumentRequest | 
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)
if_match = 'if_match_example' # str | Contains an ETag value from a GET request to make the request conditional. (optional)

try: 
    # Update a Customer Payment Instrument
    api_response = api_instance.patch_customers_payment_instrument(customer_token_id, payment_instrument_token_id, patch_customer_payment_instrument_request, profile_id=profile_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->patch_customers_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **payment_instrument_token_id** | **str**| The TokenId of a payment instrument. | 
 **patch_customer_payment_instrument_request** | [**PatchCustomerPaymentInstrumentRequest**](PatchCustomerPaymentInstrumentRequest.md)|  | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 
 **if_match** | **str**| Contains an ETag value from a GET request to make the request conditional. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrument**](Tmsv2customersEmbeddedDefaultPaymentInstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customer_payment_instrument**
> Tmsv2customersEmbeddedDefaultPaymentInstrument post_customer_payment_instrument(customer_token_id, post_customer_payment_instrument_request, profile_id=profile_id)

Create a Customer Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
post_customer_payment_instrument_request = CyberSource.PostCustomerPaymentInstrumentRequest() # PostCustomerPaymentInstrumentRequest | 
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Create a Customer Payment Instrument
    api_response = api_instance.post_customer_payment_instrument(customer_token_id, post_customer_payment_instrument_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->post_customer_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **post_customer_payment_instrument_request** | [**PostCustomerPaymentInstrumentRequest**](PostCustomerPaymentInstrumentRequest.md)|  | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrument**](Tmsv2customersEmbeddedDefaultPaymentInstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

