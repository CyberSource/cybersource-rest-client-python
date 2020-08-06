# CyberSource.AsymmetricKeyManagementApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_p12_keys**](AsymmetricKeyManagementApi.md#create_p12_keys) | **POST** /kms/v2/keys-asym | Create one or more PKCS#12 keys
[**delete_bulk_p12_keys**](AsymmetricKeyManagementApi.md#delete_bulk_p12_keys) | **POST** /kms/v2/keys-asym/deletes | Delete one or more PKCS#12 keys
[**get_p12_key_details**](AsymmetricKeyManagementApi.md#get_p12_key_details) | **GET** /kms/v2/keys-asym/{keyId} | Retrieves PKCS#12 key details


# **create_p12_keys**
> InlineResponse2011 create_p12_keys(create_p12_keys_request)

Create one or more PKCS#12 keys

'Create one or more PKCS#12 keys' 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AsymmetricKeyManagementApi()
create_p12_keys_request = CyberSource.CreateP12KeysRequest() # CreateP12KeysRequest | 

try: 
    # Create one or more PKCS#12 keys
    api_response = api_instance.create_p12_keys(create_p12_keys_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsymmetricKeyManagementApi->create_p12_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_p12_keys_request** | [**CreateP12KeysRequest**](CreateP12KeysRequest.md)|  | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_p12_keys**
> InlineResponse2003 delete_bulk_p12_keys(delete_bulk_p12_keys_request)

Delete one or more PKCS#12 keys

'Delete one or more PKCS#12 keys' 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AsymmetricKeyManagementApi()
delete_bulk_p12_keys_request = CyberSource.DeleteBulkP12KeysRequest() # DeleteBulkP12KeysRequest | 

try: 
    # Delete one or more PKCS#12 keys
    api_response = api_instance.delete_bulk_p12_keys(delete_bulk_p12_keys_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsymmetricKeyManagementApi->delete_bulk_p12_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_bulk_p12_keys_request** | [**DeleteBulkP12KeysRequest**](DeleteBulkP12KeysRequest.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_p12_key_details**
> InlineResponse2002 get_p12_key_details(key_id)

Retrieves PKCS#12 key details

Retrieves keys details by providing the key id.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AsymmetricKeyManagementApi()
key_id = 'key_id_example' # str | Key ID. 

try: 
    # Retrieves PKCS#12 key details
    api_response = api_instance.get_p12_key_details(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsymmetricKeyManagementApi->get_p12_key_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Key ID.  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

