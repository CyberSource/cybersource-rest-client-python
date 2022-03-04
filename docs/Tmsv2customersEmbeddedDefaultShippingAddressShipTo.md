# Tmsv2customersEmbeddedDefaultShippingAddressShipTo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the recipient.  | [optional] 
**last_name** | **str** | Last name of the recipient.  | [optional] 
**company** | **str** | Company associated with the shipping address.  | [optional] 
**address1** | **str** | First line of the shipping address.  | [optional] 
**address2** | **str** | Second line of the shipping address.  | [optional] 
**locality** | **str** | City of the shipping address.  | [optional] 
**administrative_area** | **str** | State or province of the shipping address. Use 2 character the State, Province, and Territory Codes for the United States and Canada.  | [optional] 
**postal_code** | **str** | Postal code for the shipping address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  **American Express Direct**\\ Before sending the postal code to the processor, CyberSource removes all nonalphanumeric characters and, if the remaining value is longer than nine characters, truncates the value starting from the right side.  | [optional] 
**country** | **str** | Country of the shipping address. Use the two-character ISO Standard Country Codes.  | [optional] 
**email** | **str** | Email associated with the shipping address.  | [optional] 
**phone_number** | **str** | Phone number associated with the shipping address.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


