# CyberSource.TaxesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_tax**](TaxesApi.md#calculate_tax) | **POST** /vas/v2/tax | Calculate Taxes
[**void_tax**](TaxesApi.md#void_tax) | **PATCH** /vas/v2/tax/{id} | Void Taxes


# **calculate_tax**
> VasV2PaymentsPost201Response calculate_tax(tax_request)

Calculate Taxes

The tax calculation service provides real-time sales tax and VAT calculations for orders placed with your business worldwide.  It enhances your ability to conduct business globally and enables you to avoid the risk and complexity of managing online tax calculation.  The service supports product-based tax rules and exemptions for goods and services.  The tax rates are updated twice a month and calculations include sub-level detail (rates per taxing jurisdiction, names and types of jurisdictions). Implementation guidance, list of supported countries, and information on tax reporting are in the [Tax User Guide](https://developer.cybersource.com/docs/cybs/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview.html). The availability of API features for a merchant can depend on the portfolio configuration and may need to be enabled at the portfolio level before they can be added to merchant accounts. 

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

