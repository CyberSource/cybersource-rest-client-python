# CyberSource.SecureFileShareApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file**](SecureFileShareApi.md#get_file) | **GET** /sfs/v1/files/{fileId} | Download a file with file identifier
[**get_file_detail**](SecureFileShareApi.md#get_file_detail) | **GET** /sfs/v1/file-details | Get list of files


# **get_file**
> get_file(file_id, organization_id=organization_id)

Download a file with file identifier

Download a file for the given file identifier

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SecureFileShareApi()
file_id = 'file_id_example' # str | Unique identifier for each file
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Download a file with file identifier
    api_instance.get_file(file_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling SecureFileShareApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for each file | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/xml, text/csv, application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_detail**
> V1FileDetailsGet200Response get_file_detail(start_date, end_date, organization_id=organization_id)

Get list of files

Get list of files and it's information of them available inside the report directory

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SecureFileShareApi()
start_date = '2013-10-20' # date | Valid start date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd 
end_date = '2013-10-20' # date | Valid end date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd 
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Get list of files
    api_response = api_instance.get_file_detail(start_date, end_date, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecureFileShareApi->get_file_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Valid start date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd  | 
 **end_date** | **date**| Valid end date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd  | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

[**V1FileDetailsGet200Response**](V1FileDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

