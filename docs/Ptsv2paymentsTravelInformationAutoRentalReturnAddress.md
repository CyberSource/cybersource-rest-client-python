# Ptsv2paymentsTravelInformationAutoRentalReturnAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City where the auto was returned to the rental agency.  | [optional] 
**state** | **str** | State in which the auto was returned to the rental agency. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  For authorizations, this field is supported for Visa, MasterCard, and American Express.  For captures, this field is supported only for MasterCard and American Express.  | [optional] 
**country** | **str** | Country where the auto was returned to the rental agency. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  | [optional] 
**location_id** | **str** | Code, address, phone number, etc. used to identify the location of the auto rental return. This field is supported only for MasterCard and American Express.  | [optional] 
**address1** | **str** | When merchant wants to send the rental address&#39;s street address.  | [optional] 
**postal_code** | **str** | When merchant wants to send the return address&#39;s postal code.  | [optional] 
**location** | **str** | This field contains the location where the taxi passenger was dropped off or where the auto rental vehicle was returned.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


