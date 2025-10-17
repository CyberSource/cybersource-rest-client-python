# InlineResponse20011

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InlineResponse20011Links**](InlineResponse20011Links.md) |  | [optional] 
**batch_id** | **str** | Unique identification number assigned to the submitted request. | [optional] 
**batch_created_date** | **str** | ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ | [optional] 
**batch_source** | **str** | Valid Values:   * SCHEDULER   * TOKEN_API   * CREDIT_CARD_FILE_UPLOAD   * AMEX_REGSITRY   * AMEX_REGISTRY_API   * AMEX_MAINTENANCE  | [optional] 
**merchant_reference** | **str** | Reference used by merchant to identify batch. | [optional] 
**batch_ca_endpoints** | **str** |  | [optional] 
**status** | **str** | Valid Values:   * REJECTED   * RECEIVED   * VALIDATED   * DECLINED   * PROCESSING   * COMPLETED  | [optional] 
**totals** | [**InlineResponse20010EmbeddedTotals**](InlineResponse20010EmbeddedTotals.md) |  | [optional] 
**billing** | [**InlineResponse20011Billing**](InlineResponse20011Billing.md) |  | [optional] 
**description** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


