# CyberSource.BinLookupApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_info**](BinLookupApi.md#get_account_info) | **POST** /bin/v1/binlookup | BIN Lookup API


# **get_account_info**
> InlineResponse2011 get_account_info(create_bin_lookup_request)

BIN Lookup API

The BIN Lookup Service is a versatile business tool that provides card network agnostic solution designed to ensure frictionless transaction experience by utilizing up-to-date Bank Identification Number (BIN) attributes sourced from multiple global and regional data sources. This service helps to improve authorization rates by helping to route transactions to the best-suited card network, minimizes fraud through card detail verification and aids in regulatory compliance by identifying card properties. The service is flexible and provides businesses  with a flexible choice of inputs such as primary account number (PAN), network token from major networks which includes device PAN (DPAN), and all types of tokens generated via CyberSource Token Management Service (TMS). Currently, the range of available credentials is contingent on the networks enabled for the business entity. Therefore, the network information specified in this documentation is illustrative and subject to personalized offerings for each reseller or merchant. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BinLookupApi()
create_bin_lookup_request = CyberSource.CreateBinLookupRequest() # CreateBinLookupRequest | 

try: 
    # BIN Lookup API
    api_response = api_instance.get_account_info(create_bin_lookup_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BinLookupApi->get_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bin_lookup_request** | [**CreateBinLookupRequest**](CreateBinLookupRequest.md)|  | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

