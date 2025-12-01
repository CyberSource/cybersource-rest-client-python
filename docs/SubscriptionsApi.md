# CyberSource.SubscriptionsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_subscription**](SubscriptionsApi.md#activate_subscription) | **POST** /rbs/v1/subscriptions/{id}/activate | Reactivating a Suspended Subscription
[**cancel_subscription**](SubscriptionsApi.md#cancel_subscription) | **POST** /rbs/v1/subscriptions/{id}/cancel | Cancel a Subscription
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /rbs/v1/subscriptions | Create a Subscription
[**get_all_subscriptions**](SubscriptionsApi.md#get_all_subscriptions) | **GET** /rbs/v1/subscriptions | Get a List of Subscriptions
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /rbs/v1/subscriptions/{id} | Get a Subscription
[**get_subscription_code**](SubscriptionsApi.md#get_subscription_code) | **GET** /rbs/v1/subscriptions/code | Get a Subscription Code
[**suspend_subscription**](SubscriptionsApi.md#suspend_subscription) | **POST** /rbs/v1/subscriptions/{id}/suspend | Suspend a Subscription
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PATCH** /rbs/v1/subscriptions/{id} | Update a Subscription


# **activate_subscription**
> ActivateSubscriptionResponse activate_subscription(id, process_missed_payments=process_missed_payments)

Reactivating a Suspended Subscription

# Reactivating a Suspended Subscription  You can reactivate a suspended subscription for the next billing cycle. You cannot reactivate a canceled or completed subscription.  You can specify whether you want to process missed payments for the period during which the subscription was suspended using the `processMissedPayments` query parameter by setting it to true or false.  If no value is specified, the system will default to `true`.  **Important:** The \"processMissedPayments\" query parameter is only effective when the Ask each time before reactivating option is selected in the reactivation settings. If any other option is chosen, the value provided in the request will be ignored by the system. For more information, see the [Recurring Billing User Guide](https://developer.cybersource.com/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/recurring-billing-user-about-guide.html).  You can check how many payments were missed and the total amount by retrieving the subscription details, where you will find the `reactivationInformation` object. See: [Retrieving a Subscription](https://developer.cybersource.com/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-getting-a-subscription.html). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsApi()
id = 'id_example' # str | Subscription Id
process_missed_payments = true # bool | Indicates if missed payments should be processed from the period when the subscription was suspended. By default, this is set to true. When any option other than \"Ask each time before reactivating\" is selected in the reactivation settings, the value that you enter will be ignored.  (optional) (default to true)

try: 
    # Reactivating a Suspended Subscription
    api_response = api_instance.activate_subscription(id, process_missed_payments=process_missed_payments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->activate_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription Id | 
 **process_missed_payments** | **bool**| Indicates if missed payments should be processed from the period when the subscription was suspended. By default, this is set to true. When any option other than \&quot;Ask each time before reactivating\&quot; is selected in the reactivation settings, the value that you enter will be ignored.  | [optional] [default to true]

### Return type

[**ActivateSubscriptionResponse**](ActivateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subscription**
> CancelSubscriptionResponse cancel_subscription(id)

Cancel a Subscription

Cancel a Subscription

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsApi()
id = 'id_example' # str | Subscription Id

try: 
    # Cancel a Subscription
    api_response = api_instance.cancel_subscription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->cancel_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription Id | 

### Return type

[**CancelSubscriptionResponse**](CancelSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> CreateSubscriptionResponse create_subscription(create_subscription_request)

Create a Subscription

Create a Recurring Billing Subscription

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsApi()
create_subscription_request = CyberSource.CreateSubscriptionRequest() # CreateSubscriptionRequest | 

try: 
    # Create a Subscription
    api_response = api_instance.create_subscription(create_subscription_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription_request** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | 

### Return type

[**CreateSubscriptionResponse**](CreateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions**
> GetAllSubscriptionsResponse get_all_subscriptions(offset=offset, limit=limit, code=code, status=status)

Get a List of Subscriptions

Retrieve Subscriptions by Subscription Code & Subscription Status. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsApi()
offset = 56 # int | Page offset number. (optional)
limit = 56 # int | Number of items to be returned. Default - `20`, Max - `100`  (optional)
code = 'code_example' # str | Filter by Subscription Code (optional)
status = 'status_example' # str | Filter by Subscription Status (optional)

try: 
    # Get a List of Subscriptions
    api_response = api_instance.get_all_subscriptions(offset=offset, limit=limit, code=code, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_all_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Page offset number. | [optional] 
 **limit** | **int**| Number of items to be returned. Default - &#x60;20&#x60;, Max - &#x60;100&#x60;  | [optional] 
 **code** | **str**| Filter by Subscription Code | [optional] 
 **status** | **str**| Filter by Subscription Status | [optional] 

### Return type

[**GetAllSubscriptionsResponse**](GetAllSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> GetSubscriptionResponse get_subscription(id)

Get a Subscription

Get a Subscription by Subscription Id

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsApi()
id = 'id_example' # str | Subscription Id

try: 
    # Get a Subscription
    api_response = api_instance.get_subscription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription Id | 

### Return type

[**GetSubscriptionResponse**](GetSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_code**
> GetSubscriptionCodeResponse get_subscription_code()

Get a Subscription Code

Get a Unique Subscription Code

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsApi()

try: 
    # Get a Subscription Code
    api_response = api_instance.get_subscription_code()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSubscriptionCodeResponse**](GetSubscriptionCodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_subscription**
> SuspendSubscriptionResponse suspend_subscription(id)

Suspend a Subscription

Suspend a Subscription 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsApi()
id = 'id_example' # str | Subscription Id

try: 
    # Suspend a Subscription
    api_response = api_instance.suspend_subscription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->suspend_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription Id | 

### Return type

[**SuspendSubscriptionResponse**](SuspendSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> UpdateSubscriptionResponse update_subscription(id, update_subscription)

Update a Subscription

Update a Subscription by Subscription Id

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.SubscriptionsApi()
id = 'id_example' # str | Subscription Id
update_subscription = CyberSource.UpdateSubscription() # UpdateSubscription | Update Subscription

try: 
    # Update a Subscription
    api_response = api_instance.update_subscription(id, update_subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->update_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription Id | 
 **update_subscription** | [**UpdateSubscription**](UpdateSubscription.md)| Update Subscription | 

### Return type

[**UpdateSubscriptionResponse**](UpdateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

