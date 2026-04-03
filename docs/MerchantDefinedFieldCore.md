# MerchantDefinedFieldCore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_type** | **str** | Possible values: - text - select | 
**label** | **str** |  | 
**customer_visible** | **bool** |  | [optional] [default to False]
**text_min_length** | **int** | Should be used only if fieldType &#x3D; \&quot;text\&quot; | [optional] 
**text_max_length** | **int** | Should be used only if fieldType &#x3D; \&quot;text\&quot; | [optional] 
**text_default_value** | **str** | Should be used only if fieldType &#x3D; \&quot;text\&quot; | [optional] 
**possible_values** | **str** | Should be mandatory and used only if fieldType &#x3D; \&quot;select\&quot; | [optional] 
**read_only** | **bool** |  | [optional] [default to False]
**merchant_defined_data_index** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


