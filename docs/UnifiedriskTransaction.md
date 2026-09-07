# UnifiedriskTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique identifier for the transaction being assessed | [optional] 
**status** | **str** | Transaction status: NEW, APPROVED, DECLINED, REVERSED, FRAUD | [optional] 
**status_reason** | **str** | Reason code for the transaction status | [optional] 
**message_type** | **str** | Message type: AUTHORIZATION, INQUIRY, ADVICE, REVERSAL | [optional] 
**type** | **str** | The type of transaction being processed | [optional] 
**attribute** | **str** | Transaction attribute: AGGREGATION, CARDLESS_ATM, etc | [optional] 
**initiator** | **str** | Who initiated transaction: MERCHANT, CUSTOMER | [optional] 
**channel** | **str** | Channel used: ONLINE, MOBILE, ATM, BRANCH, etc | [optional] 
**timestamp** | **datetime** | Local transaction timestamp without timezone | [optional] 
**cutoff_date_time** | **datetime** | Cutoff date/time for event or journey | [optional] 
**is_recurring** | **bool** | Indicates if this is a recurring transaction | [optional] 
**pre_order** | **bool** | Indicates if this is a pre-order | [optional] 
**pre_order_date** | **date** | Expected availability date for pre-order | [optional] 
**reordered** | **bool** | Indicates if customer is reordering | [optional] 
**destination_country** | **str** | Destination country for funds | [optional] 
**decline_phase** | **str** | Phase where transaction was declined | [optional] 
**trusted_merchant** | **bool** | Indicates if merchant is on trusted list | [optional] 
**additional_fees** | [**UnifiedriskTransactionAdditionalFees**](UnifiedriskTransactionAdditionalFees.md) |  | [optional] 
**amount** | [**UnifiedriskTransactionAmount**](UnifiedriskTransactionAmount.md) |  | [optional] 
**recurring_details** | [**UnifiedriskTransactionRecurringDetails**](UnifiedriskTransactionRecurringDetails.md) |  | [optional] 
**direction** | **str** | Direction of the transaction flow relative to the customer&#39;s account (e.g., CREDIT for incoming funds, DEBIT for outgoing funds). Determines risk model orientation and velocity tracking | [optional] 
**is_chargeback** | **bool** | Indicates whether this transaction represents a chargeback or dispute reversal. True signals a disputed transaction requiring fraud investigation and issuer liability assessment | [optional] 
**fraud_liability** | **str** | Indicates which party bears fraud liability for this transaction (e.g., ISSUER, MERCHANT, ACQUIRER). Liability shifts apply in 3DS-authenticated or EMV chip transactions | [optional] 
**on_us_flag** | **bool** | Indicates whether the transaction is an on-us transaction where the issuing and acquiring institutions are the same entity. On-us transactions may follow different risk rules and processing paths | [optional] 
**number_of_transactions** | **int** | Total count of transactions associated with this batch, order, or session. Used for velocity-based risk rules and aggregated fraud monitoring | [optional] 
**batch_details** | [**UnifiedriskTransactionBatchDetails**](UnifiedriskTransactionBatchDetails.md) |  | [optional] 
**check_details** | [**UnifiedriskTransactionCheckDetails**](UnifiedriskTransactionCheckDetails.md) |  | [optional] 
**purpose** | **str** | Business purpose or reason code for this transaction (e.g., PURCH for purchase, SALA for salary, REFND for refund). Used for transaction classification and AML monitoring | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


