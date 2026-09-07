# UnifiedriskDevicePointOfSale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attended_indicator** | **bool** | Card acceptor representative in attendance at the point of service during the transaction. When an acceptor&#39;s terminal is semi-attended (for example, multiple terminals supervised by a single clerk), | [optional] 
**card_data_entry_mode** | **str** | Entry mode of the card data for the transaction; possible values are: CDFL CardOnFile Card information are stored on a file. ICPY ICCProximity ICC contactless proximity MGST MagneticStripe ICCY ICCCon | [optional] 
**card_present** | **bool** | Indicates whether the transaction has been initiated by a card physically present (true) or not (false). | [optional] 
**cardholder_activated** | **bool** | Indicates whether the automated device was operated solely by the cardholder or not (for example, vending machine, automated fuel dispenser, ATM, kiosk, etc.). | [optional] 
**cardholder_present** | **str** | Indicates whether the transaction has been initiated in presence of the cardholder or not. It can assume multiple values (e.g. \&quot;cardholder present\&quot;, \&quot;cardholder not present telephone\&quot;, etc). | [optional] 
**e_commerce_data** | **str** | This is a free text field that can be used if additional e-commerce data is available. Please note that this field should not contain any cardholder data or sensitive authentication data (SAD), as def | [optional] 
**e_commerce_indicator** | **bool** | Indicates whether the point of service is an e-commerce one (true) or not (false). When true, the cardPresent field is expected to be set to false. | [optional] 
**icc_fallback_indicator** | **bool** | Indicates a chip data fallback, where the chip cannot be read due to a technical issue with the chip which results in the technology \&quot;falling back\&quot; from ICC to a magnetic stripe transaction. | [optional] 
**ip_address** | **str** | IP address of point of service terminal | [optional] 
**magnetic_stripe_fallback_indicator** | **bool** | Indicates a magstripe fallback where the magnetic strip cannot be read which results in the technology \&quot;falling back\&quot; to manually keying the card details into the pos. | [optional] 
**moto_indicator** | **bool** | Indicates whether the context of the point of service is a MOTO one (true) or not (false). When true, the cardPresent field is expected to be set to false. | [optional] 
**partial_approval_supported** | **bool** | Indicates whether the point of service supports partial approval or not. true: partial approval is supported false: partial approval is not supported | [optional] 
**security_characteristics** | **str** | This fields identifies the security characteristics of the communication link in the card acceptance process; possible values are: CETE CardholderEndToEndEncryption CPTE CardholderPointToPointEncrypti | [optional] 
**storage_location** | **str** | This field details the location where the payments credentials (tipically a card number or payment token) are stored. This is only applicable to payments where the credentials are stored by or on beha | [optional] 
**unattended_level_category** | **str** | Card scheme defined transaction category level on an unattended terminal. It identifies the type of terminal. The values are typically mandated by the card scheme being used. Examples for Mastercard a | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


