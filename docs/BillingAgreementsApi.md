# CyberSource.BillingAgreementsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_agreements_de_registration**](BillingAgreementsApi.md#billing_agreements_de_registration) | **PATCH** /pts/v2/billing-agreements/{id} | Modify a Billing Agreement
[**billing_agreements_intimation**](BillingAgreementsApi.md#billing_agreements_intimation) | **POST** /pts/v2/billing-agreements/{id}/intimations | Standing Instruction intimation
[**billing_agreements_registration**](BillingAgreementsApi.md#billing_agreements_registration) | **POST** /pts/v2/billing-agreements | Create a Billing Agreement


# **billing_agreements_de_registration**
> PtsV2ModifyBillingAgreementPost201Response billing_agreements_de_registration(modify_billing_agreement, id)

Modify a Billing Agreement

#### Standing Instruction: Standing Instruction with or without Token.  #### Revoke Mandate: When you revoke a mandate, any pending direct debits linked to that mandate are canceled. No notifications are sent. When you revoke a mandate with no pending direct debits, the Bacs scheme or customer's bank notify you of any subsequent direct debit events. When you revoke a mandate, you cannot send a direct debit request using the mandate ID. Customer payments cannot be made against a revoked mandate. You can revoke a mandate when the customer:   - Requests that you revoke the mandate.   - Closes their account with you. Possible revoke mandate status values -   - Revoked—the revoke mandate request was successfully processed.   - Failed—the revoke mandate request was not accepted.  #### Update Mandate: In most cases, the account details of an existing mandate cannot be updated in the Bacs schema, except by creating a new mandate. However, some very limited customer information, like name and address, can be updated to the mandate without needing to revoke it first  #### Mandate Status: After the customer signs the mandate, request that the mandate status service verify the mandate status. Possible mandate status values:   - Active—the mandate is successfully created. A direct debit can be sent for this mandate ID.   - Pending—a pending mandate means the mandate is not yet signed.   - Failed—the customer did not authenticate.   - Expired—the deadline to create the mandate passed.   - Revoked—the mandate is cancelled.  #### Paypal Billing Agreement:  A billing agreement is set up between PayPal and your customer. When you collect the details of a customer's billing agreement, you are able to bill that customer without requiring an authorization for each payment.  You can bill the customer at the same time you process their PayPal Express checkout order, which simplifies your business processes. 

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
    # Modify a Billing Agreement
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

[**PtsV2ModifyBillingAgreementPost201Response**](PtsV2ModifyBillingAgreementPost201Response.md)

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
> PtsV2CreateBillingAgreementPost201Response billing_agreements_registration(create_billing_agreement)

Create a Billing Agreement

#### Standing Instruction: Standing Instruction with or without Token. Transaction amount in case First payment is coming along with registration. Only 2 decimal places allowed  #### Create Mandate: You can create a mandate through the direct debit mandate flow. Possible create mandate status values:   - Pending—the create mandate request was successfully processed.   - Failed—the create mandate request was not accepted.  #### Import Mandate: In the Bacs scheme, a mandate is created with a status of active. Direct debit collections can be made against it immediately. You can import a mandate to the CyberSource database when:   - You have existing customers with signed, active mandates   - You manage mandates outside of CyberSource.  When you import an existing mandate to the CyberSource database, provide a unique value for the mandate ID or the request results in an error. If an import mandate request is not accepted, the import mandate status value is failed. 

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
    # Create a Billing Agreement
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

[**PtsV2CreateBillingAgreementPost201Response**](PtsV2CreateBillingAgreementPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

