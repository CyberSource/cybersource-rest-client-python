# UnifiedriskPaymentCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name on the card | [optional] 
**number** | **str** | Tokenized or masked card number | [optional] 
**card_network** | **str** | Card network: VISA, MASTERCARD, AMEX, etc | [optional] 
**type** | **str** | Card type: CREDIT, DEBIT, PREPAID etc. | [optional] 
**sub_type** | **str** | Card subtype: GOLD, PLATINUM, etc | [optional] 
**bin** | **str** | Bank Identification Number (first 6 digits) | [optional] 
**expiration_month** | **str** | Card expiration month | [optional] 
**expiration_year** | **str** | Card expiration year | [optional] 
**issue_date** | **date** | Date card was issued | [optional] 
**issuer_country** | **str** | Country where card was issued | [optional] 
**brand** | **str** | Card network: VISA, MASTERCARD, AMEX, etc | [optional] 
**sequence_number** | **int** | Sequence number for cards with same PAN | [optional] 
**last4** | **str** | Last 4 digits of card number | [optional] 
**status** | **str** | Card status: ACTIVE, BLOCKED, CANCELLED | [optional] 
**token_transaction_type** | **str** | Transaction type that provided the token data | [optional] 
**token_details** | [**UnifiedriskPaymentCardTokenDetails**](UnifiedriskPaymentCardTokenDetails.md) |  | [optional] 
**added_at_checkout** | **bool** | Whether the card was newly entered during checkout | [optional] 
**par_details** | [**UnifiedriskPaymentCardParDetails**](UnifiedriskPaymentCardParDetails.md) |  | [optional] 
**expiry_date** | **str** | Card expiry date in MMYYYY or MMYY format, used for matching against the expiry date declared during enrollment and to flag expired or about-to-expire cards | [optional] 
**entity_id** | **str** | Unique entity identifier for the card as assigned by the card scheme or token service provider, used for lifecycle and risk management | [optional] 
**bin_entity_id** | **str** | Entity identifier linked to the card&#39;s BIN, used to identify the issuing institution or program associated with the card&#39;s BIN range | [optional] 
**security_code** | **str** | Result or presence indicator for Card Security Code (CVV2/CVC2/CID) verification. Indicates whether the security code was present, verified, or matched by the issuer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


