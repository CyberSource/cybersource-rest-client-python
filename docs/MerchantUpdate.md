# MerchantUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** | Doing business as (DBA) name | [optional] 
**merchant_url** | **str** | Base merchant URL (must use HTTPS) | [optional] 
**cryptogram_type** | **str** | Authentication cryptogram type  Possible values: - TAVV - DAVV | [optional] 
**payment_payload_type** | **str** | Credential delivery format  Possible values: - ENCRYPTED - UNENCRYPTED | [optional] 
**acceptance_relationships** | **list[str]** | List of acceptance network relationships | [optional] 
**protocol_interactions** | [**list[Iccv1merchantsProtocolInteractions]**](Iccv1merchantsProtocolInteractions.md) | List of protocol configurations | [optional] 
**web_integrations** | [**Iccv1merchantsWebIntegrations**](Iccv1merchantsWebIntegrations.md) |  | [optional] 
**api_integrations** | [**Iccv1merchantsApiIntegrations**](Iccv1merchantsApiIntegrations.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


