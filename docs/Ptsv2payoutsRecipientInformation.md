# Ptsv2payoutsRecipientInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the recipient.    This field is applicable for AFT &amp; OCT transactions.  Only alpha numeric values are supported. Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to sent to the processor.  | [optional] 
**middle_name** | **str** | Middle name of the recipient.    This field is applicable for AFT &amp; OCT transactions.  Only alpha numeric values are supported. Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to sent to the processor.  | [optional] 
**last_name** | **str** | Last name of the recipient.  This field is applicable for AFT &amp; OCT transactions.  Only alpha numeric values are supported. Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to sent to the processor.  | [optional] 
**address1** | **str** | The street address of the recipient This field is applicable for AFT and OCT transactions.  Only alpha numeric values are supported. Special characters not in the standard ASCII character set are not supported and will be stripped before being sent to sent to the processor.  | [optional] 
**locality** | **str** | The city of the recipient. This field is applicable for AFT and OCT transactions.  Only alpha numeric values are supported. Special characters not in the standard ASCII character set are not supported and will be stripped before being sent to sent to the processor.  | [optional] 
**administrative_area** | **str** | The state or province of the recipient. This field is applicable for AFT and OCT transactions when the recipient country is US or CA. Else it is optional.  Must be a two character value  | [optional] 
**country** | **str** | The country associated with the address of the recipient. This field is applicable for AFT and OCT transactions.  Must be a two character ISO country code.  For example, see [ISO Country Code](https://developer.cybersource.com/docs/cybs/en-us/country-codes/reference/all/na/country-codes/country-codes.html)  | [optional] 
**postal_code** | **str** | Recipient postal code. Required only for FDCCompass. | [optional] 
**phone_number** | **str** | Recipient phone number. Required only for FDCCompass. | [optional] 
**alias_name** | **str** | Account owner alias name.  | [optional] 
**nationality** | **str** | Account Owner Nationality | [optional] 
**country_of_birth** | **str** | Account Owner Country of Birth | [optional] 
**occupation** | **str** | Account Owner Occupation | [optional] 
**email** | **str** | Account Owner email address | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


