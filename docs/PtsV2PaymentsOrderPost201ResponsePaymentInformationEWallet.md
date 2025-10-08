# PtsV2PaymentsOrderPost201ResponsePaymentInformationEWallet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer, passed in the return_url field by PayPal after customer approval. | [optional] 
**funding_source** | **str** | Payment mode for the authorization or order transaction.  INSTANT_TRANSFER  MANUAL_BANK_TRANSFER  DELAYED_TRANSFER  ECHECK  UNRESTRICTED (default)—this value is available only when configured by PayPal for the merchant. INSTANT | [optional] 
**funding_source_sale** | **str** | Payment method for the unit purchase. Possible values: - &#x60;UNRESTRICTED (default)—this value is only available if configured by PayPal for the merchant.&#x60; - &#x60;INSTANT&#x60;  | [optional] 
**user_name** | **str** | The Venmo user name chosen by the user, also known as a Venmo handle.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


