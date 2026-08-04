# InlineResponse20019

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Overall ingestion result: - &#x60;success&#x60; — all products were validated and saved - &#x60;partial_success&#x60; — some products failed validation; &#x60;errors&#x60; lists the failures - &#x60;failed&#x60; — no products were saved; check &#x60;errors&#x60; for details   Possible values: - success - partial_success - failed | [optional] 
**feed_id** | **str** | Unique identifier for this feed ingestion job. Use this with the Syndication Status endpoint to monitor the asynchronous protocol sync progress (e.g. to Google Merchant Center).  | [optional] 
**total_submitted** | **int** | Total number of product records in the submitted feed. | [optional] 
**success_count** | **int** | Number of products that passed validation and were saved to the catalog. | [optional] 
**failed_count** | **int** | Number of products that failed validation and were not saved. | [optional] 
**errors** | [**list[InlineResponse20019Errors]**](InlineResponse20019Errors.md) | Per-product validation errors for products that failed ingestion. Each entry identifies the product, the specific field that failed, and the reason. &#x60;null&#x60; when &#x60;failed_count&#x60; is zero.  | [optional] 
**ingested_at** | **datetime** | ISO 8601 timestamp when the ingestion completed. | [optional] 
**forwarded_to_agent** | **bool** | Indicates whether the ingested products were scheduled for syndication to the configured AI agent endpoint. Set to &#x60;true&#x60; when at least one product was successfully saved. Note: syndication is asynchronous — this field confirms the dispatch was initiated, not that the agent received the data.  | [optional] 
**agent_endpoint** | **str** | The AI agent endpoint URL that the products were forwarded to. Present when &#x60;forwarded_to_agent&#x60; is &#x60;true&#x60;.  | [optional] 
**forwarded_to_ucp_agent** | **bool** | Indicates whether the ingested products were scheduled for syndication to the UCP (Unified Commerce Platform) agent. Set to &#x60;true&#x60; when UCP syndication is enabled and at least one product was successfully saved.  | [optional] 
**google_merchant** | [**InlineResponse20019GoogleMerchant**](InlineResponse20019GoogleMerchant.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


