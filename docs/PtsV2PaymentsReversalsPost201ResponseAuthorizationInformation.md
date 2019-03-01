# PtsV2PaymentsReversalsPost201ResponseAuthorizationInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_code** | **str** | The authorization code returned by the processor. | [optional] 
**reason_code** | **str** | Reply flag for the original transaction. | [optional] 
**reversal_submitted** | **str** | Flag indicating whether a full authorization reversal was successfully submitted.  Possible values: - Y: The authorization reversal was successfully submitted. - N: The authorization reversal was not successfully submitted. You must send a credit request for a refund.  This field is supported only for **FDC Nashville Global**.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


