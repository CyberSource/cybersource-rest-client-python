# CyberSource.EMVTagDetailsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_emv_tags**](EMVTagDetailsApi.md#get_emv_tags) | **GET** /tss/v2/transactions/emvTagDetails | Retrieve the EMV Dictionary
[**parse_emv_tags**](EMVTagDetailsApi.md#parse_emv_tags) | **POST** /tss/v2/transactions/emvTagDetails | Parse an EMV String


# **get_emv_tags**
> TssV2GetEmvTags200Response get_emv_tags()

Retrieve the EMV Dictionary

Returns the entire EMV tag dictionary

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.EMVTagDetailsApi()

try: 
    # Retrieve the EMV Dictionary
    api_response = api_instance.get_emv_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EMVTagDetailsApi->get_emv_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TssV2GetEmvTags200Response**](TssV2GetEmvTags200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_emv_tags**
> TssV2PostEmvTags200Response parse_emv_tags(body)

Parse an EMV String

Pass an EMV Tag-Length-Value (TLV) string for parsing.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.EMVTagDetailsApi()
body = CyberSource.Body() # Body | 

try: 
    # Parse an EMV String
    api_response = api_instance.parse_emv_tags(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EMVTagDetailsApi->parse_emv_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 

### Return type

[**TssV2PostEmvTags200Response**](TssV2PostEmvTags200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

