# CreateWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Client friendly webhook name. | [optional] 
**description** | **str** | Client friendly webhook description. | [optional] 
**organization_id** | **str** | Organization Identifier (OrgId) or Merchant Identifier (MID). | [optional] 
**products** | [**list[Notificationsubscriptionsv2webhooksProducts1]**](Notificationsubscriptionsv2webhooksProducts1.md) | To see the valid productId and eventTypes, call the \&quot;Create and Manage Webhooks - Retrieve a list of event types\&quot; endpoint. | [optional] 
**webhook_url** | **str** | The client&#39;s endpoint (URL) to receive webhooks. | [optional] 
**health_check_url** | **str** | The client&#39;s health check endpoint (URL). This should be as close as possible to the actual webhookUrl. If the user does not provide the health check URL, it is the user&#39;s responsibility to re-activate the webhook if it is deactivated by calling the test endpoint.  | [optional] 
**retry_policy** | [**Notificationsubscriptionsv2webhooksRetryPolicy**](Notificationsubscriptionsv2webhooksRetryPolicy.md) |  | [optional] 
**security_policy** | [**Notificationsubscriptionsv2webhooksSecurityPolicy1**](Notificationsubscriptionsv2webhooksSecurityPolicy1.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


