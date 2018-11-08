# CyberSource.TransactionBatchApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pts_v1_transaction_batches_id_get**](TransactionBatchApi.md#pts_v1_transaction_batches_id_get) | **GET** /pts/v1/transaction-batches/{id} | Get an individual batch file Details processed through the Offline Transaction Submission Services


# **pts_v1_transaction_batches_id_get**
> pts_v1_transaction_batches_id_get(id)

Get an individual batch file Details processed through the Offline Transaction Submission Services

Provide the search range

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TransactionBatchApi()
id = 'id_example' # str | The batch id assigned for the template.

try: 
    # Get an individual batch file Details processed through the Offline Transaction Submission Services
    api_instance.pts_v1_transaction_batches_id_get(id)
except ApiException as e:
    print("Exception when calling TransactionBatchApi->pts_v1_transaction_batches_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The batch id assigned for the template. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

