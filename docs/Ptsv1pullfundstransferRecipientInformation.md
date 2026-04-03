# Ptsv1pullfundstransferRecipientInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_area** | **str** | Recipient&#39;s state. Use the State, Province, and Territory Codes for the United States and Canada. Value must be an ISO Standard State Code:  https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf  | [optional] 
**postal_code** | **str** | Recipient&#39;s postal code.  | [optional] 
**country** | **str** | Recipient&#39;s country code. Check that this field contains 2-character alpha ISO 3166-1 standard values.  | [optional] 
**personal_identification** | [**Ptsv1pullfundstransferRecipientInformationPersonalIdentification**](Ptsv1pullfundstransferRecipientInformationPersonalIdentification.md) |  | [optional] 
**first_name** | **str** | Recipient&#39;s first name.  | [optional] 
**middle_initial** | **str** | Middle Initial of recipient. This field is supported by FDC Compass.  | [optional] 
**middle_name** | **str** | Recipient&#39;s middle name. This field is a pass through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  | [optional] 
**last_name** | **str** | Recipient&#39;s last name. Conditional field. If &#x60;recipientInformation.sameAsSender&#x60; &#x3D; &#x60;false&#x60;, this field is mandatory.  | [optional] 
**address1** | **str** | Street address of recipient. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.  | [optional] 
**address2** | **str** | Second line of the recipient&#39;s address.  | [optional] 
**building_number** | **str** | This field contains the house or the building number of the recipient address.  | [optional] 
**locality** | **str** | Recipient city.  | [optional] 
**identification_number** | **str** | Government-issued identification number.  Conditional: This field is mandatory if the &#x60;processingInformation.businessApplicationId&#x60; is any of the following:   - &#x60;AA&#x60; - &#x60;PP&#x60; - &#x60;TU&#x60; - &#x60;BI&#x60; - &#x60;WT&#x60; - &#x60;FT&#x60; - and country code &#x3D; &#x60;BR&#x60;, &#x60;AR&#x60;, &#x60;CO&#x60;, &#x60;PE&#x60;, in &#x60;recipientInformation.countryCode&#x60; (Argentina, Brazil, Colombia, and Peru)  | [optional] 
**type** | **str** | &#x60;B&#x60; for Business or &#x60;I&#x60; for individual.  Conditional:  If &#x60;recipientInformation.identificationNumber&#x60; is present, then this field is mandatory.  | [optional] 
**descriptor** | **str** | Recipient first name, this will be concatenated with the 4-digit originator abbreviation.  | [optional] 
**account_id** | **str** | Identifier for the recipient&#39;s account.  | [optional] 
**account_type** | **str** | Identifies the recipient&#39;s account type. This field is applicable for AFT transactions.  Valid values are:  - &#x60;00&#x60; Other - &#x60;01&#x60; Routing transit number (RTN) and bank account - &#x60;02&#x60; IBAN - &#x60;03&#x60; Card account - &#x60;04&#x60; Email - &#x60;05&#x60; Phone number - &#x60;06&#x60; Bank account number (BAN) and bank identification code (BIC) - &#x60;07&#x60; Wallet ID - &#x60;08&#x60; Social network ID  | [optional] 
**alias_name** | **str** | Account owner alias name.  | [optional] 
**country_of_birth** | **str** | Account Owner Country of Birth  | [optional] 
**date_of_birth** | **str** | Recipient&#39;s date of birth. Format: YYYYMMDD.  | [optional] 
**email** | **str** | Account Owner email address  | [optional] 
**nationality** | **str** | Account Owner Nationality  | [optional] 
**occupation** | **str** | Account Owner Occupation  | [optional] 
**street_name** | **str** | This field contains the street name of the recipient&#39;s address.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


