# AccessTokenResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Created JWT token. | [optional] 
**token_type** | **str** | Bearer. | [optional] 
**refresh_token** | **str** | Newly created JWT token for initial request or if refresh token expired, else the same refresh token as in the request. | [optional] 
**expires_in** | **int** | Number of seconds left till the access token gets expired. | [optional] 
**scope** | **str** | List of permissions for APIs. | [optional] 
**refresh_token_expires_in** | **int** | Number of seconds left till the refresh token gets expired. | [optional] 
**client_status** | **str** | Successful response can be returned only if client status is active. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


