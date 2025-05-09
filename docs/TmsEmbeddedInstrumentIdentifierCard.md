# TmsEmbeddedInstrumentIdentifierCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | The customer&#39;s payment card number, also known as the Primary Account Number (PAN). You can also use this field for encoded account numbers.  | [optional] 
**expiration_month** | **str** | Two-digit month in which the payment card expires.  Format: &#x60;MM&#x60;.  Possible Values: &#x60;01&#x60; through &#x60;12&#x60;.  | [optional] 
**expiration_year** | **str** | Four-digit year in which the credit card expires.  Format: &#x60;YYYY&#x60;.  | [optional] 
**security_code** | **str** | Card Verification Code.  This value is sent to the issuer to support the approval of a network token provision. It is not persisted against the Instrument Identifier.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


