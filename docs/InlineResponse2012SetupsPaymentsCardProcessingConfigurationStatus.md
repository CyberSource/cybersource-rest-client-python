# InlineResponse2012SetupsPaymentsCardProcessingConfigurationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** | This is NOT for MVP | [optional] 
**version** | **str** |  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. &#x60;Format: YYYY-MM-DDThh:mm:ssZ&#x60;  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**status** | **str** | Possible values: - SUCCESS - PARTIAL - PENDING - NOT_SETUP | [optional] 
**reason** | **str** | Possible values: - PENDING_PROVISIONING_PROCESS - MISSING_DATA - INVALID_DATA - DUPLICATE_FIELD - NOT_APPLICABLE | [optional] 
**details** | **list[dict(str, str)]** |  | [optional] 
**message** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


