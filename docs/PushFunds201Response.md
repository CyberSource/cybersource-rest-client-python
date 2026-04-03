# PushFunds201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;  **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  | [optional] 
**status** | **str** | The status of the submitted transaction.  Possible values: - AUTHORIZED - DECLINED - SERVER_ERROR - INVALID_REQUEST - PARTIAL_AUTHORIZED  | [optional] 
**reconciliation_id** | **str** | Cybersource or merchant generated transaction reference number. This is sent to the processor and is echoed back in the response to the merchant. This is This value is used for reconciliation purposes.  | [optional] 
**client_reference_information** | [**PushFunds201ResponseClientReferenceInformation**](PushFunds201ResponseClientReferenceInformation.md) |  | [optional] 
**recipient_information** | [**PushFunds201ResponseRecipientInformation**](PushFunds201ResponseRecipientInformation.md) |  | [optional] 
**merchant_information** | [**PushFunds201ResponseMerchantInformation**](PushFunds201ResponseMerchantInformation.md) |  | [optional] 
**error_information** | [**PushFunds201ResponseErrorInformation**](PushFunds201ResponseErrorInformation.md) |  | [optional] 
**processor_information** | [**PushFunds201ResponseProcessorInformation**](PushFunds201ResponseProcessorInformation.md) |  | [optional] 
**order_information** | [**PushFunds201ResponseOrderInformation**](PushFunds201ResponseOrderInformation.md) |  | [optional] 
**payment_information** | [**PushFunds201ResponsePaymentInformation**](PushFunds201ResponsePaymentInformation.md) |  | [optional] 
**processing_information** | [**PushFunds201ResponseProcessingInformation**](PushFunds201ResponseProcessingInformation.md) |  | [optional] 
**links** | [**PushFunds201ResponseLinks**](PushFunds201ResponseLinks.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


