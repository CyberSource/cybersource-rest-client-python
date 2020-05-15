# CyberSource.PurchaseAndRefundDetailsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_purchase_and_refund_details**](PurchaseAndRefundDetailsApi.md#get_purchase_and_refund_details) | **GET** /reporting/v3/purchase-refund-details | Get Purchase and Refund Details


# **get_purchase_and_refund_details**
> ReportingV3PurchaseRefundDetailsGet200Response get_purchase_and_refund_details(start_time, end_time, organization_id=organization_id, payment_subtype=payment_subtype, view_by=view_by, group_name=group_name, offset=offset, limit=limit)

Get Purchase and Refund Details

Download the Purchase and Refund Details report. This report report includes all purchases and refund transactions, as well as all activities related to transactions resulting in an adjustment to the net proceeds. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.PurchaseAndRefundDetailsApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
end_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z) 
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)
payment_subtype = 'ALL' # str | Payment Subtypes.   - **ALL**:  All Payment Subtypes   - **VI** :  Visa   - **MC** :  Master Card   - **AX** :  American Express   - **DI** :  Discover   - **DP** :  Pinless Debit  (optional) (default to ALL)
view_by = 'requestDate' # str | View results by Request Date or Submission Date.   - **requestDate** : Request Date   - **submissionDate**: Submission Date  (optional) (default to requestDate)
group_name = 'group_name_example' # str | Valid CyberSource Group Name.User can define groups using CBAPI and Group Management Module in EBC2. Groups are collection of organizationIds (optional)
offset = 56 # int | Offset of the Purchase and Refund Results. (optional)
limit = 2000 # int | Results count per page. Range(1-2000) (optional) (default to 2000)

try: 
    # Get Purchase and Refund Details
    api_response = api_instance.get_purchase_and_refund_details(start_time, end_time, organization_id=organization_id, payment_subtype=payment_subtype, view_by=view_by, group_name=group_name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseAndRefundDetailsApi->get_purchase_and_refund_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **end_time** | **datetime**| Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 
 **payment_subtype** | **str**| Payment Subtypes.   - **ALL**:  All Payment Subtypes   - **VI** :  Visa   - **MC** :  Master Card   - **AX** :  American Express   - **DI** :  Discover   - **DP** :  Pinless Debit  | [optional] [default to ALL]
 **view_by** | **str**| View results by Request Date or Submission Date.   - **requestDate** : Request Date   - **submissionDate**: Submission Date  | [optional] [default to requestDate]
 **group_name** | **str**| Valid CyberSource Group Name.User can define groups using CBAPI and Group Management Module in EBC2. Groups are collection of organizationIds | [optional] 
 **offset** | **int**| Offset of the Purchase and Refund Results. | [optional] 
 **limit** | **int**| Results count per page. Range(1-2000) | [optional] [default to 2000]

### Return type

[**ReportingV3PurchaseRefundDetailsGet200Response**](ReportingV3PurchaseRefundDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json, application/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

