# ListAgentKeysResponse200

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Agent identifier (64-char SHA-256 hash) | 
**agent_name** | **str** | Agent name | 
**keys** | [**list[AgentRegistrationResponse201Keys]**](AgentRegistrationResponse201Keys.md) | List of keys (without agentId/agentName/agentType since they are at parent level) | 
**pagination** | [**ListAgentKeysResponse200Pagination**](ListAgentKeysResponse200Pagination.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


