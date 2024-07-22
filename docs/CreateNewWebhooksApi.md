# CyberSource.CreateNewWebhooksApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_subscription**](CreateNewWebhooksApi.md#create_webhook_subscription) | **POST** /notification-subscriptions/v1/webhooks | Create a Webhook
[**find_products_to_subscribe**](CreateNewWebhooksApi.md#find_products_to_subscribe) | **GET** /notification-subscriptions/v1/products/{organizationId} | Find Products You Can Subscribe To
[**save_sym_egress_key**](CreateNewWebhooksApi.md#save_sym_egress_key) | **POST** /kms/egress/v2/keys-sym | Create Webhook Security Keys


# **create_webhook_subscription**
> InlineResponse2014 create_webhook_subscription(create_webhook_request=create_webhook_request)

Create a Webhook

Create a new webhook subscription. Before creating a webhook, ensure that a security key has been created at the top of this developer center section. You will not need to pass us back the key during the creation of the webhook, but you will receive an error if you did not already create a key or store one on file. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CreateNewWebhooksApi()
create_webhook_request = CyberSource.CreateWebhookRequest() # CreateWebhookRequest | The webhook payload (optional)

try: 
    # Create a Webhook
    api_response = api_instance.create_webhook_subscription(create_webhook_request=create_webhook_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateNewWebhooksApi->create_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)| The webhook payload | [optional] 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_products_to_subscribe**
> list[InlineResponse2003] find_products_to_subscribe(organization_id)

Find Products You Can Subscribe To

Retrieve a list of products and event types that your account is eligible for. These products and events are the ones that you may subscribe to in the next step of creating webhooks.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CreateNewWebhooksApi()
organization_id = 'organization_id_example' # str | The Organization Identifier.

try: 
    # Find Products You Can Subscribe To
    api_response = api_instance.find_products_to_subscribe(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateNewWebhooksApi->find_products_to_subscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The Organization Identifier. | 

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_sym_egress_key**
> InlineResponse2013 save_sym_egress_key(v_c_sender_organization_id, v_c_permissions, v_c_correlation_id=v_c_correlation_id, save_sym_egress_key=save_sym_egress_key)

Create Webhook Security Keys

Create security keys that CyberSource will use internally to connect to your servers and validate messages using a digital signature.  Select the CREATE example for CyberSource to generate the key on our server and maintain it for you as well. Remeber to save the key in the API response, so that you can use it to validate messages later. 

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
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

