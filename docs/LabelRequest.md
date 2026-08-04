# LabelRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **list[str]** | Actions to perform. For label submission, specify VISA_PROTECT_RISK_INSIGHTS. | 
**events** | **list[str]** | Must be LABELS for label submission requests. | 
**request_id** | **str** | Unique identifier for the label submission request | [optional] 
**event_time** | **datetime** | The time that the real-world event occurred. | [optional] 
**transaction** | [**UnifiedriskTransaction**](UnifiedriskTransaction.md) |  | 
**labels** | [**UnifiedriskLabels**](UnifiedriskLabels.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


