# Iccv1checkoutsessionsPaymentInstruments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Client-assigned instrument identifier. | [optional] 
**type** | **str** | Payment method type (e.g. &#x60;card&#x60;, &#x60;wallet&#x60;). | [optional] 
**handler_id** | **str** | Payment handler or processor identifier (e.g. &#x60;visa&#x60;). | [optional] 
**handler_name** | **str** | Human-readable name of the payment handler. | [optional] 
**brand** | **str** | Card brand (e.g. &#x60;visa&#x60;, &#x60;mastercard&#x60;). | [optional] 
**last_digits** | **str** | Last 4 digits of the card number for display purposes. | [optional] 
**token** | **str** | Opaque payment token from the payment provider. | [optional] 
**credential** | [**Iccv1checkoutsessionsPaymentCredential**](Iccv1checkoutsessionsPaymentCredential.md) |  | [optional] 
**billing_address** | [**Iccv1checkoutsessionsPaymentBillingAddress**](Iccv1checkoutsessionsPaymentBillingAddress.md) |  | [optional] 
**selected** | **bool** | Whether this instrument is selected for the current session. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


