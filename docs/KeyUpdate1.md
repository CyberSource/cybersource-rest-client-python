# KeyUpdate1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | Unique name for the key | [optional] 
**encryption_key** | **str** | Base64-encoded public key (JWE key wrap public key) | [optional] 
**algorithm** | **str** | JWE key wrap algorithm  Possible values: - RSA-OAEP - RSA-OAEP-256 - RSA-OAEP-384 - RSA-OAEP-512 | [optional] 
**encryption_type** | **str** | JWE content encryption algorithm  Possible values: - A256GCM - A128GCM - C20P - A256CBC-HS512 - A128CBC-HS256 - A256CCM - A128CCM | [optional] 
**expiration_date** | **datetime** | Key expiration date in UTC | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


