# CyberSource.PaymentInstrumentApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payment_instrument**](PaymentInstrumentApi.md#delete_payment_instrument) | **DELETE** /tms/v1/paymentinstruments/{paymentInstrumentId} | Delete a Payment Instrument
[**get_payment_instrument**](PaymentInstrumentApi.md#get_payment_instrument) | **GET** /tms/v1/paymentinstruments/{paymentInstrumentId} | Retrieve a Payment Instrument
[**patch_payment_instrument**](PaymentInstrumentApi.md#patch_payment_instrument) | **PATCH** /tms/v1/paymentinstruments/{paymentInstrumentId} | Update a Payment Instrument
[**post_payment_instrument**](PaymentInstrumentApi.md#post_payment_instrument) | **POST** /tms/v1/paymentinstruments | Create a Payment Instrument


# **delete_payment_instrument**
> delete_payment_instrument(payment_instrument_id, profile_id=profile_id)

Delete a Payment Instrument

|  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Deleting a Payment Instrument**<br>Your system can use this API to delete an existing Payment Instrument.<br>Any Instrument Identifiers representing the card number will also be deleted if they are not associated with any other Payment Instruments. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentApi()
payment_instrument_id = 'payment_instrument_id_example' # str | The Id of a payment instrument.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete a Payment Instrument
    api_instance.delete_payment_instrument(payment_instrument_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->delete_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_payment_instrument**
> PostPaymentInstrumentRequest get_payment_instrument(payment_instrument_id, profile_id=profile_id, retrieve_bin_details=retrieve_bin_details)

Retrieve a Payment Instrument

|  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Retrieving a Payment Instrument**<br>Your system can use this API to retrieve an existing Payment Instrument.<br>To perform a payment with a particular Payment Instrument simply specify the [Payment Instrument Id in the payments request](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-customer-payment-instrument-and-shipping-address-token-id_liveconsole-tab-request-body). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentApi()
payment_instrument_id = 'payment_instrument_id_example' # str | The Id of a payment instrument.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)
retrieve_bin_details = true # bool | Retrieve the Bin Details of PAN or network token (optional)

try: 
    # Retrieve a Payment Instrument
    api_response = api_instance.get_payment_instrument(payment_instrument_id, profile_id=profile_id, retrieve_bin_details=retrieve_bin_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->get_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_instrument_id** | **str**| The Id of a payment instrument. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 
 **retrieve_bin_details** | **bool**| Retrieve the Bin Details of PAN or network token | [optional] 

### Return type

[**PostPaymentInstrumentRequest**](PostPaymentInstrumentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_payment_instrument**
> PatchPaymentInstrumentRequest patch_payment_instrument(payment_instrument_id, patch_payment_instrument_request, profile_id=profile_id, retrieve_bin_details=retrieve_bin_details, if_match=if_match)

Update a Payment Instrument

|  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Updating a Payment Instrument**<br>Your system can use this API to update an existing Payment Instrument. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentApi()
payment_instrument_id = 'payment_instrument_id_example' # str | The Id of a payment instrument.
patch_payment_instrument_request = CyberSource.PatchPaymentInstrumentRequest() # PatchPaymentInstrumentRequest | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)
retrieve_bin_details = true # bool | Retrieve the Bin Details of PAN or network token (optional)
if_match = 'if_match_example' # str | Contains an ETag value from a GET request to make the request conditional. (optional)

try: 
    # Update a Payment Instrument
    api_response = api_instance.patch_payment_instrument(payment_instrument_id, patch_payment_instrument_request, profile_id=profile_id, retrieve_bin_details=retrieve_bin_details, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->patch_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_instrument_id** | **str**| The Id of a payment instrument. | 
 **patch_payment_instrument_request** | [**PatchPaymentInstrumentRequest**](PatchPaymentInstrumentRequest.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 
 **retrieve_bin_details** | **bool**| Retrieve the Bin Details of PAN or network token | [optional] 
 **if_match** | **str**| Contains an ETag value from a GET request to make the request conditional. | [optional] 

### Return type

[**PatchPaymentInstrumentRequest**](PatchPaymentInstrumentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_payment_instrument**
> PostPaymentInstrumentRequest post_payment_instrument(post_payment_instrument_request, profile_id=profile_id, retrieve_bin_details=retrieve_bin_details)

Create a Payment Instrument

|  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**<br><br>**Creating a Payment Instrument**<br>It is recommended you [create a Payment Instrument via a Payment Authorization](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-with-customer-token-creation_liveconsole-tab-request-body), this can be for a zero amount.<br>In Europe: You should perform Payer Authentication alongside the Authorization.|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Payment Network Tokens**<br>Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires.<br>A Payment Network Token will be automatically created and used in future payments if you are enabled for the service.<br>A Payment Network Token can also be [provisioned for an existing Instrument Identifier](#token-management_instrument-identifier_enroll-an-instrument-identifier-for-payment-network-token).<br>For more information about Payment Network Tokens see the Developer Guide.<br><br>**Payments with Payment Instruments**<br>To perform a payment with a particular Payment Instrument specify the [Payment Instrument in the payment request](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-customer-payment-instrument-and-shipping-address-token-id_liveconsole-tab-request-body). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentApi()
post_payment_instrument_request = CyberSource.PostPaymentInstrumentRequest() # PostPaymentInstrumentRequest | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)
retrieve_bin_details = true # bool | Retrieve the Bin Details of PAN or network token (optional)

try: 
    # Create a Payment Instrument
    api_response = api_instance.post_payment_instrument(post_payment_instrument_request, profile_id=profile_id, retrieve_bin_details=retrieve_bin_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->post_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_payment_instrument_request** | [**PostPaymentInstrumentRequest**](PostPaymentInstrumentRequest.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 
 **retrieve_bin_details** | **bool**| Retrieve the Bin Details of PAN or network token | [optional] 

### Return type

[**PostPaymentInstrumentRequest**](PostPaymentInstrumentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

