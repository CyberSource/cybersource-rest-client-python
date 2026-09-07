# UnifiedriskPaymentCheck

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_number** | **str** | Serial number printed on the physical check, used for duplicate detection, check fraud prevention, and reconciliation | [optional] 
**deposit_slip_id** | **str** | Unique identifier for the deposit slip associated with the check deposit, used for linking deposited checks to branch transactions | [optional] 
**deposit_location** | [**UnifiedriskPaymentCheckDepositLocation**](UnifiedriskPaymentCheckDepositLocation.md) |  | [optional] 
**micr_account_number** | **str** | Account number encoded in the MICR (Magnetic Ink Character Recognition) line at the bottom of the check, used for automated account identification | [optional] 
**routing_transit_number** | **str** | Bank routing and transit number (RTN) encoded in the MICR line of the check, identifying the financial institution on which the check is drawn | [optional] 
**split_deposit_flag** | **bool** | Indicates whether the check deposit has been split across multiple accounts. Split deposits may indicate structuring or kiting attempts | [optional] 
**split_account_id1** | **str** | First destination account ID in a split check deposit, used for tracking the allocation of funds across multiple accounts | [optional] 
**split_account_id2** | **str** | Second destination account ID in a split check deposit | [optional] 
**split_account_id3** | **str** | Third destination account ID in a split check deposit | [optional] 
**split_account_id4** | **str** | Fourth destination account ID in a split check deposit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


