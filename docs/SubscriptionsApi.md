# CyberSource.SubscriptionsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_subscription**](SubscriptionsApi.md#activate_subscription) | **POST** /rbs/v1/subscriptions/{id}/activate | Activate a Subscription
[**cancel_subscription**](SubscriptionsApi.md#cancel_subscription) | **POST** /rbs/v1/subscriptions/{id}/cancel | Cancel a Subscription
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /rbs/v1/subscriptions | Create a Subscription
[**get_all_subscriptions**](SubscriptionsApi.md#get_all_subscriptions) | **GET** /rbs/v1/subscriptions | Get a List of Subscriptions
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /rbs/v1/subscriptions/{id} | Get a Subscription
[**get_subscription_code**](SubscriptionsApi.md#get_subscription_code) | **GET** /rbs/v1/subscriptions/code | Get a Subscription Code
[**suspend_subscription**](SubscriptionsApi.md#suspend_subscription) | **POST** /rbs/v1/subscriptions/{id}/suspend | Suspend a Subscription
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PATCH** /rbs/v1/subscriptions/{id} | Update a Subscription


# **activate_subscription**
> InlineResponse2009 activate_subscription(id)

Activate a Subscription

Activate a `CANCELLED` Or `SUSPENDED` Subscription 

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
    # Activate a Subscription
    api_response = api_instance.activate_subscription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->activate_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription Id | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subscription**
> InlineResponse202 cancel_subscription(id)

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

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> InlineResponse2011 create_subscription(create_subscription_request)

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

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions**
> InlineResponse2006 get_all_subscriptions(offset=offset, limit=limit, code=code, status=status)

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

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> InlineResponse2007 get_subscription(id)

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

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_code**
> InlineResponse20010 get_subscription_code()

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

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_subscription**
> InlineResponse2021 suspend_subscription(id)

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

[**InlineResponse2021**](InlineResponse2021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> InlineResponse2008 update_subscription(id, update_subscription)

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

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json, application/hal+json, application/json;charset=utf-8, application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

