# PushFunds201ResponseProcessorInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **int** | Network transaction identifier (TID). This value can be used to identify a specific transaction when you are discussing the transaction with your processor.  | [optional] 
**response_code** | **str** | Transaction status from the processor.  | [optional] 
**approval_code** | **str** | Issuer-generated approval code for the transaction.  | [optional] 
**system_trace_audit_number** | **str** | System audit number. Returned by authorization and incremental authorization services.  Visa Platform Connect  System trace number that must be printed on the customer&#39;s receipt.  | [optional] 
**response_code_source** | **str** | Used by Visa only and contains the response source/reason code that identifies the source of the response decision.  | [optional] 
**retrieval_reference_number** | **str** | Unique reference number returned by the processor that identifies the transaction at the network.  Supported by Mastercard Send  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


