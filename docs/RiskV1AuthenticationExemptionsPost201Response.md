# RiskV1AuthenticationExemptionsPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PtsV2IncrementalAuthorizationPatch201ResponseLinks**](PtsV2IncrementalAuthorizationPatch201ResponseLinks.md) |  | [optional] 
**id** | **str** | An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; Example &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  | [optional] 
**status** | **str** | The status for authentication-exemptions 201. Value is: - AUTHENTICATION_EXEMPTIONS_SUCCESSFUL  | [optional] 
**risk_information** | [**RiskV1AuthenticationExemptionsPost201ResponseRiskInformation**](RiskV1AuthenticationExemptionsPost201ResponseRiskInformation.md) |  | [optional] 
**consumer_authentication_information** | [**RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation**](RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation.md) |  | [optional] 
**error_information** | [**PtsV2PaymentsPost201ResponseErrorInformation**](PtsV2PaymentsPost201ResponseErrorInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


