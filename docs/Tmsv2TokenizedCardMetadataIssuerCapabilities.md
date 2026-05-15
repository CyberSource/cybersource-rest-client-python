# Tmsv2TokenizedCardMetadataIssuerCapabilities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_binding_supported** | **bool** | Indicates if the issuer supports device binding.  | [optional] 
**cardholder_verification_supported** | **bool** | Indicates if the issuer participates in step-up authentication that requires cardholder verification.  | [optional] 
**trusted_beneficiary_enrollment_supported** | **bool** | Indicates if the issuer supports trusted beneficiary enrollment. e.g allowing cardholders to designate trusted merchants or payment recipients that can be exempt from step-up authentication.  | [optional] 
**delegated_authentication_supported** | **bool** | Indicates if the issuer supports delegated authentication. e.g allowing approved thrird parties to perform authentication on behalf of the issuer.  | [optional] 
**obo_device_binding_supported** | **bool** | Indicates if the issuer supports on-behalf-of device binding. e.g allowing approved third parties to perform device binding on behalf of the issuer.  | [optional] 
**token_lcm_notifications_supported** | **bool** | Indicates if the issuer supports receiving token lifecycle management notifications. e.g receiving updates on changes to the token&#39;s status or attributes.  | [optional] 
**fpan_lcm_notifications_supported** | **bool** | Indicates if the issuer supports receiving PAN lifecycle management notifications. e.g receiving updates on changes to the underlying card&#39;s status or attributes.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


