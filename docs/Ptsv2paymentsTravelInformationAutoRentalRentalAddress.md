# Ptsv2paymentsTravelInformationAutoRentalRentalAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City in which the auto was rented.  For authorizations, this field is supported for Visa, MasterCard, and American Express.  For captures, this field is supported only for American Express.  For all other card types, this field is ignored.  | [optional] 
**state** | **str** | State in which the auto was rented. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  | [optional] 
**country** | **str** | Country where the auto was rented. Use the [ISO Standard Country Codes.](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) This field is supported only for American Express.  | [optional] 
**location_id** | **str** | The agency code, address, phone number, etc., used to identify the location where the vehicle was rented.  | [optional] 
**address1** | **str** | Address from where the vehicle was rented.  | [optional] 
**address2** | **str** | Address from where the vehicle was rented.  | [optional] 
**postal_code** | **str** | When merchant wants to send the rental address&#39;s postal code.  | [optional] 
**location** | **str** | This field contains the location where a taxi passenger was picked up or where an auto rental vehicle was picked up. In most cases, this is the rental agency&#39;s business name that appears on the storefront and/or customer receipts, commonly referred to as the DBA (Doing Business As) name. However, if the vehicle was picked up at another location (e.g., a hotel,auto dealership, repair shop, etc.), the name of that location should be used. This entry must be easily recognized by the Cardmember to avoid unnecessary inquiries. If the name is more than 38  characters, use proper and meaningful abbreviation, when possible.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


