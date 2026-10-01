# InlineResponse20018

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The checkout session identifier. | 
**status** | **str** | Will always be &#x60;canceled&#x60; on a successful response.  Possible values: - canceled | 
**currency** | **str** | ISO 4217 lowercase currency code. | 
**buyer** | [**AcpCheckoutSessionResponseBuyer**](AcpCheckoutSessionResponseBuyer.md) |  | [optional] 
**line_items** | [**list[InlineResponse20112LineItems]**](InlineResponse20112LineItems.md) | Line items with merchant-confirmed pricing. | 
**fulfillment_address** | [**InlineResponse20017FulfillmentAddress**](InlineResponse20017FulfillmentAddress.md) |  | [optional] 
**fulfillment_options** | [**list[InlineResponse20112FulfillmentOptions]**](InlineResponse20112FulfillmentOptions.md) | Available fulfillment methods with pricing. | 
**fulfillment_option_id** | **str** | ID of the currently selected fulfillment option. | [optional] 
**totals** | [**list[InlineResponse20112Totals]**](InlineResponse20112Totals.md) | Order cost breakdown as typed total lines. All amounts in minor units (cents). | 
**messages** | [**list[InlineResponse20112Messages]**](InlineResponse20112Messages.md) | Informational or error messages from the merchant backend. | 
**links** | [**list[InlineResponse20112Links]**](InlineResponse20112Links.md) | Related resource links from the merchant (e.g. terms of use, privacy policy). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


