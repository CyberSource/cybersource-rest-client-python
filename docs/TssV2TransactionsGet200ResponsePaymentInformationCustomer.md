# TssV2TransactionsGet200ResponsePaymentInformationCustomer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Unique identifier for the customer&#39;s card and billing information.  When you use Payment Tokenization or Recurring Billing and you include this value in your request, many of the fields that are normally required for an authorization or credit become optional.  **NOTE** When you use Payment Tokenization or Recurring Billing, the value for the Customer ID is actually the Cybersource payment token for a customer. This token stores information such as the consumer&#39;s card number so it can be applied towards bill payments, recurring payments, or one-time payments. By using this token in a payment API request, the merchant doesn&#39;t need to pass in data such as the card number or expiration date in the request itself.  | [optional] 
**id** | **str** | Unique identifier for the Customer token that was created as part of a bundled TOKEN_CREATE action.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


