# CyberSource.AuthenticationExemptionsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_exemptions**](AuthenticationExemptionsApi.md#authentication_exemptions) | **POST** /risk/v1/authentication-exemptions | Authentication Exemptions Service


# **authentication_exemptions**
> RiskV1AuthenticationExemptionsPost201Response authentication_exemptions(authentication_exemptions_request)

Authentication Exemptions Service

A new CYBS branded service to connect to VISA’s REST API to enable Visa Transaction Advisor (VTA) as a standalone service for merchants to support PSD2/SCA adoption and exemptions processing startegy in Europe.VTA Provides intelligent risk data to merchants as inputs to their in-house fraud management tools for fraud mitigation on Visa transactions. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AuthenticationExemptionsApi()
authentication_exemptions_request = CyberSource.AuthenticationExemptionsRequest() # AuthenticationExemptionsRequest | 

try: 
    # Authentication Exemptions Service
    api_response = api_instance.authentication_exemptions(authentication_exemptions_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationExemptionsApi->authentication_exemptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_exemptions_request** | [**AuthenticationExemptionsRequest**](AuthenticationExemptionsRequest.md)|  | 

### Return type

[**RiskV1AuthenticationExemptionsPost201Response**](RiskV1AuthenticationExemptionsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

