# V2paymentsProcessingInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture** | **bool** | Flag that specifies whether to also include capture service in the submitted request or not. | [optional] [default to False]
**processor_id** | **str** | Value that identifies the processor/acquirer to use for the transaction. This value is supported only for **CyberSource through VisaNet**.  | [optional] 
**business_application_id** | **str** | TBD | [optional] 
**commerce_indicator** | **str** | Type of transaction. Some payment card companies use this information when determining discount rates. When you omit this field for **Ingenico ePayments**, the processor uses the default transaction type they have on file for you instead of the default value listed here.  | [optional] 
**payment_solution** | **str** | Type of digital payment solution that is being used for the transaction. Possible Values:   - **visacheckout**: Visa Checkout.  - **001**: Apple Pay.  - **005**: Masterpass. Required for Masterpass transactions on OmniPay Direct.  - **006**: Android Pay.  - **008**: Samsung Pay.  | [optional] 
**reconciliation_id** | **str** | Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22).  | [optional] 
**link_id** | **str** | Value that links the current payment request to the original request. Set this value to the ID that was returned in the reply message from the original payment request.  This value is used for:   - Partial authorizations.  - Split shipments.  | [optional] 
**purchase_level** | **str** | Set this field to 3 to indicate that the request includes Level III data. | [optional] 
**report_group** | **str** | Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Litle**.  | [optional] 
**visa_checkout_id** | **str** | Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field.  | [optional] 
**issuer** | [**V2paymentsProcessingInformationIssuer**](V2paymentsProcessingInformationIssuer.md) |  | [optional] 
**authorization_options** | [**V2paymentsProcessingInformationAuthorizationOptions**](V2paymentsProcessingInformationAuthorizationOptions.md) |  | [optional] 
**capture_options** | [**V2paymentsProcessingInformationCaptureOptions**](V2paymentsProcessingInformationCaptureOptions.md) |  | [optional] 
**recurring_options** | [**V2paymentsProcessingInformationRecurringOptions**](V2paymentsProcessingInformationRecurringOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


