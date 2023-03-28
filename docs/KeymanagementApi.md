# CyberSource.KeymanagementApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_keys**](KeymanagementApi.md#search_keys) | **GET** /kms/v2/keys | Search Keys


# **search_keys**
> InlineResponse20011 search_keys(offset=offset, limit=limit, sort=sort, organization_ids=organization_ids, key_ids=key_ids, key_types=key_types, expiration_start_date=expiration_start_date, expiration_end_date=expiration_end_date)

Search Keys

Search one or more Keys

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.KeymanagementApi()
offset = 56 # int | This allows you to specify the page offset from the resulting list resultset you want the records to be returned (optional)
limit = 56 # int | This allows you to specify the total number of records to be returned off the resulting list resultset (optional)
sort = 'sort_example' # str | This allows you to specify a comma separated list of fields in the order which the resulting list resultset must be sorted. (optional)
organization_ids = ['organization_ids_example'] # list[str] | List of Orgaization Ids to search. The maximum size of the organization Ids list is 1. The maximum length of Organization Id is 30. (optional)
key_ids = ['key_ids_example'] # list[str] | List of Key Ids to search. The maximum size of the Key Ids list is 1 (optional)
key_types = ['key_types_example'] # list[str] | Key Type, Possible values -  certificate, password, pgp and scmp_api. When Key Type is provided atleast one more filter needs to be provided (optional)
expiration_start_date = '2013-10-20T19:20:30+01:00' # datetime | Expiry Filter Start Date. When Expiration Date filter is provided, atleast one more filter needs to be provided (optional)
expiration_end_date = '2013-10-20T19:20:30+01:00' # datetime | Expiry Filter End Date. When Expiration Date filter is provided, atleast one more filter needs to be provided (optional)

try: 
    # Search Keys
    api_response = api_instance.search_keys(offset=offset, limit=limit, sort=sort, organization_ids=organization_ids, key_ids=key_ids, key_types=key_types, expiration_start_date=expiration_start_date, expiration_end_date=expiration_end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagementApi->search_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| This allows you to specify the page offset from the resulting list resultset you want the records to be returned | [optional] 
 **limit** | **int**| This allows you to specify the total number of records to be returned off the resulting list resultset | [optional] 
 **sort** | **str**| This allows you to specify a comma separated list of fields in the order which the resulting list resultset must be sorted. | [optional] 
 **organization_ids** | [**list[str]**](str.md)| List of Orgaization Ids to search. The maximum size of the organization Ids list is 1. The maximum length of Organization Id is 30. | [optional] 
 **key_ids** | [**list[str]**](str.md)| List of Key Ids to search. The maximum size of the Key Ids list is 1 | [optional] 
 **key_types** | [**list[str]**](str.md)| Key Type, Possible values -  certificate, password, pgp and scmp_api. When Key Type is provided atleast one more filter needs to be provided | [optional] 
 **expiration_start_date** | **datetime**| Expiry Filter Start Date. When Expiration Date filter is provided, atleast one more filter needs to be provided | [optional] 
 **expiration_end_date** | **datetime**| Expiry Filter End Date. When Expiration Date filter is provided, atleast one more filter needs to be provided | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

