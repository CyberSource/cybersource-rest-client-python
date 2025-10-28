# CardProcessingConfigCommonAcquirers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | Identifier of the acquirer. This number is usually assigned by Visa. | [optional] 
**interbank_card_association_id** | **str** | Number assigned by MasterCard to banks to identify the member in transactions. | [optional] 
**discover_institution_id** | **str** | Assigned by Discover to identify the acquirer. | [optional] 
**country_code** | **str** | ISO 4217 format. | [optional] 
**file_destination_bin** | **str** | The BIN to which this capturefile is sent. This field must contain a valid BIN. | [optional] 
**merchant_verification_value** | **str** | Identify merchants that participate in Select Merchant Fee (SMF) programs. Unique to the merchant. | [optional] 
**merchant_id** | **str** | Merchant ID assigned by an acquirer or a processor. Should not be overriden by any other party. | [optional] 
**terminal_id** | **str** | The &#39;Terminal Id&#39; aka TID, is an identifier used for with your payments processor. Depending on the processor and payment acceptance type this may also be the default Terminal ID used for Card Present and Virtual Terminal transactions.  | [optional] 
**allow_multiple_bills** | **bool** | Allows multiple captures for a single authorization transaction.  | [optional] 
**enable_transaction_reference_number** | **bool** | To enable merchant to send in transaction reference number (unique reconciliation ID). | [optional] 
**payment_types** | [**dict(str, CardProcessingConfigCommonPaymentTypes)**](CardProcessingConfigCommonPaymentTypes.md) | Valid values are: * VISA * MASTERCARD * AMERICAN_EXPRESS * CUP * EFTPOS * DINERS_CLUB * DISCOVER * JCB  | [optional] 
**currencies** | [**dict(str, CardProcessingConfigCommonCurrencies)**](CardProcessingConfigCommonCurrencies.md) | Three-character [ISO 4217 ALPHA-3 Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


