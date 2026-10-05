# InlineResponse20112FulfillmentOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique fulfillment option ID. Pass as &#x60;fulfillment_option_id&#x60; to select it. | 
**type** | **str** | Fulfillment method type.  Possible values: - shipping - digital | 
**title** | **str** | Display name for this fulfillment option. | 
**subtitle** | **str** | Additional description (e.g. estimated delivery window). | [optional] 
**carrier** | **str** | Carrier name for shipping options. | [optional] 
**earliest_delivery_time** | **datetime** | Earliest estimated delivery in RFC 3339 format. | [optional] 
**latest_delivery_time** | **datetime** | Latest estimated delivery in RFC 3339 format. | [optional] 
**subtotal** | **int** | Shipping cost before tax, in minor units. | 
**tax** | **int** | Tax on shipping cost, in minor units. | 
**total** | **int** | Total shipping cost including tax, in minor units. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


