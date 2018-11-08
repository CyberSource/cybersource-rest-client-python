# CyberSource.TransactionDetailsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction**](TransactionDetailsApi.md#get_transaction) | **GET** /tss/v2/transactions/{id} | Retrieve a Transaction


# **get_transaction**
> TssV2TransactionsGet200Response get_transaction(id)

Retrieve a Transaction

Include the Request ID in the GET request to retrieve the transaction details.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TransactionDetailsApi()
id = 'id_example' # str | Request ID. 

try: 
    # Retrieve a Transaction
    api_response = api_instance.get_transaction(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionDetailsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Request ID.  | 

### Return type

[**TssV2TransactionsGet200Response**](TssV2TransactionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

