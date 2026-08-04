# KeyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | Unique identifier for the key | 
**public_key** | **str** | Base64-encoded public key. Supports PEM (PKCS#8, PKCS#1), JWK, DER, and OpenSSH formats. Max 10000 characters. | 
**algorithm** | **str** | Signing algorithm. Must match the key type (e.g., an RSA key requires RSA-SHA256 or RSA-SHA512).  Possible values: - RSA-SHA256 - RSA-SHA512 - ECDSA-SHA256 - ECDSA-SHA512 - EdDSA | 
**expiration_date** | **datetime** | Key expiration date in UTC (defaults to 14 days from now if not provided) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


