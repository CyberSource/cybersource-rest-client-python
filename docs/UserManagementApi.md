# CyberSource.UserManagementApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_users**](UserManagementApi.md#get_users) | **GET** /ums/v1/users | Get User Information - Deprecated


# **get_users**
> UmsV1UsersGet200Response get_users(organization_id=organization_id, user_name=user_name, permission_id=permission_id, role_id=role_id)

Get User Information - Deprecated

This endpoint is deprecated. Please use the search end point.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.UserManagementApi()
organization_id = 'organization_id_example' # str | This is the orgId of the organization which the user belongs to. (optional)
user_name = 'user_name_example' # str | User ID of the user you want to get details on. (optional)
permission_id = 'permission_id_example' # str | permission that you are trying to search user on. (optional)
role_id = 'role_id_example' # str | role of the user you are trying to search on. (optional)

try: 
    # Get User Information - Deprecated
    api_response = api_instance.get_users(organization_id=organization_id, user_name=user_name, permission_id=permission_id, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| This is the orgId of the organization which the user belongs to. | [optional] 
 **user_name** | **str**| User ID of the user you want to get details on. | [optional] 
 **permission_id** | **str**| permission that you are trying to search user on. | [optional] 
 **role_id** | **str**| role of the user you are trying to search on. | [optional] 

### Return type

[**UmsV1UsersGet200Response**](UmsV1UsersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

