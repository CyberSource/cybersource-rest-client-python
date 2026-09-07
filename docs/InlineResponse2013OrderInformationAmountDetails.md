# InlineResponse2013OrderInformationAmountDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**markup_rate** | **str** | The markup between the offer exchange rate and wholesale rates, i.e. the mark up. Expressed as a percentage of 100, e.g. 3.75.  If the markup value is not supplied in the API, and the Acquiring BIN is provided, the markup configured during onboarding will be picked up and applied to the transaction. To override any markup defaults set up on the account, always send a markup value of 0.00 to indicate 0% markup.   Supported by Visa Direct.  | [optional] 
**exchange_rate** | **str** | Exchange rate returned by the card network. | [optional] 
**original_amount** | **str** | Amount in your original local pricing currency.  This value cannot be negative. You can include a decimal point (.) in this field to denote the currency exponent, but you cannot include any other special characters.  If needed, CyberSource truncates the amount to the correct number of decimal places.  | [optional] 
**destination_amount** | **str** | Amount in your destination&#39;s local pricing currency.  This value cannot be negative. You can include a decimal point (.) in this field to denote the currency exponent, but you cannot include any other special characters.  If needed, CyberSource truncates the amount to the correct number of decimal places.  | [optional] 
**original_amount_without_markup** | **str** | Original Transaction Amount excluding markup in source currency. This field will be returned in a source-to-destination inquiry response when markup is applicable.  Supported by Visa Direct  | [optional] 
**settlement_amount** | **str** | The transaction amount in settlement currency. | [optional] 
**settlement_currency** | **str** | The currency in which Visa or Mastercard settles with the acquirer/acquirer.  Use [ISO 4217 3-Alpha Currency Codes](https://developer.cybersource.com/content/dam/docs/cybs/en-us/currency-codes/reference/all/na/currency-codes.pdf).  | [optional] 
**settlement_exchange_rate** | **str** | Exchange rate returned by the card network for settlement. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


