# CyberSource.DecisionManagerApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_negative**](DecisionManagerApi.md#add_negative) | **POST** /risk/v1/lists/{type}/entries | List Management
[**create_bundled_decision_manager_case**](DecisionManagerApi.md#create_bundled_decision_manager_case) | **POST** /risk/v1/decisions | Create Decision Manager
[**fraud_update**](DecisionManagerApi.md#fraud_update) | **POST** /risk/v1/decisions/{id}/marking | Fraud Marking


# **add_negative**
> RiskV1UpdatePost201Response add_negative(type, add_negative_list_request)

List Management

This call adds/deletes/converts the request information in the negative list.  Provide the list to be updated as the path parameter. This value can be 'postiive', 'negative' or 'review'. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DecisionManagerApi()
type = 'type_example' # str | The list to be updated. It can be 'positive', 'negative' or 'review'.
add_negative_list_request = CyberSource.AddNegativeListRequest() # AddNegativeListRequest | 

try: 
    # List Management
    api_response = api_instance.add_negative(type, add_negative_list_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionManagerApi->add_negative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The list to be updated. It can be &#39;positive&#39;, &#39;negative&#39; or &#39;review&#39;. | 
 **add_negative_list_request** | [**AddNegativeListRequest**](AddNegativeListRequest.md)|  | 

### Return type

[**RiskV1UpdatePost201Response**](RiskV1UpdatePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bundled_decision_manager_case**
> RiskV1DecisionsPost201Response create_bundled_decision_manager_case(create_bundled_decision_manager_case_request)

Create Decision Manager

Decision Manager can help you automate and streamline your fraud operations. Decision Manager will return a decision based on the request values.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DecisionManagerApi()
create_bundled_decision_manager_case_request = CyberSource.CreateBundledDecisionManagerCaseRequest() # CreateBundledDecisionManagerCaseRequest | 

try: 
    # Create Decision Manager
    api_response = api_instance.create_bundled_decision_manager_case(create_bundled_decision_manager_case_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionManagerApi->create_bundled_decision_manager_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bundled_decision_manager_case_request** | [**CreateBundledDecisionManagerCaseRequest**](CreateBundledDecisionManagerCaseRequest.md)|  | 

### Return type

[**RiskV1DecisionsPost201Response**](RiskV1DecisionsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fraud_update**
> RiskV1UpdatePost201Response fraud_update(id, fraud_marking_action_request)

Fraud Marking

This can be used to - 1. Add known fraudulent data to the fraud history 2. Remove data added to history with Transaction Marking Tool or by uploading chargeback files 3. Remove chargeback data from history that was automatically added. For detailed information, contact your Cybersource representative  Place the request ID of the transaction you want to mark as suspect (or remove from history) as the path parameter in this request. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DecisionManagerApi()
id = 'id_example' # str | Request ID of the transaction that you want to mark as suspect or remove from history.
fraud_marking_action_request = CyberSource.FraudMarkingActionRequest() # FraudMarkingActionRequest | 

try: 
    # Fraud Marking
    api_response = api_instance.fraud_update(id, fraud_marking_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionManagerApi->fraud_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Request ID of the transaction that you want to mark as suspect or remove from history. | 
 **fraud_marking_action_request** | [**FraudMarkingActionRequest**](FraudMarkingActionRequest.md)|  | 

### Return type

[**RiskV1UpdatePost201Response**](RiskV1UpdatePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

