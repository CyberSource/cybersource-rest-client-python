# MerchantUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** | Doing business as (DBA) name | [optional] 
**merchant_url** | **str** | Base URL of the merchant&#39;s domain. Must use HTTPS and be unique — raises 409 if already registered. | [optional] 
**cryptogram_type** | **str** | Authentication cryptogram type used for payment credential generation.  Possible values: - TAVV - DAVV | [optional] 
**payment_payload_type** | **str** | Credential delivery format. Set to ***ENCRYPTED*** to enable JWE-encrypted payload delivery — requires an active encryption key. Returns 400 if no active key exists.  Possible values: - ENCRYPTED - UNENCRYPTED | [optional] 
**acceptance_relationships** | **list[str]** | List of payment network acceptance relationships (e.g., \&quot;Visa\&quot;). | [optional] 
**protocol_interactions** | [**list[Iccv1merchantsProtocolInteractions]**](Iccv1merchantsProtocolInteractions.md) | List of protocol interaction configurations defining the merchant&#39;s endpoint for each supported protocol (ucp, acp, x402). | [optional] 
**web_integrations** | [**Iccv1merchantsWebIntegrations**](Iccv1merchantsWebIntegrations.md) |  | [optional] 
**api_integrations** | [**Iccv1merchantsApiIntegrations**](Iccv1merchantsApiIntegrations.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


