# CyberSource.MerchantRegistrationApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_merchant_key**](MerchantRegistrationApi.md#activate_merchant_key) | **POST** /icc/v1/merchants/{merchantId}/keys/{keyId}/activate | Activate a merchant key
[**add_merchant_key**](MerchantRegistrationApi.md#add_merchant_key) | **POST** /icc/v1/merchants/{merchantId}/keys | Add a key to a merchant
[**get_merchant**](MerchantRegistrationApi.md#get_merchant) | **GET** /icc/v1/merchants/{merchantId} | Get a merchant
[**get_merchant_key**](MerchantRegistrationApi.md#get_merchant_key) | **GET** /icc/v1/merchants/{merchantId}/keys/{keyId} | Get a key by merchant and key ID
[**list_merchant_keys**](MerchantRegistrationApi.md#list_merchant_keys) | **GET** /icc/v1/merchants/{merchantId}/keys | List keys for a merchant
[**register_merchant**](MerchantRegistrationApi.md#register_merchant) | **POST** /icc/v1/merchants | Register a merchant
[**update_merchant**](MerchantRegistrationApi.md#update_merchant) | **PUT** /icc/v1/merchants/{merchantId} | Update a merchant
[**update_merchant_key**](MerchantRegistrationApi.md#update_merchant_key) | **PUT** /icc/v1/merchants/{merchantId}/keys/{keyId} | Update a merchant key


# **activate_merchant_key**
> ActivateMerchantKeyResponse200 activate_merchant_key(merchant_id, key_id)

Activate a merchant key

**Activate a Merchant Key**<br>Activates a deactivated encryption key for the specified merchant.<br><br> **Note:** Expired keys must be renewed via `PUT /merchants/{merchantId}/keys/{keyId}` before they can be activated.<br> Returns **403** if the merchant is deactivated or the key is expired, **404** if the merchant or key is not found, **409** if the key is already active. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantRegistrationApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_id = 'key_id_example' # str | Unique key identifier (UUID)

try: 
    # Activate a merchant key
    api_response = api_instance.activate_merchant_key(merchant_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantRegistrationApi->activate_merchant_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique merchant identifier (UUID) | 
 **key_id** | **str**| Unique key identifier (UUID) | 

### Return type

[**ActivateMerchantKeyResponse200**](ActivateMerchantKeyResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_merchant_key**
> ActivateMerchantKeyResponse200 add_merchant_key(merchant_id, key_request)

Add a key to a merchant

**Add a Key to a Merchant**<br>Adds a new encryption key for the specified merchant. The new key is created as ***active*** immediately.<br><br> **Note:** Adding a new key automatically deactivates all previously active keys for this merchant (single-active key invariant).<br> Returns **403** if the merchant is deactivated, **404** if the merchant is not found. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantRegistrationApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_request = CyberSource.KeyRequest1() # KeyRequest1 | Key creation request

try: 
    # Add a key to a merchant
    api_response = api_instance.add_merchant_key(merchant_id, key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantRegistrationApi->add_merchant_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique merchant identifier (UUID) | 
 **key_request** | [**KeyRequest1**](KeyRequest1.md)| Key creation request | 

### Return type

[**ActivateMerchantKeyResponse200**](ActivateMerchantKeyResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant**
> MerchantRegistrationResponse201 get_merchant(merchant_id)

Get a merchant

**Get a Merchant**<br>Retrieves a single merchant by its unique identifier, including all associated encryption keys.<br><br> Returns **404** if the merchant is not found. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantRegistrationApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)

try: 
    # Get a merchant
    api_response = api_instance.get_merchant(merchant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantRegistrationApi->get_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique merchant identifier (UUID) | 

### Return type

[**MerchantRegistrationResponse201**](MerchantRegistrationResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_key**
> ActivateMerchantKeyResponse200 get_merchant_key(merchant_id, key_id)

Get a key by merchant and key ID

**Get a Merchant Key**<br>Retrieves a specific encryption key by merchant ID and key ID.<br><br> Returns **404** if the merchant or key is not found. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantRegistrationApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_id = 'key_id_example' # str | Unique key identifier (UUID)

try: 
    # Get a key by merchant and key ID
    api_response = api_instance.get_merchant_key(merchant_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantRegistrationApi->get_merchant_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique merchant identifier (UUID) | 
 **key_id** | **str**| Unique key identifier (UUID) | 

### Return type

[**ActivateMerchantKeyResponse200**](ActivateMerchantKeyResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_merchant_keys**
> ListMerchantKeysResponse200 list_merchant_keys(merchant_id, status=status)

List keys for a merchant

**List Keys for a Merchant**<br>Returns all encryption keys associated with the specified merchant, with optional filtering by key status.<br><br> Returns **404** if the merchant is not found. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantRegistrationApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
status = 'status_example' # str | Filter by key status: 'active', 'deactivated', or 'expired'. Omit to return all keys. (optional)

try: 
    # List keys for a merchant
    api_response = api_instance.list_merchant_keys(merchant_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantRegistrationApi->list_merchant_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique merchant identifier (UUID) | 
 **status** | **str**| Filter by key status: &#39;active&#39;, &#39;deactivated&#39;, or &#39;expired&#39;. Omit to return all keys. | [optional] 

### Return type

[**ListMerchantKeysResponse200**](ListMerchantKeysResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_merchant**
> MerchantRegistrationResponse201 register_merchant(merchant_request)

Register a merchant

**Register a Merchant**<br>Onboards a new merchant into the Visa Merchant Registry Service (VMRS). The merchant declares how payment credentials should be delivered: cryptogram type (TAVV or DAVV), transaction indicator (TAP — Trusted Agent Protocol, ACG — Agentic Checkout Gateway, or BOTH), and whether credentials should be encrypted.<br><br> If `paymentPayloadType` is set to ***ENCRYPTED***, an `encryptionKey` must be provided.<br> Returns **409** if a merchant with the same `merchantUrl` or `vmid` already exists. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantRegistrationApi()
merchant_request = CyberSource.MerchantRequest() # MerchantRequest | Merchant registration request

try: 
    # Register a merchant
    api_response = api_instance.register_merchant(merchant_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantRegistrationApi->register_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_request** | [**MerchantRequest**](MerchantRequest.md)| Merchant registration request | 

### Return type

[**MerchantRegistrationResponse201**](MerchantRegistrationResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_merchant**
> MerchantRegistrationResponse201 update_merchant(merchant_id, merchant_update)

Update a merchant

**Update a Merchant**<br>Updates merchant configuration. The following fields can be modified: `merchantName`, `merchantUrl`, `cryptogramType`, `paymentPayloadType`, `acceptanceRelationships`, `protocolInteractions`, `webIntegrations`, and `apiIntegrations`.<br><br> Partial updates are supported — only provided fields are changed. The `vmid` and `indicator` fields cannot be updated via this endpoint.<br> Returns **400** if switching to ***ENCRYPTED*** without an active encryption key, **403** if the merchant is deactivated, **404** if not found, **409** if the new `merchantUrl` already exists. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantRegistrationApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
merchant_update = CyberSource.MerchantUpdate() # MerchantUpdate | Merchant update request

try: 
    # Update a merchant
    api_response = api_instance.update_merchant(merchant_id, merchant_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantRegistrationApi->update_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique merchant identifier (UUID) | 
 **merchant_update** | [**MerchantUpdate**](MerchantUpdate.md)| Merchant update request | 

### Return type

[**MerchantRegistrationResponse201**](MerchantRegistrationResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_merchant_key**
> ActivateMerchantKeyResponse200 update_merchant_key(merchant_id, key_id, key_update)

Update a merchant key

**Update a Merchant Key**<br>Updates encryption key information. The following fields can be modified: `keyName`, `encryptionKey`, `algorithm`, `encryptionType`, and `expirationDate`.<br><br> Returns **403** if the merchant is deactivated, key is deactivated, or key is expired, **404** if the merchant or key is not found, **409** if the new `keyName` already exists. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantRegistrationApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_id = 'key_id_example' # str | Unique key identifier (UUID)
key_update = CyberSource.KeyUpdate1() # KeyUpdate1 | Key update request

try: 
    # Update a merchant key
    api_response = api_instance.update_merchant_key(merchant_id, key_id, key_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantRegistrationApi->update_merchant_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique merchant identifier (UUID) | 
 **key_id** | **str**| Unique key identifier (UUID) | 
 **key_update** | [**KeyUpdate1**](KeyUpdate1.md)| Key update request | 

### Return type

[**ActivateMerchantKeyResponse200**](ActivateMerchantKeyResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

