# CyberSource.DecisionManagerApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_decision_manager_case**](DecisionManagerApi.md#create_decision_manager_case) | **POST** /risk/v1/decisions | Create Decision Manager case


# **create_decision_manager_case**
> RiskV1DecisionsPost201Response create_decision_manager_case(create_decision_manager_case_request)

Create Decision Manager case

This is the combined request to the Decision Manager Service for a transaction sent to Cybersource. Decision Manager will return a decision based on the request values. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.DecisionManagerApi()
create_decision_manager_case_request = CyberSource.CreateDecisionManagerCaseRequest() # CreateDecisionManagerCaseRequest | 

try: 
    # Create Decision Manager case
    api_response = api_instance.create_decision_manager_case(create_decision_manager_case_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionManagerApi->create_decision_manager_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_decision_manager_case_request** | [**CreateDecisionManagerCaseRequest**](CreateDecisionManagerCaseRequest.md)|  | 

### Return type

[**RiskV1DecisionsPost201Response**](RiskV1DecisionsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

