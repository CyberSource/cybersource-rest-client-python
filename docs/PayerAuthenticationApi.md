# CyberSource.PayerAuthenticationApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_payer_auth_enrollment**](PayerAuthenticationApi.md#check_payer_auth_enrollment) | **POST** /risk/v1/authentications | Check Payer Auth Enrollment
[**validate_authentication_results**](PayerAuthenticationApi.md#validate_authentication_results) | **POST** /risk/v1/authentication-results | Validate Authentication Results


# **check_payer_auth_enrollment**
> RiskV1AuthenticationsPost201Response check_payer_auth_enrollment(check_payer_auth_enrollment_request)

Check Payer Auth Enrollment

This call verifies that the card is enrolled in a card authentication program.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PayerAuthenticationApi()
check_payer_auth_enrollment_request = CyberSource.CheckPayerAuthEnrollmentRequest() # CheckPayerAuthEnrollmentRequest | 

try: 
    # Check Payer Auth Enrollment
    api_response = api_instance.check_payer_auth_enrollment(check_payer_auth_enrollment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayerAuthenticationApi->check_payer_auth_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_payer_auth_enrollment_request** | [**CheckPayerAuthEnrollmentRequest**](CheckPayerAuthEnrollmentRequest.md)|  | 

### Return type

[**RiskV1AuthenticationsPost201Response**](RiskV1AuthenticationsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_authentication_results**
> RiskV1AuthenticationResultsPost201Response validate_authentication_results(validate_request)

Validate Authentication Results

This call retrieves and validates the authentication results from issuer and allows the merchant to proceed with processing the payment. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PayerAuthenticationApi()
validate_request = CyberSource.ValidateRequest() # ValidateRequest | 

try: 
    # Validate Authentication Results
    api_response = api_instance.validate_authentication_results(validate_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayerAuthenticationApi->validate_authentication_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_request** | [**ValidateRequest**](ValidateRequest.md)|  | 

### Return type

[**RiskV1AuthenticationResultsPost201Response**](RiskV1AuthenticationResultsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

