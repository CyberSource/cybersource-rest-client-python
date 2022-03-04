# CyberSource.DownloadXSDApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_xsdv2**](DownloadXSDApi.md#get_xsdv2) | **GET** /reporting/v3/xsds/{reportDefinitionNameVersion} | Download XSD for Report


# **get_xsdv2**
> get_xsdv2(report_definition_name_version)

Download XSD for Report

Used to download XSDs for reports on no-auth.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DownloadXSDApi()
report_definition_name_version = 'report_definition_name_version_example' # str | Name and version of XSD file to download. Some XSDs only have one version. In that case version name is not needed. Some example values are DecisionManagerDetailReport, DecisionManagerTypes

try: 
    # Download XSD for Report
    api_instance.get_xsdv2(report_definition_name_version)
except ApiException as e:
    print("Exception when calling DownloadXSDApi->get_xsdv2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_definition_name_version** | **str**| Name and version of XSD file to download. Some XSDs only have one version. In that case version name is not needed. Some example values are DecisionManagerDetailReport, DecisionManagerTypes | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

