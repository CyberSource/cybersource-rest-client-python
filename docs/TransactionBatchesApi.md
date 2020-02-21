# CyberSource.TransactionBatchesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_batch_details**](TransactionBatchesApi.md#get_transaction_batch_details) | **GET** /pts/v1/transaction-batch-details/{id} | Get Transaction Details for a given Batch Id
[**get_transaction_batch_id**](TransactionBatchesApi.md#get_transaction_batch_id) | **GET** /pts/v1/transaction-batches/{id} | Get Individual Batch File
[**get_transaction_batches**](TransactionBatchesApi.md#get_transaction_batches) | **GET** /pts/v1/transaction-batches | Get a List of Batch Files


# **get_transaction_batch_details**
> get_transaction_batch_details(id, upload_date=upload_date, status=status)

Get Transaction Details for a given Batch Id

Provides real-time detailed status information about the transactions that you previously uploaded in the Business Center or processed with the Offline Transaction File Submission service. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TransactionBatchesApi()
id = 'id_example' # str | The batch id assigned for the template.
upload_date = '2013-10-20' # date | Date in which the original batch file was uploaded. Date must be in ISO-8601 format. Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14) **Example date format:**  - yyyy-MM-dd  (optional)
status = 'status_example' # str | Allows you to filter by rejected response.  Valid values: - Rejected  (optional)

try: 
    # Get Transaction Details for a given Batch Id
    api_instance.get_transaction_batch_details(id, upload_date=upload_date, status=status)
except ApiException as e:
    print("Exception when calling TransactionBatchesApi->get_transaction_batch_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The batch id assigned for the template. | 
 **upload_date** | **date**| Date in which the original batch file was uploaded. Date must be in ISO-8601 format. Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14) **Example date format:**  - yyyy-MM-dd  | [optional] 
 **status** | **str**| Allows you to filter by rejected response.  Valid values: - Rejected  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: text/csv, application/xml, text/vnd.cybersource.map-csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_batch_id**
> PtsV1TransactionBatchesIdGet200Response get_transaction_batch_id(id)

Get Individual Batch File

Provide the search range

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TransactionBatchesApi()
id = 'id_example' # str | The batch id assigned for the template.

try: 
    # Get Individual Batch File
    api_response = api_instance.get_transaction_batch_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionBatchesApi->get_transaction_batch_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The batch id assigned for the template. | 

### Return type

[**PtsV1TransactionBatchesIdGet200Response**](PtsV1TransactionBatchesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_batches**
> PtsV1TransactionBatchesGet200Response get_transaction_batches(start_time, end_time)

Get a List of Batch Files

Provide the search range

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TransactionBatchesApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZZ 
end_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZZ 

try: 
    # Get a List of Batch Files
    api_response = api_instance.get_transaction_batches(start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionBatchesApi->get_transaction_batches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)   **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZZ  | 
 **end_time** | **datetime**| Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)   **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZZ  | 

### Return type

[**PtsV1TransactionBatchesGet200Response**](PtsV1TransactionBatchesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

