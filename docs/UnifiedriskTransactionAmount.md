# UnifiedriskTransactionAmount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Transaction amount in the specified currency | [optional] 
**currency** | **str** | ISO 4217 3-letter currency code | [optional] 
**base_currency** | **str** | Base currency for multi-currency transactions | [optional] 
**base_value** | **str** | Amount in base currency | [optional] 
**merchant_currency** | **str** | ISO 4217 3-letter code for the merchant&#39;s local currency used to express the transaction amount (e.g., EUR for EU merchants). Used for cross-currency risk analysis | [optional] 
**merchant_value** | **str** | Transaction amount expressed in the merchant&#39;s local currency, used for cross-currency comparison and risk threshold evaluation against merchant&#39;s baseline | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


