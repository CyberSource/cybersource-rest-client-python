# InlineResponse4006

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submit_time_utc** | **datetime** | Time of request in UTC. &#x60;Format: YYYY-MM-DDThh:mm:ssZ&#x60;  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**status** | **str** | The http status description of the submitted request. | [optional] 
**reason** | **str** | Documented reason codes. Client should be able to use the key for generating their own error message Possible Values:   - &#39;INVALID_DATA&#39;   - &#39;SYSTEM_ERROR&#39;   - &#39;RESOURCE_NOT_FOUND&#39;  | [optional] 
**message** | **str** | Descriptive message for the error. | [optional] 
**details** | [**list[InlineResponse4006Details]**](InlineResponse4006Details.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


