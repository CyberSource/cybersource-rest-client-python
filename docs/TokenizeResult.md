# TokenizeResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The Key ID. | [optional] 
**token** | **str** | The generated token. The token replaces card data and is used as the Subscription ID in the CyberSource Simple Order API or SCMP API. | [optional] 
**masked_pan** | **str** | The masked card number displaying the first 6 digits and the last 4 digits. | [optional] 
**card_type** | **str** | The card type. | [optional] 
**timestamp** | **int** | The UTC date and time in milliseconds at which the signature was generated. | [optional] 
**signed_fields** | **str** | Indicates which fields from the response make up the data that is used when verifying the response signature. See the [sample code] (https://github.com/CyberSource/cybersource-flex-samples/blob/master/java/spring-boot/src/main/java/com/cybersource/flex/application/CheckoutController.java) on how to verify the signature. | [optional] 
**signature** | **str** | Flex-generated digital signature. To ensure the values have not been tampered with while passing through the client, verify this server-side using the public key generated from the /keys resource. | [optional] 
**discoverable_services** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


