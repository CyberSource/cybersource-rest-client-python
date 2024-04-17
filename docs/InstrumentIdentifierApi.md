# CyberSource.InstrumentIdentifierApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instrument_identifier**](InstrumentIdentifierApi.md#delete_instrument_identifier) | **DELETE** /tms/v1/instrumentidentifiers/{instrumentIdentifierId} | Delete an Instrument Identifier
[**get_instrument_identifier**](InstrumentIdentifierApi.md#get_instrument_identifier) | **GET** /tms/v1/instrumentidentifiers/{instrumentIdentifierId} | Retrieve an Instrument Identifier
[**get_instrument_identifier_payment_instruments_list**](InstrumentIdentifierApi.md#get_instrument_identifier_payment_instruments_list) | **GET** /tms/v1/instrumentidentifiers/{instrumentIdentifierId}/paymentinstruments | List Payment Instruments for an Instrument Identifier
[**patch_instrument_identifier**](InstrumentIdentifierApi.md#patch_instrument_identifier) | **PATCH** /tms/v1/instrumentidentifiers/{instrumentIdentifierId} | Update an Instrument Identifier
[**post_instrument_identifier**](InstrumentIdentifierApi.md#post_instrument_identifier) | **POST** /tms/v1/instrumentidentifiers | Create an Instrument Identifier
[**post_instrument_identifier_enrollment**](InstrumentIdentifierApi.md#post_instrument_identifier_enrollment) | **POST** /tms/v1/instrumentidentifiers/{instrumentIdentifierId}/enrollment | Enroll an Instrument Identifier for Payment Network Token


# **delete_instrument_identifier**
> delete_instrument_identifier(instrument_identifier_id, profile_id=profile_id)

Delete an Instrument Identifier

|  |  |  | | --- | --- | --- | |**Instrument Identifiers**<br>An Instrument Identifier represents either a card number, or in the case of an ACH bank account, the routing <br>and account numbers.<br>The same token Id is returned for a specific card number or bank account & routing number allowing the <br>Instrument Identifier Id to be used for cross-channel payment tracking.<br>An Instrument Identifier can exist independently but also be associated with a [Customer Payment Instrument](#token-management_customer-payment-instrument_create-a-customer-payment-instrument) <br>or [Standalone Payment Instrument](#token-management_payment-instrument_create-a-payment-instrument).|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Deleting an Instrument Identifier**<br>Your system can use this API to delete an existing Instrument Identifier.<br>An Instrument Identifier cannot be deleted if it is linked to any Payment Instruments.<br>You can [retrieve all Payment Instruments associated with an Instrument Identifier](#token-management_instrument-identifier_list-payment-instruments-for-an-instrument-identifier). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_id = 'instrument_identifier_id_example' # str | The Id of an Instrument Identifier.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete an Instrument Identifier
    api_instance.delete_instrument_identifier(instrument_identifier_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->delete_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_id** | **str**| The Id of an Instrument Identifier. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifier**
> PostInstrumentIdentifierRequest get_instrument_identifier(instrument_identifier_id, profile_id=profile_id)

Retrieve an Instrument Identifier

|  |  |  | | --- | --- | --- | |**Instrument Identifiers**<br>An Instrument Identifier represents either a card number, or in the case of an ACH bank account, the routing and account number.<br>The same token Id is returned for a specific card number or bank account & routing number allowing the Instrument Identifier Id to be used for cross-channel payment tracking.<br>An Instrument Identifier can exist independently but also be associated with a [Customer Payment Instrument](#token-management_customer-payment-instrument_create-a-customer-payment-instrument) or [Standalone Payment Instrument](#token-management_payment-instrument_create-a-payment-instrument).<br><br>**Retrieving an Instrument Identifier**<br>Your system can use this API to retrieve an Instrument Identifier.<br>**Note: the actual card data will be masked.**<br>The Instrument Identifier will also be returned when retrieving a [Customer](#token-management_customer_retrieve-a-customer), [Customer Payment Instrument](#token-management_customer-payment-instrument_retrieve-a-customer-payment-instrument) or [Standalone Payment Instrument](#token-management_payment-instrument_retrieve-a-payment-instrument).|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Payment Network Tokens**<br>Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires.<br>A Payment Network Token will be automatically created and used in future payments if you are enabled for the service.<br>A Payment Network Token can also be [provisioned for an existing Instrument Identifier](#token-management_instrument-identifier_enroll-an-instrument-identifier-for-payment-network-token).<br>For more information about Payment Network Tokens see the Developer Guide.<br><br>**Payments with Instrument Identifiers**<br>To perform a payment with an Instrument Identifier simply specify the [Instrument Identifier Id in the payments request along with the expiration date, card type, & billing address](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-instrument-identifier-token-id_liveconsole-tab-request-body).<br>When an Instrument Identifier is used in a payment the **_previousTransactionId_** and **_originalAuthorizedAmount_** values are automatically recorded.<br>These values will be added for you to future Merchant Initiated Transaction payments. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_id = 'instrument_identifier_id_example' # str | The Id of an Instrument Identifier.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve an Instrument Identifier
    api_response = api_instance.get_instrument_identifier(instrument_identifier_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->get_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_id** | **str**| The Id of an Instrument Identifier. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**PostInstrumentIdentifierRequest**](PostInstrumentIdentifierRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifier_payment_instruments_list**
> PaymentInstrumentList1 get_instrument_identifier_payment_instruments_list(instrument_identifier_id, profile_id=profile_id, offset=offset, limit=limit)

List Payment Instruments for an Instrument Identifier

|  |  |  | | --- | --- | --- | |**Instrument Identifiers**<br>An Instrument Identifier represents either a card number, or in the case of an ACH bank account, the routing <br>and account numbers.<br>The same token Id is returned for a specific card number or bank account & routing number allowing the <br>Instrument Identifier Id to be used for cross-channel payment tracking.<br>An Instrument Identifier can exist independently but also be associated with a [Customer Payment Instrument](#token-management_customer-payment-instrument_create-a-customer-payment-instrument) <br>or [Standalone Payment Instrument](#token-management_payment-instrument_create-a-payment-instrument).|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Retrieving all Payment Instruments associated with an Instrument Identifier**<br>Your system can use this API to retrieve all Payment Instruments linked to an Instrument Identifier. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_id = 'instrument_identifier_id_example' # str | The Id of an Instrument Identifier.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)
offset = 0 # int | Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. (optional) (default to 0)
limit = 20 # int | The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. (optional) (default to 20)

try: 
    # List Payment Instruments for an Instrument Identifier
    api_response = api_instance.get_instrument_identifier_payment_instruments_list(instrument_identifier_id, profile_id=profile_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->get_instrument_identifier_payment_instruments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_id** | **str**| The Id of an Instrument Identifier. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 
 **offset** | **int**| Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. | [optional] [default to 0]
 **limit** | **int**| The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. | [optional] [default to 20]

### Return type

[**PaymentInstrumentList1**](PaymentInstrumentList1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_instrument_identifier**
> PatchInstrumentIdentifierRequest patch_instrument_identifier(instrument_identifier_id, patch_instrument_identifier_request, profile_id=profile_id, if_match=if_match)

Update an Instrument Identifier

|  |  |  | | --- | --- | --- | |**Instrument Identifiers**<br>An Instrument Identifier represents either a card number, or in the case of an ACH bank account, the routing and account number.<br>The same token Id is returned for a specific card number or bank account & routing number allowing the Instrument Identifier Id to be used for cross-channel payment tracking.<br>An Instrument Identifier can exist independently but also be associated with a [Customer Payment Instrument](#token-management_customer-payment-instrument_create-a-customer-payment-instrument) or [Standalone Payment Instrument](#token-management_payment-instrument_create-a-payment-instrument).|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Updating an Instrument Identifier**<br>When an Instrument Identifier is used in a payment the **_previousTransactionId_** and **_originalAuthorizedAmount_** values are automatically recorded.<br>These values will be added for you to future Merchant Initiated Transaction payments.<br>Your system can use this API to update these values. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_id = 'instrument_identifier_id_example' # str | The Id of an Instrument Identifier.
patch_instrument_identifier_request = CyberSource.PatchInstrumentIdentifierRequest() # PatchInstrumentIdentifierRequest | Specify the previous transaction Id to update.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)
if_match = 'if_match_example' # str | Contains an ETag value from a GET request to make the request conditional. (optional)

try: 
    # Update an Instrument Identifier
    api_response = api_instance.patch_instrument_identifier(instrument_identifier_id, patch_instrument_identifier_request, profile_id=profile_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->patch_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_id** | **str**| The Id of an Instrument Identifier. | 
 **patch_instrument_identifier_request** | [**PatchInstrumentIdentifierRequest**](PatchInstrumentIdentifierRequest.md)| Specify the previous transaction Id to update. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 
 **if_match** | **str**| Contains an ETag value from a GET request to make the request conditional. | [optional] 

### Return type

[**PatchInstrumentIdentifierRequest**](PatchInstrumentIdentifierRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_instrument_identifier**
> PostInstrumentIdentifierRequest post_instrument_identifier(post_instrument_identifier_request, profile_id=profile_id)

Create an Instrument Identifier

|  |  |  | | --- | --- | --- | |**Instrument Identifiers**<br>An Instrument Identifier represents either a card number, or in the case of an ACH bank account, the routing and account number.<br>The same token Id is returned for a specific card number or bank account & routing number allowing the Instrument Identifier Id to be used for cross-channel payment tracking.<br>An Instrument Identifier can exist independently but also be associated with a [Customer Payment Instrument](#token-management_customer-payment-instrument_create-a-customer-payment-instrument) or [Standalone Payment Instrument](#token-management_payment-instrument_create-a-payment-instrument).<br><br>**Creating an Instrument Identifier**<br>It is recommended you [create an Instrument Identifier via a Payment Authorization](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-with-instrument-identifier-token-creation_liveconsole-tab-request-body), this can be for a zero amount.<br>An Instrument Identifier will also be created if you [create a Customer via a Payment Authorization](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-with-customer-token-creation_liveconsole-tab-request-body)<br>In Europe: You should perform Payer Authentication alongside the Authorization.|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Payment Network Tokens**<br>Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires.<br>A Payment Network Token will be automatically created and used in future payments if you are enabled for the service.<br>A Payment Network Token can also be [provisioned for an existing Instrument Identifier](#token-management_instrument-identifier_enroll-an-instrument-identifier-for-payment-network-token).<br>For more information about Payment Network Tokens see the Developer Guide.<br><br>**Payments with Instrument Identifiers**<br>To perform a payment with an Instrument Identifier simply specify the [Instrument Identifier Id in the payments request along with the expiration date, card type, & billing address](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-instrument-identifier-token-id_liveconsole-tab-request-body).<br>When an Instrument Identifier is used in a payment the **_previousTransactionId_** and **_originalAuthorizedAmount_** values are automatically recorded.<br>These values will be added for you to future Merchant Initiated Transaction payments. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
post_instrument_identifier_request = CyberSource.PostInstrumentIdentifierRequest() # PostInstrumentIdentifierRequest | Specify either a Card, Bank Account or Enrollable Card
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Create an Instrument Identifier
    api_response = api_instance.post_instrument_identifier(post_instrument_identifier_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->post_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_instrument_identifier_request** | [**PostInstrumentIdentifierRequest**](PostInstrumentIdentifierRequest.md)| Specify either a Card, Bank Account or Enrollable Card | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**PostInstrumentIdentifierRequest**](PostInstrumentIdentifierRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_instrument_identifier_enrollment**
> post_instrument_identifier_enrollment(instrument_identifier_id, post_instrument_identifier_enrollment_request, profile_id=profile_id)

Enroll an Instrument Identifier for Payment Network Token

|  |  |  | | --- | --- | --- | |**Instrument Identifiers**<br>An Instrument Identifier represents either a card number, or in the case of an ACH bank account, the routing and account number.<br>The same token Id is returned for a specific card number or bank account & routing number allowing the Instrument Identifier Id to be used for cross-channel payment tracking.<br>An Instrument Identifier can exist independently but also be associated with a [Customer Payment Instrument](#token-management_customer-payment-instrument_create-a-customer-payment-instrument) or [Standalone Payment Instrument](#token-management_payment-instrument_create-a-payment-instrument).|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Enroll an Instrument Identifier for a Payment Network Token**<br>Your system can use this API to provision a Network token for an existing Instrument Identifier.<br>Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires.<br>A Network token can be [provisioned when creating an Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier_samplerequests-dropdown_create-instrument-identifier-card-enroll-for-network-token_liveconsole-tab-request-body).This will occur automatically when creating a [Customer](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-with-customer-token-creation_liveconsole-tab-request-body), [Payment Instrument](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-create-default-payment-instrument-shipping-address-for-existing-customer_liveconsole-tab-request-body) or [Instrument Identifier](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-with-instrument-identifier-token-creation_liveconsole-tab-request-body) via the Payments API.<br>For more information about Payment Network Tokens see the Developer Guide. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_id = 'instrument_identifier_id_example' # str | The Id of an Instrument Identifier.
post_instrument_identifier_enrollment_request = CyberSource.PostInstrumentIdentifierEnrollmentRequest() # PostInstrumentIdentifierEnrollmentRequest | Specify Enrollable Card details
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Enroll an Instrument Identifier for Payment Network Token
    api_instance.post_instrument_identifier_enrollment(instrument_identifier_id, post_instrument_identifier_enrollment_request, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->post_instrument_identifier_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_id** | **str**| The Id of an Instrument Identifier. | 
 **post_instrument_identifier_enrollment_request** | [**PostInstrumentIdentifierEnrollmentRequest**](PostInstrumentIdentifierEnrollmentRequest.md)| Specify Enrollable Card details | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

