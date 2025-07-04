# Rbsv1subscriptionsClientReferenceInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | &gt; Deprecated: This field is ignored.  Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  #### Used by **Authorization** Required field.  #### PIN Debit Requests for PIN debit reversals need to use the same merchant reference number that was used in the transaction that is being reversed.  Required field for all PIN Debit requests (purchase, credit, and reversal).  #### FDC Nashville Global Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports.  | [optional] 
**comments** | **str** | &gt; Deprecated: This field is ignored.  Brief description of the order or any comment you wish to add to the order.  | [optional] 
**partner** | [**Rbsv1subscriptionsClientReferenceInformationPartner**](Rbsv1subscriptionsClientReferenceInformationPartner.md) |  | [optional] 
**application_name** | **str** | &gt; Deprecated: This field is ignored.  The name of the Connection Method client (such as Virtual Terminal or SOAP Toolkit API) that the merchant uses to send a transaction request to CyberSource.  | [optional] 
**application_version** | **str** | &gt; Deprecated: This field is ignored.  Version of the CyberSource application or integration used for a transaction.  | [optional] 
**application_user** | **str** | &gt; Deprecated: This field is ignored.  The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


