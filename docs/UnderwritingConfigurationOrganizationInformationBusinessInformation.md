# UnderwritingConfigurationOrganizationInformationBusinessInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_identifier** | **str** | Tax ID for the business | 
**country_registration** | **str** | Country where the business is registered. Two character country code, ISO 3166-1 alpha-2. | 
**legal_name** | **str** | The legally registered name of the business | 
**doing_business_as** | **str** | The DBA of the business. | 
**business_description** | **str** | Short description of the Business | 
**registration_number** | **str** | Registration ID for Enterprise Merchant | [optional] 
**stock_exchange** | **str** | Which stock exchange is the company trading in? | [optional] 
**ticker_symbol** | **str** | Stock Symbol on the exchange | [optional] 
**start_date** | **date** | When did Business start. Format: YYYY-MM-DD Example 2016-08-11 equals August 11, 2016 | 
**merchant_category_code** | **str** | Industry standard Merchant Category Code (MCC) | 
**mcc_description** | **str** | MCC Description | [optional] 
**website_url** | **str** | Website for the Business | [optional] 
**business_type** | **str** | Business type  Possible values: - PARTNERSHIP - SOLE_PROPRIETORSHIP - CORPORATION - LLC - NON_PROFIT - TRUST | 
**local_mcc** | **list[str]** |  | [optional] 
**country_phone_number** | **str** | Country of the Business phone number. Two character country code, ISO 3166-1 alpha-2. | 
**phone_number** | **str** | Business Phone Number | 
**email** | **str** | Business Email Address | 
**what_your_company_does** | **str** | What your company does and how you market your service | [optional] 
**address** | [**UnderwritingConfigurationOrganizationInformationBusinessInformationAddress**](UnderwritingConfigurationOrganizationInformationBusinessInformationAddress.md) |  | [optional] 
**trading_address** | [**UnderwritingConfigurationOrganizationInformationBusinessInformationTradingAddress**](UnderwritingConfigurationOrganizationInformationBusinessInformationTradingAddress.md) |  | [optional] 
**business_contact** | [**UnderwritingConfigurationOrganizationInformationBusinessInformationBusinessContact**](UnderwritingConfigurationOrganizationInformationBusinessInformationBusinessContact.md) |  | [optional] 
**business_details** | [**UnderwritingConfigurationOrganizationInformationBusinessInformationBusinessDetails**](UnderwritingConfigurationOrganizationInformationBusinessInformationBusinessDetails.md) |  | [optional] 
**owner_information** | [**list[UnderwritingConfigurationOrganizationInformationBusinessInformationOwnerInformation]**](UnderwritingConfigurationOrganizationInformationBusinessInformationOwnerInformation.md) |  | [optional] 
**director_information** | [**list[UnderwritingConfigurationOrganizationInformationBusinessInformationDirectorInformation]**](UnderwritingConfigurationOrganizationInformationBusinessInformationDirectorInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


