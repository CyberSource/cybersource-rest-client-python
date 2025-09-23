# Riskv1decisionsDeviceInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookies_accepted** | **str** | Whether the customer&#39;s browser accepts cookies. This field can contain one of the following values: - &#x60;yes&#x60;: The customer&#39;s browser accepts cookies. - &#x60;no&#x60;: The customer&#39;s browser does not accept cookies.  | [optional] 
**ip_address** | **str** | IP address of the customer.  #### Used by **Authorization, Capture, and Credit** Optional field.  | [optional] 
**host_name** | **str** | DNS resolved hostname from &#x60;ipAddress&#x60;. | [optional] 
**fingerprint_session_id** | **str** | Field that contains the session ID that you send to Decision Manager to obtain the device fingerprint information. The string can contain uppercase and lowercase letters, digits, hyphen (-), and underscore (_). However, do not use the same uppercase and lowercase letters to indicate different session IDs.  The session ID must be unique for each merchant ID. You can use any string that you are already generating, such as an order number or web session ID.  The session ID must be unique for each page load, regardless of an individual&#39;s web session ID. If a user navigates to a profiled page and is assigned a web session, navigates away from the profiled page, then navigates back to the profiled page, the generated session ID should be different and unique. You may use a web session ID, but it is preferable to use an application GUID (Globally Unique Identifier). This measure ensures that a unique ID is generated every time the page is loaded, even if it is the same user reloading the page.  | [optional] 
**http_browser_email** | **str** | Email address set in the customer&#39;s browser, which may differ from customer email.  | [optional] 
**user_agent** | **str** | Customer&#39;s browser as identified from the HTTP header data. For example, &#x60;Mozilla&#x60; is the value that identifies the Netscape browser.  | [optional] 
**raw_data** | [**list[Ptsv2paymentsDeviceInformationRawData]**](Ptsv2paymentsDeviceInformationRawData.md) |  | [optional] 
**http_accept_browser_value** | **str** | Value of the Accept header sent by the customer&#39;s web browser. **Note** If the customer&#39;s browser provides a value, you must include it in your request.  | [optional] 
**http_accept_content** | **str** | The exact content of the HTTP accept header.  | [optional] 
**http_browser_language** | **str** | Value represents the browser language as defined in IETF BCP47. Example:en-US, refer  https://en.wikipedia.org/wiki/IETF_language_tag for more details.  | [optional] 
**http_browser_java_enabled** | **bool** | A Boolean value that represents the ability of the cardholder browser to execute Java. Value is returned from the navigator.javaEnabled property. Possible Values:True/False  | [optional] 
**http_browser_java_script_enabled** | **bool** | A Boolean value that represents the ability of the cardholder browser to execute JavaScript. Possible Values:True/False. **Note**: Merchants should be able to know the values from fingerprint details of cardholder&#39;s browser.  | [optional] 
**http_browser_color_depth** | **str** | Value represents the bit depth of the color palette for displaying images, in bits per pixel. Example : 24, refer https://en.wikipedia.org/wiki/Color_depth for more details  | [optional] 
**http_browser_screen_height** | **str** | Total height of the Cardholder&#39;s scree in pixels, example: 864.  | [optional] 
**http_browser_screen_width** | **str** | Total width of the cardholder&#39;s screen in pixels. Example: 1536.  | [optional] 
**http_browser_time_difference** | **str** | Time difference between UTC time and the cardholder browser local time, in minutes, Example:300  | [optional] 
**user_agent_browser_value** | **str** | Value of the User-Agent header sent by the customer&#39;s web browser. Note If the customer&#39;s browser provides a value, you must include it in your request.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


