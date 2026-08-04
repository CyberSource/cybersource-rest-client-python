# Ptsv2paymentsRecurringPaymentInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | The date after which no further recurring authorizations should be performed. Format: &#x60;YYYY-MM-DD&#x60; **Note** This field is required for recurring transactions.  | [optional] 
**frequency** | **int** | Integer value indicating the minimum number of days between recurring authorizations. A frequency of monthly is indicated by the value 28. Multiple of 28 days will be used to indicate months.  Example: 6 months &#x3D; 168  Example values accepted (31 days): - 31 - 031 - 0031  **Note** This field is required for recurring transactions.  | [optional] 
**number_of_payments** | **int** | Total number of payments for the duration of the recurring subscription.  | [optional] 
**original_purchase_date** | **str** | Date of original purchase. Required for recurring transactions. Format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; **Note**: If this field is empty, the current date is used.  | [optional] 
**sequence_number** | **int** | This field is mandatory for Cartes Bancaires recurring transactions on Credit Mutuel-CIC.       This field records recurring sequence, e.g. 1st for initial,  2 for subsequent, 3 etc  | [optional] 
**type** | **str** | This contains the type of recurring payment. Valid Values : 1 - Registration/First transaction 2 - Subsequent transaction 3 - Modification 4 - Cancellation  | [optional] 
**occurrence** | **str** | This value indicates how often a recurring payment occurs. Valid Values : • 01 (Daily) • 02 (Twice weekly) • 03 (Weekly) • 04 (Ten days) • 05 (Fortnightly) • 06 (Monthly) • 07 (Every two months) • 08 (Trimester) • 09 (Quarterly) • 10 (Twice yearly) • 11 (Annually) • 12 (Unscheduled)  | [optional] 
**validation_indicator** | **str** | This tag will contain a value that indicates whether or not the recurring payment transaction has been validated. Valid values : 0- Not validated 1- Validated  | [optional] 
**amount_type** | **str** | Indicates recurring amount type agreed by the cardholder Valid Values : 1- Fixed amount recurring payment 2- Recurring payment with maximum amount  | [optional] 
**maximum_amount** | **str** | This API field will contain the maximum amount agreed to by the cardholder. The currency of this amount will be specified in Field 49—Currency Code,Transaction.  | [optional] 
**reference_number** | **str** | This will contain a unique reference number for the recurring payment transaction.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


