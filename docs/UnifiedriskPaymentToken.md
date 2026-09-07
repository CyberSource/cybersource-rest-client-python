# UnifiedriskPaymentToken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The actual token string or transient token JWT value used as a payment reference. This replaces the raw payment credential in tokenized payment flows | [optional] 
**expiry_date** | **str** | Expiry date of the payment token, in MMYYYY or MMYY format. Expired tokens must not be used for payment processing | [optional] 
**jti** | **str** | JWT ID (jti claim) from the transient token, providing a unique identifier for the token JWT for nonce validation and replay prevention | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


