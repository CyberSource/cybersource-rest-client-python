# PullFunds201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;  **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  | [optional] 
**order_information** | [**PullFunds201ResponseOrderInformation**](PullFunds201ResponseOrderInformation.md) |  | [optional] 
**status** | **str** | The status of the submitted transaction.  Possible values: - AUTHORIZED - DECLINED - SERVER_ERROR - INVALID_REQUEST - PARTIAL_AUTHORIZED  | [optional] 
**error_information** | [**PullFunds201ResponseErrorInformation**](PullFunds201ResponseErrorInformation.md) |  | [optional] 
**processor_information** | [**PullFunds201ResponseProcessorInformation**](PullFunds201ResponseProcessorInformation.md) |  | [optional] 
**links** | [**PullFunds201ResponseLinks**](PullFunds201ResponseLinks.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


