# UnifiedriskPaymentVerificationAdditional

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** | Paper signature verification: SUCCESS, FAILURE     | [optional] 
**account_holder_auth** | **str** | Account holder authentication value: SUCCESS, FAILURE     | [optional] 
**authentication_token** | **str** | Authentication token verification: SUCCESS, FAILURE     | [optional] 
**cardholder_id_data** | **str** | Cardholder ID data verification: SUCCESS, FAILURE     | [optional] 
**passive_auth** | **str** | Passive authentication: SUCCESS, FAILURE     | [optional] 
**sim_swap** | **str** | SIM swap check: NO_SWAP_DETECTED, SWAP_DETECTED     | [optional] 
**secure_corp_payment_indicator** | **str** | Secure Corporate Payment Indicator (SCPI) flag assigned by the issuer to indicate a trusted commercial or corporate payment credential. Impacts SCA (Strong Customer Authentication) exemption eligibility under PSD2 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


