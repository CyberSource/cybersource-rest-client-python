# TssV2TransactionsGet200ResponseProcessorInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processor** | [**TssV2TransactionsGet200ResponseProcessorInformationProcessor**](TssV2TransactionsGet200ResponseProcessorInformationProcessor.md) |  | [optional] 
**transaction_id** | **str** | Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this value.  | [optional] 
**network_transaction_id** | **str** | The description for this field is not available. | [optional] 
**response_id** | **str** | The description for this field is not available. | [optional] 
**provider_transaction_id** | **str** | The description for this field is not available. | [optional] 
**approval_code** | **str** | Authorization code. Returned only when the processor returns this value.  | [optional] 
**response_code** | **str** | For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  Important Do not use this field to evaluate the result of the authorization.  | [optional] 
**avs** | [**PtsV2PaymentsPost201ResponseProcessorInformationAvs**](PtsV2PaymentsPost201ResponseProcessorInformationAvs.md) |  | [optional] 
**card_verification** | [**Riskv1decisionsCardVerification**](Riskv1decisionsCardVerification.md) |  | [optional] 
**ach_verification** | [**PtsV2PaymentsPost201ResponseProcessorInformationAchVerification**](PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.md) |  | [optional] 
**electronic_verification_results** | [**TssV2TransactionsGet200ResponseProcessorInformationElectronicVerificationResults**](TssV2TransactionsGet200ResponseProcessorInformationElectronicVerificationResults.md) |  | [optional] 
**system_trace_audit_number** | **str** | This field is returned only for **American Express Direct** and **CyberSource through VisaNet**.  **American Express Direct**  System trace audit number (STAN). This value identifies the transaction and is useful when investigating a chargeback dispute.  **CyberSource through VisaNet**  System trace number that must be printed on the customer’s receipt.  | [optional] 
**response_code_source** | **str** | Used by Visa only and contains the response source/reason code that identifies the source of the response decision.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


