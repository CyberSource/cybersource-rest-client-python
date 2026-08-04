# InlineResponse20019GoogleMerchantProducts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Product item ID. | [optional] 
**title** | **str** | Product title. | [optional] 
**ucp_valid** | **bool** | Whether the product passed UCP validation. | [optional] 
**ucp_errors** | **list[str]** | UCP validation errors (empty if ucpValid is true). | [optional] 
**google_upload_status** | **str** | Google upload status for this product.   Possible values: - UPLOADED - SKIPPED - FAILED | [optional] 
**google_resource_name** | **str** | Google Merchant resource name assigned after upload. | [optional] 
**google_error** | **str** | Error message from Google if upload failed. Null on success. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


