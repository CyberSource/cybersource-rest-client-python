# CyberSource.CreditApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit**](CreditApi.md#create_credit) | **POST** /pts/v2/credits/ | Process a Credit


# **create_credit**
> PtsV2CreditsPost201Response create_credit(create_credit_request)

Process a Credit

POST to the credit resource to credit funds to a specified credit card.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CreditApi()
create_credit_request = CyberSource.CreateCreditRequest() # CreateCreditRequest | 

try: 
    # Process a Credit
    api_response = api_instance.create_credit(create_credit_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditApi->create_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_credit_request** | [**CreateCreditRequest**](CreateCreditRequest.md)|  | 

### Return type

[**PtsV2CreditsPost201Response**](PtsV2CreditsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

