# AgentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the agent | 
**domain** | **str** | Fully-qualified HTTPS URL of the agent&#39;s home domain. Must be unique — registration raises 409 if it already exists. | 
**description** | **str** | Description of the agent&#39;s purpose or capabilities | 
**contact_email** | **str** | Contact email for the team or individual responsible for this agent | 
**token_requestor_id** | **str** | Token Requestor ID (TRID) assigned by Visa | 
**agent_metadata** | **object** | Free-form metadata object for agent context (e.g., AI framework, language, runtime). Max 10KB. | [optional] 
**keys** | [**list[Iccv1agentsKeys]**](Iccv1agentsKeys.md) | Optional array of public keys to register alongside the agent. Keys are created in ***deactivated*** state and must be activated separately via POST /agents/{agentId}/keys/{keyId}/activate.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


