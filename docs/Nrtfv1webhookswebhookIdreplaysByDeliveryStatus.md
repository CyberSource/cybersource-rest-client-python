# Nrtfv1webhookswebhookIdreplaysByDeliveryStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the webhook. Options are FAILED or RETRY | [optional] 
**start_time** | **datetime** | The start time in yyyy-mm-dd hh:mm:ss.ms format. Maximum value is 1 month prior to todays system time.  The difference between Start Time and End Time cannot exceed a 24 hour window within the last month.  | [optional] 
**end_time** | **datetime** | The end time in yyyy-mm-dd hh:mm:ss.ms format.  The difference between Start Time and End Time cannot exceed a 24 hour window within the last month.  | [optional] 
**hours_back** | **int** | Alternative parameter to startTime/endTime.  It evaluates the startTime using the current system time (endTime) and the hoursBack value (default &#x3D; 24hrs).  | [optional] 
**product_id** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


