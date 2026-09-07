# UnifiedriskAuthentication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_id** | **str** | Unique identifier assigned to an authentication attempt | [optional] 
**method** | **str** | Authentication method used during the authentication/MFA process | [optional] 
**mfa_successful** | **bool** | Whether multi-factor authentication was completed successfully | [optional] 
**phone_number** | **str** | Phone number used for authentication (e.g., SMS/voice MFA) | [optional] 
**email** | **str** | Email address used for authentication (e.g., verification code delivery) | [optional] 
**other** | **str** | Additional authentication-related information not captured by other fields | [optional] 
**three_ds_requestor_id** | **str** | Unique identifier assigned to the 3D Secure requestor (typically the merchant or payment service provider) by the directory server for authentication routing | [optional] 
**three_ds_requestor_name** | **str** | The business or brand name of the 3D Secure requestor as registered with the card network directory server | [optional] 
**challenge** | [**UnifiedriskAuthenticationChallenge**](UnifiedriskAuthenticationChallenge.md) |  | [optional] 
**decoupled_indicator** | **str** | Indicates whether decoupled authentication is requested or supported, allowing the cardholder to authenticate outside the main transaction flow. Values - \&quot;Y\&quot; (supported and preferred), \&quot;N\&quot; (do not use) | [optional] 
**decoupled_max_time** | **str** | Maximum time in minutes allowed for the cardholder to complete a decoupled authentication, after which the session expires | [optional] 
**three_ri_indicator** | **str** | Indicates the reason for the 3DS Requestor Initiated (3RI) transaction - a merchant-initiated authentication without active cardholder participation. Values defined by EMVCo 3DS specification | [optional] 
**authentication_indicator** | **str** | Indicates the type of authentication request being made, such as payment authentication, non-payment authentication, or recurring/installment transactions | [optional] 
**authentication_date** | **str** | The date and time when the cardholder completed authentication, used for tracking authentication timing and fraud analysis | [optional] 
**language_preference** | **list[str]** | The cardholder&#39;s preferred language for the authentication challenge interface, expressed as an IETF BCP 47 language tag (e.g., en-US, fr-FR) | [optional] 
**spc_support** | **str** | Indicates whether the merchant&#39;s environment supports the Secure Payment Confirmation (SPC) protocol for frictionless authentication using FIDO2/WebAuthn credentials | [optional] 
**spc_incomplete_indicator** | **str** | Indicates the reason why an SPC (Secure Payment Confirmation) transaction was not completed, helping distinguish cardholder-initiated abandonment from technical failures | [optional] 
**version** | **str** | The 3D Secure protocol version used for this authentication attempt (e.g., \&quot;2.1.0\&quot;, \&quot;2.2.0\&quot;), which determines which fields and features are supported | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


