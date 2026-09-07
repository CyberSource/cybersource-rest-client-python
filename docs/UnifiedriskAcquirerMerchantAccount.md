# UnifiedriskAcquirerMerchantAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_account_branch_id** | **str** | Unique identifier for the specific branch or location of the merchant&#39;s account within the acquiring bank&#39;s organizational structure | [optional] 
**merchant_account_id** | **str** | The primary account identifier assigned by the acquirer to the merchant for payment processing and settlement purposes | [optional] 
**merchant_account_id_format** | **str** | Describes the format or standard used for the merchant account identifier (e.g., ISO, Proprietary, Numeric) | [optional] 
**security_amount** | [**UnifiedriskAcquirerMerchantAccountSecurityAmount**](UnifiedriskAcquirerMerchantAccountSecurityAmount.md) |  | [optional] 
**settlement_frequency** | **int** | The number of days between settlement cycles defining how often funds are transferred from the acquirer to the merchant&#39;s account (e.g., 1 for daily, 7 for weekly) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


