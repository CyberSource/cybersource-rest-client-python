# CyberSource.PlansApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_plan**](PlansApi.md#activate_plan) | **POST** /rbs/v1/plans/{id}/activate | Activate a Plan
[**create_plan**](PlansApi.md#create_plan) | **POST** /rbs/v1/plans | Create a Plan
[**deactivate_plan**](PlansApi.md#deactivate_plan) | **POST** /rbs/v1/plans/{id}/deactivate | Deactivate a Plan
[**delete_plan**](PlansApi.md#delete_plan) | **DELETE** /rbs/v1/plans/{id} | Delete a Plan
[**get_plan**](PlansApi.md#get_plan) | **GET** /rbs/v1/plans/{id} | Get a Plan
[**get_plan_code**](PlansApi.md#get_plan_code) | **GET** /rbs/v1/plans/code | Get a Plan Code
[**get_plans**](PlansApi.md#get_plans) | **GET** /rbs/v1/plans | Get a List of Plans
[**update_plan**](PlansApi.md#update_plan) | **PATCH** /rbs/v1/plans/{id} | Update a Plan


# **activate_plan**
> InlineResponse2004 activate_plan(id)

Activate a Plan

Activate a Plan

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PlansApi()
id = 'id_example' # str | Plan Id

try: 
    # Activate a Plan
    api_response = api_instance.activate_plan(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->activate_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan Id | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plan**
> InlineResponse201 create_plan(create_plan_request)

Create a Plan

The recurring billing service enables you to manage payment plans and subscriptions for recurring payment schedules. It securely stores your customer's payment information and personal data within secure Visa data centers, reducing storage risks and PCI DSS scope through the use of *Token Management* (*TMS*).  The three key elements of *Cybersource* Recurring Billing are:  -  **Token**: stores customer billing, shipping, and payment details.  -  **Plan**: stores the billing schedule.  -  **Subscription**: combines the token and plan, and defines the subscription start date, name, and description.  The APIs in this section demonstrate the management of the Plans and Subscriptions. For Tokens please refer to [Token Management](#token-management) 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PlansApi()
create_plan_request = CyberSource.CreatePlanRequest() # CreatePlanRequest | 

try: 
    # Create a Plan
    api_response = api_instance.create_plan(create_plan_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->create_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_plan_request** | [**CreatePlanRequest**](CreatePlanRequest.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_plan**
> InlineResponse2004 deactivate_plan(id)

Deactivate a Plan

Deactivate a Plan

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PlansApi()
id = 'id_example' # str | Plan Id

try: 
    # Deactivate a Plan
    api_response = api_instance.deactivate_plan(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->deactivate_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan Id | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plan**
> InlineResponse2002 delete_plan(id)

Delete a Plan

Delete a Plan is only allowed: - plan status is in `DRAFT` - plan status is in `ACTIVE`, and `INACTIVE` only allowed when no subscriptions attached to a plan in the lifetime of a plan 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PlansApi()
id = 'id_example' # str | Plan Id

try: 
    # Delete a Plan
    api_response = api_instance.delete_plan(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->delete_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan Id | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan**
> InlineResponse2001 get_plan(id)

Get a Plan

Retrieve a Plan details by Plan Id.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PlansApi()
id = 'id_example' # str | Plan Id

try: 
    # Get a Plan
    api_response = api_instance.get_plan(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->get_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan Id | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_code**
> InlineResponse2005 get_plan_code()

Get a Plan Code

Get a Unique Plan Code

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PlansApi()

try: 
    # Get a Plan Code
    api_response = api_instance.get_plan_code()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->get_plan_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plans**
> InlineResponse200 get_plans(offset=offset, limit=limit, code=code, status=status, name=name)

Get a List of Plans

Retrieve Plans by Plan Code & Plan Status. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PlansApi()
offset = 56 # int | Page offset number. (optional)
limit = 56 # int | Number of items to be returned. Default - `20`, Max - `100`  (optional)
code = 'code_example' # str | Filter by Plan Code (optional)
status = 'status_example' # str | Filter by Plan Status (optional)
name = 'name_example' # str | Filter by Plan Name. (First sub string or full string) **[Not Recommended]**  (optional)

try: 
    # Get a List of Plans
    api_response = api_instance.get_plans(offset=offset, limit=limit, code=code, status=status, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->get_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Page offset number. | [optional] 
 **limit** | **int**| Number of items to be returned. Default - &#x60;20&#x60;, Max - &#x60;100&#x60;  | [optional] 
 **code** | **str**| Filter by Plan Code | [optional] 
 **status** | **str**| Filter by Plan Status | [optional] 
 **name** | **str**| Filter by Plan Name. (First sub string or full string) **[Not Recommended]**  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plan**
> InlineResponse2003 update_plan(id, update_plan_request)

Update a Plan

Update a Plan  Plan in `DRAFT` status - All updates are allowed on Plan with `DRAFT` status  Plan in `ACTIVE` status [Following fields are **Not Updatable**] - `planInformation.billingPeriod` - `planInformation.billingCycles` [Update is only allowed to **increase** billingCycles] - `orderInformation.amountDetails.currency` 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PlansApi()
id = 'id_example' # str | Plan Id
update_plan_request = CyberSource.UpdatePlanRequest() # UpdatePlanRequest | 

try: 
    # Update a Plan
    api_response = api_instance.update_plan(id, update_plan_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->update_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan Id | 
 **update_plan_request** | [**UpdatePlanRequest**](UpdatePlanRequest.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

