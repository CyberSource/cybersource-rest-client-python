# CyberSource.KeymanagementpgpApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_pgp**](KeymanagementpgpApi.md#update_pgp) | **PATCH** /kms/v2/keys-pgp/{keyId} | Activate or De-activate PGP Key


# **update_pgp**
> object update_pgp(key_id, update_pgp_keys_request)

Activate or De-activate PGP Key

Activate or De-activate PGP Key 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.KeymanagementpgpApi()
key_id = 'key_id_example' # str | Key ID. 
update_pgp_keys_request = CyberSource.UpdatePGPKeysRequest() # UpdatePGPKeysRequest | 

try: 
    # Activate or De-activate PGP Key
    api_response = api_instance.update_pgp(key_id, update_pgp_keys_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagementpgpApi->update_pgp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Key ID.  | 
 **update_pgp_keys_request** | [**UpdatePGPKeysRequest**](UpdatePGPKeysRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

