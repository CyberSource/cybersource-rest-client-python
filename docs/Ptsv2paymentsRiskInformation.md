# Ptsv2paymentsRiskInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**Ptsv2paymentsRiskInformationProfile**](Ptsv2paymentsRiskInformationProfile.md) |  | [optional] 
**event_type** | **str** | Specifies one of the following types of events: - login - account_creation - account_update For regular payment transactions, do not send this field.  | [optional] 
**buyer_history** | [**Ptsv2paymentsRiskInformationBuyerHistory**](Ptsv2paymentsRiskInformationBuyerHistory.md) |  | [optional] 
**auxiliary_data** | [**list[Ptsv2paymentsRiskInformationAuxiliaryData]**](Ptsv2paymentsRiskInformationAuxiliaryData.md) |  | [optional] 
**store** | [**Ptsv2paymentsRiskInformationStore**](Ptsv2paymentsRiskInformationStore.md) |  | [optional] 
**authentication_type** | **str** | • 01 &#x3D; Static Passcode • 02 &#x3D; SMS OTP • 03 &#x3D; Key fob or EMV card reader OTP • 04 &#x3D; App OTP • 05 &#x3D; OTP Other • 07 &#x3D; OOB Biometrics • 08 &#x3D; OOB Login • 09 &#x3D; OOB Other • 10 &#x3D; Other • 11 &#x3D; Push Confirmation • 12 &#x3D; Decoupled • 13 &#x3D; WebAuthn • 14 &#x3D; SPC • 15 &#x3D; Behavioural biometrics  | [optional] 
**pickup_days** | **float** | Number of days between transaction date and rental pickup date  | [optional] 
**external_score** | [**Ptsv2paymentsRiskInformationExternalScore**](Ptsv2paymentsRiskInformationExternalScore.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


