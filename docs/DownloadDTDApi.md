# CyberSource.DownloadDTDApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dtdv2**](DownloadDTDApi.md#get_dtdv2) | **GET** /reporting/v3/dtds/{reportDefinitionNameVersion} | Download DTD for Report


# **get_dtdv2**
> get_dtdv2(report_definition_name_version)

Download DTD for Report

Used to download DTDs for reports on no-auth.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DownloadDTDApi()
report_definition_name_version = 'report_definition_name_version_example' # str | Name and version of DTD file to download. Some DTDs only have one version. In that case version name is not needed. Some example values are ctdr-1.0, tdr, pbdr-1.1

try: 
    # Download DTD for Report
    api_instance.get_dtdv2(report_definition_name_version)
except ApiException as e:
    print("Exception when calling DownloadDTDApi->get_dtdv2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_definition_name_version** | **str**| Name and version of DTD file to download. Some DTDs only have one version. In that case version name is not needed. Some example values are ctdr-1.0, tdr, pbdr-1.1 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/xml-dtd

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

