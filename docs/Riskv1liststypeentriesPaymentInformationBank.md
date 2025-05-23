# Riskv1liststypeentriesPaymentInformationBank

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Customer&#39;s bank account number. You can use this field only when scoring a direct debit transaction. Use this field if you do not or are not allowed to provide the IBAN. Note Do not use the IBAN in this field. Use nly the traditional account number information. For the IBAN, use bank_iban.  | [optional] 
**code** | **str** | Country-specific code used to identify the customer&#39;s bank. Required for some countries if you do not or are not allowed to provide the IBAN instead. You can use this field only when scoring a direct debit transaction. For specific requirements, see \&quot;Required Bank Account Information by Country,\&quot;  | [optional] 
**country** | **str** | Country where the bank is located. Use the two-character ISO codes. You can use this field only when scoring a direct debit transaction.  | [optional] 
**iban** | **str** | International Bank Account Number (IBAN) for the bank account. For some countries you can provide this number instead of the traditional bank account information. You can use this field only when scoring a direct debit transaction. For specific requirements, see \&quot;Required Bank Account Information by Country,\&quot;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


