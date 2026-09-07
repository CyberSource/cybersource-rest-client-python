# VpriTransactionInsightsAdditionalDataCardBinData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_bin** | **str** | The BIN submitted for lookup, consisting of the first 6 or 8 digits of the card number, identifying the issuing institution. | [optional] 
**issuer_bin_country** | **str** | ISO 3166-1 alpha-2 country code of the card-issuing institution. Useful for detecting geographic mismatches between issuer and transaction origin. | [optional] 
**issuer_name** | **str** | Full name of the card-issuing bank or financial institution. | [optional] 
**card_bin** | **str** | Resolved card BIN returned by the lookup service, which may differ from issuerBin in certain co-branded or affiliated card scenarios. | [optional] 
**card_funding_source** | **str** | Funding source type of the card indicating how transactions are funded (e.g., CREDIT, DEBIT, PREPAID). Used for risk segmentation by payment method. | [optional] 
**card_funding_source_sub_type** | **str** | Sub-classification of the funding source (e.g., business, consumer). Enables more granular risk profiling within a funding source category. | [optional] 
**card_brand** | **str** | Card network brand code (e.g., 001 for Visa, 002 for Mastercard). Used for brand-specific fraud rule application. | [optional] 
**card_product_id** | **str** | Product identifier for the card product issued. May be an alphanumeric code or a product name depending on the issuer. | [optional] 
**card_product_description** | **str** | Human-readable description of the card product. Useful for client-facing displays or product-level fraud analysis. | [optional] 
**status** | **str** | Result status of the BIN lookup. Indicates whether the BIN was successfully matched in the lookup service.  Possible values: - matched - no_match - error | [optional] 
**warnings** | [**list[UnifiedRiskPost201ResponseResultsRISKINSIGHTSPackagesTransactionInsightsInsightsWarnings]**](UnifiedRiskPost201ResponseResultsRISKINSIGHTSPackagesTransactionInsightsInsightsWarnings.md) | BIN-lookup-specific warnings. An empty array indicates a clean lookup. Warning codes include BIN_NO_MATCH, BIN_INPUT_MISSING, BIN_LOOKUP_ERROR, BIN_AMBIGUOUS, BIN_LOOKUP_INPUT_ERROR. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


