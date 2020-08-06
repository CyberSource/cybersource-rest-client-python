# InvoicingV2InvoicesAllGet200ResponseInvoices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InvoicingV2InvoicesAllGet200ResponseLinks1**](InvoicingV2InvoicesAllGet200ResponseLinks1.md) |  | [optional] 
**id** | **str** | An unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  #### PIN debit Returned for all PIN debit services.  | [optional] 
**status** | **str** | The status of the invoice.  Possible values: - DRAFT - CREATED - SENT - PARTIAL - PAID - CANCELED  | [optional] 
**customer_information** | [**InvoicingV2InvoicesAllGet200ResponseCustomerInformation**](InvoicingV2InvoicesAllGet200ResponseCustomerInformation.md) |  | [optional] 
**invoice_information** | [**InvoicingV2InvoicesAllGet200ResponseInvoiceInformation**](InvoicingV2InvoicesAllGet200ResponseInvoiceInformation.md) |  | [optional] 
**order_information** | [**InvoicingV2InvoicesAllGet200ResponseOrderInformation**](InvoicingV2InvoicesAllGet200ResponseOrderInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


