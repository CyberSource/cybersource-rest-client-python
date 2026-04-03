# Acpv1tokensDeviceInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agent** | **str** | Base64 Encoded userAgent string of the connecting client application, with no padding.   User agent string of the connecting client application.   Conditionality:   - Required for browsers - Optional for non-browsers  | [optional] 
**application_name** | **str** | Name of the connecting client application. | 
**fingerprint_session_id** | **str** | Device Fingerprinting Session identifier. | 
**country** | **str** | ISO 3166-1 alpha-2 country code. The country where the Consumer is accessing the service from. | [optional] 
**device_data** | [**Acpv1tokensDeviceInformationDeviceData**](Acpv1tokensDeviceInformationDeviceData.md) |  | 
**ip_address** | **str** | IP address of the consumer&#39;s device. | 
**client_device_id** | **str** | Unique identifier of the consumer&#39;s device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


