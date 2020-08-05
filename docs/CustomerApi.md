# CyberSource.CustomerApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer**](CustomerApi.md#delete_customer) | **DELETE** /tms/v2/customers/{customerTokenId} | Delete a Customer
[**get_customer**](CustomerApi.md#get_customer) | **GET** /tms/v2/customers/{customerTokenId} | Retrieve a Customer
[**patch_customer**](CustomerApi.md#patch_customer) | **PATCH** /tms/v2/customers/{customerTokenId} | Update a Customer
[**post_customer**](CustomerApi.md#post_customer) | **POST** /tms/v2/customers | Create a Customer


# **delete_customer**
> delete_customer(customer_token_id, profile_id=profile_id)

Delete a Customer

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete a Customer
    api_instance.delete_customer(customer_token_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling CustomerApi->delete_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> TmsV2CustomersResponse get_customer(customer_token_id, profile_id=profile_id)

Retrieve a Customer

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve a Customer
    api_response = api_instance.get_customer(customer_token_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**TmsV2CustomersResponse**](TmsV2CustomersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_customer**
> TmsV2CustomersResponse patch_customer(customer_token_id, patch_customer_request, profile_id=profile_id, if_match=if_match)

Update a Customer

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerApi()
customer_token_id = 'customer_token_id_example' # str | The TokenId of a customer.
patch_customer_request = CyberSource.PatchCustomerRequest() # PatchCustomerRequest | 
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)
if_match = 'if_match_example' # str | Contains an ETag value from a GET request to make the request conditional. (optional)

try: 
    # Update a Customer
    api_response = api_instance.patch_customer(customer_token_id, patch_customer_request, profile_id=profile_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->patch_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_token_id** | **str**| The TokenId of a customer. | 
 **patch_customer_request** | [**PatchCustomerRequest**](PatchCustomerRequest.md)|  | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 
 **if_match** | **str**| Contains an ETag value from a GET request to make the request conditional. | [optional] 

### Return type

[**TmsV2CustomersResponse**](TmsV2CustomersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customer**
> TmsV2CustomersResponse post_customer(post_customer_request, profile_id=profile_id)

Create a Customer

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CustomerApi()
post_customer_request = CyberSource.PostCustomerRequest() # PostCustomerRequest | 
profile_id = 'profile_id_example' # str | The id of a profile containing user specific TMS configuration. (optional)

try: 
    # Create a Customer
    api_response = api_instance.post_customer(post_customer_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->post_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_customer_request** | [**PostCustomerRequest**](PostCustomerRequest.md)|  | 
 **profile_id** | **str**| The id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**TmsV2CustomersResponse**](TmsV2CustomersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

