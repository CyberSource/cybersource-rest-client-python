# CyberSource.InvoiceSettingsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_settings**](InvoiceSettingsApi.md#get_invoice_settings) | **GET** /invoicing/v2/invoiceSettings | Get Invoice Settings
[**update_invoice_settings**](InvoiceSettingsApi.md#update_invoice_settings) | **PUT** /invoicing/v2/invoiceSettings | Update Invoice Settings


# **get_invoice_settings**
> InvoicingV2InvoiceSettingsGet200Response get_invoice_settings()

Get Invoice Settings

Get the invoice settings for the invoice payment page.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InvoiceSettingsApi()

try: 
    # Get Invoice Settings
    api_response = api_instance.get_invoice_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceSettingsApi->get_invoice_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InvoicingV2InvoiceSettingsGet200Response**](InvoicingV2InvoiceSettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_settings**
> InvoicingV2InvoiceSettingsGet200Response update_invoice_settings(invoice_settings_request)

Update Invoice Settings

Update invoice settings for the invoice payment page.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InvoiceSettingsApi()
invoice_settings_request = CyberSource.InvoiceSettingsRequest() # InvoiceSettingsRequest | 

try: 
    # Update Invoice Settings
    api_response = api_instance.update_invoice_settings(invoice_settings_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceSettingsApi->update_invoice_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_settings_request** | [**InvoiceSettingsRequest**](InvoiceSettingsRequest.md)|  | 

### Return type

[**InvoicingV2InvoiceSettingsGet200Response**](InvoicingV2InvoiceSettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

