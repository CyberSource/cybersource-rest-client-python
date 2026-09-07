# UnifiedriskOrderShipping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | First line of the shipping address.Required field for authorization if any shipping address information is included in the request; otherwise, optional.#### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder&#39;s location when shipTo objects are not present. | [optional] 
**address_line2** | **str** | Second line of the shipping address.Optional field.#### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder&#39;s location when shipTo objects are not present. | [optional] 
**address_line3** | **str** | Third line of the shipping address.#### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder&#39;s location when shipTo objects are not present. | [optional] 
**administrative_area** | **str** | State or province of the shipping address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf) (maximum length: 2)   Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value   | [optional] 
**country** | **str** | Country of the shipping address. Use the two-character [ISO Standard Country Codes.] | [optional] 
**destination_types** | **str** | Shipping destination of item. Example: Commercial, Residential, Store | [optional] 
**locality** | **str** | City of the shipping address.Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.#### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder&#39;s location when shipTo objects are not present. | [optional] 
**first_name** | **str** | First name of the recipient.#### Litle Maximum length: 25#### All other processors Maximum length: 60Optional field. | [optional] 
**last_name** | **str** | Last name of the recipient.#### Litle Maximum length: 25#### All other processors Maximum length: 60Optional field. | [optional] 
**middle_name** | **str** | Middle name of the recipient.#### Litle Maximum length: 25#### All other processors Maximum length: 60Optional field. | [optional] 
**phone_number** | **str** | Phone number associated with the shipping address. | [optional] 
**postal_code** | **str** | Postal code for the shipping address. The postal code must consist of 5 to 9 digits.Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]Example 12345-6789When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][ | [optional] 
**destination_code** | **int** | Indicates destination chosen for the transaction. Possible values: - 01- Ship to cardholder billing address - 02- Ship to another verified address on file with merchant - 03- Ship to address that is different than billing address - 04- Ship to store (store address should be populated on request) - 05- Digital goods - 06- Travel and event tickets, not shipped - 07- Other | [optional] 
**delivery_type** | **str** | Delivery/fulfillment method  Possible values: - shipToHome - storePickup - lockerPickup - curbside | [optional] 
**gift_wrap** | **bool** | Boolean that indicates whether the customer requested gift wrapping for this purchase. This field can contain one of the following values: - true: The customer requested gift wrapping. - false: The customer did not request gift wrapping. | [optional] 
**shipping_method** | **str** | Shipping method for the product. Possible values:   - &#x60;lowcost&#x60;: Lowest-cost service  - &#x60;sameday&#x60;: Courier or same-day service  - &#x60;oneday&#x60;: Next-day or overnight service  - &#x60;twoday&#x60;: Two-day service   | [optional] 
**store** | [**UnifiedriskOrderShippingStore**](UnifiedriskOrderShippingStore.md) |  | [optional] 
**store_address** | [**UnifiedriskOrderShippingStoreAddress**](UnifiedriskOrderShippingStoreAddress.md) |  | [optional] 
**email** | **str** | Email address of the recipient or shipping contact for order confirmation, dispatch notifications, and delivery tracking | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


