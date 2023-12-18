# PaymentsProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsCustomerNotifications

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_receipt_page_enabled** | **bool** | Toggles the custom receipt page, where merchants can receive the results of the transaction and display appropriate messaging. Usually set by web developers integrating to Secure Acceptance. | [optional] 
**receipt_email_address** | **str** | Email address where a copy of the payer&#39;s receipt email is sent, when notificationReceiptEmailEnabled is true. | [optional] 
**customer_receipt_email_enabled** | **bool** | Toggles an email receipt sent to the payer&#39;s email address on payment success. | [optional] 
**custom_cancel_page** | **str** | URL to which transaction results are POSTed when the payer clicks &#39;Cancel&#39; on the Hosted Checkout. Triggered when customCancelPageEnabled is true. Usually set by web developers integrating to Secure Acceptance. | [optional] 
**custom_receipt_page** | **str** | URL to which transaction results are POSTed when the payer requests a payment on the Hosted Checkout. Triggered when customCancelPageEnabled is true. Usually set by web developers integrating to Secure Acceptance. | [optional] 
**custom_cancel_page_enabled** | **bool** | Toggles the custom cancel page, where merchants can receive notice that the payer has canceled, and display appropriate messaging and direction. Usually set by web developers integrating to Secure Acceptance. | [optional] 
**notification_receipt_email_enabled** | **bool** | Toggles whether merchant receives a copy of the payer&#39;s receipt email. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


