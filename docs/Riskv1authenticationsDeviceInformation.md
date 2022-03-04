# Riskv1authenticationsDeviceInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address of the customer.  #### Used by **Authorization, Capture, and Credit** Optional field.  | [optional] 
**raw_data** | [**list[Ptsv2paymentsDeviceInformationRawData]**](Ptsv2paymentsDeviceInformationRawData.md) |  | [optional] 
**http_accept_browser_value** | **str** | Value of the Accept header sent by the customer’s web browser. **Note** If the customer’s browser provides a value, you must include it in your request.  | [optional] 
**http_accept_content** | **str** | The exact content of the HTTP accept header.  | [optional] 
**http_browser_language** | **str** | Value represents the browser language as defined in IETF BCP47. Example:en-US, refer  https://en.wikipedia.org/wiki/IETF_language_tag for more details.  | [optional] 
**http_browser_java_enabled** | **bool** | A Boolean value that represents the ability of the cardholder browser to execute Java. Value is returned from the navigator.javaEnabled property. Possible Values:True/False  | [optional] 
**http_browser_java_script_enabled** | **bool** | A Boolean value that represents the ability of the cardholder browser to execute JavaScript. Possible Values:True/False. **Note**: Merchants should be able to know the values from fingerprint details of cardholder&#39;s browser.  | [optional] 
**http_browser_color_depth** | **str** | Value represents the bit depth of the color palette for displaying images, in bits per pixel. Example : 24, refer https://en.wikipedia.org/wiki/Color_depth for more details  | [optional] 
**http_browser_screen_height** | **str** | Total height of the Cardholder&#39;s scree in pixels, example: 864.  | [optional] 
**http_browser_screen_width** | **str** | Total width of the cardholder&#39;s screen in pixels. Example: 1536.  | [optional] 
**http_browser_time_difference** | **str** | Time difference between UTC time and the cardholder browser local time, in minutes, Example:300  | [optional] 
**user_agent_browser_value** | **str** | Value of the User-Agent header sent by the customer’s web browser. Note If the customer’s browser provides a value, you must include it in your request.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


