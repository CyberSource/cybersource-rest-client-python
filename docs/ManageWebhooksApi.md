# CyberSource.ManageWebhooksApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_subscriptions_v1_webhooks_get**](ManageWebhooksApi.md#notification_subscriptions_v1_webhooks_get) | **GET** /notification-subscriptions/v1/webhooks | Get Details On All Created Webhooks
[**notification_subscriptions_v1_webhooks_webhook_id_delete**](ManageWebhooksApi.md#notification_subscriptions_v1_webhooks_webhook_id_delete) | **DELETE** /notification-subscriptions/v1/webhooks/{webhookId} | Delete a Webhook Subscription
[**notification_subscriptions_v1_webhooks_webhook_id_get**](ManageWebhooksApi.md#notification_subscriptions_v1_webhooks_webhook_id_get) | **GET** /notification-subscriptions/v1/webhooks/{webhookId} | Get Details On a Single Webhook
[**notification_subscriptions_v1_webhooks_webhook_id_patch**](ManageWebhooksApi.md#notification_subscriptions_v1_webhooks_webhook_id_patch) | **PATCH** /notification-subscriptions/v1/webhooks/{webhookId} | Update a Webhook Subscription
[**nrtf_v1_webhooks_webhook_id_replays_post**](ManageWebhooksApi.md#nrtf_v1_webhooks_webhook_id_replays_post) | **POST** /nrtf/v1/webhooks/{webhookId}/replays | Replay Previous Webhooks
[**save_asym_egress_key**](ManageWebhooksApi.md#save_asym_egress_key) | **POST** /kms/egress/v2/keys-asym | Message Level Encryption


# **notification_subscriptions_v1_webhooks_get**
> list[InlineResponse2004] notification_subscriptions_v1_webhooks_get(organization_id, product_id, event_type)

Get Details On All Created Webhooks

Retrieve a list of all previously created webhooks.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ManageWebhooksApi()
organization_id = 'organization_id_example' # str | The Organization Identifier.
product_id = 'product_id_example' # str | The Product Identifier.
event_type = 'event_type_example' # str | The Event Type.

try: 
    # Get Details On All Created Webhooks
    api_response = api_instance.notification_subscriptions_v1_webhooks_get(organization_id, product_id, event_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageWebhooksApi->notification_subscriptions_v1_webhooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The Organization Identifier. | 
 **product_id** | **str**| The Product Identifier. | 
 **event_type** | **str**| The Event Type. | 

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_subscriptions_v1_webhooks_webhook_id_delete**
> notification_subscriptions_v1_webhooks_webhook_id_delete(webhook_id)

Delete a Webhook Subscription

Delete the webhook. Please note that deleting a particular webhook does not delete the history of the webhook notifications.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ManageWebhooksApi()
webhook_id = 'webhook_id_example' # str | The webhook identifier.

try: 
    # Delete a Webhook Subscription
    api_instance.notification_subscriptions_v1_webhooks_webhook_id_delete(webhook_id)
except ApiException as e:
    print("Exception when calling ManageWebhooksApi->notification_subscriptions_v1_webhooks_webhook_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook identifier. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_subscriptions_v1_webhooks_webhook_id_get**
> InlineResponse2004 notification_subscriptions_v1_webhooks_webhook_id_get(webhook_id)

Get Details On a Single Webhook

Retrieve the details of a specific webhook by supplying the webhook ID in the path.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ManageWebhooksApi()
webhook_id = 'webhook_id_example' # str | The webhook Identifier

try: 
    # Get Details On a Single Webhook
    api_response = api_instance.notification_subscriptions_v1_webhooks_webhook_id_get(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageWebhooksApi->notification_subscriptions_v1_webhooks_webhook_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook Identifier | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_subscriptions_v1_webhooks_webhook_id_patch**
> notification_subscriptions_v1_webhooks_webhook_id_patch(webhook_id, update_webhook=update_webhook)

Update a Webhook Subscription

Update the webhook subscription using PATCH.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ManageWebhooksApi()
webhook_id = 'webhook_id_example' # str | The Webhook Identifier.
update_webhook = CyberSource.UpdateWebhook() # UpdateWebhook | The webhook payload or changes to apply. (optional)

try: 
    # Update a Webhook Subscription
    api_instance.notification_subscriptions_v1_webhooks_webhook_id_patch(webhook_id, update_webhook=update_webhook)
except ApiException as e:
    print("Exception when calling ManageWebhooksApi->notification_subscriptions_v1_webhooks_webhook_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The Webhook Identifier. | 
 **update_webhook** | [**UpdateWebhook**](UpdateWebhook.md)| The webhook payload or changes to apply. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nrtf_v1_webhooks_webhook_id_replays_post**
> nrtf_v1_webhooks_webhook_id_replays_post(webhook_id, replay_webhooks=replay_webhooks)

Replay Previous Webhooks

Initiate a webhook replay request to replay transactions that happened in the past.  Cannot execute more than 1 replay request at a time. While one request is processing, you will not be allowed to execute another replay.  The difference between Start and End time cannot exceed a 24 hour window, and 1 month is the farthest date back that is eligible for replay. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ManageWebhooksApi()
webhook_id = 'webhook_id_example' # str | The webhook uuid identifier.
replay_webhooks = CyberSource.ReplayWebhooks() # ReplayWebhooks | The request query (optional)

try: 
    # Replay Previous Webhooks
    api_instance.nrtf_v1_webhooks_webhook_id_replays_post(webhook_id, replay_webhooks=replay_webhooks)
except ApiException as e:
    print("Exception when calling ManageWebhooksApi->nrtf_v1_webhooks_webhook_id_replays_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook uuid identifier. | 
 **replay_webhooks** | [**ReplayWebhooks**](ReplayWebhooks.md)| The request query | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_asym_egress_key**
> InlineResponse2014 save_asym_egress_key(v_c_sender_organization_id, v_c_permissions, save_asym_egress_key, v_c_correlation_id=v_c_correlation_id)

Message Level Encryption

Store and manage certificates that will be used to preform Message Level Encryption (MLE). Each new webhook will need its own unique asymmetric certificate. You can either use a digital certificate issued/signed by a CA or self-sign your own using the documentation available on the Developer Guide. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ManageWebhooksApi()
v_c_sender_organization_id = 'v_c_sender_organization_id_example' # str | Sender organization id
v_c_permissions = 'v_c_permissions_example' # str | Encoded user permissions returned by the CGK, for the entity user who initiated the boarding
save_asym_egress_key = CyberSource.SaveAsymEgressKey() # SaveAsymEgressKey | Provide egress Asymmetric key information to save (create or store)
v_c_correlation_id = 'v_c_correlation_id_example' # str | A globally unique id associated with your request (optional)

try: 
    # Message Level Encryption
    api_response = api_instance.save_asym_egress_key(v_c_sender_organization_id, v_c_permissions, save_asym_egress_key, v_c_correlation_id=v_c_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageWebhooksApi->save_asym_egress_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v_c_sender_organization_id** | **str**| Sender organization id | 
 **v_c_permissions** | **str**| Encoded user permissions returned by the CGK, for the entity user who initiated the boarding | 
 **save_asym_egress_key** | [**SaveAsymEgressKey**](SaveAsymEgressKey.md)| Provide egress Asymmetric key information to save (create or store) | 
 **v_c_correlation_id** | **str**| A globally unique id associated with your request | [optional] 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

