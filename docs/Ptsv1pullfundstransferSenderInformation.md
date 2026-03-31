# Ptsv1pullfundstransferSenderInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** | Sender&#39;s postal code. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.  | [optional] 
**first_name** | **str** | First name of sender. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.  | [optional] 
**middle_initial** | **str** | Middle Initial of sender  | [optional] 
**middle_name** | **str** | This field contains the middle name of the entity funding the transaction.  | [optional] 
**last_name** | **str** | Last name of sender. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.  | [optional] 
**address1** | **str** | Street address of sender. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.  | [optional] 
**address2** | **str** | Second line of the sender&#39;s address.  | [optional] 
**locality** | **str** | City of sender. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.  | [optional] 
**administrative_area** | **str** | Sender&#39;s state. Use the **State, Province, and Territory Codes for the United States and Canada**. This field is conditional: it is required if in the United States or Canada, and transaction is using neither a Customer nor Payment Instrument token.   Value must be an ISO Standard State Code: [https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf)  | [optional] 
**country** | **str** | Country of sender. Check that this field contains 2 character alpha ISO 3166-1 standard values. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.  | [optional] 
**payment_information** | [**Ptsv1pullfundstransferSenderInformationPaymentInformation**](Ptsv1pullfundstransferSenderInformationPaymentInformation.md) |  | [optional] 
**consumer_authentication** | [**Ptsv1pullfundstransferSenderInformationConsumerAuthentication**](Ptsv1pullfundstransferSenderInformationConsumerAuthentication.md) |  | [optional] 
**personal_identification** | [**Ptsv1pullfundstransferSenderInformationPersonalIdentification**](Ptsv1pullfundstransferSenderInformationPersonalIdentification.md) |  | [optional] 
**reference_number** | **str** | Visa Direct(16 characters)   If the transaction is a money transfer, pre-paid load, or credit card bill pay, and if the sender intends to fund the transaction with a non-financial instrument (for example, cash), a reference number unique to the sender is required.   If the transaction is a funds disbursement, the field is required.  | [optional] 
**account** | [**Ptsv1pullfundstransferSenderInformationAccount**](Ptsv1pullfundstransferSenderInformationAccount.md) |  | [optional] 
**alias_name** | **str** | Sender&#39;s alias name.  | [optional] 
**country_of_birth** | **str** | Account Owner Country of Birth.  | [optional] 
**date_of_birth** | **str** | Sender&#39;s date of birth. Format: YYYYMMDD.  | [optional] 
**email** | **str** | Account Owner email address  | [optional] 
**name** | **str** | Name of sender. Use this field if the sender is a business.  | [optional] 
**nationality** | **str** | Account Owner Nationality  | [optional] 
**occupation** | **str** | Account Owner Occupation.  | [optional] 
**phone_number** | **str** | Sender&#39;s phone number.  | [optional] 
**type** | **str** | This field identifies if the sender is a business or an individual.   The valid values are:   • &#x60;B&#x60; (Business)   • &#x60;I&#x60; (Individual)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


