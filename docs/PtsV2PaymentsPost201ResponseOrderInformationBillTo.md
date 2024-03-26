# PtsV2PaymentsPost201ResponseOrderInformationBillTo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**address1** | **str** | First line of the billing street address.  | [optional] 
**address2** | **str** | Second line of the billing street address.  | [optional] 
**locality** | **str** | City of the billing address.  | [optional] 
**postal_code** | **str** | Postal code for the billing address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits] Example: 12345-6789 When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space] [numeric][alpha][numeric] Example: A1B 2C3  | [optional] 
**administrative_area** | **str** | State or province of the billing address. Use the State, Province, and Territory Codes for the United States and Canada.  | [optional] 
**country** | **str** | Country of the billing address. Use the two-character ISO Standard Country Codes.  | [optional] 
**email** | **str** | Email address of the customer.  | [optional] 
**alternate_phone_number_verification_status** | **str** | #### Visa Platform Connect Contains one of the following values that will identify the phone number result code in the account verification response message:  &#39;VERIFIED&#39; - Customer verified  &#39;UNVERIFIED&#39; - Customer not verified  &#39;FAILED&#39; - Customer verification failed  | [optional] 
**alternate_email_verification_status** | **str** | #### Visa Platform Connect Contains one of the following values that will identify the phone number result code in the account verification response message:  &#39;VERIFIED&#39; - Customer verified  &#39;UNVERIFIED&#39; - Customer not verified  &#39;FAILED&#39; - Customer verification failed  | [optional] 
**phone_number** | **str** | Customer&#39;s phone number.  It is recommended that you include the country code when the order is from outside the U.S.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Optional field.  #### Worldpay VAP Optional field.  #### All other processors Not used.  | [optional] 
**name_suffix** | **str** | Customer&#39;s name suffix.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


