# UnifiedriskPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Payment method: CARD, BANK_ACCOUNT, WALLET | [optional] 
**customer_id** | **str** | Payment customer token ID | [optional] 
**customer_id_legacy** | **str** | Legacy customer ID for payment tokenization | [optional] 
**card** | [**UnifiedriskPaymentCard**](UnifiedriskPaymentCard.md) |  | [optional] 
**verification** | [**UnifiedriskPaymentVerification**](UnifiedriskPaymentVerification.md) |  | [optional] 
**wallet** | [**UnifiedriskPaymentWallet**](UnifiedriskPaymentWallet.md) |  | [optional] 
**bank_account** | [**UnifiedriskPaymentBankAccount**](UnifiedriskPaymentBankAccount.md) |  | [optional] 
**counterparty** | [**UnifiedriskPaymentCounterparty**](UnifiedriskPaymentCounterparty.md) |  | [optional] 
**approvals** | [**UnifiedriskPaymentApprovals**](UnifiedriskPaymentApprovals.md) |  | [optional] 
**bank** | **object** | Container for additional bank-specific information related to the payment, including routing codes, clearing house details, and bank-specific metadata | [optional] 
**token** | [**UnifiedriskPaymentToken**](UnifiedriskPaymentToken.md) |  | [optional] 
**batch** | [**UnifiedriskPaymentBatch**](UnifiedriskPaymentBatch.md) |  | [optional] 
**sub_method** | **str** | The specific sub-type of the payment method used (e.g., SEPA_CREDIT_TRANSFER, FASTER_PAYMENTS, ACH_NEXT_DAY). Provides granular detail within the broader payment method | [optional] 
**purpose** | **str** | The business or regulatory purpose code for the payment (e.g., SUPP for supplier payment, SALA for salary, CHAR for charity). Used for AML monitoring and regulatory reporting | [optional] 
**clearing_speed** | **str** | Indicates the speed at which the payment will be cleared and settled (e.g., REAL_TIME, SAME_DAY, NEXT_DAY, STANDARD). Faster clearing speeds on large amounts may indicate fraud | [optional] 
**execution_timestamp** | **str** | The date and time when the payment execution was initiated or scheduled by the payer or payment system, in ISO 8601 format | [optional] 
**group_id** | **str** | An identifier linking multiple related payments into a logical group (e.g., bulk payroll run ID, campaign payment group). Used for aggregated risk monitoring | [optional] 
**check** | [**UnifiedriskPaymentCheck**](UnifiedriskPaymentCheck.md) |  | [optional] 
**wire** | [**UnifiedriskPaymentWire**](UnifiedriskPaymentWire.md) |  | [optional] 
**type** | **str** | Specifies the underlying payment instrument type for this transaction (e.g., CARD, BANK_TRANSFER, CHECK, WIRE, ACH). Used for routing to the appropriate risk model and clearing network | [optional] 
**sdk** | [**UnifiedriskPaymentSdk**](UnifiedriskPaymentSdk.md) |  | [optional] 
**location_id** | **str** | Physical location (branch or ATM) in which the activity took place (if that&#39;s a physical branch). Identifier for staff location, site, or service centre. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


