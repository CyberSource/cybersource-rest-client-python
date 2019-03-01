# Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This field indicates whether the transaction is a merchant-initiated transaction or customer-initiated transaction.  Valid values: - **customer** - **merchant**  | [optional] 
**credential_stored_on_file** | **bool** | Flag that indicates whether merchant intends to use this transaction to store payment credentials for follow-up merchant-initiated transactions.  Valid values: - &#x60;true&#x60; means merchant will use this transaction to store payment credentials for follow-up merchant-initiated transactions. - &#x60;false&#x60; means merchant will not use this transaction to store payment credentials for follow-up merchant-initiated transactions.  See \&quot;Merchant-Initiated Transactions,\&quot; page 177.  **NOTE:** The value for this field does not correspond to any data in the TC 33 capture file5. This field is supported only for Visa transactions on CyberSource through VisaNet.  | [optional] 
**stored_credential_used** | **bool** | Flag that indicates whether merchant is intend to use this transaction to store payment credential for follow-up merchant-initiated transactions or not.  Possible values: - **true** - **false**  | [optional] 
**merchant_initiated_transaction** | [**Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction**](Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


