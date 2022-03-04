# CyberSource.VerificationApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_export_compliance**](VerificationApi.md#validate_export_compliance) | **POST** /risk/v1/export-compliance-inquiries | Validate export compliance
[**verify_customer_address**](VerificationApi.md#verify_customer_address) | **POST** /risk/v1/address-verifications | Verify customer address


# **validate_export_compliance**
> RiskV1ExportComplianceInquiriesPost201Response validate_export_compliance(validate_export_compliance_request)

Validate export compliance

This call checks customer data against specified watch lists to ensure export compliance. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.VerificationApi()
validate_export_compliance_request = CyberSource.ValidateExportComplianceRequest() # ValidateExportComplianceRequest | 

try: 
    # Validate export compliance
    api_response = api_instance.validate_export_compliance(validate_export_compliance_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->validate_export_compliance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_export_compliance_request** | [**ValidateExportComplianceRequest**](ValidateExportComplianceRequest.md)|  | 

### Return type

[**RiskV1ExportComplianceInquiriesPost201Response**](RiskV1ExportComplianceInquiriesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_customer_address**
> RiskV1AddressVerificationsPost201Response verify_customer_address(verify_customer_address_request)

Verify customer address

This call verifies that the customer address submitted is valid.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.VerificationApi()
verify_customer_address_request = CyberSource.VerifyCustomerAddressRequest() # VerifyCustomerAddressRequest | 

try: 
    # Verify customer address
    api_response = api_instance.verify_customer_address(verify_customer_address_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->verify_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_customer_address_request** | [**VerifyCustomerAddressRequest**](VerifyCustomerAddressRequest.md)|  | 

### Return type

[**RiskV1AddressVerificationsPost201Response**](RiskV1AddressVerificationsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

