# Ptsv1pushfundstransferRecipientInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_information** | [**Ptsv1pushfundstransferRecipientInformationPaymentInformation**](Ptsv1pushfundstransferRecipientInformationPaymentInformation.md) |  | [optional] 
**address1** | **str** | First line of the recipient&#39;s address. Required for card payments  | [optional] 
**address2** | **str** | Second line of the recipient&#39;s address  | [optional] 
**locality** | **str** | Recipient city.  | [optional] 
**postal_code** | **str** | Recipient postal code.   For USA, this must be a valid value of 5 digits or 5 digits hyphen 4 digits, for example &#39;63368&#39;, &#39;63368-5555&#39;. For other regions, this can be alphanumeric, length 1-10.  Mandatory for card payments.  | [optional] 
**administrative_area** | **str** | The recipient&#39;s province, state or territory. Conditional, required if recipient&#39;s country is USA or CAN. Must be an ISO 3166-2 uppercase alpha 2 or 3 character country subdivision code. For example, Missouri is MO.  See https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf  Required for card payments.  | [optional] 
**country** | **str** | Recipient country code. Use the ISO Standard Alpha Country Codes.  https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf  | [optional] 
**first_name** | **str** | First name of recipient.  | [optional] 
**middle_name** | **str** | Sender&#39;s middle name. This field is a passthrough, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  | [optional] 
**last_name** | **str** | Last name of recipient.  | [optional] 
**phone_number** | **str** | Recipient phone number.  This field is supported by FDC Compass.  Mastercard Send: Max length is 15 with no dashes or spaces.  | [optional] 
**personal_identification** | [**Ptsv1pushfundstransferRecipientInformationPersonalIdentification**](Ptsv1pushfundstransferRecipientInformationPersonalIdentification.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


