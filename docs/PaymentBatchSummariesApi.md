# CyberSource.PaymentBatchSummariesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_batch_summary**](PaymentBatchSummariesApi.md#get_payment_batch_summary) | **GET** /reporting/v3/payment-batch-summaries | Get Payment Batch Summary Data


# **get_payment_batch_summary**
> ReportingV3PaymentBatchSummariesGet200Response get_payment_batch_summary(start_time, end_time, organization_id=organization_id, roll_up=roll_up, breakdown=breakdown, start_day_of_week=start_day_of_week)

Get Payment Batch Summary Data

Scope can be either account/merchant or reseller.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PaymentBatchSummariesApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
end_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)
roll_up = 'roll_up_example' # str | Conditional - RollUp for data for day/week/month. Required while getting breakdown data for a Merchant (optional)
breakdown = 'breakdown_example' # str | Conditional - Breakdown on account_rollup/all_merchant/selected_merchant. Required while getting breakdown data for a Merchant. (optional)
start_day_of_week = 56 # int | Optional - Start day of week to breakdown data for weeks in a month (optional)

try: 
    # Get Payment Batch Summary Data
    api_response = api_instance.get_payment_batch_summary(start_time, end_time, organization_id=organization_id, roll_up=roll_up, breakdown=breakdown, start_day_of_week=start_day_of_week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentBatchSummariesApi->get_payment_batch_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **end_time** | **datetime**| Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 
 **roll_up** | **str**| Conditional - RollUp for data for day/week/month. Required while getting breakdown data for a Merchant | [optional] 
 **breakdown** | **str**| Conditional - Breakdown on account_rollup/all_merchant/selected_merchant. Required while getting breakdown data for a Merchant. | [optional] 
 **start_day_of_week** | **int**| Optional - Start day of week to breakdown data for weeks in a month | [optional] 

### Return type

[**ReportingV3PaymentBatchSummariesGet200Response**](ReportingV3PaymentBatchSummariesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json, text/csv, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

