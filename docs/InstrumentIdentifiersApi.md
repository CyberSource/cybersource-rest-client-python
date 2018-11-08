# CyberSource.InstrumentIdentifiersApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tms_v1_instrumentidentifiers_post**](InstrumentIdentifiersApi.md#tms_v1_instrumentidentifiers_post) | **POST** /tms/v1/instrumentidentifiers | Create an Instrument Identifier


# **tms_v1_instrumentidentifiers_post**
> TmsV1InstrumentidentifiersPost200Response tms_v1_instrumentidentifiers_post(profile_id, body)

Create an Instrument Identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InstrumentIdentifiersApi()
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration.
body = CyberSource.Body() # Body | Please specify either a Card or Bank Account.

try: 
    # Create an Instrument Identifier
    api_response = api_instance.tms_v1_instrumentidentifiers_post(profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentIdentifiersApi->tms_v1_instrumentidentifiers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | 
 **body** | [**Body**](Body.md)| Please specify either a Card or Bank Account. | 

### Return type

[**TmsV1InstrumentidentifiersPost200Response**](TmsV1InstrumentidentifiersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

