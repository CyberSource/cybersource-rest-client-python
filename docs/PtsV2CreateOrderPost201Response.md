# PtsV2CreateOrderPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  Returned by Cybersource for all services.  | [optional] 
**update_time_utc** | **str** | The date and time when the request was last updated. **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.).  | [optional] 
**status** | **str** | The status of the submitted transaction. Possible values:   - CREATED   - SAVED   - APPROVED   - VOIDED   - COMPLETED   - PAYER_ACTION_REQUIRED  | [optional] 
**reconciliation_id** | **str** | Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response.  | [optional] 
**client_reference_information** | [**PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation**](PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation.md) |  | [optional] 
**processor_information** | [**PtsV2CreateOrderPost201ResponseProcessorInformation**](PtsV2CreateOrderPost201ResponseProcessorInformation.md) |  | [optional] 
**payment_information** | [**PtsV2PaymentsOrderPost201ResponsePaymentInformation**](PtsV2PaymentsOrderPost201ResponsePaymentInformation.md) |  | [optional] 
**buyer_information** | [**PtsV2CreateOrderPost201ResponseBuyerInformation**](PtsV2CreateOrderPost201ResponseBuyerInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


