# Acpv1instructionsMandates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mandate_id** | **str** | Unique identifier with in the context of a purchase-intent for the mandate.   Assigned by Partner. Id shall not be reused when a mandate is updated/deleted.  | 
**preferred_merchant_name** | **str** | User merchant preference. | [optional] 
**merchant_category** | **str** | Merchant category Description. | [optional] 
**merchant_category_code** | **str** | Merchant category Code. Once it is checked, it has to be valid merchant category code. Ex:\&quot; 5311\&quot; | [optional] 
**decline_threshold** | [**Acpv1instructionsDeclineThreshold**](Acpv1instructionsDeclineThreshold.md) |  | 
**recurring_payment_information** | [**Acpv1instructionsRecurringPaymentInformation**](Acpv1instructionsRecurringPaymentInformation.md) |  | [optional] 
**effective_until_time** | **str** | UTC time in Unix epoch format. | 
**quantity** | **str** | Quantity of the product. | [optional] 
**description** | **str** | Description of the product. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


