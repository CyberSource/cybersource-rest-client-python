# InlineResponse20012

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**report_created_date** | **str** | ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ | [optional] 
**batch_id** | **str** | Unique identification number assigned to the submitted request. | [optional] 
**batch_source** | **str** | Valid Values:   * SCHEDULER   * TOKEN_API   * CREDIT_CARD_FILE_UPLOAD   * AMEX_REGSITRY   * AMEX_REGISTRY_API   * AMEX_MAINTENANCE  | [optional] 
**batch_ca_endpoints** | **str** |  | [optional] 
**batch_created_date** | **str** | ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ | [optional] 
**merchant_reference** | **str** | Reference used by merchant to identify batch. | [optional] 
**totals** | [**InlineResponse20010EmbeddedTotals**](InlineResponse20010EmbeddedTotals.md) |  | [optional] 
**billing** | [**InlineResponse20011Billing**](InlineResponse20011Billing.md) |  | [optional] 
**records** | [**list[InlineResponse20012Records]**](InlineResponse20012Records.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


