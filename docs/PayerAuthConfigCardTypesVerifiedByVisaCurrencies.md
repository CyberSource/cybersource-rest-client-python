# PayerAuthConfigCardTypesVerifiedByVisaCurrencies

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_codes** | **list[str]** | Supported currency codes are numeric ISO 4217 codes, such as 840 for US Dollar and 978 for Euro.  For backward compatibility, we also support the &#39;ALL&#39; code, which represents all currencies.  In the UI, &#39;ALL&#39; is displayed as &#39;Default&#39;.  | [optional] 
**acquirer_id** | **str** | The Acquirer ID value, often referred to as the Acquirer BIN, is specific to an Acquirer. The value is created by Cardinal in their system and the Acquirer may not know that the Acquirer ID is different from their Acquiring BIN. It is most often the Acquiring BIN + \&quot;-1000\&quot; but the trailing character can be different. **Note** We will need to double check with Cardinal before setting up the Portfolio Template in production.  | [optional] 
**processor_merchant_id** | **str** | Processor Merchant ID is the Merchant ID assigned by your acquiring bank. This Merchant ID should also be used by your bank to register your account to the card scheme Directory Server for processing Payer Authentication services.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


