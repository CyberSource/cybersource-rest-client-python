# V2paymentsidcapturesProcessingInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_solution** | **str** | Type of digital payment solution that is being used for the transaction. Possible Values:   - **visacheckout**: Visa Checkout.  - **001**: Apple Pay.  - **005**: Masterpass. Required for Masterpass transactions on OmniPay Direct.  - **006**: Android Pay.  - **008**: Samsung Pay.  | [optional] 
**reconciliation_id** | **str** | Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22).  | [optional] 
**link_id** | **str** | Value that links the current payment request to the original request. Set this value to the ID that was returned in the reply message from the original payment request.  This value is used for:   - Partial authorizations.  - Split shipments.  | [optional] 
**report_group** | **str** | Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Litle**.  | [optional] 
**visa_checkout_id** | **str** | Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field.  | [optional] 
**purchase_level** | **str** | Set this field to 3 to indicate that the request includes Level III data. | [optional] 
**issuer** | [**V2paymentsProcessingInformationIssuer**](V2paymentsProcessingInformationIssuer.md) |  | [optional] 
**authorization_options** | [**V2paymentsidcapturesProcessingInformationAuthorizationOptions**](V2paymentsidcapturesProcessingInformationAuthorizationOptions.md) |  | [optional] 
**capture_options** | [**V2paymentsidcapturesProcessingInformationCaptureOptions**](V2paymentsidcapturesProcessingInformationCaptureOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


