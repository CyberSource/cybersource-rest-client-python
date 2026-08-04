# AgentRegistrationResponse201

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique agent identifier (64-char SHA-256 hash of domain + email + tokenRequestorId) | 
**name** | **str** | Agent name | 
**domain** | **str** | Agent domain URL | 
**description** | **str** | Agent description | [optional] 
**contact_email** | **str** | Contact email | [optional] 
**token_requestor_id** | **str** | Unique token requestor identifier | 
**agent_type** | **str** | Agent classification: &#39;trusted&#39; (commercially onboarded) or &#39;known&#39; (open-source/unverified)  Possible values: - trusted - known | 
**agent_metadata** | **dict(str, str)** | Additional agent metadata | [optional] 
**is_active** | **bool** | Whether the agent is active | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 
**keys** | [**list[AgentRegistrationResponse201Keys]**](AgentRegistrationResponse201Keys.md) | List of keys associated with the agent | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


