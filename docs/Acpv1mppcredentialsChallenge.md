# Acpv1mppcredentialsChallenge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique challenge identifier issued by the merchant server. | 
**realm** | **str** | Merchant realm (typically the API domain). | 
**amount** | **str** | Amount in the smallest currency unit (e.g., &#39;4999&#39; &#x3D; $49.99). | 
**currency** | **str** | Three-letter ISO 4217 currency code, lowercase (e.g., &#39;usd&#39;). | 
**accepted_networks** | **list[str]** | Card networks accepted by the merchant (e.g., [&#39;visa&#39;, &#39;mastercard&#39;]). | 
**merchant_id** | **str** | Merchant identifier (maps to &#39;recipient&#39; in MPP spec request object). | 
**merchant_name** | **str** | Human-readable merchant name. | 
**encryption_jwk** | [**Acpv1mppcredentialsChallengeEncryptionJwk**](Acpv1mppcredentialsChallengeEncryptionJwk.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


