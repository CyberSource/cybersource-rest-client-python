# Ucv1sessionsDataAggregatorInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator_id** | **str** | Value that identifies you as a payment aggregator. Get this value from the processor.  | [optional] 
**name** | **str** | Your payment aggregator business name.  **American Express Direct**\\ The maximum length of the aggregator name depends on the length of the sub-merchant name. The combined length for both values must not exceed 36 characters.\\  | [optional] 
**sub_merchant** | [**Ucv1sessionsDataAggregatorInformationSubMerchant**](Ucv1sessionsDataAggregatorInformationSubMerchant.md) |  | [optional] 
**street_address** | **str** | Acquirer street name. | [optional] 
**city** | **str** | Acquirer city. | [optional] 
**state** | **str** | Acquirer state. | [optional] 
**postal_code** | **str** | Acquirer postal code. | [optional] 
**country** | **str** | Acquirer country used for Payment Facilitator scenarios. | [optional] 
**service_providername** | **str** | Contains transfer service provider name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


