# UpdateWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Client friendly webhook name. | [optional] 
**organization_id** | **str** | Organization Id. | [optional] 
**description** | **str** | Client friendly webhook description. | [optional] 
**products** | [**list[Notificationsubscriptionsv2webhooksProducts]**](Notificationsubscriptionsv2webhooksProducts.md) |  | [optional] 
**webhook_url** | **str** | The client&#39;s endpoint (URL) to receive webhooks. | [optional] 
**health_check_url** | **str** | The client&#39;s health check endpoint (URL). This should be as close as possible to the actual webhookUrl. | [optional] 
**security_policy** | [**Notificationsubscriptionsv2webhooksSecurityPolicy**](Notificationsubscriptionsv2webhooksSecurityPolicy.md) |  | [optional] 
**additional_attributes** | **list[dict(str, str)]** | Additional, free form configuration data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


