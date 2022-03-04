# CreateAdhocReportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Valid CyberSource Organization Id | [optional] 
**report_definition_name** | **str** |  | [optional] 
**report_fields** | **list[str]** | List of fields which needs to get included in a report | [optional] 
**report_mime_type** | **str** | &#39;Format of the report&#39;                  Valid values: - application/xml - text/csv  | [optional] 
**report_name** | **str** | Name of the report | [optional] 
**timezone** | **str** | Timezone of the report | [optional] 
**report_start_time** | **datetime** | Start time of the report | [optional] 
**report_end_time** | **datetime** | End time of the report | [optional] 
**report_filters** | [**Reportingv3reportsReportFilters**](Reportingv3reportsReportFilters.md) |  | [optional] 
**report_preferences** | [**Reportingv3reportsReportPreferences**](Reportingv3reportsReportPreferences.md) |  | [optional] 
**group_name** | **str** | Specifies the group name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


