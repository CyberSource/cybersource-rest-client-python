# ListAgentKeysResponse200

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Agent identifier (64-char SHA-256 hash) | 
**agent_name** | **str** | Display name of the agent | 
**keys** | [**list[AgentRegistrationResponse201Keys]**](AgentRegistrationResponse201Keys.md) | Paginated list of public keys belonging to this agent (agentId/agentName/agentType omitted — available at the parent level) | 
**pagination** | [**ListAgentKeysResponse200Pagination**](ListAgentKeysResponse200Pagination.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


