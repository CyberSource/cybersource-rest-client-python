# CyberSource.UserManagementSearchApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_users**](UserManagementSearchApi.md#search_users) | **POST** /ums/v1/users/search | Search User Information


# **search_users**
> UmsV1UsersGet200Response search_users(search_request)

Search User Information

This endpoint is to get all the user information depending on the filter criteria passed in request body.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.UserManagementSearchApi()
search_request = CyberSource.SearchRequest() # SearchRequest | 

try: 
    # Search User Information
    api_response = api_instance.search_users(search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementSearchApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**UmsV1UsersGet200Response**](UmsV1UsersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

