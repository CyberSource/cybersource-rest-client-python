# ReportingV3ReportSubscriptionsGet200ResponseSubscriptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Selected Organization Id | [optional] 
**report_definition_id** | **str** | Report Definition Id | [optional] 
**report_definition_name** | **str** | Report Definition Class | [optional] 
**report_mime_type** | **str** | Report Format                          Valid values: - application/xml - text/csv  | [optional] 
**report_frequency** | **str** | &#39;Report Frequency&#39; **NOTE: Do not document USER_DEFINED Frequency field in developer center**  Valid values: - DAILY - WEEKLY - MONTHLY - USER_DEFINED  | [optional] 
**report_interval** | **str** | If the reportFrequency is User-defined, reportInterval should be in **ISO 8601 time format** Please refer the following link to know more about ISO 8601 format.[Rfc Time Format](https://en.wikipedia.org/wiki/ISO_8601#Durations)  **Example time format for 2 hours and 30 Mins:**   - PT2H30M **NOTE: Do not document reportInterval field in developer center**  | [optional] 
**report_name** | **str** | Report Name | [optional] 
**timezone** | **str** | Time Zone | [optional] 
**start_time** | **datetime** | Start Time | [optional] 
**start_day** | **int** | Start Day | [optional] 
**report_fields** | **list[str]** | List of all fields String values | [optional] 
**report_filters** | **dict(str, list[str])** | List of filters to apply | [optional] 
**report_preferences** | [**Reportingv3reportsReportPreferences**](Reportingv3reportsReportPreferences.md) |  | [optional] 
**group_id** | **str** | Id for the selected group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


