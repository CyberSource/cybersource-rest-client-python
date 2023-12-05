# PaymentsProductsECheckConfigurationInformationConfigurationsFeaturesAccountValidationServiceProcessors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avs_account_ownership_service** | **bool** | *NEW* Determined in WF eTicket if account has opted into the Account Ownership Service. | [optional] 
**avs_account_status_service** | **bool** | *NEW* Determined in WF eTicket if account has opted into the Account Status Service. | [optional] 
**avs_signed_agreement** | **bool** | *NEW* Taken from Addendum Agreement Column in boarding form. | [optional] 
**avs_additional_id** | **str** | *NEW* Also known as the Additional ID. Taken from the boarding form. | [optional] 
**enable_avs** | **bool** | *NEW* | [optional] [default to True]
**avs_entity_id** | **str** | *NEW* Also known as the AVS Gateway Entity ID. | [optional] 
**enable_avs_token_creation** | **bool** | *NEW* Applicable if the merchant wants to run AVS on token creation requests only. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


