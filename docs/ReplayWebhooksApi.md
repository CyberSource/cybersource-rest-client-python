# CyberSource.ReplayWebhooksApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replay_previous_webhooks**](ReplayWebhooksApi.md#replay_previous_webhooks) | **POST** /nrtf/v1/webhooks/{webhookId}/replays | Replay Previous Webhooks


# **replay_previous_webhooks**
> replay_previous_webhooks(webhook_id, replay_webhooks_request=replay_webhooks_request)

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
api_instance = CyberSource.ReplayWebhooksApi()
webhook_id = 'webhook_id_example' # str | The webhook uuid identifier.
replay_webhooks_request = CyberSource.ReplayWebhooksRequest() # ReplayWebhooksRequest | The request query (optional)

try: 
    # Replay Previous Webhooks
    api_instance.replay_previous_webhooks(webhook_id, replay_webhooks_request=replay_webhooks_request)
except ApiException as e:
    print("Exception when calling ReplayWebhooksApi->replay_previous_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook uuid identifier. | 
 **replay_webhooks_request** | [**ReplayWebhooksRequest**](ReplayWebhooksRequest.md)| The request query | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

