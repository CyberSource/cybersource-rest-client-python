# CyberSource.ReportSubscriptionsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](ReportSubscriptionsApi.md#create_subscription) | **PUT** /reporting/v3/report-subscriptions | Create Report Subscription for a report name by organization
[**delete_subscription**](ReportSubscriptionsApi.md#delete_subscription) | **DELETE** /reporting/v3/report-subscriptions/{reportName} | Delete subscription of a report name by organization
[**get_all_subscriptions**](ReportSubscriptionsApi.md#get_all_subscriptions) | **GET** /reporting/v3/report-subscriptions | Get all subscriptions
[**get_subscription**](ReportSubscriptionsApi.md#get_subscription) | **GET** /reporting/v3/report-subscriptions/{reportName} | Get subscription for report name
[**reporting_v3_predefined_report_subscriptions_put**](ReportSubscriptionsApi.md#reporting_v3_predefined_report_subscriptions_put) | **PUT** /reporting/v3/predefined-report-subscriptions | Create a Standard or Classic subscription


# **create_subscription**
> create_subscription(create_report_subscription_request, organization_id=organization_id)

Create Report Subscription for a report name by organization

Create a report subscription for your organization. The report name must be unique. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportSubscriptionsApi()
create_report_subscription_request = CyberSource.CreateReportSubscriptionRequest() # CreateReportSubscriptionRequest | Report subscription request payload
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Create Report Subscription for a report name by organization
    api_instance.create_subscription(create_report_subscription_request, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportSubscriptionsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_report_subscription_request** | [**CreateReportSubscriptionRequest**](CreateReportSubscriptionRequest.md)| Report subscription request payload | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(report_name)

Delete subscription of a report name by organization

Delete a report subscription for your organization. You must know the unique name of the report you want to delete. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportSubscriptionsApi()
report_name = 'report_name_example' # str | Name of the Report to Delete

try: 
    # Delete subscription of a report name by organization
    api_instance.delete_subscription(report_name)
except ApiException as e:
    print("Exception when calling ReportSubscriptionsApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_name** | **str**| Name of the Report to Delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions**
> ReportingV3ReportSubscriptionsGet200Response get_all_subscriptions()

Get all subscriptions

View a summary of all report subscriptions. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportSubscriptionsApi()

try: 
    # Get all subscriptions
    api_response = api_instance.get_all_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportSubscriptionsApi->get_all_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReportingV3ReportSubscriptionsGet200Response**](ReportingV3ReportSubscriptionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> ReportingV3ReportSubscriptionsGet200ResponseSubscriptions get_subscription(report_name)

Get subscription for report name

View the details of a report subscription, such as the report format or report frequency, using the report’s unique name. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportSubscriptionsApi()
report_name = 'report_name_example' # str | Name of the Report to Retrieve

try: 
    # Get subscription for report name
    api_response = api_instance.get_subscription(report_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportSubscriptionsApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_name** | **str**| Name of the Report to Retrieve | 

### Return type

[**ReportingV3ReportSubscriptionsGet200ResponseSubscriptions**](ReportingV3ReportSubscriptionsGet200ResponseSubscriptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reporting_v3_predefined_report_subscriptions_put**
> reporting_v3_predefined_report_subscriptions_put(predefined_subscription_request_bean, organization_id=organization_id)

Create a Standard or Classic subscription

Create or update an already existing classic or standard subscription. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ReportSubscriptionsApi()
predefined_subscription_request_bean = CyberSource.PredefinedSubscriptionRequestBean() # PredefinedSubscriptionRequestBean | Report subscription request payload
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)

try: 
    # Create a Standard or Classic subscription
    api_instance.reporting_v3_predefined_report_subscriptions_put(predefined_subscription_request_bean, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportSubscriptionsApi->reporting_v3_predefined_report_subscriptions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predefined_subscription_request_bean** | [**PredefinedSubscriptionRequestBean**](PredefinedSubscriptionRequestBean.md)| Report subscription request payload | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

