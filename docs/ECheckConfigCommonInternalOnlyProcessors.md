# ECheckConfigCommonInternalOnlyProcessors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_ccs** | **bool** | *NEW* Flag to indicate whether the processor is migrated to the Common Connectivity Services Platform. Applicable for VPC and amexdirect processors.  | [optional] 
**terminal_id** | **str** | *NEW* The &#39;Terminal Id&#39; aka TID, is an identifier used for with your payments processor. Depending on the processor and payment acceptance type this may also be the default Terminal ID used for Card Present and Virtual Terminal transactions. Applicable for VPC processors.  | [optional] 
**enable15an_transaction_reference_number** | **bool** | *NEW* This ensures the transaction reference # contains an identifier that can be viewed in CYBS | [optional] [default to True]
**portal_supported_paytypes** | **str** | *NEW* This is used by the EBC2 application | [optional] [default to 'CHECK']
**settlement_method** | **str** | *NEW*  Possible values: - BEST_GUESS | [optional] [default to 'BEST_GUESS']
**verification_level** | **str** | *NEW*  Possible values: - VALIDATION | [optional] [default to 'VALIDATION']
**set_completed_state** | **bool** | *Moved* When set to Yes we will automatically update transactions to a completed status X-number of days after the transaction comes through; if no failure notification is received. When set to No means we will not update transaction status in this manner. For BAMS/Bank of America merchants, they should be set to No unless we are explicitly asked to set a merchant to YES. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


