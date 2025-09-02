# UpdateWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Client friendly webhook name. | [optional] 
**organization_id** | **str** | Organization Id. | [optional] 
**description** | **str** | Client friendly webhook description. | [optional] 
**products** | [**list[Notificationsubscriptionsv2webhooksProducts]**](Notificationsubscriptionsv2webhooksProducts.md) |  | [optional] 
**webhook_url** | **str** | The client&#39;s endpoint (URL) to receive webhooks. | [optional] 
**notification_scope** | **str** | The webhook scope. 1. SELF The Webhook is used to deliver webhooks for only this Organization (or Merchant). 2. DESCENDANTS The Webhook is used to deliver webhooks for this Organization and its children. This field is optional.    Possible values: - SELF - DESCENDANTS | [optional] [default to 'DESCENDANTS']
**health_check_url** | **str** | The client&#39;s health check endpoint (URL). | [optional] 
**security_policy** | [**Notificationsubscriptionsv2webhooksSecurityPolicy**](Notificationsubscriptionsv2webhooksSecurityPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


