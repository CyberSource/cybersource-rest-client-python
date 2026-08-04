# CyberSource.TransactionQueryApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_query_api**](TransactionQueryApi.md#create_query_api) | **POST** /pts/v2/payouts/transaction-query/{id} | Query Transaction Details


# **create_query_api**
> InlineResponse2015 create_query_api(id, body, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id, limit=limit, offset=offset)

Query Transaction Details

Query the status and details of payouts transactions including Pull Funds, Push Funds, and Pull Funds Reversals 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TransactionQueryApi()
id = 'id_example' # str | This is the CyberSource Request ID generated for successfully processed AFT/OCT that needs to be queried. 
body = CyberSource.Body1() # Body1 | 
content_type = 'content_type_example' # str | 
x_requestid = 'x_requestid_example' # str | 
v_c_merchant_id = 'v_c_merchant_id_example' # str | 
v_c_permissions = 'v_c_permissions_example' # str | 
v_c_correlation_id = 'v_c_correlation_id_example' # str | 
v_c_organization_id = 'v_c_organization_id_example' # str | 
limit = 56 # int | The maximum number of options to be retrieved from the processor and displayed to the consumer.  (optional)
offset = 56 # int | Offset from the first item in the list of options received from the processor. If you want to display the options in multiple lists, this number represents the first option displayed in each list.  (optional)

try: 
    # Query Transaction Details
    api_response = api_instance.create_query_api(id, body, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionQueryApi->create_query_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| This is the CyberSource Request ID generated for successfully processed AFT/OCT that needs to be queried.  | 
 **body** | [**Body1**](Body1.md)|  | 
 **content_type** | **str**|  | 
 **x_requestid** | **str**|  | 
 **v_c_merchant_id** | **str**|  | 
 **v_c_permissions** | **str**|  | 
 **v_c_correlation_id** | **str**|  | 
 **v_c_organization_id** | **str**|  | 
 **limit** | **int**| The maximum number of options to be retrieved from the processor and displayed to the consumer.  | [optional] 
 **offset** | **int**| Offset from the first item in the list of options received from the processor. If you want to display the options in multiple lists, this number represents the first option displayed in each list.  | [optional] 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

