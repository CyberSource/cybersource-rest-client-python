# RiskV1AuthenticationsPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PtsV2IncrementalAuthorizationPatch201ResponseLinks**](PtsV2IncrementalAuthorizationPatch201ResponseLinks.md) |  | [optional] 
**id** | **str** | An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; Example &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  | [optional] 
**submit_time_local** | **str** | Time that the transaction was submitted in local time. | [optional] 
**status** | **str** | The status for payerAuthentication 201 enroll and validate calls. Possible values are: - AUTHENTICATION_SUCCESSFUL - PENDING_AUTHENTICATION  | [optional] 
**reason** | **str** | The reason of the status. Possible values are: - Authentication_Completed_Or_Skipped_Sucessfully - Pending_Authentication  | [optional] 
**message** | **str** | The message describing the reason of the status. Value is: - The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction.  | [optional] 
**client_reference_information** | [**PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation**](PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation.md) |  | [optional] 
**order_information** | [**RiskV1AuthenticationsPost201ResponseOrderInformation**](RiskV1AuthenticationsPost201ResponseOrderInformation.md) |  | [optional] 
**consumer_authentication_information** | [**RiskV1AuthenticationsPost201ResponseConsumerAuthenticationInformation**](RiskV1AuthenticationsPost201ResponseConsumerAuthenticationInformation.md) |  | [optional] 
**error_information** | [**PtsV2PaymentsPost201ResponseErrorInformation**](PtsV2PaymentsPost201ResponseErrorInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


