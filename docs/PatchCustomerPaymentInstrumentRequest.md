# PatchCustomerPaymentInstrumentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentLinks**](Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentLinks.md) |  | [optional] 
**id** | **str** | The Id of the Payment Instrument Token. | [optional] 
**object** | **str** | The type.  Possible Values: - paymentInstrument  | [optional] 
**default** | **bool** | Flag that indicates whether customer payment instrument is the dafault. Possible Values:  - &#x60;true&#x60;: Payment instrument is customer&#39;s default.  - &#x60;false&#x60;: Payment instrument is not customer&#39;s default.  | [optional] 
**state** | **str** | Issuers state for the card number. Possible Values: - ACTIVE - CLOSED : The account has been closed.  | [optional] 
**type** | **str** | The type of Payment Instrument. Possible Values: - cardHash  | [optional] 
**bank_account** | [**Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentBankAccount**](Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentBankAccount.md) |  | [optional] 
**card** | [**Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentCard**](Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentCard.md) |  | [optional] 
**buyer_information** | [**Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentBuyerInformation**](Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentBuyerInformation.md) |  | [optional] 
**bill_to** | [**Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentBillTo**](Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentBillTo.md) |  | [optional] 
**processing_information** | [**TmsPaymentInstrumentProcessingInfo**](TmsPaymentInstrumentProcessingInfo.md) |  | [optional] 
**merchant_information** | [**TmsMerchantInformation**](TmsMerchantInformation.md) |  | [optional] 
**instrument_identifier** | [**Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentInstrumentIdentifier**](Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentInstrumentIdentifier.md) |  | [optional] 
**metadata** | [**Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentMetadata**](Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentMetadata.md) |  | [optional] 
**embedded** | [**Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentEmbedded**](Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentEmbedded.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


