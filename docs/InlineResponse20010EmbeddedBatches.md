# InlineResponse20010EmbeddedBatches

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InlineResponse20010EmbeddedLinks**](InlineResponse20010EmbeddedLinks.md) |  | [optional] 
**batch_id** | **str** | Unique identification number assigned to the submitted request. | [optional] 
**batch_created_date** | **str** | ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ | [optional] 
**batch_modified_date** | **str** | ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ | [optional] 
**batch_source** | **str** | Valid Values:   * SCHEDULER   * TOKEN_API   * CREDIT_CARD_FILE_UPLOAD   * AMEX_REGSITRY   * AMEX_REGISTRY_API   * AMEX_REGISTRY_API_SYNC   * AMEX_MAINTENANCE  | [optional] 
**token_source** | **str** | Valid Values:   * SECURE_STORAGE   * TMS   * CYBERSOURCE  | [optional] 
**merchant_reference** | **str** | Reference used by merchant to identify batch. | [optional] 
**batch_ca_endpoints** | **list[str]** | Valid Values:   * VISA   * MASTERCARD   * AMEX  | [optional] 
**status** | **str** | Valid Values:   * REJECTED   * RECEIVED   * VALIDATED   * DECLINED   * PROCESSING   * COMPLETE  | [optional] 
**totals** | [**InlineResponse20010EmbeddedTotals**](InlineResponse20010EmbeddedTotals.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


