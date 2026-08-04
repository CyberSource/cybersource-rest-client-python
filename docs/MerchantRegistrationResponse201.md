# MerchantRegistrationResponse201

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique merchant identifier (UUID) | 
**merchant_name** | **str** | Doing business as (DBA) name | 
**merchant_url** | **str** | Base merchant URL | 
**vmid** | **str** | Visa Merchant ID | [optional] 
**cryptogram_type** | **str** | Authentication cryptogram type  Possible values: - TAVV - DAVV | [optional] 
**payment_payload_type** | **str** | Credential delivery format  Possible values: - ENCRYPTED - UNENCRYPTED | [optional] 
**indicator** | **str** | Transaction processing type  Possible values: - TAP - ACG - BOTH | 
**merchant_metadata** | **object** | Additional merchant metadata | [optional] 
**acceptance_relationships** | **list[str]** | List of acceptance network relationships | [optional] 
**protocol_interactions** | [**list[Iccv1merchantsProtocolInteractions]**](Iccv1merchantsProtocolInteractions.md) | List of protocol interaction configurations (ucp, acp, x402) | [optional] 
**web_integrations** | [**Iccv1merchantsWebIntegrations**](Iccv1merchantsWebIntegrations.md) |  | [optional] 
**api_integrations** | [**Iccv1merchantsApiIntegrations**](Iccv1merchantsApiIntegrations.md) |  | [optional] 
**is_active** | **bool** | Whether the merchant is active | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 
**keys** | [**list[MerchantRegistrationResponse201Keys]**](MerchantRegistrationResponse201Keys.md) | List of encryption keys associated with the merchant | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


