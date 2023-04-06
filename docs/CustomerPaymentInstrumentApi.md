# CyberSource.CustomerPaymentInstrumentApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer_payment_instrument**](CustomerPaymentInstrumentApi.md#delete_customer_payment_instrument) | **DELETE** /tms/v2/customers/{customerId}/payment-instruments/{paymentInstrumentId} | Delete a Customer Payment Instrument
[**get_customer_payment_instrument**](CustomerPaymentInstrumentApi.md#get_customer_payment_instrument) | **GET** /tms/v2/customers/{customerId}/payment-instruments/{paymentInstrumentId} | Retrieve a Customer Payment Instrument
[**get_customer_payment_instruments_list**](CustomerPaymentInstrumentApi.md#get_customer_payment_instruments_list) | **GET** /tms/v2/customers/{customerId}/payment-instruments | List Payment Instruments for a Customer
[**patch_customers_payment_instrument**](CustomerPaymentInstrumentApi.md#patch_customers_payment_instrument) | **PATCH** /tms/v2/customers/{customerId}/payment-instruments/{paymentInstrumentId} | Update a Customer Payment Instrument
[**post_customer_payment_instrument**](CustomerPaymentInstrumentApi.md#post_customer_payment_instrument) | **POST** /tms/v2/customers/{customerId}/payment-instruments | Create a Customer Payment Instrument


# **delete_customer_payment_instrument**
> delete_customer_payment_instrument(customer_id, payment_instrument_id, profile_id=profile_id)

Delete a Customer Payment Instrument

|  |  |  | | --- | --- | --- | |**Customer Payment Instrument**<br>A Customer Payment Instrument represents tokenized customer payment information such as expiration date, billing address & card type.<br>A [Customer](#token-management_customer_create-a-customer) can have [one or more Payment Instruments](#token-management_customer-payment-instrument_retrieve-a-customer-payment-instrument), with one allocated as the Customers default for use in payments.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Deleting a Customers Payment Instrument**<br>Your system can use this API to delete an existing Payment Instrument for a Customer.<br>Any Instrument Identifiers representing the card number will also be deleted if they are not associated with any other Payment Instruments.<br>If a customer has more than one Payment Instrument then the default Payment Instrument cannot be deleted without first selecting a [new default Payment Instrument](#token-management_customer-payment-instrument_update-a-customer-payment-instrument_samplerequests-dropdown_make-customer-payment-instrument-the-default_liveconsole-tab-request-body). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_id = 'customer_id_example' # str | The Id of a Customer.
payment_instrument_id = 'payment_instrument_id_example' # str | The Id of a payment instrument.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete a Customer Payment Instrument
    api_instance.delete_customer_payment_instrument(customer_id, payment_instrument_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->delete_customer_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The Id of a Customer. | 
 **payment_instrument_id** | **str**| The Id of a payment instrument. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_payment_instrument**
> Tmsv2customersEmbeddedDefaultPaymentInstrument get_customer_payment_instrument(customer_id, payment_instrument_id, profile_id=profile_id)

Retrieve a Customer Payment Instrument

|  |  |  | | --- | --- | --- | |**Customer Payment Instrument**<br>A Customer Payment Instrument represents tokenized customer payment information such as expiration date, billing address & card type.<br>A [Customer](#token-management_customer_create-a-customer) can have [one or more Payment Instruments](#token-management_customer-payment-instrument_retrieve-a-customer-payment-instrument), with one allocated as the Customers default for use in payments.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Retrieving a Customer Payment Instrument**<br>Your system can use this API to retrieve an existing Payment Instrument for a Customer.<br>To perform a payment with a particular Payment Instrument simply specify the [Payment Instrument Id in the payments request](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-customer-payment-instrument-and-shipping-address-token-id_liveconsole-tab-request-body). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_id = 'customer_id_example' # str | The Id of a Customer.
payment_instrument_id = 'payment_instrument_id_example' # str | The Id of a payment instrument.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve a Customer Payment Instrument
    api_response = api_instance.get_customer_payment_instrument(customer_id, payment_instrument_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->get_customer_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The Id of a Customer. | 
 **payment_instrument_id** | **str**| The Id of a payment instrument. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrument**](Tmsv2customersEmbeddedDefaultPaymentInstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_payment_instruments_list**
> PaymentInstrumentList get_customer_payment_instruments_list(customer_id, profile_id=profile_id, offset=offset, limit=limit)

List Payment Instruments for a Customer

|  |  |  | | --- | --- | --- | |**Customer Payment Instrument**<br>A Customer Payment Instrument represents tokenized customer payment information such as expiration date, billing address & card type.<br>A [Customer](#token-management_customer_create-a-customer) can have [one or more Payment Instruments](#token-management_customer-payment-instrument_retrieve-a-customer-payment-instrument), with one allocated as the Customers default for use in payments.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Retrieving all Customer Payment Instruments**<br>Your system can use this API to retrieve all existing Payment Instruments for a Customer. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_id = 'customer_id_example' # str | The Id of a Customer.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)
offset = 0 # int | Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. (optional) (default to 0)
limit = 20 # int | The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. (optional) (default to 20)

try: 
    # List Payment Instruments for a Customer
    api_response = api_instance.get_customer_payment_instruments_list(customer_id, profile_id=profile_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->get_customer_payment_instruments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The Id of a Customer. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 
 **offset** | **int**| Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. | [optional] [default to 0]
 **limit** | **int**| The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. | [optional] [default to 20]

### Return type

[**PaymentInstrumentList**](PaymentInstrumentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_customers_payment_instrument**
> Tmsv2customersEmbeddedDefaultPaymentInstrument patch_customers_payment_instrument(customer_id, payment_instrument_id, patch_customer_payment_instrument_request, profile_id=profile_id, if_match=if_match)

Update a Customer Payment Instrument

|  |  |  | | --- | --- | --- | |**Customer Payment Instrument**<br>A Customer Payment Instrument represents tokenized customer payment information such as expiration date, billing address & card type.<br>A [Customer](#token-management_customer_create-a-customer) can have [one or more Payment Instruments](#token-management_customer-payment-instrument_retrieve-a-customer-payment-instrument), with one allocated as the Customers default for use in payments.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Updating a Customers Payment Instrument**<br>Your system can use this API to update an existing Payment Instrument for a Customer, including selecting a [default Payment Instrument](#token-management_customer-payment-instrument_update-a-customer-payment-instrument_samplerequests-dropdown_make-customer-payment-instrument-the-default_liveconsole-tab-request-body) for use in payments. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_id = 'customer_id_example' # str | The Id of a Customer.
payment_instrument_id = 'payment_instrument_id_example' # str | The Id of a payment instrument.
patch_customer_payment_instrument_request = CyberSource.PatchCustomerPaymentInstrumentRequest() # PatchCustomerPaymentInstrumentRequest | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)
if_match = 'if_match_example' # str | Contains an ETag value from a GET request to make the request conditional. (optional)

try: 
    # Update a Customer Payment Instrument
    api_response = api_instance.patch_customers_payment_instrument(customer_id, payment_instrument_id, patch_customer_payment_instrument_request, profile_id=profile_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->patch_customers_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The Id of a Customer. | 
 **payment_instrument_id** | **str**| The Id of a payment instrument. | 
 **patch_customer_payment_instrument_request** | [**PatchCustomerPaymentInstrumentRequest**](PatchCustomerPaymentInstrumentRequest.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 
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
> Tmsv2customersEmbeddedDefaultPaymentInstrument post_customer_payment_instrument(customer_id, post_customer_payment_instrument_request, profile_id=profile_id)

Create a Customer Payment Instrument

|  |  |  | | --- | --- | --- | |**Customer Payment Instrument**<br>A Customer Payment Instrument represents tokenized customer payment information such as expiration date, billing address & card type.<br>A [Customer](#token-management_customer_create-a-customer) can have [one or more Payment Instruments](#token-management_customer-payment-instrument_retrieve-a-customer-payment-instrument), with one allocated as the Customers default for use in payments.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br><br>**Creating a Customer Payment Instrument**<br>It is recommended you [create a Customer Payment Instrument via a Payment Authorization](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-create-default-payment-instrument-shipping-address-for-existing-customer_liveconsole-tab-request-body), this can be for a zero amount.<br>In Europe: You should perform Payer Authentication alongside the Authorization.|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Payment Network Tokens**<br>Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires.<br>A Payment Network Token will be automatically created and used in future payments if you are enabled for the service.<br>A Payment Network Token can also be [provisioned for an existing Instrument Identifier](#token-management_instrument-identifier_enroll-an-instrument-identifier-for-payment-network-token).<br>For more information about Payment Network Tokens see the Developer Guide.<br><br>**Payments with Customers Payment Instrument**<br>To perform a payment with a particular Payment Instrument or Shipping Address specify the [Payment Instrument in the payment request](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-customer-payment-instrument-and-shipping-address-token-id_liveconsole-tab-request-body). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerPaymentInstrumentApi()
customer_id = 'customer_id_example' # str | The Id of a Customer.
post_customer_payment_instrument_request = CyberSource.PostCustomerPaymentInstrumentRequest() # PostCustomerPaymentInstrumentRequest | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Create a Customer Payment Instrument
    api_response = api_instance.post_customer_payment_instrument(customer_id, post_customer_payment_instrument_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerPaymentInstrumentApi->post_customer_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The Id of a Customer. | 
 **post_customer_payment_instrument_request** | [**PostCustomerPaymentInstrumentRequest**](PostCustomerPaymentInstrumentRequest.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrument**](Tmsv2customersEmbeddedDefaultPaymentInstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

