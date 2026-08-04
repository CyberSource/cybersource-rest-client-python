# InlineResponse20020

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | Total number of products across all pages. | [optional] 
**merchant_id** | **str** | Merchant whose catalog is returned, or \&quot;all\&quot; if no filter applied. | [optional] 
**products** | [**list[InlineResponse20020Products]**](InlineResponse20020Products.md) | List of product records for the current page. | [optional] 
**page** | **int** | Current page number (0-based). | [optional] 
**size** | **int** | Page size used in this response. | [optional] 
**total_pages** | **int** | Total number of pages available. | [optional] 
**has_next** | **bool** | Whether more pages exist after the current page. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


