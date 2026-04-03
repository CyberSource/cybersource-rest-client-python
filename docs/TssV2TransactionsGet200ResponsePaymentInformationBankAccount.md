# TssV2TransactionsGet200ResponsePaymentInformationBankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suffix** | **str** | Last four digits of the customer&#39;s payment account number.  | [optional] 
**prefix** | **str** | Bank Identification Number (BIN). This is the initial four to six numbers on a credit card account number.  | [optional] 
**check_number** | **str** | Check number.  Chase Paymentech Solutions - Optional. CyberSource ACH Service - Not used. RBS WorldPay Atlanta - Optional on debits. Required on credits. TeleCheck - Strongly recommended on debit requests. Optional on credits.  | [optional] 
**type** | **str** | Account type.  Possible values:  - **C**: Checking.  - **G**: General ledger. This value is supported only on Wells Fargo ACH.  - **S**: Savings (U.S. dollars only).  - **X**: Corporate checking (U.S. dollars only).  | [optional] 
**name** | **str** | Name used on the bank account. You can use this field only when scoring a direct debit transaction  | [optional] 
**check_digit** | **str** | Code used to validate the customer&#39;s account number. Required for some countries if you do not or are not allowed to provide the IBAN instead. You may use this field only when scoring a direct debit transaction.  | [optional] 
**encoder_id** | **str** | Identifier for the bank that provided the customer&#39;s encoded account number.  To obtain the bank identifier, contact your processor.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


