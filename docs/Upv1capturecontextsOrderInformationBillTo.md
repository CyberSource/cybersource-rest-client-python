# Upv1capturecontextsOrderInformationBillTo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Payment card billing street address as it appears on the credit card issuer’s records.  | [optional] 
**address2** | **str** | Used for additional address information. For example: _Attention: Accounts Payable_ Optional field.  | [optional] 
**address3** | **str** | Additional address information (third line of the billing address) | [optional] 
**address4** | **str** | Additional address information (fourth line of the billing address)  | [optional] 
**administrative_area** | **str** | State or province of the billing address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  | [optional] 
**building_number** | **str** | Building number in the street address.  | [optional] 
**country** | **str** | Payment card billing country. Use the two-character [ISO Standard Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  | [optional] 
**district** | **str** | Customer’s neighborhood, community, or region (a barrio in Brazil) within the city or municipality  | [optional] 
**locality** | **str** | Payment card billing city.  | [optional] 
**postal_code** | **str** | Postal code for the billing address. The postal code must consist of 5 to 9 digits.  | [optional] 
**company** | [**Upv1capturecontextsOrderInformationBillToCompany**](Upv1capturecontextsOrderInformationBillToCompany.md) |  | [optional] 
**email** | **str** | Customer&#39;s email address, including the full domain name.  | [optional] 
**first_name** | **str** | Customer’s first name. This name must be the same as the name on the card | [optional] 
**last_name** | **str** | Customer’s last name. This name must be the same as the name on the card.  | [optional] 
**middle_name** | **str** | Customer’s middle name.  | [optional] 
**name_suffix** | **str** | Customer’s name suffix.  | [optional] 
**title** | **str** | Title.  | [optional] 
**phone_number** | **str** | Customer’s phone number.  | [optional] 
**phone_type** | **str** | Customer&#39;s phone number type.  #### For Payouts: This field may be sent only for FDC Compass.  Possible Values: * day * home * night * work  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


