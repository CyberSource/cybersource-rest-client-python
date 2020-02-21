# PredefinedSubscriptionRequestBean

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_definition_name** | **str** | Valid Report Definition Name | 
**subscription_type** | **str** | The subscription type for which report definition is required. Valid values are CLASSIC and STANDARD. Valid Values:   - CLASSIC   - STANDARD  | 
**report_name** | **str** |  | [optional] 
**report_mime_type** | **str** | Report Format             Valid Values:   - application/xml   - text/csv  | [optional] 
**report_frequency** | **str** | &#39;The frequency for which subscription is created. For Standard we can have DAILY, WEEKLY and MONTHLY. But for Classic we will have only DAILY.&#39; **NOTE: Do not document USER_DEFINED Frequency field in developer center** Valid Values: - &#39;DAILY&#39; - &#39;WEEKLY&#39; - &#39;MONTHLY&#39; - &#39;USER_DEFINED&#39;  | [optional] 
**report_interval** | **str** | If the reportFrequency is User-defined, reportInterval should be in **ISO 8601 time format** Please refer the following link to know more about ISO 8601 format.[Rfc Time Format](https://en.wikipedia.org/wiki/ISO_8601#Durations)  **Example time format for 2 hours and 30 Mins:**   - PT2H30M **NOTE: Do not document reportInterval field in developer center**  | [optional] 
**timezone** | **str** | By Default the timezone for Standard subscription is PST. And for Classic subscription it will be GMT. If user provides any other time zone apart from PST for Standard subscription api should error out. | [optional] 
**start_time** | **str** | The hour at which the report generation should start. It should be in hhmm format. By Default it will be 0000. The format is 24 hours format. | [optional] 
**start_day** | **int** | This is the start day if the frequency is WEEKLY or MONTHLY. The value varies from 1-7 for WEEKLY and 1-31 for MONTHLY. For WEEKLY 1 means Sunday and 7 means Saturday. By default the value is 1. | [optional] 
**subscription_status** | **str** | The status for subscription which is either created or updated. By default it is ACTIVE. Valid Values:   - ACTIVE   - INACTIVE  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


