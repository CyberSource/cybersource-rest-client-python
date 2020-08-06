# TssV2TransactionsGet200Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  #### PIN debit Returned for all PIN debit services.  | [optional] 
**root_id** | **str** | Contains the transaction identifier for the first transaction in the series of transactions. For example, you might send an authorization request for a payment, followed by a capture request for that payment, and then a refund request for that captured payment. Each of those requests, if successful, creates a resource that is assigned an identifier, which is returned in the response. The rootId identifies the first ID in the series, which in this case would be the ID of the original authorization. | [optional] 
**reconciliation_id** | **str** | Reference number for the transaction. This value is not returned for all processors.  Returned by authorization service.  ##### PIN debit Returned by PIN debit credit, PIN debit purchase, and PIN debit reversal.  #### Atos Positive string (6)  #### All other processors String (60)  | [optional] 
**merchant_id** | **str** | Your CyberSource merchant ID. | [optional] 
**status** | **str** | The status of the submitted transaction. | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  Returned by authorization service.  #### PIN debit Time when the PIN debit credit, PIN debit purchase or PIN debit reversal was requested.  Returned by PIN debit credit, PIN debit purchase or PIN debit reversal.  | [optional] 
**application_information** | [**TssV2TransactionsGet200ResponseApplicationInformation**](TssV2TransactionsGet200ResponseApplicationInformation.md) |  | [optional] 
**buyer_information** | [**TssV2TransactionsGet200ResponseBuyerInformation**](TssV2TransactionsGet200ResponseBuyerInformation.md) |  | [optional] 
**client_reference_information** | [**TssV2TransactionsGet200ResponseClientReferenceInformation**](TssV2TransactionsGet200ResponseClientReferenceInformation.md) |  | [optional] 
**consumer_authentication_information** | [**TssV2TransactionsGet200ResponseConsumerAuthenticationInformation**](TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.md) |  | [optional] 
**device_information** | [**TssV2TransactionsGet200ResponseDeviceInformation**](TssV2TransactionsGet200ResponseDeviceInformation.md) |  | [optional] 
**error_information** | [**TssV2TransactionsGet200ResponseErrorInformation**](TssV2TransactionsGet200ResponseErrorInformation.md) |  | [optional] 
**installment_information** | [**TssV2TransactionsGet200ResponseInstallmentInformation**](TssV2TransactionsGet200ResponseInstallmentInformation.md) |  | [optional] 
**fraud_marking_information** | [**TssV2TransactionsGet200ResponseFraudMarkingInformation**](TssV2TransactionsGet200ResponseFraudMarkingInformation.md) |  | [optional] 
**merchant_defined_information** | [**list[Ptsv2paymentsMerchantDefinedInformation]**](Ptsv2paymentsMerchantDefinedInformation.md) | The object containing the custom data that the merchant defines.  | [optional] 
**merchant_information** | [**TssV2TransactionsGet200ResponseMerchantInformation**](TssV2TransactionsGet200ResponseMerchantInformation.md) |  | [optional] 
**order_information** | [**TssV2TransactionsGet200ResponseOrderInformation**](TssV2TransactionsGet200ResponseOrderInformation.md) |  | [optional] 
**payment_information** | [**TssV2TransactionsGet200ResponsePaymentInformation**](TssV2TransactionsGet200ResponsePaymentInformation.md) |  | [optional] 
**processing_information** | [**TssV2TransactionsGet200ResponseProcessingInformation**](TssV2TransactionsGet200ResponseProcessingInformation.md) |  | [optional] 
**processor_information** | [**TssV2TransactionsGet200ResponseProcessorInformation**](TssV2TransactionsGet200ResponseProcessorInformation.md) |  | [optional] 
**point_of_sale_information** | [**TssV2TransactionsGet200ResponsePointOfSaleInformation**](TssV2TransactionsGet200ResponsePointOfSaleInformation.md) |  | [optional] 
**risk_information** | [**TssV2TransactionsGet200ResponseRiskInformation**](TssV2TransactionsGet200ResponseRiskInformation.md) |  | [optional] 
**sender_information** | [**TssV2TransactionsGet200ResponseSenderInformation**](TssV2TransactionsGet200ResponseSenderInformation.md) |  | [optional] 
**links** | [**TssV2TransactionsGet200ResponseLinks**](TssV2TransactionsGet200ResponseLinks.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


