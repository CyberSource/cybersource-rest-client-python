# Ptsv2paymentsidcapturesProcessingInformationJapanPaymentOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | This value is a 2-digit code indicating the payment method. Use Payment Method Code value that applies to the tranasction. - 10 (One-time payment) - 21, 22, 23, 24  (Bonus(one-time)payment) - 61 (Installment payment) - 31, 32, 33, 34  (Integrated (Bonus + Installment)payment) - 80 (Revolving payment)  | [optional] 
**bonuses** | **str** | Field contains the number of bonuses.  | [optional] 
**installments** | **str** | Number of Installments.  | [optional] 
**first_billing_month** | **str** | Billing month in MM format.  | [optional] 
**bonus_amount** | **str** | This field contains the bonus amount.  | [optional] 
**bonus_month** | **str** | This field contains the Japan specific first bonus month.  | [optional] 
**second_bonus_amount** | **str** | Field contains the second bonus amount.  | [optional] 
**second_bonus_month** | **str** | Field contains the Japan specific second bonus month.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


