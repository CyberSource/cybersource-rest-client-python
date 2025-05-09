# Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This field indicates whether the transaction is a merchant-initiated transaction or customer-initiated transaction.  Valid values: - **customer** - **merchant**  | [optional] 
**credential_stored_on_file** | **bool** | Indicates to the issuing bank two things: - The merchant has received consent from the cardholder to store their card details on file - The merchant wants the issuing bank to check out the card details before the merchant initiates their first transaction for this cardholder. The purpose of the merchant-initiated transaction is to ensure that the cardholder&#39;s credentials are valid (that the card is not stolen or has restrictions) and that the card details are good to be stored on the merchant&#39;s file for future transactions.  Valid values: - &#x60;true&#x60; means merchant will use this transaction to store payment credentials for follow-up merchant-initiated transactions. - &#x60;false&#x60; means merchant will not use this transaction to store payment credentials for follow-up merchant-initiated transactions.  **NOTE:** The value for this field does not correspond to any data in the TC 33 capture file5.  This field is supported only for Visa transactions on CyberSource through VisaNet.  | [optional] 
**stored_credential_used** | **bool** | Indicates to an issuing bank whether a merchant-initiated transaction came from a card that was already stored on file.  Possible values: - **true** means the merchant-initiated transaction came from a card that was already stored on file. - **false**  means the merchant-initiated transaction came from a card that was not stored on file.  | [optional] 
**merchant_initiated_transaction** | [**Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction**](Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


