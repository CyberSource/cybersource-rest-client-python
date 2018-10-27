# InlineResponse201

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InlineResponse201Links**](InlineResponse201Links.md) |  | [optional] 
**embedded** | [**InlineResponse201Embedded**](InlineResponse201Embedded.md) |  | [optional] 
**id** | **str** | An unique identification number assigned by CyberSource to identify the submitted request. | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. &#x60;Format: YYYY-MM-DDThh:mm:ssZ&#x60;  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**status** | **str** | The status of the submitted transaction. | [optional] 
**reconciliation_id** | **str** | The reconciliation id for the submitted transaction. This value is not returned for all processors.  | [optional] 
**error_information** | [**InlineResponse201ErrorInformation**](InlineResponse201ErrorInformation.md) |  | [optional] 
**client_reference_information** | [**InlineResponse201ClientReferenceInformation**](InlineResponse201ClientReferenceInformation.md) |  | [optional] 
**processor_information** | [**InlineResponse201ProcessorInformation**](InlineResponse201ProcessorInformation.md) |  | [optional] 
**payment_information** | [**InlineResponse201PaymentInformation**](InlineResponse201PaymentInformation.md) |  | [optional] 
**order_information** | [**InlineResponse201OrderInformation**](InlineResponse201OrderInformation.md) |  | [optional] 
**point_of_sale_information** | [**InlineResponse201PointOfSaleInformation**](InlineResponse201PointOfSaleInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


