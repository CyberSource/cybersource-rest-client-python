# AddAgentKeyResponse201

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique key identifier. Generated from VARS. | 
**agent_id** | **str** | Agent identifier | 
**agent_name** | **str** | Agent name | 
**agent_type** | **str** | Agent classification  Possible values: - trusted - known | 
**key_name** | **str** | Unique identifier for the key | 
**public_key** | **str** | Base64-encoded public key | 
**algorithm** | **str** | Signing algorithm  Possible values: - RSA-SHA256 - RSA-SHA512 - ECDSA-SHA256 - ECDSA-SHA512 - EdDSA | 
**expiration_date** | **datetime** | Key expiration date in UTC | 
**status** | **str** | Key lifecycle status  Possible values: - active - deactivated - expired | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


