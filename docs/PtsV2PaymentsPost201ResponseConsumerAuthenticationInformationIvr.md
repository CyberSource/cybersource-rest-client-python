# PtsV2PaymentsPost201ResponseConsumerAuthenticationInformationIvr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_message** | **bool** | Flag to indicate if a valid IVR transaction was detected.  | [optional] 
**encryption_key** | **str** | Encryption key to be used in the event the ACS requires encryption of the credential field.  | [optional] 
**encryption_mandatory** | **bool** | Flag to indicate if the ACS requires the credential to be encrypted.  | [optional] 
**encryption_type** | **str** | An indicator from the ACS to inform the type of encryption that should be used in the event the ACS requires encryption of the credential field.  | [optional] 
**label** | **str** | An ACS Provided label that can be presented to the Consumer. Recommended use with an application.  | [optional] 
**prompt** | **str** | An ACS provided string that can be presented to the Consumer. Recommended use with an application.  | [optional] 
**status_message** | **str** | An ACS provided message that can provide additional information or details.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


