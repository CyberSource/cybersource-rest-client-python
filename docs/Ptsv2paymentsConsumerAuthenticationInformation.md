# Ptsv2paymentsConsumerAuthenticationInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cavv** | **str** | Cardholder authentication verification value (CAVV). | [optional] 
**cavv_algorithm** | **str** | Algorithm used to generate the CAVV for Visa Secure or the UCAF authentication data for Mastercard Identity Check.  | [optional] 
**eci_raw** | **str** | Raw electronic commerce indicator (ECI). For the description and requirements, see \&quot;Payer Authentication,\&quot; page 180. | [optional] 
**pares_status** | **str** | Payer authentication response status. For the description and requirements, see \&quot;Payer Authentication,\&quot; page 180.  | [optional] 
**veres_enrolled** | **str** | Verification response enrollment status. For the description and requirements, see \&quot;Payer Authentication,\&quot; page 180. | [optional] 
**xid** | **str** | Transaction identifier. For the description and requirements, see \&quot;Payer Authentication,\&quot; page 180. | [optional] 
**ucaf_authentication_data** | **str** | Universal cardholder authentication field (UCAF) data.  For the description and requirements, see \&quot;Payer Authentication,\&quot; page 180.  | [optional] 
**ucaf_collection_indicator** | **str** | Universal cardholder authentication field (UCAF) collection indicator.  For the description and requirements, see \&quot;Payer Authentication,\&quot; page 180.  **CyberSource through VisaNet**\\ The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR7 - Position: 5 - Field: Mastercard Electronic Commerce Indicators—-UCAF Collection Indicator  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


