# Ptsv2paymentreferencesBuyerInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_birth** | **str** | Recipient&#39;s date of birth. **Format**: &#x60;YYYYMMDD&#x60;.  This field is a &#x60;pass-through&#x60;, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  | [optional] 
**gender** | **str** | Customer&#39;s gender. Possible values are F (female), M (male),O (other). | [optional] 
**language** | **str** | language setting of the user.  Supports 2-character language codes (e.g., en, fr) and 5-character locale values (e.g., en-US, fr-CA).  | [optional] 
**note_to_seller** | **str** | Note to the recipient of the funds in this transaction | [optional] 
**personal_identification** | [**list[Ptsv2paymentsidcapturesBuyerInformationPersonalIdentification]**](Ptsv2paymentsidcapturesBuyerInformationPersonalIdentification.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


