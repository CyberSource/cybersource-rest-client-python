# CyberSource.DeviceDeAssociationApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_terminal_association**](DeviceDeAssociationApi.md#delete_terminal_association) | **PATCH** /dms/v2/devices/deassociate | De-associate a device from merchant or account V2
[**post_de_associate_v3_terminal**](DeviceDeAssociationApi.md#post_de_associate_v3_terminal) | **POST** /dms/v3/devices/deassociate | De-associate a device from merchant to account or reseller and from account to reseller


# **delete_terminal_association**
> delete_terminal_association(de_association_request_body)

De-associate a device from merchant or account V2

The current association of the device will be removed and will be assigned back to parent in the hierarchy based on internal logic

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DeviceDeAssociationApi()
de_association_request_body = CyberSource.DeAssociationRequestBody() # DeAssociationRequestBody | de association of the deviceId in the request body.

try: 
    # De-associate a device from merchant or account V2
    api_instance.delete_terminal_association(de_association_request_body)
except ApiException as e:
    print("Exception when calling DeviceDeAssociationApi->delete_terminal_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **de_association_request_body** | [**DeAssociationRequestBody**](DeAssociationRequestBody.md)| de association of the deviceId in the request body. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_de_associate_v3_terminal**
> list[InlineResponse2009] post_de_associate_v3_terminal(device_de_associate_v3_request)

De-associate a device from merchant to account or reseller and from account to reseller

A device will be de-associated from its current organization and moved up in the hierarchy. The device's new position will be determined by a specified destination, either an account or a portfolio. If no destination is provided, the device will default to the currently logged-in user. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DeviceDeAssociationApi()
device_de_associate_v3_request = [CyberSource.DeviceDeAssociateV3Request()] # list[DeviceDeAssociateV3Request] | deviceId that has to be de-associated to the destination organizationId.

try: 
    # De-associate a device from merchant to account or reseller and from account to reseller
    api_response = api_instance.post_de_associate_v3_terminal(device_de_associate_v3_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceDeAssociationApi->post_de_associate_v3_terminal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_de_associate_v3_request** | [**list[DeviceDeAssociateV3Request]**](DeviceDeAssociateV3Request.md)| deviceId that has to be de-associated to the destination organizationId. | 

### Return type

[**list[InlineResponse2009]**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

