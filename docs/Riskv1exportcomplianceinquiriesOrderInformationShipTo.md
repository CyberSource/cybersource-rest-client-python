# Riskv1exportcomplianceinquiriesOrderInformationShipTo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country of the shipping address. Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. Billing address objects will be used to determine the cardholder&#39;s location when shipTo objects are not present.  | [optional] 
**first_name** | **str** | First name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field.  | [optional] 
**last_name** | **str** | Last name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


