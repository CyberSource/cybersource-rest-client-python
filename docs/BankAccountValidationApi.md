# CyberSource.BankAccountValidationApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_account_validation_request**](BankAccountValidationApi.md#bank_account_validation_request) | **POST** /bavs/v1/account-validations | Visa Bank Account Validation Service


# **bank_account_validation_request**
> InlineResponse20014 bank_account_validation_request(account_validations_request)

Visa Bank Account Validation Service

The Visa Bank Account Validation Service is a new standalone product designed to validate customer's routing and bank account number combination for ACH transactions. Merchant's can use this standalone product to validate their customer's account prior to processing an ACH transaction against the customer's account to comply with Nacha's account validation mandate for Web-debit transactions. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BankAccountValidationApi()
account_validations_request = CyberSource.AccountValidationsRequest() # AccountValidationsRequest | 

try: 
    # Visa Bank Account Validation Service
    api_response = api_instance.bank_account_validation_request(account_validations_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountValidationApi->bank_account_validation_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_validations_request** | [**AccountValidationsRequest**](AccountValidationsRequest.md)|  | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

