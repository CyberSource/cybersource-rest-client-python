# UnifiedriskTerminalAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | First line of the terminal&#39;s physical address (street number and name), used for geographic risk analysis and terminal location verification | [optional] 
**address_line2** | **str** | Second line of the terminal&#39;s address for additional location details (building name, floor, suite) | [optional] 
**address_line3** | **str** | Third line of the terminal&#39;s address for further location details | [optional] 
**address_type** | **str** | Type classification of the terminal address (e.g., BRANCH, ATM_INDOOR, ATM_OUTDOOR, KIOSK). Used for terminal risk profiling | [optional] 
**country** | **str** | ISO 3166-1 alpha-3 country code for the terminal&#39;s physical location (e.g., GBR, USA, AUS) | [optional] 
**administrative_area** | **str** | State, province, or region of the terminal&#39;s physical location, used for regional fraud pattern analysis | [optional] 
**latitude** | **float** | Geographic latitude coordinate of the terminal&#39;s physical location in decimal degrees, used for proximity and geolocation risk signals | [optional] 
**longitude** | **float** | Geographic longitude coordinate of the terminal&#39;s physical location in decimal degrees, used for proximity and geolocation risk signals | [optional] 
**postal_code** | **str** | Postal code of the terminal&#39;s physical location, used for geographic risk clustering and distance-to-home fraud signals | [optional] 
**locality** | **str** | City or town of the terminal&#39;s physical location, used for regional risk analysis and cardholder distance calculation | [optional] 
**full_address** | **str** | Complete concatenated address of the terminal as a single string, including all lines, locality, postcode, and country | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


