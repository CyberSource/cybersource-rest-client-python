# UnifiedriskPaymentBankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Account type: CHECKING, SAVINGS, CORPORATE, etc | [optional] 
**number** | **str** | Masked or tokenized account number | [optional] 
**number_format** | **str** | Account number format: IBAN, BBAN, etc | [optional] 
**routing_number** | **str** | Bank routing/transit number | [optional] 
**iban** | **str** | International Bank Account Number | [optional] 
**swift_code** | **str** | Bank SWIFT/BIC code | [optional] 
**bank_code** | **str** | Bank code | [optional] 
**check_number** | **str** | Check number for check payments | [optional] 
**check_image_reference** | **str** | Check image reference number | [optional] 
**encoder_id** | **str** | Bank encoder identifier for encoded account numbers | [optional] 
**branch_id** | **str** | Bank branch identifier | [optional] 
**flags** | **list[str]** | Account flags: VIP, COMPROMISED, etc | [optional] 
**account_holder_name** | **str** | Full name of the person or business that owns the bank account | [optional] 
**added_at_checkout** | **bool** | Whether the bank account was newly entered during checkout | [optional] 
**financial_institution** | [**UnifiedriskPaymentBankAccountFinancialInstitution**](UnifiedriskPaymentBankAccountFinancialInstitution.md) |  | [optional] 
**balance_before** | [**UnifiedriskPaymentBankAccountBalanceBefore**](UnifiedriskPaymentBankAccountBalanceBefore.md) |  | [optional] 
**credit_limit** | [**UnifiedriskPaymentBankAccountCreditLimit**](UnifiedriskPaymentBankAccountCreditLimit.md) |  | [optional] 
**branch_address** | [**UnifiedriskPaymentBankAccountBranchAddress**](UnifiedriskPaymentBankAccountBranchAddress.md) |  | [optional] 
**sub_type** | **str** | Sub-category of the bank account type providing more specific classification (e.g., PERSONAL_CHECKING, BUSINESS_SAVINGS, CORPORATE_CURRENT). Used for risk segmentation within account types | [optional] 
**account_open_date** | **str** | Date when the bank account was originally opened, in ISO 8601 format (YYYY-MM-DD). Account tenure is a key risk factor - newer accounts carry higher fraud risk | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


