# CyberSource.CreateNewWebhooksApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_sym_egress_key**](CreateNewWebhooksApi.md#save_sym_egress_key) | **POST** /kms/egress/v2/keys-sym | Create Webhook Security Keys


# **save_sym_egress_key**
> InlineResponse2013 save_sym_egress_key(v_c_sender_organization_id, v_c_permissions, v_c_correlation_id=v_c_correlation_id, save_sym_egress_key=save_sym_egress_key)

Create Webhook Security Keys

Create security keys that CyberSource will use internally to connect to your servers and validate messages using a digital signature.  Select the CREATE example for CyberSource to generate the key on our server and maintain it for you as well. Remember to save the key in the API response, so that you can use it to validate messages later. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CreateNewWebhooksApi()
v_c_sender_organization_id = 'v_c_sender_organization_id_example' # str | Sender organization id
v_c_permissions = 'v_c_permissions_example' # str | Encoded user permissions returned by the CGK, for the entity user who initiated the boarding
v_c_correlation_id = 'v_c_correlation_id_example' # str | A globally unique id associated with your request (optional)
save_sym_egress_key = CyberSource.SaveSymEgressKey() # SaveSymEgressKey | Provide egress Symmetric key information to save (create or store or refresh) (optional)

try: 
    # Create Webhook Security Keys
    api_response = api_instance.save_sym_egress_key(v_c_sender_organization_id, v_c_permissions, v_c_correlation_id=v_c_correlation_id, save_sym_egress_key=save_sym_egress_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateNewWebhooksApi->save_sym_egress_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v_c_sender_organization_id** | **str**| Sender organization id | 
 **v_c_permissions** | **str**| Encoded user permissions returned by the CGK, for the entity user who initiated the boarding | 
 **v_c_correlation_id** | **str**| A globally unique id associated with your request | [optional] 
 **save_sym_egress_key** | [**SaveSymEgressKey**](SaveSymEgressKey.md)| Provide egress Symmetric key information to save (create or store or refresh) | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

