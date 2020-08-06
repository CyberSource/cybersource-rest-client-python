# Ptsv2paymentsTokenInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jti** | **str** | TMS Transient Token, 64 hexadecimal id value representing captured payment credentials (including Sensitive Authentication Data, e.g. CVV).  | [optional] 
**transient_token_jwt** | **str** | Flex API Transient Token encoded as JWT (JSON Web Token), e.g. Flex microform or Unified Payment checkout result.  | [optional] 
**payment_instrument** | [**Ptsv2paymentsTokenInformationPaymentInstrument**](Ptsv2paymentsTokenInformationPaymentInstrument.md) |  | [optional] 
**shipping_address** | [**Ptsv2paymentsTokenInformationShippingAddress**](Ptsv2paymentsTokenInformationShippingAddress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


