# PostTokenizedCardRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_reference_id** | **str** | An identifier provided by the issuer for the account. **Required when source is ISSUER.**  | [optional] 
**consumer_id** | **str** | Identifier of the consumer within the wallet. Maximum 24 characters for VTS. | [optional] 
**create_pan_instrument_identifier** | **bool** | Specifies whether the Instrument Identifier should be created (true) or not (false) with the PAN provided for the Network Token Provision request. Possible Values: - &#x60;true&#x60;: The InstrumentIdentifier should be created. - &#x60;false&#x60;: The InstrumentIdentifier should not be created.  | [optional] 
**source** | **str** | Source of the card details. Possible Values: - ONFILE - TOKEN - ISSUER  | 
**card** | [**Tmsv2tokenizedcardsCard**](Tmsv2tokenizedcardsCard.md) |  | [optional] 
**passcode** | [**Tmsv2tokenizedcardsPasscode**](Tmsv2tokenizedcardsPasscode.md) |  | [optional] 
**bill_to** | [**Tmsv2tokenizedcardsBillTo**](Tmsv2tokenizedcardsBillTo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


