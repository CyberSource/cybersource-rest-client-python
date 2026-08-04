# UcpUpdateCheckoutSessionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The session ID being updated. | [optional] 
**line_items** | [**list[Iccv1checkoutsessionsLineItems]**](Iccv1checkoutsessionsLineItems.md) | Replacement line item list. When provided, replaces the entire cart. | [optional] 
**buyer** | [**UcpUpdateCheckoutSessionBuyer**](UcpUpdateCheckoutSessionBuyer.md) |  | [optional] 
**currency** | **str** | ISO 4217 currency code for the session (e.g. &#x60;USD&#x60;, &#x60;EUR&#x60;). | [optional] 
**payment** | [**Iccv1checkoutsessionssessionIdPayment**](Iccv1checkoutsessionssessionIdPayment.md) |  | [optional] 
**fulfillment** | [**Iccv1checkoutsessionssessionIdFulfillment**](Iccv1checkoutsessionssessionIdFulfillment.md) |  | [optional] 
**discounts** | [**Iccv1checkoutsessionssessionIdDiscounts**](Iccv1checkoutsessionssessionIdDiscounts.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


