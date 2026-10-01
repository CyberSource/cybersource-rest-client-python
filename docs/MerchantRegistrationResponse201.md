# MerchantRegistrationResponse201

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique merchant identifier (UUID) | 
**merchant_name** | **str** | Doing business as (DBA) name | 
**merchant_url** | **str** | Fully-qualified HTTPS URL of the merchant&#39;s domain | 
**vmid** | **str** | Visa Merchant ID (VMID) — unique identifier assigned by Visa | [optional] 
**cryptogram_type** | **str** | Authentication cryptogram type used for payment credential generation: &#39;TAVV&#39; (Token Authentication Verification Value) or &#39;DAVV&#39; (Device Authentication Verification Value)  Possible values: - TAVV - DAVV | [optional] 
**payment_payload_type** | **str** | Credential delivery format: &#39;ENCRYPTED&#39; (JWE-wrapped, requires an active encryption key) or &#39;UNENCRYPTED&#39;  Possible values: - ENCRYPTED - UNENCRYPTED | [optional] 
**indicator** | **str** | Transaction processing indicator: &#39;TAP&#39; (Trusted Agent Protocol), &#39;ACG&#39; (Agentic Checkout Gateway), or &#39;BOTH&#39;  Possible values: - TAP - ACG - BOTH | 
**merchant_metadata** | **object** | Free-form metadata object for additional merchant context | [optional] 
**acceptance_relationships** | **list[str]** | List of payment network acceptance relationships (e.g., \&quot;Visa\&quot;) | [optional] 
**protocol_interactions** | [**list[Iccv1merchantsProtocolInteractions]**](Iccv1merchantsProtocolInteractions.md) | List of protocol endpoint configurations defining how agents interact with this merchant (ucp, acp, x402) | [optional] 
**web_integrations** | [**MerchantRegistrationResponse201WebIntegrations**](MerchantRegistrationResponse201WebIntegrations.md) |  | [optional] 
**api_integrations** | [**MerchantRegistrationResponse201ApiIntegrations**](MerchantRegistrationResponse201ApiIntegrations.md) |  | [optional] 
**is_active** | **bool** | Whether the merchant is active | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 
**keys** | [**list[MerchantRegistrationResponse201Keys]**](MerchantRegistrationResponse201Keys.md) | List of encryption keys associated with the merchant | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


