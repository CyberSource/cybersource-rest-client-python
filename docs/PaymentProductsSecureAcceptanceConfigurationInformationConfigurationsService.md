# PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision_manager_verbose_enabled** | **bool** | Toggles whether verbose Decision Manager results should be present in the Secure Acceptance response. As this response passes through the browser, it is recommended to set this to \&quot;false\&quot; outside of debugging. | [optional] 
**declined_retry_limit** | **float** | Defines the number of retries a payer is presented with on payment declines on Hosted Checkout. Valid values are between 0 and 5. | [optional] 
**decision_manager_enabled** | **bool** | Toggles whether Decision Manager is enabled or not for Secure Acceptance transactions. Requires the transacting MID to be enabled and configured for Decicion Manager. | [optional] 
**tokenization_enabled** | **bool** | Toggles whether Tokenization is enabled or not for Secure Acceptance transactions. Requires the transacting MID to be enabled and configured for Tokenization. | [optional] 
**reverse_auth_on_address_verification_system_failure** | **bool** | Toggles whether or not an approved Authorization that fails AVS should be automatically reversed. | [optional] 
**device_fingerprint_enabled** | **bool** | Toggles whether or not fraud Device Fingerprinting is enabled on the Hosted Checkout. This simplifies enablement for Decision Manager. | [optional] 
**reverse_auth_on_card_verification_number_failure** | **bool** | Toggles whether or not an approved Authorization that fails CVN check that should be automatically reversed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


