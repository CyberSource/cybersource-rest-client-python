# CyberSource.InstrumentIdentifierApi

All URIs are relative to *https://api.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instrumentidentifiers_post**](InstrumentIdentifierApi.md#instrumentidentifiers_post) | **POST** /instrumentidentifiers | Create an Instrument Identifier
[**instrumentidentifiers_token_id_delete**](InstrumentIdentifierApi.md#instrumentidentifiers_token_id_delete) | **DELETE** /instrumentidentifiers/{tokenId} | Delete an Instrument Identifier
[**instrumentidentifiers_token_id_get**](InstrumentIdentifierApi.md#instrumentidentifiers_token_id_get) | **GET** /instrumentidentifiers/{tokenId} | Retrieve an Instrument Identifier
[**instrumentidentifiers_token_id_patch**](InstrumentIdentifierApi.md#instrumentidentifiers_token_id_patch) | **PATCH** /instrumentidentifiers/{tokenId} | Update a Instrument Identifier
[**instrumentidentifiers_token_id_paymentinstruments_get**](InstrumentIdentifierApi.md#instrumentidentifiers_token_id_paymentinstruments_get) | **GET** /instrumentidentifiers/{tokenId}/paymentinstruments | Retrieve all Payment Instruments associated with an Instrument Identifier


# **instrumentidentifiers_post**
> InlineResponse2007 instrumentidentifiers_post(profile_id, body=body)

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
body = CyberSource.Body() # Body | Please specify either a Card or Bank Account. (optional)

try: 
    # Create an Instrument Identifier
    api_response = api_instance.instrumentidentifiers_post(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->instrumentidentifiers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **body** | [**Body**](Body.md)| Please specify either a Card or Bank Account. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instrumentidentifiers_token_id_delete**
> instrumentidentifiers_token_id_delete(profile_id, token_id)

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
    api_instance.instrumentidentifiers_token_id_delete(profile_id, token_id)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->instrumentidentifiers_token_id_delete: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instrumentidentifiers_token_id_get**
> InlineResponse2007 instrumentidentifiers_token_id_get(profile_id, token_id)

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
    api_response = api_instance.instrumentidentifiers_token_id_get(profile_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->instrumentidentifiers_token_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instrumentidentifiers_token_id_patch**
> InlineResponse2007 instrumentidentifiers_token_id_patch(profile_id, token_id, body)

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
token_id = 'token_id_example' # str | The TokenId of an Instrument Identifier
body = CyberSource.Body1() # Body1 | Please specify the previous transaction Id to update.

try: 
    # Update a Instrument Identifier
    api_response = api_instance.instrumentidentifiers_token_id_patch(profile_id, token_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->instrumentidentifiers_token_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier | 
 **body** | [**Body1**](Body1.md)| Please specify the previous transaction Id to update. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instrumentidentifiers_token_id_paymentinstruments_get**
> InlineResponse2008 instrumentidentifiers_token_id_paymentinstruments_get(profile_id, token_id, offset=offset, limit=limit)

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
offset = 'offset_example' # str | Starting Payment Instrument record in zero-based dataset that should be returned as the first object in the array. Default is 0. (optional)
limit = '20' # str | The maximum number of Payment Instruments that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. (optional) (default to 20)

try: 
    # Retrieve all Payment Instruments associated with an Instrument Identifier
    api_response = api_instance.instrumentidentifiers_token_id_paymentinstruments_get(profile_id, token_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->instrumentidentifiers_token_id_paymentinstruments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 
 **offset** | **str**| Starting Payment Instrument record in zero-based dataset that should be returned as the first object in the array. Default is 0. | [optional] 
 **limit** | **str**| The maximum number of Payment Instruments that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. | [optional] [default to 20]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

