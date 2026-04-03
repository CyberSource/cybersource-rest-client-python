# Acpv1instructionsinstructionIdconfirmationsProcessorInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_data_id** | **str** | A unique reference ID that represents the dynamic data associated with a transaction | [optional] 
**transaction_type** | **str** | Type of payment transaction Possible values:   - &#39;PURCHASE&#39;   - &#39;AUTHORIZATION&#39;   - &#39;CAPTURE&#39;   - &#39;REFUND&#39;   - &#39;REVERSAL&#39;   - &#39;VERIFICATION&#39;   - &#39;CHARGEBACK&#39;   - &#39;FRAUD&#39;  | 
**transaction_status** | **str** | Status of payment transaction Possible values:   - &#39;APPROVED&#39;   - &#39;DECLINED&#39;   - &#39;PENDING&#39;   - &#39;ERROR&#39;   - &#39;CANCELLED&#39;  | 
**response_code** | **str** | 2 Digit Response code sent directly from the payment processor | [optional] 
**transaction_timestamp** | **str** | Date and time of the transaction (UTC time in Epoch format) | [optional] 
**approval_code** | **str** | Authorization code. Returned when the processor returns this value | [optional] 
**retrieval_reference_number** | **str** | Unique number to identify the transaction. It is used with other data elements to identify and track all messages related to a transaction | [optional] 
**system_trace_audit_number** | **str** | System Trace Audit Number. Audit number assigned by the payment network | [optional] 
**acquirer_reference_number** | **str** | Acquirer Reference Number. Reference number assigned by the acquirer | [optional] 
**amount_detail** | [**Acpv1instructionsinstructionIdcredentialsOrderInformationAmountDetail**](Acpv1instructionsinstructionIdcredentialsOrderInformationAmountDetail.md) |  | [optional] 
**entry_mode** | **str** | Method of entering payment card information Possible values:     - &#39;EMV&#39;   - &#39;CONTACTLESS&#39;   - &#39;MANUAL&#39;   - &#39;ECOMMERCE&#39;   - &#39;WALLET&#39;  | [optional] 
**payment_instrument** | [**Acpv1instructionsinstructionIdconfirmationsProcessorInformationPaymentInstrument**](Acpv1instructionsinstructionIdconfirmationsProcessorInformationPaymentInstrument.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


