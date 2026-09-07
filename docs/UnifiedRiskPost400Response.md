# UnifiedRiskPost400Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Echoes the unique request identifier from the original request. May be absent if the request could not be parsed (e.g., malformed JSON). | 
**submit_time_utc** | **datetime** | UTC timestamp indicating when the failed request was received by the server. | 
**errors** | [**list[UnifiedRiskPost400ResponseErrors]**](UnifiedRiskPost400ResponseErrors.md) | Root-level list of action-level errors describing what failed and why. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


