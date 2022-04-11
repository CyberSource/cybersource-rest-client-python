# CyberSource.SymmetricKeyManagementApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_v2_shared_secret_keys**](SymmetricKeyManagementApi.md#create_v2_shared_secret_keys) | **POST** /kms/v2/keys-sym | Create Shared-Secret Keys
[**create_v2_shared_secret_keys_verifi**](SymmetricKeyManagementApi.md#create_v2_shared_secret_keys_verifi) | **POST** /kms/v2/keys-sym/verifi | Create Shared-Secret Keys as per verifi spec
[**delete_bulk_symmetric_keys**](SymmetricKeyManagementApi.md#delete_bulk_symmetric_keys) | **POST** /kms/v2/keys-sym/deletes | Delete one or more Symmetric keys
[**get_key_details**](SymmetricKeyManagementApi.md#get_key_details) | **GET** /kms/v2/keys-sym/{keyId} | Retrieves shared secret key details


# **create_v2_shared_secret_keys**
> KmsV2KeysSymPost201Response create_v2_shared_secret_keys(create_shared_secret_keys_request)

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

[**KmsV2KeysSymPost201Response**](KmsV2KeysSymPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_v2_shared_secret_keys_verifi**
> KmsV2KeysSymPost201Response create_v2_shared_secret_keys_verifi(v_ic_domain, create_shared_secret_keys_request)

Create Shared-Secret Keys as per verifi spec

Create one or more Shared-Secret Keys as per Verifi spec with 32 chars, store digest algo during key generation. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SymmetricKeyManagementApi()
v_ic_domain = 'v_ic_domain_example' # str | domain
create_shared_secret_keys_request = CyberSource.CreateSharedSecretKeysRequest1() # CreateSharedSecretKeysRequest1 | 

try: 
    # Create Shared-Secret Keys as per verifi spec
    api_response = api_instance.create_v2_shared_secret_keys_verifi(v_ic_domain, create_shared_secret_keys_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymmetricKeyManagementApi->create_v2_shared_secret_keys_verifi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v_ic_domain** | **str**| domain | 
 **create_shared_secret_keys_request** | [**CreateSharedSecretKeysRequest1**](CreateSharedSecretKeysRequest1.md)|  | 

### Return type

[**KmsV2KeysSymPost201Response**](KmsV2KeysSymPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_symmetric_keys**
> KmsV2KeysSymDeletesPost200Response delete_bulk_symmetric_keys(delete_bulk_symmetric_keys_request)

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

[**KmsV2KeysSymDeletesPost200Response**](KmsV2KeysSymDeletesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_details**
> KmsV2KeysSymGet200Response get_key_details(key_id)

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

[**KmsV2KeysSymGet200Response**](KmsV2KeysSymGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

