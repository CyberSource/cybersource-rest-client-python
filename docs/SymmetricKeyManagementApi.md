# CyberSource.SymmetricKeyManagementApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_v2_shared_secret_keys**](SymmetricKeyManagementApi.md#create_v2_shared_secret_keys) | **POST** /kms/v2/keys-sym | Create Shared-Secret Keys
[**delete_bulk_symmetric_keys**](SymmetricKeyManagementApi.md#delete_bulk_symmetric_keys) | **POST** /kms/v2/keys-sym/deletes | Delete one or more Symmetric keys
[**get_key_details**](SymmetricKeyManagementApi.md#get_key_details) | **GET** /kms/v2/keys-sym/{keyId} | Retrieves shared secret key details


# **create_v2_shared_secret_keys**
> InlineResponse201 create_v2_shared_secret_keys(create_shared_secret_keys_request)

Create Shared-Secret Keys

Create one or more Shared-Secret Keys 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SymmetricKeyManagementApi()
create_shared_secret_keys_request = CyberSource.CreateSharedSecretKeysRequest() # CreateSharedSecretKeysRequest | 

try: 
    # Create Shared-Secret Keys
    api_response = api_instance.create_v2_shared_secret_keys(create_shared_secret_keys_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymmetricKeyManagementApi->create_v2_shared_secret_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_shared_secret_keys_request** | [**CreateSharedSecretKeysRequest**](CreateSharedSecretKeysRequest.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_symmetric_keys**
> InlineResponse2001 delete_bulk_symmetric_keys(delete_bulk_symmetric_keys_request)

Delete one or more Symmetric keys

'Delete one or more Symmetric keys' 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SymmetricKeyManagementApi()
delete_bulk_symmetric_keys_request = CyberSource.DeleteBulkSymmetricKeysRequest() # DeleteBulkSymmetricKeysRequest | 

try: 
    # Delete one or more Symmetric keys
    api_response = api_instance.delete_bulk_symmetric_keys(delete_bulk_symmetric_keys_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymmetricKeyManagementApi->delete_bulk_symmetric_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_bulk_symmetric_keys_request** | [**DeleteBulkSymmetricKeysRequest**](DeleteBulkSymmetricKeysRequest.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_details**
> InlineResponse200 get_key_details(key_id)

Retrieves shared secret key details

Retrieves keys details by providing the key id.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SymmetricKeyManagementApi()
key_id = 'key_id_example' # str | Key ID. 

try: 
    # Retrieves shared secret key details
    api_response = api_instance.get_key_details(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymmetricKeyManagementApi->get_key_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Key ID.  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

