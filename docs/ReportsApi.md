# CyberSource.ReportsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportsApi.md#create_report) | **POST** /reporting/v3/reports | Create Adhoc Report
[**get_report_by_report_id**](ReportsApi.md#get_report_by_report_id) | **GET** /reporting/v3/reports/{reportId} | Get Report Based on Report Id
[**search_reports**](ReportsApi.md#search_reports) | **GET** /reporting/v3/reports | Retrieve Available Reports


# **create_report**
> create_report(create_adhoc_report_request, organization_id=organization_id)

Create Adhoc Report

Create a one-time report. You must specify the type of report in reportDefinitionName. For a list of values for reportDefinitionName, see the [Reporting Developer Guide](https://www.cybersource.com/developers/documentation/reporting_and_reconciliation) 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportsApi()
create_adhoc_report_request = CyberSource.CreateAdhocReportRequest() # CreateAdhocReportRequest | Report subscription request payload
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Create Adhoc Report
    api_instance.create_report(create_adhoc_report_request, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_adhoc_report_request** | [**CreateAdhocReportRequest**](CreateAdhocReportRequest.md)| Report subscription request payload | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_by_report_id**
> ReportingV3ReportsIdGet200Response get_report_by_report_id(report_id, organization_id=organization_id)

Get Report Based on Report Id

Download a report using the reportId value. If you don’t already know this value, you can obtain it using the Retrieve available reports call. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportsApi()
report_id = 'report_id_example' # str | Valid Report Id
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Get Report Based on Report Id
    api_response = api_instance.get_report_by_report_id(report_id, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report_by_report_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Valid Report Id | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

[**ReportingV3ReportsIdGet200Response**](ReportingV3ReportsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_reports**
> ReportingV3ReportsGet200Response search_reports(start_time, end_time, time_query_type, organization_id=organization_id, report_mime_type=report_mime_type, report_frequency=report_frequency, report_name=report_name, report_definition_id=report_definition_id, report_status=report_status)

Retrieve Available Reports

Retrieve a list of the available reports to which you are subscribed. This will also give you the reportId value, which you can also use to download a report. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportsApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
end_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
time_query_type = 'time_query_type_example' # str | Specify time you would like to search  Valid values: - reportTimeFrame - executedTime 
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)
report_mime_type = 'report_mime_type_example' # str | Valid Report Format  Valid values: - application/xml - text/csv  (optional)
report_frequency = 'report_frequency_example' # str | Valid Report Frequency  Valid values: - DAILY - WEEKLY - MONTHLY - USER_DEFINED - ADHOC  (optional)
report_name = 'report_name_example' # str | Valid Report Name (optional)
report_definition_id = 56 # int | Valid Report Definition Id (optional)
report_status = 'report_status_example' # str | Valid Report Status  Valid values: - COMPLETED - PENDING - QUEUED - RUNNING - ERROR - NO_DATA  (optional)

try: 
    # Retrieve Available Reports
    api_response = api_instance.search_reports(start_time, end_time, time_query_type, organization_id=organization_id, report_mime_type=report_mime_type, report_frequency=report_frequency, report_name=report_name, report_definition_id=report_definition_id, report_status=report_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->search_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **end_time** | **datetime**| Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **time_query_type** | **str**| Specify time you would like to search  Valid values: - reportTimeFrame - executedTime  | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 
 **report_mime_type** | **str**| Valid Report Format  Valid values: - application/xml - text/csv  | [optional] 
 **report_frequency** | **str**| Valid Report Frequency  Valid values: - DAILY - WEEKLY - MONTHLY - USER_DEFINED - ADHOC  | [optional] 
 **report_name** | **str**| Valid Report Name | [optional] 
 **report_definition_id** | **int**| Valid Report Definition Id | [optional] 
 **report_status** | **str**| Valid Report Status  Valid values: - COMPLETED - PENDING - QUEUED - RUNNING - ERROR - NO_DATA  | [optional] 

### Return type

[**ReportingV3ReportsGet200Response**](ReportingV3ReportsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

