# CyberSource.OrdersApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](OrdersApi.md#create_order) | **POST** /pts/v2/intents | Create an Order
[**update_order**](OrdersApi.md#update_order) | **PATCH** /pts/v2/intents/{id} | Update an Order


# **create_order**
> PtsV2CreateOrderPost201Response create_order(create_order_request)

Create an Order

A create order request enables you to send the itemized details along with the order. This API can be used by merchants initiating their transactions with the create order API.  

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.OrdersApi()
create_order_request = CyberSource.CreateOrderRequest() # CreateOrderRequest | 

try: 
    # Create an Order
    api_response = api_instance.create_order(create_order_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_request** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | 

### Return type

[**PtsV2CreateOrderPost201Response**](PtsV2CreateOrderPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> PtsV2UpdateOrderPatch201Response update_order(id, update_order_request)

Update an Order

This API can be used in two flavours - for updating the order as well as saving the order. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.OrdersApi()
id = 'id_example' # str | The ID returned from the original create order response.
update_order_request = CyberSource.UpdateOrderRequest() # UpdateOrderRequest | 

try: 
    # Update an Order
    api_response = api_instance.update_order(id, update_order_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->update_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID returned from the original create order response. | 
 **update_order_request** | [**UpdateOrderRequest**](UpdateOrderRequest.md)|  | 

### Return type

[**PtsV2UpdateOrderPatch201Response**](PtsV2UpdateOrderPatch201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

