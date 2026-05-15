# GetSubscriptionsPaymentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GetSubscriptionsPaymentsResponseLinks**](GetSubscriptionsPaymentsResponseLinks.md) |  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  Returned by Cybersource for all services.  | [optional] 
**total_count** | **int** | Total number of payments returned for the subscription, including both past payments and those specified in scheduledPaymentsCount. | [optional] 
**cycles_completed_count** | [**GetSubscriptionsPaymentsResponseCyclesCompletedCount**](GetSubscriptionsPaymentsResponseCyclesCompletedCount.md) |  | [optional] 
**billing_cycles_to_skip** | **list[int]** | A list of billing cycles that are marked to be skipped. | [optional] 
**subscription_payment** | [**list[GetSubscriptionsPaymentsResponseSubscriptionPayment]**](GetSubscriptionsPaymentsResponseSubscriptionPayment.md) | The list of subscription payment details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


