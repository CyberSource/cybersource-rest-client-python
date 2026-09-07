# CyberSource.ForeignExchangeRatesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fx_rates**](ForeignExchangeRatesApi.md#create_fx_rates) | **POST** /pts/v2/payouts/fx-rates | Retrieve Foreign Exchange Rates


# **create_fx_rates**
> InlineResponse2013 create_fx_rates(body, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)

Retrieve Foreign Exchange Rates

Retrieve current foreign exchange rates for cross-border payouts. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ForeignExchangeRatesApi()
body = CyberSource.Body() # Body | 
content_type = 'content_type_example' # str | 
x_requestid = 'x_requestid_example' # str | 
v_c_merchant_id = 'v_c_merchant_id_example' # str | 
v_c_permissions = 'v_c_permissions_example' # str | 
v_c_correlation_id = 'v_c_correlation_id_example' # str | 
v_c_organization_id = 'v_c_organization_id_example' # str | 

try: 
    # Retrieve Foreign Exchange Rates
    api_response = api_instance.create_fx_rates(body, content_type, x_requestid, v_c_merchant_id, v_c_permissions, v_c_correlation_id, v_c_organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForeignExchangeRatesApi->create_fx_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 
 **content_type** | **str**|  | 
 **x_requestid** | **str**|  | 
 **v_c_merchant_id** | **str**|  | 
 **v_c_permissions** | **str**|  | 
 **v_c_correlation_id** | **str**|  | 
 **v_c_organization_id** | **str**|  | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

