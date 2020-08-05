# CyberSource.InstrumentIdentifierApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instrument_identifier**](InstrumentIdentifierApi.md#delete_instrument_identifier) | **DELETE** /tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId} | Delete an Instrument Identifier
[**get_instrument_identifier**](InstrumentIdentifierApi.md#get_instrument_identifier) | **GET** /tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId} | Retrieve an Instrument Identifier
[**get_instrument_identifier_payment_instruments_list**](InstrumentIdentifierApi.md#get_instrument_identifier_payment_instruments_list) | **GET** /tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}/paymentinstruments | List Payment Instruments for an Instrument Identifier
[**patch_instrument_identifier**](InstrumentIdentifierApi.md#patch_instrument_identifier) | **PATCH** /tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId} | Update an Instrument Identifier
[**post_instrument_identifier**](InstrumentIdentifierApi.md#post_instrument_identifier) | **POST** /tms/v1/instrumentidentifiers | Create an Instrument Identifier


# **delete_instrument_identifier**
> delete_instrument_identifier(instrument_identifier_token_id, profile_id=profile_id)

Delete an Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_token_id = 'instrument_identifier_token_id_example' # str | The TokenId of a Instrument Identifier.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete an Instrument Identifier
    api_instance.delete_instrument_identifier(instrument_identifier_token_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->delete_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_token_id** | **str**| The TokenId of a Instrument Identifier. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifier**
> Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier get_instrument_identifier(instrument_identifier_token_id, profile_id=profile_id)

Retrieve an Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_token_id = 'instrument_identifier_token_id_example' # str | The TokenId of a Instrument Identifier.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve an Instrument Identifier
    api_response = api_instance.get_instrument_identifier(instrument_identifier_token_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->get_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_token_id** | **str**| The TokenId of a Instrument Identifier. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier**](Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifier_payment_instruments_list**
> PaymentInstrumentListForCustomer get_instrument_identifier_payment_instruments_list(instrument_identifier_token_id, profile_id=profile_id, offset=offset, limit=limit)

List Payment Instruments for an Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_token_id = 'instrument_identifier_token_id_example' # str | The TokenId of a Instrument Identifier.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)
offset = 0 # int | Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. (optional) (default to 0)
limit = 20 # int | The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. (optional) (default to 20)

try: 
    # List Payment Instruments for an Instrument Identifier
    api_response = api_instance.get_instrument_identifier_payment_instruments_list(instrument_identifier_token_id, profile_id=profile_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->get_instrument_identifier_payment_instruments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_token_id** | **str**| The TokenId of a Instrument Identifier. | 
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

# **patch_instrument_identifier**
> Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier patch_instrument_identifier(instrument_identifier_token_id, patch_instrument_identifier_request, profile_id=profile_id, if_match=if_match)

Update an Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
instrument_identifier_token_id = 'instrument_identifier_token_id_example' # str | The TokenId of a Instrument Identifier.
patch_instrument_identifier_request = CyberSource.PatchInstrumentIdentifierRequest() # PatchInstrumentIdentifierRequest | Specify the previous transaction ID to update.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)
if_match = 'if_match_example' # str | Contains an ETag value from a GET request to make the request conditional. (optional)

try: 
    # Update an Instrument Identifier
    api_response = api_instance.patch_instrument_identifier(instrument_identifier_token_id, patch_instrument_identifier_request, profile_id=profile_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->patch_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_token_id** | **str**| The TokenId of a Instrument Identifier. | 
 **patch_instrument_identifier_request** | [**PatchInstrumentIdentifierRequest**](PatchInstrumentIdentifierRequest.md)| Specify the previous transaction ID to update. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 
 **if_match** | **str**| Contains an ETag value from a GET request to make the request conditional. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier**](Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_instrument_identifier**
> Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier post_instrument_identifier(post_instrument_identifier_request, profile_id=profile_id)

Create an Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
post_instrument_identifier_request = CyberSource.PostInstrumentIdentifierRequest() # PostInstrumentIdentifierRequest | Please specify either a Card, Bank Account or Enrollable Card
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

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
 **post_instrument_identifier_request** | [**PostInstrumentIdentifierRequest**](PostInstrumentIdentifierRequest.md)| Please specify either a Card, Bank Account or Enrollable Card | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier**](Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

