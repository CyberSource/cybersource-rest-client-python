# CyberSource.PullFundsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pull_funds_refund**](PullFundsApi.md#create_pull_funds_refund) | **POST** /pts/v1/pull-funds-transfer/{id}/refund | Process a Pull Funds Refund
[**create_pull_funds_reversal**](PullFundsApi.md#create_pull_funds_reversal) | **POST** /pts/v1/pull-funds-transfer/{id}/reversal | Process a Pull Funds Reversal
[**create_pull_funds_transfer**](PullFundsApi.md#create_pull_funds_transfer) | **POST** /pts/v1/pull-funds-transfer | Process a Pull Funds Transfer


# **create_pull_funds_refund**
> PullFundsRefund201Response create_pull_funds_refund(pull_funds_refund_request, id, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)

Process a Pull Funds Refund

Refund an Account Funding Transaction (AFT). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PullFundsApi()
pull_funds_refund_request = CyberSource.PullFundsRefundRequest() # PullFundsRefundRequest | 
id = 'id_example' # str | The transaction id of a previous Account Funding Transaction. 
content_type = 'content_type_example' # str | 
x_requestid = 'x_requestid_example' # str | 
v_c_merchant_id = 'v_c_merchant_id_example' # str | 
v_c_permissions = 'v_c_permissions_example' # str | 
v_c_correlation_id = 'v_c_correlation_id_example' # str | 
v_c_organization_id = 'v_c_organization_id_example' # str | 

try: 
    # Process a Pull Funds Refund
    api_response = api_instance.create_pull_funds_refund(pull_funds_refund_request, id, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullFundsApi->create_pull_funds_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_funds_refund_request** | [**PullFundsRefundRequest**](PullFundsRefundRequest.md)|  | 
 **id** | **str**| The transaction id of a previous Account Funding Transaction.  | 
 **content_type** | **str**|  | 
 **x_requestid** | **str**|  | 
 **v_c_merchant_id** | **str**|  | 
 **v_c_permissions** | **str**|  | 
 **v_c_correlation_id** | **str**|  | 
 **v_c_organization_id** | **str**|  | 

### Return type

[**PullFundsRefund201Response**](PullFundsRefund201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pull_funds_reversal**
> PullFundsReversal201Response create_pull_funds_reversal(pull_funds_reversal_request, id, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)

Process a Pull Funds Reversal

Reverse an Account Funding Transaction (AFT). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PullFundsApi()
pull_funds_reversal_request = CyberSource.PullFundsReversalRequest() # PullFundsReversalRequest | 
id = 'id_example' # str | The transaction id of a previous Account Funding Transaction. 
content_type = 'content_type_example' # str | 
x_requestid = 'x_requestid_example' # str | 
v_c_merchant_id = 'v_c_merchant_id_example' # str | 
v_c_permissions = 'v_c_permissions_example' # str | 
v_c_correlation_id = 'v_c_correlation_id_example' # str | 
v_c_organization_id = 'v_c_organization_id_example' # str | 

try: 
    # Process a Pull Funds Reversal
    api_response = api_instance.create_pull_funds_reversal(pull_funds_reversal_request, id, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullFundsApi->create_pull_funds_reversal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_funds_reversal_request** | [**PullFundsReversalRequest**](PullFundsReversalRequest.md)|  | 
 **id** | **str**| The transaction id of a previous Account Funding Transaction.  | 
 **content_type** | **str**|  | 
 **x_requestid** | **str**|  | 
 **v_c_merchant_id** | **str**|  | 
 **v_c_permissions** | **str**|  | 
 **v_c_correlation_id** | **str**|  | 
 **v_c_organization_id** | **str**|  | 

### Return type

[**PullFundsReversal201Response**](PullFundsReversal201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pull_funds_transfer**
> PullFunds201Response create_pull_funds_transfer(pull_funds_request, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)

Process a Pull Funds Transfer

Receive funds using an Account Funding Transaction (AFT). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PullFundsApi()
pull_funds_request = CyberSource.PullFundsRequest() # PullFundsRequest | 
content_type = 'content_type_example' # str | 
x_requestid = 'x_requestid_example' # str | 
v_c_merchant_id = 'v_c_merchant_id_example' # str | 
v_c_permissions = 'v_c_permissions_example' # str | 
v_c_correlation_id = 'v_c_correlation_id_example' # str | 
v_c_organization_id = 'v_c_organization_id_example' # str | 

try: 
    # Process a Pull Funds Transfer
    api_response = api_instance.create_pull_funds_transfer(pull_funds_request, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullFundsApi->create_pull_funds_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_funds_request** | [**PullFundsRequest**](PullFundsRequest.md)|  | 
 **content_type** | **str**|  | 
 **x_requestid** | **str**|  | 
 **v_c_merchant_id** | **str**|  | 
 **v_c_permissions** | **str**|  | 
 **v_c_correlation_id** | **str**|  | 
 **v_c_organization_id** | **str**|  | 

### Return type

[**PullFunds201Response**](PullFunds201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

