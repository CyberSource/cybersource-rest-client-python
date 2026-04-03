# Riskv1authenticationresultsConsumerAuthenticationInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_transaction_id** | **str** | Payer authentication transaction identifier passed to link the check enrollment and validate authentication messages.For Rupay,this is passed only in Re-Send OTP usecase. **Note**: Required for Standard integration, Rupay Seamless server to server integration for enroll service. Required for Hybrid integration for validate service.  | 
**authentication_transaction_context** | **str** | Authentication transaction context is used as a unique identifier to link enroll and validate call.  | [optional] 
**otp_token** | **str** | OTP entered by the card holder.  | [optional] 
**response_access_token** | **str** | JWT returned by the 3D Secure provider when the authentication is complete. Required for Hybrid integration if you use the Cybersource-generated access token. Note: Max. length of this field is 2048 characters.  | [optional] 
**signed_pares_status_reason** | **str** | Provides additional information as to why the PAResStatus has a specific value.  | [optional] 
**signed_pares** | **str** | Payer authentication result (PARes) message returned by the card-issuing bank. If you need to show proof of enrollment checking, you may need to decrypt and parse the string for the information required by the payment card company. For more information, see \&quot;Storing Payer Authentication Data,\&quot; page 160. Important The value is in base64. You must remove all carriage returns and line feeds before adding the PARes to the request.  | [optional] 
**white_list_status** | **str** | Enables the communication of trusted beneficiary/whitelist status between the ACS, the DS and the 3DS Requestor.  Possible Values:  Y - 3DS Requestor is whitelisted by cardholder  N - 3DS Requestor is not whitelisted by cardholder  | [optional] 
**credential_encrypted** | **str** | A flag to indicate if the passed credential has been encrypted by the Merchant. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


