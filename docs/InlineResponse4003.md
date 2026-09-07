# InlineResponse4003

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  | [optional] 
**submit_time_stamp_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DD&#39;T&#39;HH:mm:ssZ&#x60;  Example: &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**status** | **str** | Possible values: - INVALID_REQUEST  | [optional] 
**reason** | **str** | The reason of the status.  Possible values: - INVALID_DATA - MISSING_FIELD  | [optional] 
**message** | **str** | The detail message related to the status and reason listed above.  | [optional] 
**details** | [**list[InlineResponse2013ErrorInformationDetails]**](InlineResponse2013ErrorInformationDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


