# Ptsv2paymentsProcessingInformationPurchaseOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_electronic_benefits_transfer** | **bool** | Flag that indicates whether this transaction is an EBT transaction. Possible values: - &#x60;true&#x60; - &#x60;false&#x60;  #### PIN debit Required field for EBT and EBT voucher transactions that use PIN debit credit or PIN debit purchase; otherwise, not used.  | [optional] 
**type** | **str** | Flag that indicates an EBT voucher transaction. Possible value: - &#x60;EBT_VOUCHER&#x60;: Indicates the PIN debit transaction is an EBT voucher. - &#x60;BUY&#x60; - &#x60;RENT&#x60; - &#x60;BOOK&#x60; - &#x60;SUBSCRIBE&#x60; - &#x60;DOWNLOAD&#x60; - &#x60;ORDER&#x60; - &#x60;CONTINUE&#x60;  #### PIN debit Required field for EBT voucher transactions that use PIN debit purchase; otherwise, not used.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


