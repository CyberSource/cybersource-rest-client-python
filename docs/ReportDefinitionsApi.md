# CyberSource.ReportDefinitionsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource_info_by_report_definition**](ReportDefinitionsApi.md#get_resource_info_by_report_definition) | **GET** /reporting/v3/report-definitions/{reportDefinitionName} | Get report definition
[**get_resource_v2_info**](ReportDefinitionsApi.md#get_resource_v2_info) | **GET** /reporting/v3/report-definitions | Get reporting resource information


# **get_resource_info_by_report_definition**
> ReportingV3ReportDefinitionsNameGet200Response get_resource_info_by_report_definition(report_definition_name, organization_id=organization_id)

Get report definition

View the attributes of an individual report type. For a list of values for reportDefinitionName, see the [Reporting Developer Guide](https://www.cybersource.com/developers/documentation/reporting_and_reconciliation/) 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportDefinitionsApi()
report_definition_name = 'report_definition_name_example' # str | Name of the Report definition to retrieve
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Get report definition
    api_response = api_instance.get_resource_info_by_report_definition(report_definition_name, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDefinitionsApi->get_resource_info_by_report_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_definition_name** | **str**| Name of the Report definition to retrieve | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

[**ReportingV3ReportDefinitionsNameGet200Response**](ReportingV3ReportDefinitionsNameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_v2_info**
> ReportingV3ReportDefinitionsGet200Response get_resource_v2_info(organization_id=organization_id)

Get reporting resource information

View a list of supported reports and their attributes before subscribing to them. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportDefinitionsApi()
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Get reporting resource information
    api_response = api_instance.get_resource_v2_info(organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDefinitionsApi->get_resource_v2_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

[**ReportingV3ReportDefinitionsGet200Response**](ReportingV3ReportDefinitionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

