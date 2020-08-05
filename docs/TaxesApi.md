# CyberSource.TaxesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_tax**](TaxesApi.md#calculate_tax) | **POST** /vas/v2/tax | Calculate Taxes
[**void_tax**](TaxesApi.md#void_tax) | **PATCH** /vas/v2/tax/{id} | Void Taxes


# **calculate_tax**
> VasV2PaymentsPost201Response calculate_tax(tax_request)

Calculate Taxes

Get tax details for a transaction. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TaxesApi()
tax_request = CyberSource.TaxRequest() # TaxRequest | 

try: 
    # Calculate Taxes
    api_response = api_instance.calculate_tax(tax_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->calculate_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_request** | [**TaxRequest**](TaxRequest.md)|  | 

### Return type

[**VasV2PaymentsPost201Response**](VasV2PaymentsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_tax**
> VasV2TaxVoid200Response void_tax(void_tax_request, id)

Void Taxes

Pass the Tax Request ID in the PATCH request to void the committed tax calculation.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TaxesApi()
void_tax_request = CyberSource.VoidTaxRequest() # VoidTaxRequest | 
id = 'id_example' # str | The tax ID returned from a previous request.

try: 
    # Void Taxes
    api_response = api_instance.void_tax(void_tax_request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->void_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **void_tax_request** | [**VoidTaxRequest**](VoidTaxRequest.md)|  | 
 **id** | **str**| The tax ID returned from a previous request. | 

### Return type

[**VasV2TaxVoid200Response**](VasV2TaxVoid200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

