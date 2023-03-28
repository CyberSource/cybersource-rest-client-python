# CyberSource.BatchesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_report**](BatchesApi.md#get_batch_report) | **GET** /accountupdater/v1/batches/{batchId}/report | Retrieve a Batch Report
[**get_batch_status**](BatchesApi.md#get_batch_status) | **GET** /accountupdater/v1/batches/{batchId}/status | Retrieve a Batch Status
[**get_batches_list**](BatchesApi.md#get_batches_list) | **GET** /accountupdater/v1/batches | List Batches
[**post_batch**](BatchesApi.md#post_batch) | **POST** /accountupdater/v1/batches | Create a Batch


# **get_batch_report**
> InlineResponse20014 get_batch_report(batch_id)

Retrieve a Batch Report

**Get Batch Report**<br>This resource accepts a batch id and returns: - The batch status. - The total number of accepted, rejected, updated records. - The total number of card association responses. - The billable quantities of:   - New Account Numbers (NAN)   - New Expiry Dates (NED)   - Account Closures (ACL)   - Contact Card Holders (CCH) - Source record information including token ids, masked card number, expiration dates & card type. - Response record information including response code, reason, token ids, masked card number, expiration dates & card type. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BatchesApi()
batch_id = 'batch_id_example' # str | Unique identification number assigned to the submitted request.

try: 
    # Retrieve a Batch Report
    api_response = api_instance.get_batch_report(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchesApi->get_batch_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Unique identification number assigned to the submitted request. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_status**
> InlineResponse20013 get_batch_status(batch_id)

Retrieve a Batch Status

**Get Batch Status**<br>This resource accepts a batch id and returns: - The batch status. - The total number of accepted, rejected, updated records. - The total number of card association responses. - The billable quantities of:   - New Account Numbers (NAN)   - New Expiry Dates (NED)   - Account Closures (ACL)   - Contact Card Holders (CCH) 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BatchesApi()
batch_id = 'batch_id_example' # str | Unique identification number assigned to the submitted request.

try: 
    # Retrieve a Batch Status
    api_response = api_instance.get_batch_status(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchesApi->get_batch_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Unique identification number assigned to the submitted request. | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batches_list**
> InlineResponse20012 get_batches_list(offset=offset, limit=limit, from_date=from_date, to_date=to_date)

List Batches

**List Batches**<br>This resource accepts a optional date range, record offset and limit, returning a paginated response of batches containing: - The batch id. - The batch status. - The batch created / modified dates. - The total number of accepted, rejected, updated records. - The total number of card association responses. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BatchesApi()
offset = 0 # int | Starting record in zero-based dataset that should be returned as the first object in the array. (optional) (default to 0)
limit = 20 # int | The maximum number that can be returned in the array starting from the offset record in zero-based dataset. (optional) (default to 20)
from_date = 'from_date_example' # str | ISO-8601 format: yyyyMMddTHHmmssZ (optional)
to_date = 'to_date_example' # str | ISO-8601 format: yyyyMMddTHHmmssZ (optional)

try: 
    # List Batches
    api_response = api_instance.get_batches_list(offset=offset, limit=limit, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchesApi->get_batches_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Starting record in zero-based dataset that should be returned as the first object in the array. | [optional] [default to 0]
 **limit** | **int**| The maximum number that can be returned in the array starting from the offset record in zero-based dataset. | [optional] [default to 20]
 **from_date** | **str**| ISO-8601 format: yyyyMMddTHHmmssZ | [optional] 
 **to_date** | **str**| ISO-8601 format: yyyyMMddTHHmmssZ | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_batch**
> InlineResponse2022 post_batch(body)

Create a Batch

**Create a Batch**<br>This resource accepts TMS tokens ids of a Customer, Payment Instrument or Instrument Identifier. <br> The card numbers for the supplied tokens ids are then sent to the relevant card associations to check for updates.<br>The following type of batches can be submitted: -  **oneOff** batch containing tokens id for Visa or MasterCard card numbers. - **amexRegistration** batch containing tokens id for Amex card numbers.  A batch id will be returned on a successful response which can be used to get the batch status and the batch report. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BatchesApi()
body = CyberSource.Body() # Body | 

try: 
    # Create a Batch
    api_response = api_instance.post_batch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchesApi->post_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 

### Return type

[**InlineResponse2022**](InlineResponse2022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

