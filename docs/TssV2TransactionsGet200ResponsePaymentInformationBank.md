# TssV2TransactionsGet200ResponsePaymentInformationBank

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_number** | **str** | Bank routing number. This is also called the transit number.  | [optional] 
**branch_code** | **str** | Code used to identify the branch of the customer&#39;s bank. Required for some countries if you do not or are not allowed to provide the IBAN. Use this field only when scoring a direct debit transaction.  | [optional] 
**swift_code** | **str** | Bank&#39;s SWIFT code. You can use this field only when scoring a direct debit transaction. Required only for crossborder transactions.  | [optional] 
**bank_code** | **str** | Country-specific code used to identify the customer&#39;s bank. Required for some countries if you do not or are not allowed to provide the IBAN instead. You can use this field only when scoring a direct debit transaction.  | [optional] 
**iban** | **str** | International Bank Account Number (IBAN) for the bank account. For some countries you can provide this number instead of the traditional bank account information. You can use this field only when scoring a direct debit transaction.  | [optional] 
**account** | [**TssV2TransactionsGet200ResponsePaymentInformationBankAccount**](TssV2TransactionsGet200ResponsePaymentInformationBankAccount.md) |  | [optional] 
**mandate** | [**TssV2TransactionsGet200ResponsePaymentInformationBankMandate**](TssV2TransactionsGet200ResponsePaymentInformationBankMandate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


