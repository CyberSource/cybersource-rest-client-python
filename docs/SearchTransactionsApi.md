# CyberSource.SearchTransactionsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_search**](SearchTransactionsApi.md#create_search) | **POST** /tss/v2/searches | Create a Search Request
[**get_search**](SearchTransactionsApi.md#get_search) | **GET** /tss/v2/searches/{searchId} | Get Search Results


# **create_search**
> TssV2TransactionsPost201Response create_search(create_search_request)

Create a Search Request

Create a search request. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SearchTransactionsApi()
create_search_request = CyberSource.CreateSearchRequest() # CreateSearchRequest | 

try: 
    # Create a Search Request
    api_response = api_instance.create_search(create_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchTransactionsApi->create_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_search_request** | [**CreateSearchRequest**](CreateSearchRequest.md)|  | 

### Return type

[**TssV2TransactionsPost201Response**](TssV2TransactionsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search**
> TssV2TransactionsPost201Response get_search(search_id)

Get Search Results

Include the Search ID in the GET request to retrieve the search results.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SearchTransactionsApi()
search_id = 'search_id_example' # str | Search ID.

try: 
    # Get Search Results
    api_response = api_instance.get_search(search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchTransactionsApi->get_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| Search ID. | 

### Return type

[**TssV2TransactionsPost201Response**](TssV2TransactionsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

