# AcpUpdateCheckoutSessionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**list[Iccv1checkoutSessionsItems]**](Iccv1checkoutSessionsItems.md) | Replacement cart item list. When provided, the entire cart is replaced with this array. To add a single item, include all existing items plus the new one.  | [optional] 
**buyer** | [**AcpUpdateCheckoutSessionBuyer**](AcpUpdateCheckoutSessionBuyer.md) |  | [optional] 
**fulfillment_address** | [**Iccv1checkoutSessionssessionIdFulfillmentAddress**](Iccv1checkoutSessionssessionIdFulfillmentAddress.md) |  | [optional] 
**fulfillment_option_id** | **str** | Optional. ID of the selected fulfillment option from &#x60;fulfillment_options&#x60; in the session response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


