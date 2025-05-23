# Ptsv1pushfundstransferSenderInformationPaymentInformationCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Three-digit value that indicates the card type.  IMPORTANT It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - &#x60;001&#x60;: Visa. For card-present transactions on all processors except SIX, the Visa Electron card type is processed the same way that the Visa debit card is processed. Use card type value 001 for Visa Electron. - &#x60;002&#x60;: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - &#x60;033&#x60;: Visa Electron - &#x60;024&#x60;: Maestro - &#x60;042&#x60;: Maestro International  | [optional] 
**security_code** | **str** | 3-digit value that indicates the card Cvv2Value. Values can be 0-9.  | [optional] 
**source_account_type** | **str** | Flag that specifies the type of account associated with the card. The cardholder provides this information during the payment process.  | [optional] 
**number** | **str** | The customer&#39;s payment card number, also known as the Primary Account Number (PAN).  | [optional] 
**expiration_month** | **str** | Two-digit month in which the payment card expires.  Format: MM.  Valid values: 01 through 12. Leading 0 is required.  | [optional] 
**expiration_year** | **str** | Four-digit year in which the payment card expires.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


