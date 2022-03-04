# Ptsv2paymentsOrderInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_details** | [**Ptsv2paymentsOrderInformationAmountDetails**](Ptsv2paymentsOrderInformationAmountDetails.md) |  | [optional] 
**bill_to** | [**Ptsv2paymentsOrderInformationBillTo**](Ptsv2paymentsOrderInformationBillTo.md) |  | [optional] 
**ship_to** | [**Ptsv2paymentsOrderInformationShipTo**](Ptsv2paymentsOrderInformationShipTo.md) |  | [optional] 
**line_items** | [**list[Ptsv2paymentsOrderInformationLineItems]**](Ptsv2paymentsOrderInformationLineItems.md) |  | [optional] 
**invoice_details** | [**Ptsv2paymentsOrderInformationInvoiceDetails**](Ptsv2paymentsOrderInformationInvoiceDetails.md) |  | [optional] 
**shipping_details** | [**Ptsv2paymentsOrderInformationShippingDetails**](Ptsv2paymentsOrderInformationShippingDetails.md) |  | [optional] 
**returns_accepted** | **bool** | This is only needed when you are requesting both payment and DM service at same time.  Boolean that indicates whether returns are accepted for this order. This field can contain one of the following values: - true: Returns are accepted for this order. - false: Returns are not accepted for this order.  | [optional] 
**pre_order** | **str** | Indicates whether cardholder is placing an order with a future availability or release date. This field can contain one of these values: - MERCHANDISE_AVAILABLE: Merchandise available - FUTURE_AVAILABILITY: Future availability  | [optional] 
**pre_order_date** | **str** | Expected date that a pre-ordered purchase will be available. Format: YYYYMMDD  | [optional] 
**reordered** | **bool** | Indicates whether the cardholder is reordering previously purchased merchandise. This field can contain one of these values: - false: First time ordered - true: Reordered  | [optional] 
**total_offers_count** | **str** | Total number of articles/items in the order as a numeric decimal count. Possible values: 00 - 99  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


