# Rbsv1plansidPlanInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Plan code is an optional field, If not provided system generates and assign one  | [optional] 
**name** | **str** | Plan name  | [optional] 
**description** | **str** | Plan description  | [optional] 
**status** | **str** | Updating to &#x60;DRAFT&#x60; is not allowed from &#x60;ACTIVE&#x60; and &#x60;INACTIVE&#x60; status.  Plan Status:  - &#x60;DRAFT&#x60;  - &#x60;ACTIVE&#x60;  - &#x60;INACTIVE&#x60;  | [optional] 
**billing_period** | [**GetAllPlansResponsePlanInformationBillingPeriod**](GetAllPlansResponsePlanInformationBillingPeriod.md) |  | [optional] 
**billing_cycles** | [**Rbsv1plansPlanInformationBillingCycles**](Rbsv1plansPlanInformationBillingCycles.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


