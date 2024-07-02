# Ptsv2payoutsRecipientInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of recipient. characters. * CTV (14) * Paymentech (30)  | [optional] 
**middle_name** | **str** | Recipient&#39;s middle name. This field is a _passthrough_, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  | [optional] 
**last_name** | **str** | Last name of recipient. characters. * CTV (14) * Paymentech (30)  | [optional] 
**address1** | **str** | Recipient address information. Required only for FDCCompass. | [optional] 
**locality** | **str** | Recipient city. Required only for FDCCompass. | [optional] 
**administrative_area** | **str** | Recipient State. Required only for FDCCompass. | [optional] 
**country** | **str** | Recipient country code. Required only for FDCCompass. | [optional] 
**postal_code** | **str** | Recipient postal code. Required only for FDCCompass. | [optional] 
**phone_number** | **str** | Recipient phone number. Required only for FDCCompass. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


