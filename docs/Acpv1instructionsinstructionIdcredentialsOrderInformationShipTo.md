# Acpv1instructionsinstructionIdcredentialsOrderInformationShipTo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **str** | (Conditional) Reference identifier of the address Conditionality - Required when address is already registered with VACP System. Optional for requests when address fields are provided.  | [optional] 
**district** | **str** | Name of the business; Name of the community; c/o Name etc. Notes - Shipping Address - The final recipient&#39;s name will be captured  in deliveryContacts field. Billing Address - The Card Holder or Consumer Name will be recorded as part of Card or Order Information.  | [optional] 
**address1** | **str** | (Conditional) Address line 1 Conditionality - Required when used with the DPA Registration operation in the Management Service APIs Required when address is used as shipping/delivery Address.  | [optional] 
**address2** | **str** | Address line 2. | [optional] 
**address3** | **str** | Address line 3. | [optional] 
**locality** | **str** | (Conditional) Address city Conditionality - When used with the DPA Registration operation in the Management  Service APIs at least one of the following is required   - both city and state - zip Required if this is a shipping address in a valid format for the country  | [optional] 
**administrative_area** | **str** | (Conditional) Address state Recommendation to support ISO 3166-2 format i.e. made up of ISO 3166-1 alpha 2 country code,  followed by an alphanumeric string of 3 characters representing the state or sub-division Conditionality -  When used with the DPA Registration operation in the Management Service APIs at least one of the following is required   - both city and state - zip Required if this is a shipping address in a valid format for the country.  | [optional] 
**country** | **str** | Address country code ISO 3166-1 alpha-2 country code. | 
**postal_code** | **str** | Address zip/postal code Conditionality - When used with the DPA Registration operation in th Management Service APIs  at least one of the following is required.   - both city and state   - zip Required if this is a shipping address in a valid format for the country and has a postal code or zip code  | [optional] 
**create_time** | **str** | Date and time the address was created. UTC time in Unix epoch format. | [optional] 
**last_used_time** | **str** | Date and time the address was last used. UTC time in Unix epoch format. | [optional] 
**first_name** | **str** | First name of the recipient. | [optional] 
**middle_name** | **str** | Middle name of the recipient. | [optional] 
**last_name** | **str** | Last name of the recipient. | [optional] 
**email** | **str** | Consumer-provided email address. | [optional] 
**country_calling_code** | **str** | Phone number country code as defined by the International Telecommunication Union. | 
**phone_number** | **str** | Phone number without country code. | 
**number_is_voice_only** | **bool** | Indicates that the phone number provided is not capable of receiving text messages. | [optional] 
**instructions** | **str** | Consumer-provided delivery instructions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


