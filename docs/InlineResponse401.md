# InlineResponse401

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InlineResponse401Links**](InlineResponse401Links.md) |  | [optional] 
**code** | **str** | Valid Values:   * FORBIDDEN_RESPONSE   * VALIDATION_ERROR   * UNSUPPORTED_MEDIA_TYPE   * MALFORMED_PAYLOAD_ERROR   * SERVER_ERROR  | [optional] 
**correlation_id** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**fields** | [**list[InlineResponse401Fields]**](InlineResponse401Fields.md) |  | [optional] 
**localization_key** | **str** | Valid Values:   * cybsapi.forbidden.response   * cybsapi.validation.error   * cybsapi.media.notsupported  | [optional] 
**message** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


