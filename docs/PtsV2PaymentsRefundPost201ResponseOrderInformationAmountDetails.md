# PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_amount** | **str** | This is a multicurrency field. It contains the transaction amount (field 4), converted to the Currency used to bill the cardholder&#39;s account. This field is returned for OCT transactions.  | [optional] 
**settlement_currency** | **str** | This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder&#39;s account. This field is returned for OCT transactions.  | [optional] 
**exchange_rate** | **str** | Exchange rate returned by the DCC service. Includes a decimal point and a maximum of 4 decimal places.  For details, see &#x60;exchange_rate&#x60; request-level field description in the [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf)  | [optional] 
**foreign_amount** | **str** | Set this field to the converted amount that was returned by the DCC provider. For processor-specific information, see the &#x60;foreign_amount&#x60; field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  | [optional] 
**foreign_currency** | **str** | Set this field to the converted amount that was returned by the DCC provider.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


