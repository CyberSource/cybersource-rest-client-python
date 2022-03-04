# CyberSource.InterchangeClearingLevelDetailsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_interchange_clearing_level_details**](InterchangeClearingLevelDetailsApi.md#get_interchange_clearing_level_details) | **GET** /reporting/v3/interchange-clearing-level-details | Interchange Clearing Level data for an account or a merchant


# **get_interchange_clearing_level_details**
> ReportingV3InterchangeClearingLevelDetailsGet200Response get_interchange_clearing_level_details(start_time, end_time, organization_id=organization_id)

Interchange Clearing Level data for an account or a merchant

Interchange Clearing Level data for an account or a merchant

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InterchangeClearingLevelDetailsApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
end_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
organization_id = 'organization_id_example' # str | Valid Organization Id (optional)

try: 
    # Interchange Clearing Level data for an account or a merchant
    api_response = api_instance.get_interchange_clearing_level_details(start_time, end_time, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterchangeClearingLevelDetailsApi->get_interchange_clearing_level_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **end_time** | **datetime**| Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **organization_id** | **str**| Valid Organization Id | [optional] 

### Return type

[**ReportingV3InterchangeClearingLevelDetailsGet200Response**](ReportingV3InterchangeClearingLevelDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

