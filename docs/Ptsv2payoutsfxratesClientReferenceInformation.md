# Ptsv2payoutsfxratesClientReferenceInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | The name of the Connection Method client (such as Virtual Terminal, Batch Upload, etc.) that submitted the payment transaction request to CyberSource.  | [optional] 
**application_version** | **str** | Version of the CyberSource application or integration used for a transaction.  | [optional] 
**application_user** | **str** | The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method.  | [optional] 
**code** | **str** | Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  | [optional] 
**partner** | [**Ptsv2payoutsfxratesClientReferenceInformationPartner**](Ptsv2payoutsfxratesClientReferenceInformationPartner.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


