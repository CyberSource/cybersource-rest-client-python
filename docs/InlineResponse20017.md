# InlineResponse20017

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The checkout session identifier. | [optional] 
**status** | **str** | Will always be &#x60;completed&#x60; on a successful response.  Possible values: - completed | [optional] 
**currency** | **str** | ISO 4217 lowercase currency code. | [optional] 
**buyer** | [**AcpCompleteCheckoutResponseBuyer**](AcpCompleteCheckoutResponseBuyer.md) |  | [optional] 
**line_items** | [**list[InlineResponse20112LineItems]**](InlineResponse20112LineItems.md) | Final line items with confirmed pricing. | [optional] 
**fulfillment_address** | [**InlineResponse20017FulfillmentAddress**](InlineResponse20017FulfillmentAddress.md) |  | [optional] 
**fulfillment_options** | [**list[InlineResponse20112FulfillmentOptions]**](InlineResponse20112FulfillmentOptions.md) |  | [optional] 
**fulfillment_option_id** | **str** | ID of the selected fulfillment option. | [optional] 
**totals** | [**list[InlineResponse20112Totals]**](InlineResponse20112Totals.md) | Final order totals as typed total lines. All amounts in minor units (cents). | [optional] 
**order** | [**InlineResponse20017Order**](InlineResponse20017Order.md) |  | [optional] 
**messages** | [**list[InlineResponse20112Messages]**](InlineResponse20112Messages.md) | Informational or error messages from the merchant backend. | [optional] 
**links** | [**list[InlineResponse20112Links]**](InlineResponse20112Links.md) | Related resource links from the merchant (e.g. terms of use, privacy policy). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


