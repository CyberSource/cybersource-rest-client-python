# InlineResponse20113FulfillmentOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique fulfillment option ID. Pass as &#x60;fulfillment_option_id&#x60; to select it. | [optional] 
**type** | **str** | Fulfillment method type.  Possible values: - shipping - digital | [optional] 
**title** | **str** | Display name for this fulfillment option. | [optional] 
**subtitle** | **str** | Additional description (e.g. estimated delivery window). | [optional] 
**carrier** | **str** | Carrier name for shipping options. | [optional] 
**earliest_delivery_time** | **datetime** | Earliest estimated delivery in RFC 3339 format. | [optional] 
**latest_delivery_time** | **datetime** | Latest estimated delivery in RFC 3339 format. | [optional] 
**subtotal** | **int** | Shipping cost before tax, in minor units. | [optional] 
**tax** | **int** | Tax on shipping cost, in minor units. | [optional] 
**total** | **int** | Total shipping cost including tax, in minor units. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


