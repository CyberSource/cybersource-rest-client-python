# Ptsv2paymentsPaymentInformationSepaDirectDebit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Mandate reference as returned on the first transaction in the sequence  | [optional] 
**signature_date** | **str** | Date of the initial transaction, format is YYYY-MM-DD. Date can be taken from the finaltimestamp of the SUCCEEDED notification for the first transaction in the sequence.  | [optional] 
**url** | **str** | Valid URL pointing to the SEPA mandate, needs to be accessible by our risk and compliance department.  | [optional] 
**type** | **str** | Sequence type of the direct debit, defaults to \&quot;oneOff\&quot;. Valid values: oneOff The direct debit is executed once. first First direct debit in a series of recurring ones.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


