# Ptsv2intentsProcessingInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processing_instruction** | **str** | The instruction to process an order. - default value: &#39;NO_INSTRUCTION&#39; - &#39;ORDER_SAVED_EXPLICITLY&#39;  | [optional] 
**authorization_options** | [**Ptsv2intentsProcessingInformationAuthorizationOptions**](Ptsv2intentsProcessingInformationAuthorizationOptions.md) |  | [optional] 
**action_list** | **list[str]** | Array of actions (one or more) to be included in the order to invoke bundled services along with order. Possible values: - &#x60;AP_ORDER&#x60;: Use this when Alternative Payment Order service is requested.  | [optional] 
**high_risk_transaction_flag** | **str** | Indicates if the transaction is flagged as high risk.  | [optional] 
**transaction_retry** | **str** | Indicates if the transaction is a retry.  | [optional] 
**last_one_hr_transaction_count** | **str** | The number of transactions in the last one hour.  | [optional] 
**last_one_day_transaction_count** | **str** | The number of transactions in the last one day.  | [optional] 
**last_three_months_txn_count** | **str** | The number of transactions in the last three months.  | [optional] 
**total_transaction_count** | **str** | The total number of transactions.  | [optional] 
**pin_verification** | **str** | Indicates if PIN verification is required.  | [optional] 
**face_id_verification** | **str** | Indicates if face ID verification is required.  | [optional] 
**user_passed_verification** | **str** | Indicates if the user passed verification.  | [optional] 
**ip_address** | **str** | The IP address of the user.  | [optional] 
**transaction_date** | **str** | The date of the transaction.  | [optional] 
**tangible** | **str** | Indicates if the transaction involves tangible goods.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


