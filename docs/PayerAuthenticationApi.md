# CyberSource.PayerAuthenticationApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_payer_auth_enrollment**](PayerAuthenticationApi.md#check_payer_auth_enrollment) | **POST** /risk/v1/authentications | Check Payer Auth Enrollment
[**payer_auth_setup**](PayerAuthenticationApi.md#payer_auth_setup) | **POST** /risk/v1/authentication-setups | Setup Payer Auth
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

# **payer_auth_setup**
> RiskV1AuthenticationSetupsPost201Response payer_auth_setup(payer_auth_setup_request)

Setup Payer Auth

A new service for Merchants to get reference_id for Digital Wallets to use in place of BIN number in Cardinal. Set up file while authenticating with Cardinal. This service should be called by Merchant when payment instrument chosen or changes. This service has to be called before enrollment check.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PayerAuthenticationApi()
payer_auth_setup_request = CyberSource.PayerAuthSetupRequest() # PayerAuthSetupRequest | 

try: 
    # Setup Payer Auth
    api_response = api_instance.payer_auth_setup(payer_auth_setup_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayerAuthenticationApi->payer_auth_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payer_auth_setup_request** | [**PayerAuthSetupRequest**](PayerAuthSetupRequest.md)|  | 

### Return type

[**RiskV1AuthenticationSetupsPost201Response**](RiskV1AuthenticationSetupsPost201Response.md)

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

