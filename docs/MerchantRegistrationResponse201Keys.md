# MerchantRegistrationResponse201Keys

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique key identifier (UUID). Generated from VMRS. | 
**key_name** | **str** | Unique name for the key | 
**encryption_key** | **str** | Base64-encoded public key | 
**algorithm** | **str** | JWE key wrap algorithm  Possible values: - RSA-OAEP - RSA-OAEP-256 - RSA-OAEP-384 - RSA-OAEP-512 | 
**encryption_type** | **str** | JWE content encryption algorithm  Possible values: - A256GCM - A128GCM - C20P - A256CBC_HS512 - A128CBC_HS256 - A256CCM - A128CCM | 
**expiration_date** | **datetime** | Key expiration date in UTC | 
**status** | **str** | Key lifecycle status  Possible values: - active - deactivated - expired | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


