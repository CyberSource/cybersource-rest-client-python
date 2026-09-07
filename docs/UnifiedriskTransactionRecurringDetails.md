# UnifiedriskTransactionRecurringDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | Days between recurring payments | [optional] 
**occurrence** | **str** | Recurring frequency code: DAILY, WEEKLY, MONTHLY, etc | [optional] 
**end_date** | **date** | Date when recurring payments end | [optional] 
**number_of_payments** | **int** | Total number of payments in recurring series | [optional] 
**sequence_number** | **int** | Current sequence number in recurring series | [optional] 
**type** | **str** | Recurring type: REGISTRATION, SUBSEQUENT, MODIFICATION, CANCELLATION | [optional] 
**validation_indicator** | **str** | Indicates if recurring payment was validated | [optional] 
**amount_type** | **str** | Amount type: FIXED, VARIABLE_WITH_MAX | [optional] 
**maximum_amount** | **float** | Maximum amount for variable recurring payments | [optional] 
**original_purchase_date** | **datetime** | Date of original recurring purchase | [optional] 
**reference_number** | **str** | Reference number for recurring payment | [optional] 
**first_payment_date** | **str** | Date of the first payment in a recurring series, in ISO 8601 format (YYYY-MM-DD). Used to establish the anchor date for recurring payment scheduling and risk assessment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


