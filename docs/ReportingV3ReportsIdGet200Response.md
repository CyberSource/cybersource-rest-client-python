# ReportingV3ReportsIdGet200Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | CyberSource merchant id | [optional] 
**report_id** | **str** | Report ID Value | [optional] 
**report_definition_id** | **str** | Report definition Id | [optional] 
**report_name** | **str** | Report Name | [optional] 
**report_mime_type** | **str** | Report Format  Valid values: - application/xml - text/csv  | [optional] 
**report_frequency** | **str** | Report Frequency Value  Valid values: - DAILY - WEEKLY - MONTHLY - ADHOC  | [optional] 
**report_fields** | **list[str]** | List of Integer Values | [optional] 
**report_status** | **str** | Report Status Value  Valid values: - COMPLETED - PENDING - QUEUED - RUNNING - ERROR - NO_DATA - RERUN  | [optional] 
**report_start_time** | **datetime** | Report Start Time Value | [optional] 
**report_end_time** | **datetime** | Report End Time Value | [optional] 
**timezone** | **str** | Time Zone Value | [optional] 
**report_filters** | **dict(str, list[str])** | List of filters to apply | [optional] 
**report_preferences** | [**Reportingv3reportsReportPreferences**](Reportingv3reportsReportPreferences.md) |  | [optional] 
**group_id** | **str** | Id for selected group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


