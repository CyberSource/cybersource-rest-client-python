# CyberSource.MerchantCapabilitiesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_merchant_key**](MerchantCapabilitiesApi.md#activate_merchant_key) | **POST** /icc/v1/merchants/{merchantId}/keys/{keyId}/activate | Activate a merchant key
[**add_merchant_key**](MerchantCapabilitiesApi.md#add_merchant_key) | **POST** /icc/v1/merchants/{merchantId}/keys | Add a key to a merchant
[**deactivate_merchant_key**](MerchantCapabilitiesApi.md#deactivate_merchant_key) | **DELETE** /icc/v1/merchants/{merchantId}/keys/{keyId} | Deactivate a merchant key
[**get_merchant**](MerchantCapabilitiesApi.md#get_merchant) | **GET** /icc/v1/merchants/{merchantId} | Get a merchant
[**get_merchant_key**](MerchantCapabilitiesApi.md#get_merchant_key) | **GET** /icc/v1/merchants/{merchantId}/keys/{keyId} | Get a key by merchant and key ID
[**list_merchant_keys**](MerchantCapabilitiesApi.md#list_merchant_keys) | **GET** /icc/v1/merchants/{merchantId}/keys | List keys for a merchant
[**register_merchant**](MerchantCapabilitiesApi.md#register_merchant) | **POST** /icc/v1/merchants | Register a merchant
[**update_merchant**](MerchantCapabilitiesApi.md#update_merchant) | **PUT** /icc/v1/merchants/{merchantId} | Update a merchant
[**update_merchant_key**](MerchantCapabilitiesApi.md#update_merchant_key) | **PUT** /icc/v1/merchants/{merchantId}/keys/{keyId} | Update a merchant key


# **activate_merchant_key**
> ActivateMerchantKeyResponse200 activate_merchant_key(merchant_id, key_id)

Activate a merchant key

Activate a deactivated key. Raises 403 if merchant is deactivated, 404 if merchant or key not found, 409 if key is already active.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_id = 'key_id_example' # str | Unique key identifier (UUID)

try: 
    # Activate a merchant key
    api_response = api_instance.activate_merchant_key(merchant_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->activate_merchant_key: %s\n" % e)
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

Add a new encryption key for a merchant. Raises 401 if not authenticated, 403 if caller does not own the merchant, 404 if merchant not found.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_request = CyberSource.KeyRequest1() # KeyRequest1 | Key creation request

try: 
    # Add a key to a merchant
    api_response = api_instance.add_merchant_key(merchant_id, key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->add_merchant_key: %s\n" % e)
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

# **deactivate_merchant_key**
> DeactivateMerchantKeyResponse200 deactivate_merchant_key(merchant_id, key_id)

Deactivate a merchant key

Deactivate a key (soft delete). Raises 401 if not authenticated, 403 if caller does not own the merchant, 404 if key not found.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_id = 'key_id_example' # str | Unique key identifier (UUID)

try: 
    # Deactivate a merchant key
    api_response = api_instance.deactivate_merchant_key(merchant_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->deactivate_merchant_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique merchant identifier (UUID) | 
 **key_id** | **str**| Unique key identifier (UUID) | 

### Return type

[**DeactivateMerchantKeyResponse200**](DeactivateMerchantKeyResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant**
> MerchantRegistrationResponse201 get_merchant(merchant_id)

Get a merchant

Get merchant by ID with all associated keys. Raises 404 if merchant not found.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)

try: 
    # Get a merchant
    api_response = api_instance.get_merchant(merchant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->get_merchant: %s\n" % e)
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

Get a specific key by merchant ID and key ID. Raises 401 if not authenticated, 404 if key not found.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_id = 'key_id_example' # str | Unique key identifier (UUID)

try: 
    # Get a key by merchant and key ID
    api_response = api_instance.get_merchant_key(merchant_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->get_merchant_key: %s\n" % e)
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

List all keys for a specific merchant with optional filtering by status. Raises 404 if merchant not found.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
status = 'status_example' # str | Filter by key status: 'active', 'deactivated', or 'expired'. Omit to return all keys. (optional)

try: 
    # List keys for a merchant
    api_response = api_instance.list_merchant_keys(merchant_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->list_merchant_keys: %s\n" % e)
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

Onboard a new merchant into the VMRS. The merchant declares how they want payment data delivered: cryptogram type (TAVV or DAVV), transaction indicator (TAP, ACG, or Both), whether credentials should be encrypted, and their public encryption key if encryption is enabled. Raises 409 if merchantUrl or vmid already exists.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_request = CyberSource.MerchantRequest() # MerchantRequest | Merchant registration request

try: 
    # Register a merchant
    api_response = api_instance.register_merchant(merchant_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->register_merchant: %s\n" % e)
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

Update merchant configuration. Updatable fields: merchantName, merchantUrl, cryptogramType, acceptanceRelationships, protocolInteractions, webIntegrations, apiIntegrations. Partial updates are supported — only provided fields are changed. The vmid, indicator, and paymentPayloadType fields are not updatable here; use the enable/disable-payment-encryption endpoints for encryption changes. Raises 404 if merchant not found, 403 if merchant is deactivated, 409 if new merchantUrl already exists.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
merchant_update = CyberSource.MerchantUpdate() # MerchantUpdate | Merchant update request

try: 
    # Update a merchant
    api_response = api_instance.update_merchant(merchant_id, merchant_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->update_merchant: %s\n" % e)
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

Update key information. Updatable fields are keyName, encryptionKey, algorithm, encryptionType, and expirationDate. Raises 401 if not authenticated, 403 if caller does not own the merchant or if merchant/key is deactivated, 404 if merchant or key not found, 409 if new keyName already exists.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantCapabilitiesApi()
merchant_id = 'merchant_id_example' # str | Unique merchant identifier (UUID)
key_id = 'key_id_example' # str | Unique key identifier (UUID)
key_update = CyberSource.KeyUpdate1() # KeyUpdate1 | Key update request

try: 
    # Update a merchant key
    api_response = api_instance.update_merchant_key(merchant_id, key_id, key_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantCapabilitiesApi->update_merchant_key: %s\n" % e)
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

