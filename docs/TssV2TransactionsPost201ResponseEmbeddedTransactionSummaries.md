# TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  #### PIN debit Returned for all PIN debit services.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  Returned by authorization service.  #### PIN debit Time when the PIN debit credit, PIN debit purchase or PIN debit reversal was requested.  Returned by PIN debit credit, PIN debit purchase or PIN debit reversal.  | [optional] 
**merchant_id** | **str** | Your CyberSource merchant ID. | [optional] 
**application_information** | [**TssV2TransactionsPost201ResponseEmbeddedApplicationInformation**](TssV2TransactionsPost201ResponseEmbeddedApplicationInformation.md) |  | [optional] 
**buyer_information** | [**TssV2TransactionsPost201ResponseEmbeddedBuyerInformation**](TssV2TransactionsPost201ResponseEmbeddedBuyerInformation.md) |  | [optional] 
**client_reference_information** | [**TssV2TransactionsPost201ResponseEmbeddedClientReferenceInformation**](TssV2TransactionsPost201ResponseEmbeddedClientReferenceInformation.md) |  | [optional] 
**consumer_authentication_information** | [**TssV2TransactionsPost201ResponseEmbeddedConsumerAuthenticationInformation**](TssV2TransactionsPost201ResponseEmbeddedConsumerAuthenticationInformation.md) |  | [optional] 
**device_information** | [**TssV2TransactionsPost201ResponseEmbeddedDeviceInformation**](TssV2TransactionsPost201ResponseEmbeddedDeviceInformation.md) |  | [optional] 
**fraud_marking_information** | [**TssV2TransactionsGet200ResponseFraudMarkingInformation**](TssV2TransactionsGet200ResponseFraudMarkingInformation.md) |  | [optional] 
**merchant_defined_information** | [**list[Ptsv2paymentsMerchantDefinedInformation]**](Ptsv2paymentsMerchantDefinedInformation.md) | The object containing the custom data that the merchant defines.  | [optional] 
**merchant_information** | [**TssV2TransactionsPost201ResponseEmbeddedMerchantInformation**](TssV2TransactionsPost201ResponseEmbeddedMerchantInformation.md) |  | [optional] 
**order_information** | [**TssV2TransactionsPost201ResponseEmbeddedOrderInformation**](TssV2TransactionsPost201ResponseEmbeddedOrderInformation.md) |  | [optional] 
**payment_information** | [**TssV2TransactionsPost201ResponseEmbeddedPaymentInformation**](TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.md) |  | [optional] 
**processing_information** | [**TssV2TransactionsPost201ResponseEmbeddedProcessingInformation**](TssV2TransactionsPost201ResponseEmbeddedProcessingInformation.md) |  | [optional] 
**processor_information** | [**TssV2TransactionsPost201ResponseEmbeddedProcessorInformation**](TssV2TransactionsPost201ResponseEmbeddedProcessorInformation.md) |  | [optional] 
**point_of_sale_information** | [**TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation**](TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.md) |  | [optional] 
**risk_information** | [**TssV2TransactionsPost201ResponseEmbeddedRiskInformation**](TssV2TransactionsPost201ResponseEmbeddedRiskInformation.md) |  | [optional] 
**links** | [**TssV2TransactionsPost201ResponseEmbeddedLinks**](TssV2TransactionsPost201ResponseEmbeddedLinks.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


