# Ptsv2paymentsProcessingInformationJapanPaymentOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | This value is a 2-digit code indicating the payment method. Use Payment Method Code value that applies to the tranasction. - 10 (One-time payment) - 21, 22, 23, 24  (Bonus(one-time)payment) - 61 (Installment payment) - 31, 32, 33, 34  (Integrated (Bonus + Installment)payment) - 80 (Revolving payment)  | [optional] 
**installments** | **str** | Number of Installments.  | [optional] 
**terminal_id** | **str** | This value is the 13-digit JCCA number. | [optional] 
**first_billing_month** | **str** | Billing month in MM format.  | [optional] 
**business_name** | **str** | Business name in Japanese characters. This field is supported only on JCN Gateway and for the Sumitomo Mitsui Card Co. acquirer on CyberSource through VisaNet.  | [optional] 
**business_name_katakana** | **str** | Business name in Katakana characters. This field is supported only on JCN Gateway and for the Sumitomo Mitsui Card Co. acquirer on CyberSource through VisaNet.  | [optional] 
**jis2_track_data** | **str** | Japanese Industrial Standard Type 2 (JIS2) track data from the front of the card. This field is supported only on JCN Gateway.  | [optional] 
**business_name_alpha_numeric** | **str** | Business name in alphanumeric characters. This field is supported only on JCN Gateway and for the Sumitomo Mitsui Card Co. acquirer on CyberSource through VisaNet.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


