# CyberSource.SubscriptionsFollowOnsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_follow_on_subscription**](SubscriptionsFollowOnsApi.md#create_follow_on_subscription) | **POST** /rbs/v1/subscriptions/follow-ons/{requestId} | Create a Follow-On Subscription
[**get_follow_on_subscription**](SubscriptionsFollowOnsApi.md#get_follow_on_subscription) | **GET** /rbs/v1/subscriptions/follow-ons/{requestId} | Get a Follow-On Subscription


# **create_follow_on_subscription**
> CreateSubscriptionResponse create_follow_on_subscription(request_id, create_subscription_request)

Create a Follow-On Subscription

Create a new Subscription based on the Request Id of an existing successful Transaction.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsFollowOnsApi()
request_id = 'request_id_example' # str | Request Id of an existing successful Transaction
create_subscription_request = CyberSource.CreateSubscriptionRequest1() # CreateSubscriptionRequest1 | 

try: 
    # Create a Follow-On Subscription
    api_response = api_instance.create_follow_on_subscription(request_id, create_subscription_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsFollowOnsApi->create_follow_on_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request Id of an existing successful Transaction | 
 **create_subscription_request** | [**CreateSubscriptionRequest1**](CreateSubscriptionRequest1.md)|  | 

### Return type

[**CreateSubscriptionResponse**](CreateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_follow_on_subscription**
> GetSubscriptionResponse1 get_follow_on_subscription(request_id)

Get a Follow-On Subscription

Get details of the Subscription being created based on the Request Id of an existing successful Transaction. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsFollowOnsApi()
request_id = 'request_id_example' # str | Request Id of an existing successful Transaction

try: 
    # Get a Follow-On Subscription
    api_response = api_instance.get_follow_on_subscription(request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsFollowOnsApi->get_follow_on_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request Id of an existing successful Transaction | 

### Return type

[**GetSubscriptionResponse1**](GetSubscriptionResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

