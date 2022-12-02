# CyberSource.KeymanagementscmpApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_scmp**](KeymanagementscmpApi.md#update_scmp) | **PATCH** /kms/v2/keys-scmp/{keyId} | Update or Deactivate


# **update_scmp**
> object update_scmp(key_id, update_pgp_keys_request)

Update or Deactivate

Update or Deactivate scmp api Key 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.KeymanagementscmpApi()
key_id = 'key_id_example' # str | Key ID. 
update_pgp_keys_request = CyberSource.UpdatePGPKeysRequest1() # UpdatePGPKeysRequest1 | 

try: 
    # Update or Deactivate
    api_response = api_instance.update_scmp(key_id, update_pgp_keys_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagementscmpApi->update_scmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Key ID.  | 
 **update_pgp_keys_request** | [**UpdatePGPKeysRequest1**](UpdatePGPKeysRequest1.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

