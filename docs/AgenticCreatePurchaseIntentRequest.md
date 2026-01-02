# AgenticCreatePurchaseIntentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_correlation_id** | **str** | Client Correlation Id used during the tokenization or during FIDO assertion. | 
**payment_information** | [**Acpv1tokensPaymentInformation**](Acpv1tokensPaymentInformation.md) |  | 
**device_information** | [**Acpv1tokensDeviceInformation**](Acpv1tokensDeviceInformation.md) |  | 
**assurance_data** | [**list[Acpv1tokensAssuranceData]**](Acpv1tokensAssuranceData.md) | Assurance data. | 
**mandates** | [**list[Acpv1instructionsMandates]**](Acpv1instructionsMandates.md) | Mandate data. | 
**buyer_information** | [**Acpv1tokensBuyerInformation**](Acpv1tokensBuyerInformation.md) |  | [optional] 
**is_recurring** | **bool** | Indicates whether the transaction is recurring. Default value is false. | [optional] 
**consumer_prompt** | **str** | Recap - A summary or condensed version of user prompts that leads to the purchase. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


