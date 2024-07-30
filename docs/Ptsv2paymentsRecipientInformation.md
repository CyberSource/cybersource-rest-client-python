# Ptsv2paymentsRecipientInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Identifier for the recipient&#39;s account. Use the first six digits and last four digits of the recipient&#39;s account number. This field is a _pass-through_, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For details, see the &#x60;recipientInformation.accountId&#x60; field description in the [REST API Fields](https://developer.cybersource.com/content/dam/docs/cybs/en-us/apifields/reference/all/rest/api-fields.pdf)  | [optional] 
**last_name** | **str** | Recipient&#39;s last name. This field is a _passthrough_, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For details, see the &#x60;recipientInformation.lastName&#x60; field description in the [REST API Fields](https://developer.cybersource.com/content/dam/docs/cybs/en-us/apifields/reference/all/rest/api-fields.pdf)  | [optional] 
**middle_name** | **str** | Recipient&#39;s middle name. This field is a _passthrough_, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For details, see the &#x60;recipientInformation.middleName&#x60; field description in the [REST API Fields](https://developer.cybersource.com/content/dam/docs/cybs/en-us/apifields/reference/all/rest/api-fields.pdf)  | [optional] 
**postal_code** | **str** | Partial postal code for the recipient&#39;s address. For example, if the postal code is **NN5 7SG**, the value for this field should be the first part of the postal code: **NN5**. This field is a _pass-through_, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  | [optional] 
**date_of_birth** | **str** | Recipient&#39;s date of birth. **Format**: &#x60;YYYYMMDD&#x60;.  This field is a &#x60;pass-through&#x60;, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  | [optional] 
**beneficiary_id** | **str** | Only for e-wallets: ID, username, hash or anything uniquely identifying the ultimate beneficiary.  | [optional] 
**beneficiary_name** | **str** | Only for e-wallets: The ultimate beneficiary&#39;s full name.  | [optional] 
**beneficiary_address** | **str** | Only for e-wallets: The ultimate beneficiary&#39;s street address (street, zip code, city), excluding the country. Example: \&quot;Main street 1, 12345, Barcelona  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


