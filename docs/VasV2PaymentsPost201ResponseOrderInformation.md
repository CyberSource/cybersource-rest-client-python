# VasV2PaymentsPost201ResponseOrderInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_amount** | **str** | Total amount of tax exempt amounts. This value is the sum of the values for all the &#x60;orderInformation.lineItems[].exemptAmount&#x60; fields in the tax calculation request.  | [optional] 
**taxable_amount** | **str** | Total amount of all taxable amounts. This value is the sum of the values for all the &#x60;orderInformation.lineItems[].taxAmount&#x60; fields in the tax calculation request.  | [optional] 
**tax_amount** | **str** | Total amount of tax for all lineItems in the tax calculation request.  | [optional] 
**line_items** | [**list[VasV2PaymentsPost201ResponseOrderInformationLineItems]**](VasV2PaymentsPost201ResponseOrderInformationLineItems.md) |  | [optional] 
**tax_details** | [**list[VasV2PaymentsPost201ResponseOrderInformationTaxDetails]**](VasV2PaymentsPost201ResponseOrderInformationTaxDetails.md) |  | [optional] 
**amount_details** | [**Ptsv2paymentsidreversalsReversalInformationAmountDetails**](Ptsv2paymentsidreversalsReversalInformationAmountDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


