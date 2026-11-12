# CompleteCheckoutResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The checkout session identifier. | 
**status** | **str** | Will always be &#x60;completed&#x60; on a successful response.  Possible values: - completed | 
**currency** | **str** | ISO 4217 lowercase currency code. | 
**buyer** | [**AcpCompleteCheckoutResponseBuyer**](AcpCompleteCheckoutResponseBuyer.md) |  | 
**line_items** | [**list[CheckoutSessionResponseLineItems]**](CheckoutSessionResponseLineItems.md) | Final line items with confirmed pricing. | 
**fulfillment_address** | [**CompleteCheckoutResponseFulfillmentAddress**](CompleteCheckoutResponseFulfillmentAddress.md) |  | [optional] 
**fulfillment_options** | [**list[CheckoutSessionResponseFulfillmentOptions]**](CheckoutSessionResponseFulfillmentOptions.md) |  | 
**fulfillment_option_id** | **str** | ID of the selected fulfillment option. | 
**totals** | [**list[CheckoutSessionResponseTotals]**](CheckoutSessionResponseTotals.md) | Final order totals as typed total lines. All amounts in minor units (cents). | 
**order** | [**CompleteCheckoutResponseOrder**](CompleteCheckoutResponseOrder.md) |  | 
**messages** | [**list[CheckoutSessionResponseMessages]**](CheckoutSessionResponseMessages.md) | Informational or error messages from the merchant backend. | 
**links** | [**list[CheckoutSessionResponseLinks]**](CheckoutSessionResponseLinks.md) | Related resource links from the merchant (e.g. terms of use, privacy policy). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


