# CancelCheckoutResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The checkout session identifier. | 
**status** | **str** | Will always be &#x60;canceled&#x60; on a successful response.  Possible values: - canceled | 
**currency** | **str** | ISO 4217 lowercase currency code. | 
**buyer** | [**AcpCheckoutSessionResponseBuyer**](AcpCheckoutSessionResponseBuyer.md) |  | [optional] 
**line_items** | [**list[CheckoutSessionResponseLineItems]**](CheckoutSessionResponseLineItems.md) | Line items with merchant-confirmed pricing. | 
**fulfillment_address** | [**CheckoutSessionResponseFulfillmentAddress**](CheckoutSessionResponseFulfillmentAddress.md) |  | [optional] 
**fulfillment_options** | [**list[CheckoutSessionResponseFulfillmentOptions]**](CheckoutSessionResponseFulfillmentOptions.md) | Available fulfillment methods with pricing. | 
**fulfillment_option_id** | **str** | ID of the currently selected fulfillment option. | [optional] 
**totals** | [**list[CheckoutSessionResponseTotals]**](CheckoutSessionResponseTotals.md) | Order cost breakdown as typed total lines. All amounts in minor units (cents). | 
**messages** | [**list[CheckoutSessionResponseMessages]**](CheckoutSessionResponseMessages.md) | Informational or error messages from the merchant backend. | 
**links** | [**list[CheckoutSessionResponseLinks]**](CheckoutSessionResponseLinks.md) | Related resource links from the merchant (e.g. terms of use, privacy policy). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


