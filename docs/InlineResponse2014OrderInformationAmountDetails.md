# InlineResponse2014OrderInformationAmountDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_amount** | **str** | Amount that was authorized.  | [optional] 
**currency** | **str** | Currency used for the order. Use the three-character ISO Standard Currency Codes.  | [optional] 
**exchange_rate** | **str** | The rate of conversion of the currency given in the request.  | [optional] 
**total_amount** | **str** | Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  | [optional] 
**settlement_amount** | **str** | This is a multicurrency field. It contains the transaction amount, converted to the currency used to bill the cardholder&#39;s account.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


