# CyberSource.ReportDownloadsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_report**](ReportDownloadsApi.md#download_report) | **GET** /reporting/v3/report-downloads | Download a report


# **download_report**
> download_report(report_date, report_name, organization_id=organization_id)

Download a report

Download a report for the given report name on the specified date

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportDownloadsApi()
report_date = '2013-10-20' # date | Valid date on which to download the report in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd 
report_name = 'report_name_example' # str | Name of the report to download
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Download a report
    api_instance.download_report(report_date, report_name, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportDownloadsApi->download_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_date** | **date**| Valid date on which to download the report in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd  | 
 **report_name** | **str**| Name of the report to download | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/xml, test/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

