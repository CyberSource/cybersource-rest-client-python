# Acpv1instructionsinstructionIdconfirmationsOrderInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Unique identifier for the order | [optional] 
**order_status** | **str** | Status of the order | [optional] 
**order_date** | **str** | Order date (UTC time in Epoch format) | [optional] 
**expected_delivery_date** | **str** | Expected delivery date for the order (UTC time in Epoch format) | [optional] 
**amount_detail** | [**Acpv1instructionsinstructionIdcredentialsOrderInformationAmountDetail**](Acpv1instructionsinstructionIdcredentialsOrderInformationAmountDetail.md) |  | [optional] 
**ship_to** | [**Acpv1instructionsinstructionIdcredentialsOrderInformationShipTo**](Acpv1instructionsinstructionIdcredentialsOrderInformationShipTo.md) |  | [optional] 
**shipping_details** | [**Acpv1instructionsinstructionIdconfirmationsOrderInformationShippingDetails**](Acpv1instructionsinstructionIdconfirmationsOrderInformationShippingDetails.md) |  | [optional] 
**tracking_id** | **str** | Tracking ID for the shipment | [optional] 
**carrier** | **str** | Shipping carrier or provider | [optional] 
**line_items** | [**list[Acpv1instructionsinstructionIdcredentialsOrderInformationLineItems]**](Acpv1instructionsinstructionIdcredentialsOrderInformationLineItems.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


