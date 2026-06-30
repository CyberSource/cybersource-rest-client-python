# Iccv1instructionsinstructionIdconfirmationsOrderInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Unique identifier for the order | [optional] 
**order_status** | **str** | Status of the order | [optional] 
**order_date** | **str** | Order date (UTC time in Epoch format) | [optional] 
**expected_delivery_date** | **str** | Expected delivery date for the order (UTC time in Epoch format) | [optional] 
**amount_detail** | [**IccAmountDetail**](IccAmountDetail.md) |  | [optional] 
**ship_to** | [**Iccv1instructionsinstructionIdcredentialsOrderInformationShipTo**](Iccv1instructionsinstructionIdcredentialsOrderInformationShipTo.md) |  | [optional] 
**shipping_details** | [**IccShippingDetails**](IccShippingDetails.md) |  | [optional] 
**tracking_id** | **str** | Tracking ID for the shipment | [optional] 
**carrier** | **str** | Shipping carrier or provider | [optional] 
**line_items** | [**list[Iccv1instructionsinstructionIdcredentialsOrderInformationLineItems]**](Iccv1instructionsinstructionIdcredentialsOrderInformationLineItems.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


