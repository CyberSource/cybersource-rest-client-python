# UcpCreateCheckoutSessionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_items** | [**list[Iccv1checkoutsessionsLineItems]**](Iccv1checkoutsessionsLineItems.md) | The products the buyer wants to purchase. At least one line item is required. | 
**buyer** | [**UcpCreateCheckoutSessionBuyer**](UcpCreateCheckoutSessionBuyer.md) |  | [optional] 
**currency** | **str** | Optional. ISO 4217 currency code for the session (e.g. &#x60;USD&#x60;, &#x60;EUR&#x60;). | [optional] 
**payment** | [**Iccv1checkoutsessionsPayment**](Iccv1checkoutsessionsPayment.md) |  | [optional] 
**fulfillment** | [**Iccv1checkoutsessionsFulfillment**](Iccv1checkoutsessionsFulfillment.md) |  | [optional] 
**discounts** | [**Iccv1checkoutsessionsDiscounts**](Iccv1checkoutsessionsDiscounts.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


