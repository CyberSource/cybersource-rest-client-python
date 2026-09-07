# VpriRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **list[str]** | Actions to perform. For VPRI, specify VISA_PROTECT_RISK_INSIGHTS. Multiple actions may be included in a single request to invoke additional services simultaneously. | 
**events** | **list[str]** | The events to be performed under specific actions. For VISA_PROTECT_RISK_INSIGHTS, supported values are LABELS and INSIGHTS. | 
**transaction** | [**UnifiedriskTransaction**](UnifiedriskTransaction.md) |  | 
**request_id** | **str** | Unique identifier for the risk assessment request | [optional] 
**event_time** | **datetime** | The time that the real-world event occurred. | 
**context** | **str** | The context in which the request is made. | [optional] 
**mode** | **str** | Indicates whether the request is live or a test. | [optional] 
**request_comments** | **str** | Brief description or comments about the request | [optional] 
**schema_version** | **int** | Version of the request schema | [optional] 
**partner** | [**UnifiedriskPartner**](UnifiedriskPartner.md) |  | [optional] 
**payment** | [**UnifiedriskPayment**](UnifiedriskPayment.md) |  | [optional] 
**order** | [**UnifiedriskOrder**](UnifiedriskOrder.md) |  | [optional] 
**customer** | [**UnifiedriskCustomer**](UnifiedriskCustomer.md) |  | [optional] 
**risk_assessment** | [**UnifiedriskRiskAssessment**](UnifiedriskRiskAssessment.md) |  | [optional] 
**travel** | [**UnifiedriskTravel**](UnifiedriskTravel.md) |  | [optional] 
**merchant** | [**UnifiedriskMerchant**](UnifiedriskMerchant.md) |  | [optional] 
**acquirer** | [**UnifiedriskAcquirer**](UnifiedriskAcquirer.md) |  | [optional] 
**device** | [**UnifiedriskDevice**](UnifiedriskDevice.md) |  | [optional] 
**session** | [**UnifiedriskSession**](UnifiedriskSession.md) |  | [optional] 
**supplementary_data** | **str** | Free-form field for information not catered for by other components. Must not contain cardholder data or sensitive auth data. | [optional] 
**labels** | [**UnifiedriskLabels**](UnifiedriskLabels.md) |  | [optional] 
**account** | [**UnifiedriskAccount**](UnifiedriskAccount.md) |  | [optional] 
**authentication** | [**UnifiedriskAuthentication**](UnifiedriskAuthentication.md) |  | [optional] 
**authorization** | [**UnifiedriskAuthorization**](UnifiedriskAuthorization.md) |  | [optional] 
**browser** | [**UnifiedriskBrowser**](UnifiedriskBrowser.md) |  | [optional] 
**initiating_party** | [**UnifiedriskInitiatingParty**](UnifiedriskInitiatingParty.md) |  | [optional] 
**terminal** | [**UnifiedriskTerminal**](UnifiedriskTerminal.md) |  | [optional] 
**third_party_risk** | [**UnifiedriskThirdPartyRisk**](UnifiedriskThirdPartyRisk.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


