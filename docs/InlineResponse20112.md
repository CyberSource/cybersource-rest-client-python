# InlineResponse20112

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this checkout session. Required for all subsequent calls (update, complete, cancel).  | [optional] 
**status** | **str** | Current lifecycle state of the session per ACP spec: - &#x60;not_ready_for_payment&#x60; — session is open but not yet ready - &#x60;ready_for_payment&#x60; — session is ready to be completed - &#x60;completed&#x60; — order has been placed; session is immutable - &#x60;canceled&#x60; — session was abandoned; no charge was made   Possible values: - not_ready_for_payment - ready_for_payment - completed - canceled | [optional] 
**currency** | **str** | ISO 4217 lowercase currency code for this session. | [optional] 
**line_items** | [**list[InlineResponse20112LineItems]**](InlineResponse20112LineItems.md) | Line items with merchant-confirmed pricing. | [optional] 
**fulfillment_address** | [**InlineResponse20112FulfillmentAddress**](InlineResponse20112FulfillmentAddress.md) |  | [optional] 
**fulfillment_options** | [**list[InlineResponse20112FulfillmentOptions]**](InlineResponse20112FulfillmentOptions.md) | Available fulfillment methods with pricing. | [optional] 
**fulfillment_option_id** | **str** | ID of the currently selected fulfillment option. | [optional] 
**totals** | [**list[InlineResponse20112Totals]**](InlineResponse20112Totals.md) | Order cost breakdown as an array of typed total lines. All amounts in minor units (cents). | [optional] 
**buyer** | [**AcpCheckoutSessionResponseBuyer**](AcpCheckoutSessionResponseBuyer.md) |  | [optional] 
**payment_provider** | [**InlineResponse20112PaymentProvider**](InlineResponse20112PaymentProvider.md) |  | [optional] 
**messages** | [**list[InlineResponse20112Messages]**](InlineResponse20112Messages.md) | Informational or error messages from the merchant backend. | [optional] 
**links** | [**list[InlineResponse20112Links]**](InlineResponse20112Links.md) | Related resource links from the merchant (e.g. terms of use, privacy policy, seller shop policies).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


