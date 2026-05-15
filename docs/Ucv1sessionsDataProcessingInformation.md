# Ucv1sessionsDataProcessingInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reconciliation_id** | **str** | The reconciliation ID | [optional] 
**purpose_of_payment** | **str** | This field is applicable for AFT and OCT transactions.  For list of supported values, please refer to Developer Guide.  | [optional] 
**authorization_options** | [**Ucv1sessionsDataProcessingInformationAuthorizationOptions**](Ucv1sessionsDataProcessingInformationAuthorizationOptions.md) |  | [optional] 
**recurring_options** | [**Ucv1sessionsDataProcessingInformationRecurringOptions**](Ucv1sessionsDataProcessingInformationRecurringOptions.md) |  | [optional] 
**bank_transfer_options** | [**Ucv1sessionsDataProcessingInformationBankTransferOptions**](Ucv1sessionsDataProcessingInformationBankTransferOptions.md) |  | [optional] 
**business_application_id** | **str** | The business application Id&lt;br&gt;&lt;br&gt;  Optional field: This field cannot be configured through the Merchant Experience screens in the Business Center, but if required should be provided on a per‑transaction basis in the uc/v1/sessions API request.  | [optional] 
**commerce_indicator** | **str** | The commerce indicator&lt;br&gt;&lt;br&gt;  Optional field: This field cannot be configured through the Merchant Experience screens in the Business Center, but if required should be provided on a per‑transaction basis in the uc/v1/sessions API request.  | [optional] 
**processing_instruction** | **str** | The processing instruction&lt;br&gt;&lt;br&gt;  Optional field: This field cannot be configured through the Merchant Experience screens in the Business Center, but if required should be provided on a per‑transaction basis in the uc/v1/sessions API request.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


