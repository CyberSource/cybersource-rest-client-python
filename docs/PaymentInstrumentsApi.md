# CyberSource.PaymentInstrumentsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tms_v1_instrumentidentifiers_token_id_paymentinstruments_get**](PaymentInstrumentsApi.md#tms_v1_instrumentidentifiers_token_id_paymentinstruments_get) | **GET** /tms/v1/instrumentidentifiers/{tokenId}/paymentinstruments | Retrieve all Payment Instruments associated with an Instrument Identifier
[**tms_v1_paymentinstruments_post**](PaymentInstrumentsApi.md#tms_v1_paymentinstruments_post) | **POST** /tms/v1/paymentinstruments | Create a Payment Instrument
[**tms_v1_paymentinstruments_token_id_delete**](PaymentInstrumentsApi.md#tms_v1_paymentinstruments_token_id_delete) | **DELETE** /tms/v1/paymentinstruments/{tokenId} | Delete a Payment Instrument
[**tms_v1_paymentinstruments_token_id_get**](PaymentInstrumentsApi.md#tms_v1_paymentinstruments_token_id_get) | **GET** /tms/v1/paymentinstruments/{tokenId} | Retrieve a Payment Instrument
[**tms_v1_paymentinstruments_token_id_patch**](PaymentInstrumentsApi.md#tms_v1_paymentinstruments_token_id_patch) | **PATCH** /tms/v1/paymentinstruments/{tokenId} | Update a Payment Instrument


# **tms_v1_instrumentidentifiers_token_id_paymentinstruments_get**
> TmsV1InstrumentidentifiersPaymentinstrumentsGet200Response tms_v1_instrumentidentifiers_token_id_paymentinstruments_get(profile_id, token_id, offset=offset, limit=limit)

Retrieve all Payment Instruments associated with an Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentsApi()
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of an Instrument Identifier.
offset = 'offset_example' # str | Starting Payment Instrument record in zero-based dataset that should be returned as the first object in the array. Default is 0. (optional)
limit = '20' # str | The maximum number of Payment Instruments that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. (optional) (default to 20)

try: 
    # Retrieve all Payment Instruments associated with an Instrument Identifier
    api_response = api_instance.tms_v1_instrumentidentifiers_token_id_paymentinstruments_get(profile_id, token_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentsApi->tms_v1_instrumentidentifiers_token_id_paymentinstruments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 
 **offset** | **str**| Starting Payment Instrument record in zero-based dataset that should be returned as the first object in the array. Default is 0. | [optional] 
 **limit** | **str**| The maximum number of Payment Instruments that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. | [optional] [default to 20]

### Return type

[**TmsV1InstrumentidentifiersPaymentinstrumentsGet200Response**](TmsV1InstrumentidentifiersPaymentinstrumentsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_v1_paymentinstruments_post**
> TmsV1PaymentinstrumentsPost201Response tms_v1_paymentinstruments_post(profile_id, body)

Create a Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentsApi()
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
body = CyberSource.Body2() # Body2 | Please specify the customers payment details for card or bank account.

try: 
    # Create a Payment Instrument
    api_response = api_instance.tms_v1_paymentinstruments_post(profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentsApi->tms_v1_paymentinstruments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **body** | [**Body2**](Body2.md)| Please specify the customers payment details for card or bank account. | 

### Return type

[**TmsV1PaymentinstrumentsPost201Response**](TmsV1PaymentinstrumentsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_v1_paymentinstruments_token_id_delete**
> tms_v1_paymentinstruments_token_id_delete(profile_id, token_id)

Delete a Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentsApi()
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.

try: 
    # Delete a Payment Instrument
    api_instance.tms_v1_paymentinstruments_token_id_delete(profile_id, token_id)
except ApiException as e:
    print("Exception when calling PaymentInstrumentsApi->tms_v1_paymentinstruments_token_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_v1_paymentinstruments_token_id_get**
> TmsV1PaymentinstrumentsPost201Response tms_v1_paymentinstruments_token_id_get(profile_id, token_id)

Retrieve a Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentsApi()
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.

try: 
    # Retrieve a Payment Instrument
    api_response = api_instance.tms_v1_paymentinstruments_token_id_get(profile_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentsApi->tms_v1_paymentinstruments_token_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 

### Return type

[**TmsV1PaymentinstrumentsPost201Response**](TmsV1PaymentinstrumentsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_v1_paymentinstruments_token_id_patch**
> TmsV1PaymentinstrumentsPost201Response tms_v1_paymentinstruments_token_id_patch(profile_id, token_id, body)

Update a Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentsApi()
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.
body = CyberSource.Body3() # Body3 | Please specify the customers payment details.

try: 
    # Update a Payment Instrument
    api_response = api_instance.tms_v1_paymentinstruments_token_id_patch(profile_id, token_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentsApi->tms_v1_paymentinstruments_token_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 
 **body** | [**Body3**](Body3.md)| Please specify the customers payment details. | 

### Return type

[**TmsV1PaymentinstrumentsPost201Response**](TmsV1PaymentinstrumentsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

