# Riskv1decisionsOrderInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_details** | [**Riskv1decisionsOrderInformationAmountDetails**](Riskv1decisionsOrderInformationAmountDetails.md) |  | [optional] 
**pre_order** | **str** | Indicates whether cardholder is placing an order with a future availability or release date. This field can contain one of these values: - MERCHANDISE_AVAILABLE: Merchandise available - FUTURE_AVAILABILITY: Future availability  | [optional] 
**pre_order_date** | **str** | Expected date that a pre-ordered purchase will be available. Format: YYYYMMDD  | [optional] 
**cutoff_date_time** | **str** | Starting date and time for an event or a journey that is independent of which transportation mechanism, in UTC. The cutoffDateTime will supersede travelInformation.departureTime if both are supplied in the request. Format: YYYY-MM-DDThh:mm:ssZ. Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**reordered** | **bool** | Indicates whether the cardholder is reordering previously purchased merchandise. This field can contain one of these values: - false: First time ordered - true: Reordered  | [optional] 
**shipping_details** | [**Riskv1decisionsOrderInformationShippingDetails**](Riskv1decisionsOrderInformationShippingDetails.md) |  | [optional] 
**ship_to** | [**Riskv1decisionsOrderInformationShipTo**](Riskv1decisionsOrderInformationShipTo.md) |  | [optional] 
**returns_accepted** | **bool** | Boolean that indicates whether returns are accepted for this order. This field can contain one of the following values: - true: Returns are accepted for this order. - false: Returns are not accepted for this order.  | [optional] 
**line_items** | [**list[Riskv1decisionsOrderInformationLineItems]**](Riskv1decisionsOrderInformationLineItems.md) | This array contains detailed information about individual products in the order. | [optional] 
**bill_to** | [**Riskv1decisionsOrderInformationBillTo**](Riskv1decisionsOrderInformationBillTo.md) |  | [optional] 
**total_offers_count** | **str** | Total number of articles/items in the order as a numeric decimal count. Possible values: 00 - 99  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


