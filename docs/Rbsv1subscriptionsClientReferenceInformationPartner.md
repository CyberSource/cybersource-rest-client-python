# Rbsv1subscriptionsClientReferenceInformationPartner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developer_id** | **str** | &gt; This field is ignored when you provide the &#x60;subscriptionInformation.originalTransactionId&#x60; or update the subscription.  Identifier for the developer that helped integrate a partner solution to CyberSource.  Send this value in all requests that are sent through the partner solutions built by that developer. CyberSource assigns the ID to the developer.  **Note** When you see a developer ID of 999 in reports, the developer ID that was submitted is incorrect.  | [optional] 
**solution_id** | **str** | &gt; This field is ignored when you provide the &#x60;subscriptionInformation.originalTransactionId&#x60; or update the subscription.  Identifier for the partner that is integrated to CyberSource.  Send this value in all requests that are sent through the partner solution. CyberSource assigns the ID to the partner.  **Note** When you see a solutionId of 999 in reports, the solutionId that was submitted is incorrect.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


