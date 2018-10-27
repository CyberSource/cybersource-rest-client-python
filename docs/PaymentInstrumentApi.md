# CyberSource.PaymentInstrumentApi

All URIs are relative to *https://api.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentinstruments_post**](PaymentInstrumentApi.md#paymentinstruments_post) | **POST** /paymentinstruments | Create a Payment Instrument
[**paymentinstruments_token_id_delete**](PaymentInstrumentApi.md#paymentinstruments_token_id_delete) | **DELETE** /paymentinstruments/{tokenId} | Delete a Payment Instrument
[**paymentinstruments_token_id_get**](PaymentInstrumentApi.md#paymentinstruments_token_id_get) | **GET** /paymentinstruments/{tokenId} | Retrieve a Payment Instrument
[**paymentinstruments_token_id_patch**](PaymentInstrumentApi.md#paymentinstruments_token_id_patch) | **PATCH** /paymentinstruments/{tokenId} | Update a Payment Instrument


# **paymentinstruments_post**
> InlineResponse2016 paymentinstruments_post(profile_id, body)

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
body = CyberSource.Body2() # Body2 | Please specify the customers payment details for card or bank account.

try: 
    # Create a Payment Instrument
    api_response = api_instance.paymentinstruments_post(profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->paymentinstruments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **body** | [**Body2**](Body2.md)| Please specify the customers payment details for card or bank account. | 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paymentinstruments_token_id_delete**
> paymentinstruments_token_id_delete(profile_id, token_id)

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
    api_instance.paymentinstruments_token_id_delete(profile_id, token_id)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->paymentinstruments_token_id_delete: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paymentinstruments_token_id_get**
> InlineResponse2016 paymentinstruments_token_id_get(profile_id, token_id)

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
    api_response = api_instance.paymentinstruments_token_id_get(profile_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->paymentinstruments_token_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paymentinstruments_token_id_patch**
> InlineResponse2016 paymentinstruments_token_id_patch(profile_id, token_id, body)

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
body = CyberSource.Body3() # Body3 | Please specify the customers payment details.

try: 
    # Update a Payment Instrument
    api_response = api_instance.paymentinstruments_token_id_patch(profile_id, token_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentApi->paymentinstruments_token_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of a Payment Instrument. | 
 **body** | [**Body3**](Body3.md)| Please specify the customers payment details. | 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

