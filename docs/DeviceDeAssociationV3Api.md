# CyberSource.DeviceDeAssociationV3Api

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_de_associate_v3_terminal**](DeviceDeAssociationV3Api.md#post_de_associate_v3_terminal) | **POST** /dms/v3/devices/deassociate | De-associate a device from merchant to account or reseller and from account to reseller V3


# **post_de_associate_v3_terminal**
> list[InlineResponse2005] post_de_associate_v3_terminal(device_de_associate_v3_request)

De-associate a device from merchant to account or reseller and from account to reseller V3

A device will be de-associated from its current organization and moved up in the hierarchy. The device's new position will be determined by a specified destination, either an account or a portfolio. If no destination is provided, the device will default to the currently logged-in user. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DeviceDeAssociationV3Api()
device_de_associate_v3_request = [CyberSource.DeviceDeAssociateV3Request()] # list[DeviceDeAssociateV3Request] | deviceId that has to be de-associated to the destination organizationId.

try: 
    # De-associate a device from merchant to account or reseller and from account to reseller V3
    api_response = api_instance.post_de_associate_v3_terminal(device_de_associate_v3_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceDeAssociationV3Api->post_de_associate_v3_terminal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_de_associate_v3_request** | [**list[DeviceDeAssociateV3Request]**](DeviceDeAssociateV3Request.md)| deviceId that has to be de-associated to the destination organizationId. | 

### Return type

[**list[InlineResponse2005]**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

