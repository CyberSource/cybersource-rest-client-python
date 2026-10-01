# BoardingPayoutsConfigurationsProcessors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates if the payment route is enabled. Allows the acquirer to enable/disable processing based on the config setting but to retain the configuration profile.  | [optional] 
**acquirer** | [**BoardingPayoutsConfigurationsAcquirer**](BoardingPayoutsConfigurationsAcquirer.md) |  | [optional] 
**currencies** | **list[str]** | List of supported [ISO 4217](https://developer.cybersource.com/docs/cybs/en-us/currency-codes/reference/all/na/currency-codes/currency-codes.html) alpha-3 currency codes. | [optional] 
**countries** | **list[str]** | List of [ISO 3166-1](https://developer.cybersource.com/docs/cybs/en-us/country-codes/reference/all/na/country-codes/country-codes.html) alpha-2 country codes | [optional] 
**merchant_id** | **str** | A unique identifier value assigned by Visa for each merchant included in the identification program. | [optional] 
**terminal_id** | **str** | This field contains a code that identifies a terminal at the card acceptor location. This field is used in all messages related to a transaction. If sending transactions from a card not present environment, use the same value for all transactions. | [optional] 
**business_category_validation** | **bool** | Default: false  Override Business Application Indicator and Merchant Category Code validations for payout transaction types.  | [optional] 
**payouts_transaction_types** | **list[str]** | The supported Payouts transaction types for the processor.  | [optional] 
**merchant_pseudo_aba_number** | **str** | This is a number that uniquely identifies the merchant for PPGS transactions.  | [optional] 
**bin_lookup_eligibility_check** | **list[str]** | List of transaction types eligible for BIN Lookup Payouts Eligibility Check.  Supports \&quot;PULL_FUNDS_TRANSFER\&quot; and \&quot;PUSH_FUNDS_TRANSFER\&quot;.  | [optional] 
**fee_program_id** | **str** | This field identifies the interchange fee program applicable to each financial transaction. Fee program indicator (FPI) values correspond to the fee descriptor and rate for each existing fee program.  This field can be regarded as informational only in all authorization messages.  | [optional] 
**cps_authorization_characteristics_id** | **str** | The Authorization Characteristics Indicator (ACI) is a code used by the acquirer to request CPS qualification. If applicable, Visa changes the code to reflect the results of its CPS evaluation. | [optional] 
**national_reimbursement_fee** | **str** | A client-supplied interchange amount. | [optional] 
**settlement_service_id** | **str** | This flag enables the merchant to request for a particular settlement service to be used for settling the transaction.  Note: The default value is VIP. This field is only relevant for specific countries where the acquirer has to select National Settlement in order to settle in the national net settlement service.change   Possible values: - INTERNATIONAL_SETTLEMENT - VIP_TO_DECIDE - NATIONAL_SETTLEMENT | [optional] 
**sharing_group_code** | **str** | This U.S.-only field is optionally used by PIN Debit Gateway Service participants (merchants and acquirers) to specify the network access priority. VisaNet checks to determine if there are issuer routing preferences for a network specified by the sharing group code. If an issuer preference exists for one of the specified debit networks, VisaNet makes a routing selection based on issuer preference. If an preference exists for multiple specified debit networks, or if no issuer preference exists, VisaNet makes a selection based on acquirer routing priorities.  Possible values: - ACCEL_EXCHANGE_E - CU24_C - INTERLINK_G - MAESTRO_8 - NYCE_Y - NYCE_F - PULSE_S - PULSE_L - PULSE_H - STAR_N - STAR_W - STAR_Z - STAR_Q - STAR_M - VISA_V | [optional] 
**allow_crypto_currency_purchase** | **bool** | This field allows a merchant to send a flag that specifies whether the payment is for the purchase of cryptocurrency. | [optional] 
**merchant_mvv** | **str** | Merchant Verification Value (MVV) is used to identify merchants that participate in a variety of programs. The MVV is unique to the merchant. | [optional] 
**electronic_commerce_id** | **str** | This code identifies the level of security used in an electronic commerce transaction over an open network (for example, the Internet).  Possible values: - INTERNET - RECURRING - RECURRING_INTERNET - VBV_FAILURE - VBV_ATTEMPTED - VBV - SPA_FAILURE - SPA_ATTEMPTED - SPA | [optional] 
**merchant_descriptor** | [**BoardingPayoutsConfigurationsMerchantDescriptor**](BoardingPayoutsConfigurationsMerchantDescriptor.md) |  | [optional] 
**operating_environment** | **str** | Initiation channel of the transfer request.     Possible values: - WEB - MOBILE - BANK - KIOSK | [optional] 
**interchange_rate_designator** | **str** | The IRD used for clearing the transaction on the Mastercard network. | [optional] 
**partner_identifier** | **str** | Mastercard-assigned unique ID for registered partner. Mastercard Send Only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


