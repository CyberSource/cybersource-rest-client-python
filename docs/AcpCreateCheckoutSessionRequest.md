# AcpCreateCheckoutSessionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**list[Iccv1checkoutSessionsItems]**](Iccv1checkoutSessionsItems.md) | The items the buyer wants to purchase. At least one item is required. Each &#x60;id&#x60; must match a product already present in the merchant&#39;s ACG catalog.  | 
**buyer** | [**AcpCreateCheckoutSessionBuyer**](AcpCreateCheckoutSessionBuyer.md) |  | [optional] 
**fulfillment_address** | [**Iccv1checkoutSessionsFulfillmentAddress**](Iccv1checkoutSessionsFulfillmentAddress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


