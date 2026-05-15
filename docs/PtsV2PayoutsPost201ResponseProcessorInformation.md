# PtsV2PayoutsPost201ResponseProcessorInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_code** | **str** | Issuer-generated approval code for the transaction. | [optional] 
**response_code** | **str** | Transaction status from the processor. | [optional] 
**transaction_id** | **str** | Network transaction identifier (TID). This value can be used to identify a specific transaction when you are discussing the transaction with your processor.  | [optional] 
**system_trace_audit_number** | **str** | This field is returned only for **American Express Direct** and **CyberSource through VisaNet**. Returned by authorization and incremental authorization services.  #### American Express Direct  System trace audit number (STAN). This value identifies the transaction and is useful when investigating a chargeback dispute.  #### CyberSource through VisaNet  System trace number that must be printed on the customer&#39;s receipt.  | [optional] 
**response_code_source** | **str** | Used by Visa only and contains the response source/reason code that identifies the source of the response decision.  | [optional] 
**merchant_advice** | [**PtsV2PaymentsRefundPost201ResponseProcessorInformationMerchantAdvice**](PtsV2PaymentsRefundPost201ResponseProcessorInformationMerchantAdvice.md) |  | [optional] 
**avs** | [**PtsV2PayoutsPost201ResponseProcessorInformationAvs**](PtsV2PayoutsPost201ResponseProcessorInformationAvs.md) |  | [optional] 
**customer** | [**PtsV2PayoutsPost201ResponseProcessorInformationCustomer**](PtsV2PayoutsPost201ResponseProcessorInformationCustomer.md) |  | [optional] 
**electronic_verification_results** | [**PtsV2PayoutsPost201ResponseProcessorInformationElectronicVerificationResults**](PtsV2PayoutsPost201ResponseProcessorInformationElectronicVerificationResults.md) |  | [optional] 
**card_verification** | [**PtsV2PaymentsPost201ResponseProcessorInformationCardVerification**](PtsV2PaymentsPost201ResponseProcessorInformationCardVerification.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


