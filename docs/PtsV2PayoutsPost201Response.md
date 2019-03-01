# PtsV2PayoutsPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PtsV2PaymentsReversalsPost201ResponseLinks**](PtsV2PaymentsReversalsPost201ResponseLinks.md) |  | [optional] 
**id** | **str** | An unique identification number assigned by CyberSource to identify the submitted request. | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. &#x60;Format: YYYY-MM-DDThh:mm:ssZ&#x60;  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**status** | **str** | The status of the submitted transaction. | [optional] 
**reconciliation_id** | **str** | Cybersource or merchant generated transaction reference number. This is sent to the processor and is echoed back in the response to the merchant. This is This value is used for reconciliation purposes.  | [optional] 
**status_information** | [**PtsV2PayoutsPost201ResponseStatusInformation**](PtsV2PayoutsPost201ResponseStatusInformation.md) |  | [optional] 
**error_information** | [**PtsV2PayoutsPost201ResponseErrorInformation**](PtsV2PayoutsPost201ResponseErrorInformation.md) |  | [optional] 
**client_reference_information** | [**Ptsv2payoutsClientReferenceInformation**](Ptsv2payoutsClientReferenceInformation.md) |  | [optional] 
**merchant_information** | [**PtsV2PayoutsPost201ResponseMerchantInformation**](PtsV2PayoutsPost201ResponseMerchantInformation.md) |  | [optional] 
**order_information** | [**PtsV2PayoutsPost201ResponseOrderInformation**](PtsV2PayoutsPost201ResponseOrderInformation.md) |  | [optional] 
**processor_information** | [**PtsV2PayoutsPost201ResponseProcessorInformation**](PtsV2PayoutsPost201ResponseProcessorInformation.md) |  | [optional] 
**recipient_information** | [**PtsV2PayoutsPost201ResponseRecipientInformation**](PtsV2PayoutsPost201ResponseRecipientInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


