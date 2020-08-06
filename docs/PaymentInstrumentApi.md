# CyberSource.PaymentInstrumentApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payment_instrument**](PaymentInstrumentApi.md#delete_payment_instrument) | **DELETE** /tms/v1/paymentinstruments/{paymentInstrumentTokenId} | Delete a Payment Instrument
[**get_payment_instrument**](PaymentInstrumentApi.md#get_payment_instrument) | **GET** /tms/v1/paymentinstruments/{paymentInstrumentTokenId} | Retrieve a Payment Instrument
[**patch_payment_instrument**](PaymentInstrumentApi.md#patch_payment_instrument) | **PATCH** /tms/v1/paymentinstruments/{paymentInstrumentTokenId} | Update a Payment Instrument
[**post_payment_instrument**](PaymentInstrumentApi.md#post_payment_instrument) | **POST** /tms/v1/paymentinstruments | Create a Payment Instrument


# **delete_payment_instrument**
> delete_payment_instrument(payment_instrument_token_id, profile_id=profile_id)

Delete a Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentApi()
payment_instrument_token_id = 'payment_instrument_token_id_example' # str | The TokenId of a payment instrument.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete a Payment Instrument
    api_instance.delete_payment_instrument(payment_instrument_token_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->delete_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_payment_instrument**
> Tmsv2customersEmbeddedDefaultPaymentInstrument get_payment_instrument(payment_instrument_token_id, profile_id=profile_id)

Retrieve a Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentApi()
payment_instrument_token_id = 'payment_instrument_token_id_example' # str | The TokenId of a payment instrument.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve a Payment Instrument
    api_response = api_instance.get_payment_instrument(payment_instrument_token_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->get_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **patch_payment_instrument**
> Tmsv2customersEmbeddedDefaultPaymentInstrument patch_payment_instrument(payment_instrument_token_id, patch_payment_instrument_request, profile_id=profile_id, if_match=if_match)

Update a Payment Instrument

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentInstrumentApi()
payment_instrument_token_id = 'payment_instrument_token_id_example' # str | The TokenId of a payment instrument.
patch_payment_instrument_request = CyberSource.PatchPaymentInstrumentRequest() # PatchPaymentInstrumentRequest | 
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)
if_match = 'if_match_example' # str | Contains an ETag value from a GET request to make the request conditional. (optional)

try: 
    # Update a Payment Instrument
    api_response = api_instance.patch_payment_instrument(payment_instrument_token_id, patch_payment_instrument_request, profile_id=profile_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->patch_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_instrument_token_id** | **str**| The TokenId of a payment instrument. | 
 **patch_payment_instrument_request** | [**PatchPaymentInstrumentRequest**](PatchPaymentInstrumentRequest.md)|  | 
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

# **post_payment_instrument**
> Tmsv2customersEmbeddedDefaultPaymentInstrument post_payment_instrument(post_payment_instrument_request, profile_id=profile_id)

Create a Payment Instrument

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
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Create a Payment Instrument
    api_response = api_instance.post_payment_instrument(post_payment_instrument_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->post_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_payment_instrument_request** | [**PostPaymentInstrumentRequest**](PostPaymentInstrumentRequest.md)|  | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultPaymentInstrument**](Tmsv2customersEmbeddedDefaultPaymentInstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

