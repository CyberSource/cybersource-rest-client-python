# Riskv1authenticationsetupsTokenInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transient_token** | **str** | A temporary ID that represents the customer&#39;s payment data (which is securely stored in Visa Data Centers). Flex Microform generates this ID and sets it to expire within 15 minutes from when the ID is generated or until the first payment authorization is carried out (whichever occurs first).  Valid value for the ID is a 64-character, alphanumeric string.  Example: 1D08M4YB968R1F7YVL4TBBKYVNRIR02VZFH9CBYSQIJJXORPI1NK5C98D7F6EB53  | [optional] 
**jti** | **str** | TMS Transient Token, 64 hexadecimal id value representing captured payment credentials (including Sensitive Authentication Data, e.g. CVV).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


