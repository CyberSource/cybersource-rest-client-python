# RequestBody1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Valid CyberSource organizationId | [optional] 
**report_definition_name** | **str** | Valid Report Definition Name | 
**report_fields** | **list[str]** |  | 
**report_mime_type** | **str** |  | 
**report_frequency** | **str** | The frequency for which subscription is created. | 
**report_name** | **str** |  | 
**timezone** | **str** |  | 
**start_time** | **str** | The hour at which the report generation should start. It should be in hhmm format. | 
**start_day** | **int** | This is the start day if the frequency is WEEKLY or MONTHLY. The value varies from 1-7 for WEEKLY and 1-31 for MONTHLY. For WEEKLY 1 means Sunday and 7 means Saturday. By default the value is 1. | [optional] 
**report_filters** | **dict(str, list[str])** | List of filters to apply | [optional] 
**report_preferences** | [**ReportingV3ReportsIdGet200ResponseReportPreferences**](ReportingV3ReportsIdGet200ResponseReportPreferences.md) |  | [optional] 
**group_name** | **str** | Valid GroupName | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


