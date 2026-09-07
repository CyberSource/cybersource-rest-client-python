# UnifiedriskOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items_count** | **int** | Total number of items in order | [optional] 
**returns_accepted** | **bool** | Indicates if returns are accepted | [optional] 
**line_items** | [**list[UnifiedriskOrderLineItems]**](UnifiedriskOrderLineItems.md) |  | [optional] 
**shipping** | [**UnifiedriskOrderShipping**](UnifiedriskOrderShipping.md) |  | [optional] 
**billing** | [**UnifiedriskOrderBilling**](UnifiedriskOrderBilling.md) |  | [optional] 
**order_id** | **str** | Merchant-assigned unique identifier for this order, used for transaction correlation, dispute matching, and fraud monitoring | [optional] 
**order_description** | **str** | Free-text description of the order contents or purpose, provided by the merchant for risk analysis and dispute management | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


