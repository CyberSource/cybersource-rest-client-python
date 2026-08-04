# Iplv2paymentlinksPurchaseInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_number** | **str** | The purchase number | 
**transaction_reference_number** | **str** | The transaction reference number (TRN) is a identifier assigned to each payment transaction that allows merchants, customers, and payment processors to track and reference specific transactions throughout their lifecycle.  When provided, this value is passed to the payment processor as the reconciliation ID for the payment. For invoices this is typically the invoice number, and for purchase or donation links it is typically the link identifier.  Only letters and numbers are allowed; spaces and other special characters are not permitted.  | [optional] 
**expiration_date** | **date** | Define an expiration date for the link.  The date must be today or in the future.  Format: &#x60;YYYY-MM-DD&#x60;, where &#x60;YYYY&#x60; &#x3D; year, &#x60;MM&#x60; &#x3D; month, and &#x60;DD&#x60; &#x3D; day.  The invoice link automatically expires 12 months after the due date.  | [optional] 
**expiration_amount** | **str** | Define an expiry amount for the link.  Must be null or greater than 0.  If the total price of all transactions for this link exceeds the expiry amount, the link will expire.  | [optional] 
**expiration_quantity** | **str** | Define an expiration quantity for the link.  Must be null or greater than 0.  If the total quantity of items sold exceeds the expiration quantity, the link is expired.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


