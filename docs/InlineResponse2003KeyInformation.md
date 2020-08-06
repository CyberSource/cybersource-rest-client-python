# InlineResponse2003KeyInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Merchant Id  | [optional] 
**reference_number** | **str** | Reference number is a unique identifier provided by the client along with the organization Id. This is an optional field provided solely for the client’s convenience. If client specifies value for this field in the request, it is expected to be available in the response.  | [optional] 
**key_id** | **str** | Key Serial Number  | [optional] 
**status** | **str** | The status of the key.  Possible values:  - FAILED  - ACTIVE  - INACTIVE  - EXPIRED  | [optional] 
**message** | **str** | message in case of failed key | [optional] 
**error_information** | [**InlineResponse201ErrorInformation**](InlineResponse201ErrorInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


