# Acpv1tokensAssuranceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_type** | **str** | Type of the verification data.   Possible values:   - &#x60;CARDHOLDER&#x60; (Default)   - &#x60;DEVICE&#x60;  | [optional] 
**verification_entity** | **str** | Entity performing the verification.   Possible value:     - &#x60;10&#x60; - VISA (Default)  | [optional] 
**verification_events** | **list[str]** | Event where the verification occurred.   Possible values:     - &#x60;01&#x60; - Payment transaction   - &#x60;02&#x60; - Add card/Card enrollment   - &#x60;03&#x60; - Profile access   - &#x60;04&#x60; - Account verification  | [optional] 
**verification_method** | **str** | Method of the verification.   Possible values:     - &#x60;02&#x60; - App-based authentication   - &#x60;04&#x60; - One-time passcode   - &#x60;21&#x60; - Visa Token Service step-up: Device binding   - &#x60;22&#x60; - Visa Token Service step-up: Cardholder verification   - &#x60;23&#x60; - FIDO2  | 
**verification_results** | **str** | Result of the verification.   Possible values:     - &#x60;01&#x60; - Verified   - &#x60;02&#x60; - Not Verified   - &#x60;03&#x60; - Not performed   - &#x60;04&#x60; - Not required   - &#x60;21&#x60; - Not allowed  | 
**verification_timestamp** | **str** | Date and time the verification occurred. UTC time in Unix epoch format. | 
**authentication_context** | [**Acpv1tokensAuthenticationContext**](Acpv1tokensAuthenticationContext.md) |  | [optional] 
**authenticated_identities** | [**Acpv1tokensAuthenticatedIdentities**](Acpv1tokensAuthenticatedIdentities.md) |  | [optional] 
**additional_data** | **str** | Additional data related to assurance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


