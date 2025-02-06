# Ptsv2payoutsAggregatorInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator_id** | **str** | Value that identifies you as a payment aggregator. Get this value from the processor.  | [optional] 
**name** | **str** | Your payment aggregator business name. This field is conditionally required when aggregator id is present.  | [optional] 
**independent_sales_organization_id** | **str** | Independent sales organization ID. This field is only used for Mastercard transactions submitted through PPGS.  | [optional] 
**sub_merchant** | [**Ptsv2payoutsAggregatorInformationSubMerchant**](Ptsv2payoutsAggregatorInformationSubMerchant.md) |  | [optional] 
**street_address** | **str** | Acquirer street name. | [optional] 
**city** | **str** | Acquirer city. | [optional] 
**state** | **str** | Acquirer state. | [optional] 
**postal_code** | **str** | Acquirer postal code. | [optional] 
**country** | **str** | Acquirer country. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


