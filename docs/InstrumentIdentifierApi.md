# CyberSource.InstrumentIdentifierApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tms_v1_instrumentidentifiers_token_id_delete**](InstrumentIdentifierApi.md#tms_v1_instrumentidentifiers_token_id_delete) | **DELETE** /tms/v1/instrumentidentifiers/{tokenId} | Delete an Instrument Identifier
[**tms_v1_instrumentidentifiers_token_id_get**](InstrumentIdentifierApi.md#tms_v1_instrumentidentifiers_token_id_get) | **GET** /tms/v1/instrumentidentifiers/{tokenId} | Retrieve an Instrument Identifier
[**tms_v1_instrumentidentifiers_token_id_patch**](InstrumentIdentifierApi.md#tms_v1_instrumentidentifiers_token_id_patch) | **PATCH** /tms/v1/instrumentidentifiers/{tokenId} | Update a Instrument Identifier


# **tms_v1_instrumentidentifiers_token_id_delete**
> tms_v1_instrumentidentifiers_token_id_delete(profile_id, token_id)

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
    api_instance.tms_v1_instrumentidentifiers_token_id_delete(profile_id, token_id)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->tms_v1_instrumentidentifiers_token_id_delete: %s\n" % e)
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

# **tms_v1_instrumentidentifiers_token_id_get**
> TmsV1InstrumentidentifiersPost200Response tms_v1_instrumentidentifiers_token_id_get(profile_id, token_id)

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
    api_response = api_instance.tms_v1_instrumentidentifiers_token_id_get(profile_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->tms_v1_instrumentidentifiers_token_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 

### Return type

[**TmsV1InstrumentidentifiersPost200Response**](TmsV1InstrumentidentifiersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_v1_instrumentidentifiers_token_id_patch**
> TmsV1InstrumentidentifiersPost200Response tms_v1_instrumentidentifiers_token_id_patch(profile_id, token_id, body)

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
body = CyberSource.Body1() # Body1 | Please specify the previous transaction Id to update.

try: 
    # Update a Instrument Identifier
    api_response = api_instance.tms_v1_instrumentidentifiers_token_id_patch(profile_id, token_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifierApi->tms_v1_instrumentidentifiers_token_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **token_id** | **str**| The TokenId of an Instrument Identifier. | 
 **body** | [**Body1**](Body1.md)| Please specify the previous transaction Id to update. | 

### Return type

[**TmsV1InstrumentidentifiersPost200Response**](TmsV1InstrumentidentifiersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

