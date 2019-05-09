# CyberSource.InstrumentIdentifierApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instrument_identifier**](InstrumentIdentifierApi.md#create_instrument_identifier) | **POST** /tms/v1/instrumentidentifiers | Create an Instrument Identifier
[**delete_instrument_identifier**](InstrumentIdentifierApi.md#delete_instrument_identifier) | **DELETE** /tms/v1/instrumentidentifiers/{tokenId} | Delete an Instrument Identifier
[**get_all_payment_instruments**](InstrumentIdentifierApi.md#get_all_payment_instruments) | **GET** /tms/v1/instrumentidentifiers/{tokenId}/paymentinstruments | Retrieve all Payment Instruments associated with an Instrument Identifier
[**get_instrument_identifier**](InstrumentIdentifierApi.md#get_instrument_identifier) | **GET** /tms/v1/instrumentidentifiers/{tokenId} | Retrieve an Instrument Identifier
[**update_instrument_identifier**](InstrumentIdentifierApi.md#update_instrument_identifier) | **PATCH** /tms/v1/instrumentidentifiers/{tokenId} | Update a Instrument Identifier


# **create_instrument_identifier**
> TmsV1InstrumentIdentifiersPost200Response create_instrument_identifier(profile_id, create_instrument_identifier_request)

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
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
create_instrument_identifier_request = CyberSource.CreateInstrumentIdentifierRequest() # CreateInstrumentIdentifierRequest | Please specify either a Card, Bank Account or Enrollable Card

try: 
    # Create an Instrument Identifier
    api_response = api_instance.create_instrument_identifier(profile_id, create_instrument_identifier_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->create_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **create_instrument_identifier_request** | [**CreateInstrumentIdentifierRequest**](CreateInstrumentIdentifierRequest.md)| Please specify either a Card, Bank Account or Enrollable Card | 

### Return type

[**TmsV1InstrumentIdentifiersPost200Response**](TmsV1InstrumentIdentifiersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instrument_identifier**
> delete_instrument_identifier(profile_id, token_id)

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
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of an Instrument Identifier.

try: 
    # Delete an Instrument Identifier
    api_instance.delete_instrument_identifier(profile_id, token_id)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->delete_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_instruments**
> TmsV1InstrumentIdentifiersPaymentInstrumentsGet200Response get_all_payment_instruments(profile_id, token_id, offset=offset, limit=limit)

Retrieve all Payment Instruments associated with an Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of an Instrument Identifier.
offset = 0 # int | Starting Payment Instrument record in zero-based dataset that should be returned as the first object in the array. Default is 0. (optional) (default to 0)
limit = 20 # int | The maximum number of Payment Instruments that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. (optional) (default to 20)

try: 
    # Retrieve all Payment Instruments associated with an Instrument Identifier
    api_response = api_instance.get_all_payment_instruments(profile_id, token_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->get_all_payment_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 
 **offset** | **int**| Starting Payment Instrument record in zero-based dataset that should be returned as the first object in the array. Default is 0. | [optional] [default to 0]
 **limit** | **int**| The maximum number of Payment Instruments that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. | [optional] [default to 20]

### Return type

[**TmsV1InstrumentIdentifiersPaymentInstrumentsGet200Response**](TmsV1InstrumentIdentifiersPaymentInstrumentsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifier**
> TmsV1InstrumentIdentifiersPost200Response get_instrument_identifier(profile_id, token_id)

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
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of an Instrument Identifier.

try: 
    # Retrieve an Instrument Identifier
    api_response = api_instance.get_instrument_identifier(profile_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->get_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 

### Return type

[**TmsV1InstrumentIdentifiersPost200Response**](TmsV1InstrumentIdentifiersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instrument_identifier**
> TmsV1InstrumentIdentifiersPost200Response update_instrument_identifier(profile_id, token_id, update_instrument_identifier_request)

Update a Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifierApi()
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of an Instrument Identifier.
update_instrument_identifier_request = CyberSource.UpdateInstrumentIdentifierRequest() # UpdateInstrumentIdentifierRequest | Specify the previous transaction ID to update.

try: 
    # Update a Instrument Identifier
    api_response = api_instance.update_instrument_identifier(profile_id, token_id, update_instrument_identifier_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->update_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 
 **update_instrument_identifier_request** | [**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md)| Specify the previous transaction ID to update. | 

### Return type

[**TmsV1InstrumentIdentifiersPost200Response**](TmsV1InstrumentIdentifiersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

