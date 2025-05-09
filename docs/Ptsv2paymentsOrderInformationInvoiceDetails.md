# Ptsv2paymentsOrderInformationInvoiceDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** | Invoice Number. | [optional] 
**barcode_number** | **str** | Barcode Number. | [optional] 
**expiration_date** | **str** | Expiration Date. | [optional] 
**purchase_order_number** | **str** | Value used by your customer to identify the order. This value is typically a purchase order number. CyberSource recommends that you do not populate the field with all zeros or nines.  | [optional] 
**purchase_order_date** | **str** | Date the order was processed. &#x60;Format: YYYY-MM-DD&#x60;.  | [optional] 
**purchase_contact_name** | **str** | The name of the individual or the company contacted for company authorized purchases.  | [optional] 
**taxable** | **bool** | Flag that indicates whether an order is taxable. This value must be true if the sum of all _lineItems[].taxAmount_ values &gt; 0.  If you do not include any &#x60;lineItems[].taxAmount&#x60; values in your request, CyberSource does not include &#x60;invoiceDetails.taxable&#x60; in the data it sends to the processor.  Possible values:  - **true**  - **false**  | [optional] 
**vat_invoice_reference_number** | **str** | VAT invoice number associated with the transaction.  | [optional] 
**commodity_code** | **str** | International description code of the overall order&#39;s goods or services or the Categorizes purchases for VAT reporting. Contact your acquirer for a list of codes.  | [optional] 
**merchandise_code** | **int** | Identifier for the merchandise. This field is supported only on the processors listed in this field description.  #### American Express Direct Possible value: - 1000: Gift card  #### CyberSource through VisaNet This value must be right justified. In Japan, this value is called a _goods code_.  #### JCN Gateway This value must be right justified. In Japan, this value is called a _goods code_.  | [optional] 
**transaction_advice_addendum** | [**list[Ptsv2paymentsOrderInformationInvoiceDetailsTransactionAdviceAddendum]**](Ptsv2paymentsOrderInformationInvoiceDetailsTransactionAdviceAddendum.md) |  | [optional] 
**reference_data_code** | **str** | Code that identifies the value of the &#x60;referenceDataNumber&#x60; field.  This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor.  | [optional] 
**reference_data_number** | **str** | Reference number. The meaning of this value is identified by the value of the &#x60;referenceDataCode&#x60; field.  This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor.  | [optional] 
**sales_slip_number** | **int** | Transaction identifier that is generated. You have the option of printing the sales slip number on the receipt. This field is supported only on Cybersource through Visanet and JCN gateway.  Optional field.  #### Card Present processing message If you included this field in the request, the returned value is the value that you sent in the request. If you did not include this field in the request, the system generated this value for you.  The difference between this reply field and the &#x60;processorInformation.systemTraceAuditNumber&#x60; field is that the system generates the system trace audit number (STAN), and you must print the receipt number on the receipt; whereas you can generate the sales slip number, and you can choose to print the sales slip number on the receipt.  | [optional] 
**invoice_date** | **str** | Date of the tax calculation. Use format YYYYMMDD. You can provide a date in the past if you are calculating tax for a refund and want to know what the tax was on the date the order was placed. You can provide a date in the future if you are calculating the tax for a future date, such as an upcoming tax holiday.  The default is the date, in Pacific time, that the bank receives the request. Keep this in mind if you are in a different time zone and want the tax calculated with the rates that are applicable on a specific date.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  | [optional] 
**cost_center** | **str** | Cost centre of the merchant | [optional] 
**issuer_message** | **str** | Text message from the issuer. If you give the customer a receipt, display this value on the receipt. | [optional] 
**product_description** | **str** | Brief description of item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


