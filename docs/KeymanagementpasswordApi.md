# CyberSource.KeymanagementpasswordApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_password**](KeymanagementpasswordApi.md#update_password) | **PATCH** /kms/v2/keys-password/{keyId} | Activate or De-activate Password


# **update_password**
> object update_password(key_id, update_password_keys_request)

Activate or De-activate Password

Activate or De-activate key of type password 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.KeymanagementpasswordApi()
key_id = 'key_id_example' # str | Key ID. 
update_password_keys_request = CyberSource.UpdatePasswordKeysRequest() # UpdatePasswordKeysRequest | 

try: 
    # Activate or De-activate Password
    api_response = api_instance.update_password(key_id, update_password_keys_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagementpasswordApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Key ID.  | 
 **update_password_keys_request** | [**UpdatePasswordKeysRequest**](UpdatePasswordKeysRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

