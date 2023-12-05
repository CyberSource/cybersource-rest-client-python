# PaymentsProductsPayoutsConfigurationInformationConfigurationsPullfunds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirer_organization_id** | **str** | Valid organization in OMS with an organizationInformation.type as \&quot;acquirer\&quot;. | [optional] 
**acquiring_bin** | **int** | This code identifies the financial institution acting as the acquirer of this transaction. The acquirer is the client or system user that signed the originator or installed the unattended cardholder- activated environment. When a processing center operates for multiple acquirers, this code is for the individual client or system user, not a code for the center. | 
**allow_crypto_currency_purchase** | **bool** | This configuration allows a transaction to be flagged for cryptocurrency funds transfer. | [optional] 
**card_acceptor_id** | **str** | A unique identifier number for the originator of transfers that is unique to the processor or acquirer. | 
**originator_mvv** | **str** | Merchant Verification Value (MVV) is used to identify originators that participate in a variety of programs. The MVV is unique to the merchant. | [optional] 
**originator_name_abbreviation** | **str** | A 4 character max name abbreviation for the originator. | [optional] 
**card_terminal_id** | **str** | This field contains a code that identifies a terminal at the card acceptor location. This field is used in all messages related to a transaction. If sending transactions from a card not present environment, use the same value for all transactions. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


