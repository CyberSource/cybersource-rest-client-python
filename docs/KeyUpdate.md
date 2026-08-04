# KeyUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | Unique identifier for the key | [optional] 
**public_key** | **str** | Base64-encoded public key. Supports PEM (PKCS#8, PKCS#1), JWK, DER, and OpenSSH formats. Max 10000 characters. | [optional] 
**algorithm** | **str** | Signing algorithm. Must match the key type (e.g., an RSA key requires RSA-SHA256 or RSA-SHA512).  Possible values: - RSA-SHA256 - RSA-SHA512 - ECDSA-SHA256 - ECDSA-SHA512 - EdDSA | [optional] 
**expiration_date** | **datetime** | Key expiration date in UTC | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


