# CyberSource.RetrievalSummariesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_retrieval_summary**](RetrievalSummariesApi.md#get_retrieval_summary) | **GET** /reporting/v3/retrieval-summaries | Get Retrieval Summaries


# **get_retrieval_summary**
> ReportingV3RetrievalSummariesGet200Response get_retrieval_summary(start_time, end_time, organization_id=organization_id)

Get Retrieval Summaries

Retrieval Summary Report Description

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.RetrievalSummariesApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
end_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
organization_id = 'organization_id_example' # str | Valid Organization Id (optional)

try: 
    # Get Retrieval Summaries
    api_response = api_instance.get_retrieval_summary(start_time, end_time, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalSummariesApi->get_retrieval_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **end_time** | **datetime**| Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **organization_id** | **str**| Valid Organization Id | [optional] 

### Return type

[**ReportingV3RetrievalSummariesGet200Response**](ReportingV3RetrievalSummariesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

