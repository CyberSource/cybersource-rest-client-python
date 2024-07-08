# PtsV2PaymentsPost201ResponsePaymentInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**PtsV2PaymentsPost201ResponsePaymentAccountInformationCard**](PtsV2PaymentsPost201ResponsePaymentAccountInformationCard.md) |  | [optional] 
**tokenized_card** | [**PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard**](PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.md) |  | [optional] 
**account_features** | [**PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures**](PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures.md) |  | [optional] 
**bank** | [**PtsV2PaymentsPost201ResponsePaymentInformationBank**](PtsV2PaymentsPost201ResponsePaymentInformationBank.md) |  | [optional] 
**customer** | [**Ptsv2paymentsPaymentInformationCustomer**](Ptsv2paymentsPaymentInformationCustomer.md) |  | [optional] 
**payment_instrument** | [**Ptsv2paymentsPaymentInformationPaymentInstrument**](Ptsv2paymentsPaymentInformationPaymentInstrument.md) |  | [optional] 
**instrument_identifier** | [**PtsV2PaymentsPost201ResponsePaymentInformationInstrumentIdentifier**](PtsV2PaymentsPost201ResponsePaymentInformationInstrumentIdentifier.md) |  | [optional] 
**shipping_address** | [**Ptsv2paymentsPaymentInformationShippingAddress**](Ptsv2paymentsPaymentInformationShippingAddress.md) |  | [optional] 
**scheme** | **str** | Subtype of card account. This field can contain one of the following values: - Maestro International - Maestro UK Domestic - MasterCard Credit - MasterCard Debit - Visa Credit - Visa Debit - Visa Electron  **Note** Additional values may be present.  | [optional] 
**bin** | **str** | Credit card BIN (the first six digits of the credit card).Derived either from the &#x60;cc_bin&#x60; request field or from the first six characters of the &#x60;customer_cc_num&#x60; field.  | [optional] 
**account_type** | **str** | Type of payment card account. This field can refer to a credit card, debit card, or prepaid card account type.  | [optional] 
**issuer** | **str** | Name of the bank or entity that issued the card account.  | [optional] 
**bin_country** | **str** | Country (two-digit country code) associated with the BIN of the customer&#39;s card used for the payment. Returned if the information is available. Use this field for additional information when reviewing orders. This information is also displayed in the details page of the CyberSource Business Center.  | [optional] 
**e_wallet** | [**PtsV2PaymentsPost201ResponsePaymentInformationEWallet**](PtsV2PaymentsPost201ResponsePaymentInformationEWallet.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


