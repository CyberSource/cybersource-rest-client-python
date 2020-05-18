# TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field.  | [optional] 
**last_name** | **str** | Last name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field.  | [optional] 
**address1** | **str** | First line of the shipping address.  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  | [optional] 
**country** | **str** | Country of the shipping address. Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  | [optional] 
**phone_number** | **str** | Phone number associated with the shipping address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


