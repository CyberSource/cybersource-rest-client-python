# InlineResponse2013

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  | [optional] 
**status** | **str** | The status of the submitted transaction.  Possible values: - &#x60;COMPLETED&#x60; - &#x60;INVALID_REQUEST&#x60; - &#x60;SERVER_ERROR&#x60;  | [optional] 
**submit_time_stamp_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DD&#39;T&#39;HH:mm:ssZ&#x60;  Example: &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**order_information** | [**InlineResponse2013OrderInformation**](InlineResponse2013OrderInformation.md) |  | [optional] 
**error_information** | [**InlineResponse2013ErrorInformation**](InlineResponse2013ErrorInformation.md) |  | [optional] 
**processor_information** | [**InlineResponse2013ProcessorInformation**](InlineResponse2013ProcessorInformation.md) |  | [optional] 
**processing_information** | [**InlineResponse2013ProcessingInformation**](InlineResponse2013ProcessingInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


