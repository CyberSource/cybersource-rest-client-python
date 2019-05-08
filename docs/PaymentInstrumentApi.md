# CyberSource.PaymentInstrumentApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_instrument**](PaymentInstrumentApi.md#create_payment_instrument) | **POST** /tms/v1/paymentinstruments | Create a Payment Instrument
[**delete_payment_instrument**](PaymentInstrumentApi.md#delete_payment_instrument) | **DELETE** /tms/v1/paymentinstruments/{tokenId} | Delete a Payment Instrument
[**get_payment_instrument**](PaymentInstrumentApi.md#get_payment_instrument) | **GET** /tms/v1/paymentinstruments/{tokenId} | Retrieve a Payment Instrument
[**update_payment_instrument**](PaymentInstrumentApi.md#update_payment_instrument) | **PATCH** /tms/v1/paymentinstruments/{tokenId} | Update a Payment Instrument


# **create_payment_instrument**
> TmsV1PaymentinstrumentsPatch200Response create_payment_instrument(profile_id, create_payment_instrument_request)

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
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
create_payment_instrument_request = CyberSource.CreatePaymentInstrumentRequest() # CreatePaymentInstrumentRequest | Specify the customer's payment details for card or bank account.

try: 
    # Create a Payment Instrument
    api_response = api_instance.create_payment_instrument(profile_id, create_payment_instrument_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->create_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **create_payment_instrument_request** | [**CreatePaymentInstrumentRequest**](CreatePaymentInstrumentRequest.md)| Specify the customer&#39;s payment details for card or bank account. | 

### Return type

[**TmsV1PaymentinstrumentsPatch200Response**](TmsV1PaymentinstrumentsPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_instrument**
> delete_payment_instrument(profile_id, token_id)

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
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.

try: 
    # Delete a Payment Instrument
    api_instance.delete_payment_instrument(profile_id, token_id)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->delete_payment_instrument: %s\n" % e)
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

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_instrument**
> TmsV1PaymentinstrumentsPatch200Response get_payment_instrument(profile_id, token_id)

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
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.

try: 
    # Retrieve a Payment Instrument
    api_response = api_instance.get_payment_instrument(profile_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->get_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 

### Return type

[**TmsV1PaymentinstrumentsPatch200Response**](TmsV1PaymentinstrumentsPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_instrument**
> TmsV1PaymentinstrumentsPatch200Response update_payment_instrument(profile_id, token_id, update_payment_instrument_request)

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
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.
update_payment_instrument_request = CyberSource.UpdatePaymentInstrumentRequest() # UpdatePaymentInstrumentRequest | Specify the customer's payment details.

try: 
    # Update a Payment Instrument
    api_response = api_instance.update_payment_instrument(profile_id, token_id, update_payment_instrument_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->update_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 
 **update_payment_instrument_request** | [**UpdatePaymentInstrumentRequest**](UpdatePaymentInstrumentRequest.md)| Specify the customer&#39;s payment details. | 

### Return type

[**TmsV1PaymentinstrumentsPatch200Response**](TmsV1PaymentinstrumentsPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

