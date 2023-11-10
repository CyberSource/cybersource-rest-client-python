# TssV2TransactionsGet200ResponseTokenInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**PtsV2PaymentsPost201ResponseTokenInformationCustomer**](PtsV2PaymentsPost201ResponseTokenInformationCustomer.md) |  | [optional] 
**payment_instrument** | [**PtsV2PaymentsPost201ResponseTokenInformationPaymentInstrument**](PtsV2PaymentsPost201ResponseTokenInformationPaymentInstrument.md) |  | [optional] 
**shipping_address** | [**PtsV2PaymentsPost201ResponseTokenInformationShippingAddress**](PtsV2PaymentsPost201ResponseTokenInformationShippingAddress.md) |  | [optional] 
**instrument_identifier** | [**TssV2TransactionsGet200ResponsePaymentInformationInstrumentIdentifier**](TssV2TransactionsGet200ResponsePaymentInformationInstrumentIdentifier.md) |  | [optional] 
**jti** | **str** | TMS Transient Token, 64 hexadecimal id value representing captured payment credentials (including Sensitive Authentication Data, e.g. CVV).  | [optional] 
**transient_token_jwt** | **str** | Flex API Transient Token encoded as JWT (JSON Web Token), e.g. Flex microform or Unified Payment checkout result.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


