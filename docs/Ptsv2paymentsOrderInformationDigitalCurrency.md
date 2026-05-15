# Ptsv2paymentsOrderInformationDigitalCurrency

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Currently, Visa uses a broad \&quot;cryptocurrency\&quot; indicator. The enhancement will introduce specific values to identify the type of digital currency or coin involved, such as Central Bank Digital Currency (CBDC), stable coins, blockchain-native tokens, and Non-Fungible Tokens (NFTs). Values: - 1: CBDC_TOKENDEPOSIT - 2: STABLE_COIN - 3: BLOCKCHAIN_NATIVE_TOKEN - 4: NFT | [optional] 
**ramp_provider_country** | **str** | Ramp is a platform where we can buy Digital currency, for example Coinbase. This value identifies the country where the Ramp provider is registered. | [optional] 
**conversion_affiliate** | **str** | Affiliate is the platform for the digital currency transactions. The merchant provides the Affiliate country for transaction processing. The combination of affiliate country and ramp country helps to derive the foreign retail indicator. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


