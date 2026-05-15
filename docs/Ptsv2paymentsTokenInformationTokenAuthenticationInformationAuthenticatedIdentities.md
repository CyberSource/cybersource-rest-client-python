# Ptsv2paymentsTokenInformationTokenAuthenticationInformationAuthenticatedIdentities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Data related to the authenticated identity. Contains verification payload from the identity provider.  | [optional] 
**provider** | **str** | Provider of the authenticated identity. Identifies the authentication service or identity provider.   Possible values: - CLIENT_DEVICE_CERT_JWS - VISA_PAYMENT_PASSKEY | [optional] 
**id** | **str** | Unique identifier for the authenticated identity. A distinctive and non-transparent identifier for correlation purposes.  | [optional] 
**relying_party_id** | **str** | Identifier of the relying party that requested the authentication.  | [optional] 
**user_authentication_method** | **str** | The method used to authenticate the user.   Possible values: - USERNAME_PASSWORD - PASSCODE_PASSWORD - PASSCODE - PASSWORD - PATTERN - BIOMETRIC_FINGERPRINT - BIOMETRIC_FACIAL - BIOMETRIC_IRIS - BIOMETRIC_VOICE - BIOMETRIC_BEHAVIORAL - DEVICE_UNLOCKED_METHOD_UNKNOWN - OTP_SMS - OTP_EMAIL - OTP_SMS_KNOWLEDGE - KNOWLEDGE_BASED_AUTHENTICATION - USER_UNVERIFIED - BIOMETRIC | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


