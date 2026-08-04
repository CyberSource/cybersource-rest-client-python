# CyberSource.TransactionRiskLabelingApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_labels**](TransactionRiskLabelingApi.md#submit_labels) | **POST** /unifiedrisk | Transaction Risk Labeling


# **submit_labels**
> InlineResponse2013 submit_labels(label_request)

Transaction Risk Labeling

The Labels endpoint enables clients to submit post-transaction feedback, including both the decision made on the transaction  (such as accept or reject) and the final outcome (such as confirmed fraud, valid, or suspected).  Consistent label submission is critical to achieving optimal model performance, as it directly drives model accuracy, tuning,  and the quality of client‑specific insights over time

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TransactionRiskLabelingApi()
label_request = CyberSource.LabelRequest() # LabelRequest | Label submission request

try: 
    # Transaction Risk Labeling
    api_response = api_instance.submit_labels(label_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionRiskLabelingApi->submit_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_request** | [**LabelRequest**](LabelRequest.md)| Label submission request | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

