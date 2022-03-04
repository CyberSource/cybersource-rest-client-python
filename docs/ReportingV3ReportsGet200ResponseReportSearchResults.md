# ReportingV3ReportsGet200ResponseReportSearchResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**ReportingV3ReportsGet200ResponseLink**](ReportingV3ReportsGet200ResponseLink.md) |  | [optional] 
**report_definition_id** | **str** | Unique Report Identifier of each report type | [optional] 
**report_name** | **str** | Name of the report specified by merchant while creating the report | [optional] 
**report_mime_type** | **str** | Format of the report to get generated Valid Values: - application/xml - text/csv  | [optional] 
**report_frequency** | **str** | Frequency of the report to get generated Valid Values: - DAILY - WEEKLY - MONTHLY - ADHOC  | [optional] 
**status** | **str** | Status of the report Valid Values: - COMPLETED - PENDING - QUEUED - RUNNING - ERROR - NO_DATA  | [optional] 
**report_start_time** | **datetime** | Specifies the report start time in ISO 8601 format | [optional] 
**report_end_time** | **datetime** | Specifies the report end time in ISO 8601 format | [optional] 
**timezone** | **str** | Time Zone | [optional] 
**report_id** | **str** | Unique identifier generated for every reports | [optional] 
**organization_id** | **str** | CyberSource Merchant Id | [optional] 
**queued_time** | **datetime** | Specifies the time of the report in queued  in ISO 8601 format | [optional] 
**report_generating_time** | **datetime** | Specifies the time of the report started to generate  in ISO 8601 format | [optional] 
**report_completed_time** | **datetime** | Specifies the time of the report completed the generation  in ISO 8601 format | [optional] 
**subscription_type** | **str** | Specifies whether the subscription created is either Custom, Standard or Classic  | [optional] 
**group_id** | **str** | Id for selected group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


