# Tmsv2customersEmbeddedDefaultPaymentInstrumentCardTokenizedInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestor_id** | **str** | Value that identifies your business and indicates that the cardholder&#39;s account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider&#39;s database.  **Note** This field is supported only through **VisaNet** and **FDC Nashville Global**.  | [optional] 
**transaction_type** | **str** | Type of transaction that provided the token data. This value does not specify the token service provider; it specifies the entity that provided you with information about the token.  Set the value for this field to 1. An application on the customer&#39;s mobile device provided the token data.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


