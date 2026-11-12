# FeedJobStatusResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique identifier of the feed submission job. | [optional] 
**status** | **str** | Overall status of the feed job.  Possible values: - PENDING - PROCESSING - COMPLETED - FAILED | [optional] 
**processing** | [**FeedProcessingSummary**](FeedProcessingSummary.md) |  | [optional] 
**syndication** | [**dict(str, FeedSyndicationProtocolStatus)**](FeedSyndicationProtocolStatus.md) | Per-protocol syndication status, keyed by lowercase protocol name (e.g. &#x60;acp&#x60;, &#x60;ucp&#x60;).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


