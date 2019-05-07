# CyberSource.PaymentInstrumentApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_instrument**](PaymentInstrumentApi.md#create_payment_instrument) | **POST** /tms/v1/paymentinstruments | Create a Payment Instrument
[**delete_payment_instrument**](PaymentInstrumentApi.md#delete_payment_instrument) | **DELETE** /tms/v1/paymentinstruments/{tokenId} | Delete a Payment Instrument
[**get_payment_instrument**](PaymentInstrumentApi.md#get_payment_instrument) | **GET** /tms/v1/paymentinstruments/{tokenId} | Retrieve a Payment Instrument
[**update_payment_instrument**](PaymentInstrumentApi.md#update_payment_instrument) | **PATCH** /tms/v1/paymentinstruments/{tokenId} | Update a Payment Instrument


# **create_payment_instrument**
> TmsV1PaymentinstrumentsPatch200Response create_payment_instrument(profile_id, v_c_merchant_id, v_c_correlation_id, create_payment_instrument_request, client_application=client_application)

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
v_c_merchant_id = 'v_c_merchant_id_example' # str | CyberSource merchant id.
v_c_correlation_id = 'v_c_correlation_id_example' # str | The mandatory correlation id passed by upstream (calling) system.
create_payment_instrument_request = CyberSource.CreatePaymentInstrumentRequest() # CreatePaymentInstrumentRequest | Specify the customer's payment details for card or bank account.
client_application = 'client_application_example' # str | Client application name (optional)

try: 
    # Create a Payment Instrument
    api_response = api_instance.create_payment_instrument(profile_id, v_c_merchant_id, v_c_correlation_id, create_payment_instrument_request, client_application=client_application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->create_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **v_c_merchant_id** | **str**| CyberSource merchant id. | 
 **v_c_correlation_id** | **str**| The mandatory correlation id passed by upstream (calling) system. | 
 **create_payment_instrument_request** | [**CreatePaymentInstrumentRequest**](CreatePaymentInstrumentRequest.md)| Specify the customer&#39;s payment details for card or bank account. | 
 **client_application** | **str**| Client application name | [optional] 

### Return type

[**TmsV1PaymentinstrumentsPatch200Response**](TmsV1PaymentinstrumentsPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_instrument**
> delete_payment_instrument(profile_id, v_c_merchant_id, v_c_correlation_id, token_id, client_application=client_application)

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
v_c_merchant_id = 'v_c_merchant_id_example' # str | CyberSource merchant id.
v_c_correlation_id = 'v_c_correlation_id_example' # str | The mandatory correlation id passed by upstream (calling) system.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.
client_application = 'client_application_example' # str | Client application name (optional)

try: 
    # Delete a Payment Instrument
    api_instance.delete_payment_instrument(profile_id, v_c_merchant_id, v_c_correlation_id, token_id, client_application=client_application)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->delete_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **v_c_merchant_id** | **str**| CyberSource merchant id. | 
 **v_c_correlation_id** | **str**| The mandatory correlation id passed by upstream (calling) system. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 
 **client_application** | **str**| Client application name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_instrument**
> TmsV1PaymentinstrumentsPatch200Response get_payment_instrument(profile_id, v_c_merchant_id, v_c_correlation_id, token_id, client_application=client_application)

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
v_c_merchant_id = 'v_c_merchant_id_example' # str | CyberSource merchant id.
v_c_correlation_id = 'v_c_correlation_id_example' # str | The mandatory correlation id passed by upstream (calling) system.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.
client_application = 'client_application_example' # str | Client application name (optional)

try: 
    # Retrieve a Payment Instrument
    api_response = api_instance.get_payment_instrument(profile_id, v_c_merchant_id, v_c_correlation_id, token_id, client_application=client_application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->get_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **v_c_merchant_id** | **str**| CyberSource merchant id. | 
 **v_c_correlation_id** | **str**| The mandatory correlation id passed by upstream (calling) system. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 
 **client_application** | **str**| Client application name | [optional] 

### Return type

[**TmsV1PaymentinstrumentsPatch200Response**](TmsV1PaymentinstrumentsPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_instrument**
> TmsV1PaymentinstrumentsPatch200Response update_payment_instrument(profile_id, v_c_merchant_id, v_c_correlation_id, token_id, update_payment_instrument_request, client_application=client_application)

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
v_c_merchant_id = 'v_c_merchant_id_example' # str | CyberSource merchant id.
v_c_correlation_id = 'v_c_correlation_id_example' # str | The mandatory correlation id passed by upstream (calling) system.
token_id = 'token_id_example' # str | The TokenId of a Payment Instrument.
update_payment_instrument_request = CyberSource.UpdatePaymentInstrumentRequest() # UpdatePaymentInstrumentRequest | Specify the customer's payment details.
client_application = 'client_application_example' # str | Client application name (optional)

try: 
    # Update a Payment Instrument
    api_response = api_instance.update_payment_instrument(profile_id, v_c_merchant_id, v_c_correlation_id, token_id, update_payment_instrument_request, client_application=client_application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->update_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **v_c_merchant_id** | **str**| CyberSource merchant id. | 
 **v_c_correlation_id** | **str**| The mandatory correlation id passed by upstream (calling) system. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 
 **update_payment_instrument_request** | [**UpdatePaymentInstrumentRequest**](UpdatePaymentInstrumentRequest.md)| Specify the customer&#39;s payment details. | 
 **client_application** | **str**| Client application name | [optional] 

### Return type

[**TmsV1PaymentinstrumentsPatch200Response**](TmsV1PaymentinstrumentsPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

