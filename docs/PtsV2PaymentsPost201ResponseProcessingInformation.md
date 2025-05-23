# PtsV2PaymentsPost201ResponseProcessingInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_transfer_options** | [**PtsV2PaymentsPost201ResponseProcessingInformationBankTransferOptions**](PtsV2PaymentsPost201ResponseProcessingInformationBankTransferOptions.md) |  | [optional] 
**payment_solution** | **str** | Type of digital payment solution for the transaction. Possible Values:   - &#x60;visacheckout&#x60;: Visa Checkout. This value is required for Visa Checkout transactions. For details, see &#x60;payment_solution&#x60; field description in [Visa Checkout Using the REST API.](https://developer.cybersource.com/content/dam/docs/cybs/en-us/apifields/reference/all/rest/api-fields.pdf)  - &#x60;001&#x60;: Apple Pay.  - &#x60;004&#x60;: Cybersource In-App Solution.  - &#x60;005&#x60;: Masterpass. This value is required for Masterpass transactions on OmniPay Direct.   - &#x60;006&#x60;: Android Pay.  - &#x60;007&#x60;: Chase Pay.  - &#x60;008&#x60;: Samsung Pay.  - &#x60;012&#x60;: Google Pay.  - &#x60;013&#x60;: Cybersource P2PE Decryption  - &#x60;014&#x60;: Mastercard credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token.  - &#x60;015&#x60;: Visa credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token.  - &#x60;027&#x60;: Click to Pay.  | [optional] 
**enhanced_data_enabled** | **bool** | The possible values for the reply field are: - &#x60;true&#x60; : the airline data was included in the request to the processor. - &#x60;false&#x60; : the airline data was not included in the request to the processor.  Returned by authorization, capture, or credit services.  | [optional] 
**capture_options** | [**PtsV2PaymentsPost201ResponseProcessingInformationCaptureOptions**](PtsV2PaymentsPost201ResponseProcessingInformationCaptureOptions.md) |  | [optional] 
**authorization_options** | [**PtsV2PaymentsPost201ResponseProcessingInformationAuthorizationOptions**](PtsV2PaymentsPost201ResponseProcessingInformationAuthorizationOptions.md) |  | [optional] 
**purchase_options** | [**PtsV2PaymentsPost201ResponseProcessingInformationPurchaseOptions**](PtsV2PaymentsPost201ResponseProcessingInformationPurchaseOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


