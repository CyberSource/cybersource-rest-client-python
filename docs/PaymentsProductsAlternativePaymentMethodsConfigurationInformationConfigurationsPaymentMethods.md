# PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurationsPaymentMethods

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Merchant ID for the payment method. This is a unique identifier for the merchant. example. mid12345678  | [optional] 
**logo_url** | **str** | URL of the logo for the payment method. This is used for branding purposes. example: http://www.test.com  | [optional] 
**redirect_success_url** | **str** | URL to redirect to after a successful transaction. This is where the user will be sent after completing the payment. example: http://www.test.com/success  | [optional] 
**redirect_cancel_url** | **str** | URL to redirect to if the user cancels the transaction. This is where the user will be sent if they choose to cancel the payment. example: http://www.test.com/cancel  | [optional] 
**redirect_failure_url** | **str** | URL to redirect to if the transaction fails. This is where the user will be sent if there is an error during the payment process. example: http://www.test.com/failure  | [optional] 
**underwriting** | [**UnderwritingConfiguration**](UnderwritingConfiguration.md) |  | [optional] 
**additional_configurations** | [**list[PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurationsAdditionalConfigurations]**](PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurationsAdditionalConfigurations.md) | Additional configurations for the payment method. This can include various settings specific to the payment method.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


