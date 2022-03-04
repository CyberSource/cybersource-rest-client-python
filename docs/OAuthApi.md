# CyberSource.OAuthApi

All URIs are relative to *https://api-ma.Cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_token**](OAuthApi.md#create_access_token) | **POST** /oauth2/v3/token | Create access token and refresh token


# **create_access_token**
> AccessTokenResponse create_access_token(create_access_token_request, v_c_client_correlation_id=v_c_client_correlation_id)

Create access token and refresh token

This request is used by technology partners to obtain an access token and a refresh token, which are contained in the response.  The partner can then use the access token for authentication when submitting API requests to CyberSource on behalf of the merchant.   The request must include the authorization code that was included in the URL redirect response from CyberSource (see [full documentation](https://developer.cybersource.com/api/developer-guides/OAuth/cybs_extend_intro.html)). Access tokens expire after 15 minutes. The refresh token is used to create a new access token, it expires after one year. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.OAuthApi()
create_access_token_request = CyberSource.CreateAccessTokenRequest() # CreateAccessTokenRequest | Request payload
v_c_client_correlation_id = 'v_c_client_correlation_id_example' # str | We recommended that you submit this header with a unique value in every client request to this endpoint.  It is sent back in the response header and logged both in the request log and response log.  (optional)

try: 
    # Create access token and refresh token
    api_response = api_instance.create_access_token(create_access_token_request, v_c_client_correlation_id=v_c_client_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->create_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_access_token_request** | [**CreateAccessTokenRequest**](CreateAccessTokenRequest.md)| Request payload | 
 **v_c_client_correlation_id** | **str**| We recommended that you submit this header with a unique value in every client request to this endpoint.  It is sent back in the response header and logged both in the request log and response log.  | [optional] 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

