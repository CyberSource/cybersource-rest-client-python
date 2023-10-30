# CreateWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Client friendly webhook name. | [optional] 
**description** | **str** | Client friendly webhook description. | [optional] 
**organization_id** | **str** | Organization Identifier (OrgId) or Merchant Identifier (MID). | [optional] 
**product_id** | **str** | To see the valid productId and eventTypes, call the \&quot;Create and Manage Webhooks - Retrieve a list of event types\&quot; endpoint. | [optional] 
**event_types** | **list[str]** | Array of the different events for a given product id. | [optional] 
**webhook_url** | **str** | The client&#39;s endpoint (URL) to receive webhooks. | [optional] 
**health_check_url** | **str** | The client&#39;s health check endpoint (URL). This should be as close as possible to the actual webhookUrl. If the user does not provide the health check URL, it is the user&#39;s responsibility to re-activate the webhook if it is deactivated by calling the test endpoint.  | [optional] 
**notification_scope** | **str** | The webhook scope. 1. SELF The Webhook is used to deliver webhooks for only this Organization (or Merchant). 2. DESCENDANTS The Webhook is used to deliver webhooks for this Organization and its children. 3. CUSTOM The Webhook is used to deliver webhooks for the OrgIds (or MiDs) explicitly listed in scopeData field.  | [optional] 
**retry_policy** | [**Notificationsubscriptionsv1webhooksRetryPolicy**](Notificationsubscriptionsv1webhooksRetryPolicy.md) |  | [optional] 
**security_policy** | [**Notificationsubscriptionsv1webhooksSecurityPolicy1**](Notificationsubscriptionsv1webhooksSecurityPolicy1.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


