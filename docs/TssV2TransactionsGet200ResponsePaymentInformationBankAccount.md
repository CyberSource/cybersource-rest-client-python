# TssV2TransactionsGet200ResponsePaymentInformationBankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suffix** | **str** | The description for this field is not available. | [optional] 
**prefix** | **str** | The description for this field is not available. | [optional] 
**check_number** | **str** | Check number.  Chase Paymentech Solutions - Optional. CyberSource ACH Service - Not used. RBS WorldPay Atlanta - Optional on debits. Required on credits. TeleCheck - Strongly recommended on debit requests. Optional on credits.  | [optional] 
**type** | **str** | Account type.  Possible values:  - **C**: Checking.  - **G**: General ledger. This value is supported only on Wells Fargo ACH.  - **S**: Savings (U.S. dollars only).  - **X**: Corporate checking (U.S. dollars only).  | [optional] 
**name** | **str** | The description for this field is not available. | [optional] 
**check_digit** | **str** | The description for this field is not available. | [optional] 
**encoder_id** | **str** | Identifier for the bank that provided the customer’s encoded account number.  To obtain the bank identifier, contact your processor. See \&quot;Encoded Account Numbers,\&quot; page 39.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


