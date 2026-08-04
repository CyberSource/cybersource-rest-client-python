# InlineResponse2013ResultsRISKINSIGHTS

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Echoes the unique identifier from the original label request. | [optional] 
**response_timestamp** | **datetime** | ISO 8601 timestamp when the VPRI service processed the label submission. | [optional] 
**status** | **str** | Processing status of the label submission.  Possible values: - COMPLETED - INVALID_REQUEST - SERVER_ERROR | [optional] 
**reason** | **str** | Machine-readable reason code when status is not COMPLETED. | [optional] 
**message** | **str** | Human-readable message when status is not COMPLETED. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


