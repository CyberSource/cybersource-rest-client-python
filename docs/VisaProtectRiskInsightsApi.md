# CyberSource.VisaProtectRiskInsightsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_vpri**](VisaProtectRiskInsightsApi.md#submit_vpri) | **POST** /unifiedrisk | Visa Protect Risk Insights


# **submit_vpri**
> UnifiedRiskPost201Response submit_vpri(vpri_request)

Visa Protect Risk Insights

VPRI delivers real-time, AI-driven risk scores and insights via a data-only API to enrich existing fraud strategies and improve decisioning. It integrates easily into existing workflows and provides immediate value by identifying legitimate behavior across Visa's global network—helping reduce false declines and increase acceptance.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.VisaProtectRiskInsightsApi()
vpri_request = CyberSource.VpriRequest() # VpriRequest | VPRI request for Transaction Risk Scoring or Transaction Risk Labeling

try: 
    # Visa Protect Risk Insights
    api_response = api_instance.submit_vpri(vpri_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisaProtectRiskInsightsApi->submit_vpri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpri_request** | [**VpriRequest**](VpriRequest.md)| VPRI request for Transaction Risk Scoring or Transaction Risk Labeling | 

### Return type

[**UnifiedRiskPost201Response**](UnifiedRiskPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

