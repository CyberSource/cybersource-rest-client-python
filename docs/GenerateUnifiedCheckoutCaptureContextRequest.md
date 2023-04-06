# GenerateUnifiedCheckoutCaptureContextRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_origins** | **list[str]** |  | [optional] 
**client_version** | **str** | version number of Unified Checkout being used | [optional] 
**allowed_card_networks** | **list[str]** |  | [optional] 
**allowed_payment_types** | **list[str]** |  | [optional] 
**country** | **str** | Country the purchase is originating from (e.g. country of the merchant). Use the two- character ISO Standard | [optional] 
**locale** | **str** | Localization of the User experience conforming to the ISO 639-1 language standards and two-character ISO Standard Country Code | [optional] 
**capture_mandate** | [**Upv1capturecontextsCaptureMandate**](Upv1capturecontextsCaptureMandate.md) |  | [optional] 
**order_information** | [**Upv1capturecontextsOrderInformation**](Upv1capturecontextsOrderInformation.md) |  | [optional] 
**checkout_api_initialization** | [**Upv1capturecontextsCheckoutApiInitialization**](Upv1capturecontextsCheckoutApiInitialization.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


