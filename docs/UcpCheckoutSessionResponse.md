# UcpCheckoutSessionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ucp** | [**UcpCheckoutSessionResponseUcp**](UcpCheckoutSessionResponseUcp.md) |  | [optional] 
**id** | **str** | Unique UCP session identifier. Required for all subsequent UCP calls (update, complete, cancel).  | [optional] 
**status** | **str** | Current lifecycle state of the session. - &#x60;active&#x60; — open and modifiable - &#x60;completed&#x60; — order placed, immutable - &#x60;cancelled&#x60; — abandoned, no charge made   Possible values: - active - completed - cancelled | [optional] 
**currency** | **str** | ISO 4217 currency code for this session (e.g. &#x60;USD&#x60;, &#x60;EUR&#x60;). | [optional] 
**buyer** | [**UcpCheckoutSessionResponseBuyer**](UcpCheckoutSessionResponseBuyer.md) |  | [optional] 
**line_items** | [**list[UcpCheckoutSessionResponseLineItems]**](UcpCheckoutSessionResponseLineItems.md) | Cart line items with merchant-confirmed pricing. | [optional] 
**totals** | [**list[Iccv1checkoutsessionsFulfillmentTotals]**](Iccv1checkoutsessionsFulfillmentTotals.md) | Order cost breakdown. Each entry represents one total type (subtotal, tax, shipping, discount, or grand total). Amounts are in **cents** (not micros).  | [optional] 
**fulfillment** | [**Iccv1checkoutsessionsResponseFulfillment**](Iccv1checkoutsessionsResponseFulfillment.md) |  | [optional] 
**payment** | [**Iccv1checkoutsessionsResponsePayment**](Iccv1checkoutsessionsResponsePayment.md) |  | [optional] 
**discounts** | [**Iccv1checkoutsessionsResponseDiscounts**](Iccv1checkoutsessionsResponseDiscounts.md) |  | [optional] 
**order** | [**UcpCheckoutSessionResponseOrder**](UcpCheckoutSessionResponseOrder.md) |  | [optional] 
**links** | [**list[CheckoutSessionResponseLinks]**](CheckoutSessionResponseLinks.md) | Related resource links (e.g. terms of use, privacy policy). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


