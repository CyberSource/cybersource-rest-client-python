# CyberSource.BillingAgreementsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_agreements_de_registration**](BillingAgreementsApi.md#billing_agreements_de_registration) | **PATCH** /pts/v2/billing-agreements/{id} | Standing Instruction Cancellation or Modification
[**billing_agreements_intimation**](BillingAgreementsApi.md#billing_agreements_intimation) | **POST** /pts/v2/billing-agreements/{id}/intimations | Standing Instruction intimation
[**billing_agreements_registration**](BillingAgreementsApi.md#billing_agreements_registration) | **POST** /pts/v2/billing-agreements | Standing Instruction completion registration


# **billing_agreements_de_registration**
> PtsV2CreditsPost201Response1 billing_agreements_de_registration(modify_billing_agreement, id)

Standing Instruction Cancellation or Modification

Standing Instruction with or without Token

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BillingAgreementsApi()
modify_billing_agreement = CyberSource.ModifyBillingAgreement() # ModifyBillingAgreement | 
id = 'id_example' # str | ID for de-registration or cancellation of Billing Agreement

try: 
    # Standing Instruction Cancellation or Modification
    api_response = api_instance.billing_agreements_de_registration(modify_billing_agreement, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingAgreementsApi->billing_agreements_de_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_billing_agreement** | [**ModifyBillingAgreement**](ModifyBillingAgreement.md)|  | 
 **id** | **str**| ID for de-registration or cancellation of Billing Agreement | 

### Return type

[**PtsV2CreditsPost201Response1**](PtsV2CreditsPost201Response1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_agreements_intimation**
> PtsV2CreditsPost201Response1 billing_agreements_intimation(intimate_billing_agreement, id)

Standing Instruction intimation

Standing Instruction with or without Token.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BillingAgreementsApi()
intimate_billing_agreement = CyberSource.IntimateBillingAgreement() # IntimateBillingAgreement | 
id = 'id_example' # str | ID for intimation of Billing Agreement

try: 
    # Standing Instruction intimation
    api_response = api_instance.billing_agreements_intimation(intimate_billing_agreement, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingAgreementsApi->billing_agreements_intimation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intimate_billing_agreement** | [**IntimateBillingAgreement**](IntimateBillingAgreement.md)|  | 
 **id** | **str**| ID for intimation of Billing Agreement | 

### Return type

[**PtsV2CreditsPost201Response1**](PtsV2CreditsPost201Response1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_agreements_registration**
> PtsV2CreditsPost201Response1 billing_agreements_registration(create_billing_agreement)

Standing Instruction completion registration

Standing Instruction with or without Token. Transaction amount in case First payment is coming along with registration. Only 2 decimal places allowed

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.BillingAgreementsApi()
create_billing_agreement = CyberSource.CreateBillingAgreement() # CreateBillingAgreement | 

try: 
    # Standing Instruction completion registration
    api_response = api_instance.billing_agreements_registration(create_billing_agreement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingAgreementsApi->billing_agreements_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_billing_agreement** | [**CreateBillingAgreement**](CreateBillingAgreement.md)|  | 

### Return type

[**PtsV2CreditsPost201Response1**](PtsV2CreditsPost201Response1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

