# Ptsv1pushfundstransferOrderInformationAmountDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **str** | Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  Note For VPC, FDCCompass, Paymentech, Visa Direct, and Mastercard Send processors, the maximum supported numeric characters is 12.  Important Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths.  For zero dollar authorizations, this field may set to 0.00. Zero dollar authorizations are used for account validation only and do not place a hold or move funds.  | 
**currency** | **str** | Use a 3-character alpha currency code for currency of the funds transfer.  ISO standard currencies: http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf  Currency must be supported by the processor.  | 
**source_currency** | **str** | Use a 3-character alpha currency code for source currency of the funds transfer. Supported for card and bank account based cross border funds transfers.  ISO standard currencies: http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf  | [optional] 
**destination_currency** | **str** | Use a 3-character alpha currency code for destination currency of the funds transfer. Supported for card and bank account based cross border funds transfers.  ISO standard currencies: http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf  | [optional] 
**surcharge** | [**Ptsv2paymentsOrderInformationAmountDetailsOctsurcharge**](Ptsv2paymentsOrderInformationAmountDetailsOctsurcharge.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


