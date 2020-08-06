# CyberSource.CustomerShippingAddressApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer_shipping_address**](CustomerShippingAddressApi.md#delete_customer_shipping_address) | **DELETE** /tms/v2/customers/{customerTokenId}/shipping-addresses/{shippingAddressTokenId} | Delete a Customer Shipping Address
[**get_customer_shipping_address**](CustomerShippingAddressApi.md#get_customer_shipping_address) | **GET** /tms/v2/customers/{customerTokenId}/shipping-addresses/{shippingAddressTokenId} | Retrieve a Customer Shipping Address
[**get_customer_shipping_addresses_list**](CustomerShippingAddressApi.md#get_customer_shipping_addresses_list) | **GET** /tms/v2/customers/{customerTokenId}/shipping-addresses | List Shipping Addresses for a Customer
[**patch_customers_shipping_address**](CustomerShippingAddressApi.md#patch_customers_shipping_address) | **PATCH** /tms/v2/customers/{customerTokenId}/shipping-addresses/{shippingAddressTokenId} | Update a Customer Shipping Address
[**post_customer_shipping_address**](CustomerShippingAddressApi.md#post_customer_shipping_address) | **POST** /tms/v2/customers/{customerTokenId}/shipping-addresses | Create a Customer Shipping Address


# **delete_customer_shipping_address**
> delete_customer_shipping_address(customer_token_id, shipping_address_token_id, profile_id=profile_id)

Delete a Customer Shipping Address

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerShippingAddressApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
shipping_address_token_id = 'shipping_address_token_id_example' # str | The TokenId of an shipping address.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete a Customer Shipping Address
    api_instance.delete_customer_shipping_address(customer_token_id, shipping_address_token_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling CustomerShippingAddressApi->delete_customer_shipping_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **shipping_address_token_id** | **str**| The TokenId of an shipping address. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_shipping_address**
> Tmsv2customersEmbeddedDefaultShippingAddress get_customer_shipping_address(customer_token_id, shipping_address_token_id, profile_id=profile_id)

Retrieve a Customer Shipping Address

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerShippingAddressApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
shipping_address_token_id = 'shipping_address_token_id_example' # str | The TokenId of an shipping address.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve a Customer Shipping Address
    api_response = api_instance.get_customer_shipping_address(customer_token_id, shipping_address_token_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerShippingAddressApi->get_customer_shipping_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **shipping_address_token_id** | **str**| The TokenId of an shipping address. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultShippingAddress**](Tmsv2customersEmbeddedDefaultShippingAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_shipping_addresses_list**
> ShippingAddressListForCustomer get_customer_shipping_addresses_list(customer_token_id, profile_id=profile_id, offset=offset, limit=limit)

List Shipping Addresses for a Customer

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerShippingAddressApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)
offset = 0 # int | Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. (optional) (default to 0)
limit = 20 # int | The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. (optional) (default to 20)

try: 
    # List Shipping Addresses for a Customer
    api_response = api_instance.get_customer_shipping_addresses_list(customer_token_id, profile_id=profile_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerShippingAddressApi->get_customer_shipping_addresses_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 
 **offset** | **int**| Starting record in zero-based dataset that should be returned as the first object in the array. Default is 0. | [optional] [default to 0]
 **limit** | **int**| The maximum number that can be returned in the array starting from the offset record in zero-based dataset. Default is 20, maximum is 100. | [optional] [default to 20]

### Return type

[**ShippingAddressListForCustomer**](ShippingAddressListForCustomer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_customers_shipping_address**
> Tmsv2customersEmbeddedDefaultShippingAddress patch_customers_shipping_address(customer_token_id, shipping_address_token_id, patch_customer_shipping_address_request, profile_id=profile_id, if_match=if_match)

Update a Customer Shipping Address

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerShippingAddressApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
shipping_address_token_id = 'shipping_address_token_id_example' # str | The TokenId of an shipping address.
patch_customer_shipping_address_request = CyberSource.PatchCustomerShippingAddressRequest() # PatchCustomerShippingAddressRequest | 
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)
if_match = 'if_match_example' # str | Contains an ETag value from a GET request to make the request conditional. (optional)

try: 
    # Update a Customer Shipping Address
    api_response = api_instance.patch_customers_shipping_address(customer_token_id, shipping_address_token_id, patch_customer_shipping_address_request, profile_id=profile_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerShippingAddressApi->patch_customers_shipping_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **shipping_address_token_id** | **str**| The TokenId of an shipping address. | 
 **patch_customer_shipping_address_request** | [**PatchCustomerShippingAddressRequest**](PatchCustomerShippingAddressRequest.md)|  | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 
 **if_match** | **str**| Contains an ETag value from a GET request to make the request conditional. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultShippingAddress**](Tmsv2customersEmbeddedDefaultShippingAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customer_shipping_address**
> Tmsv2customersEmbeddedDefaultShippingAddress post_customer_shipping_address(customer_token_id, post_customer_shipping_address_request, profile_id=profile_id)

Create a Customer Shipping Address

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerShippingAddressApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
post_customer_shipping_address_request = CyberSource.PostCustomerShippingAddressRequest() # PostCustomerShippingAddressRequest | 
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Create a Customer Shipping Address
    api_response = api_instance.post_customer_shipping_address(customer_token_id, post_customer_shipping_address_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerShippingAddressApi->post_customer_shipping_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **post_customer_shipping_address_request** | [**PostCustomerShippingAddressRequest**](PostCustomerShippingAddressRequest.md)|  | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**Tmsv2customersEmbeddedDefaultShippingAddress**](Tmsv2customersEmbeddedDefaultShippingAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

