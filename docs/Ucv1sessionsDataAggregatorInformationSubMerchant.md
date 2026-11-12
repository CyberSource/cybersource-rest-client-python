# Ucv1sessionsDataAggregatorInformationSubMerchant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_acceptor_id** | **str** | Unique identifier assigned by the payment card company to the sub-merchant. | [optional] 
**id** | **str** | The ID you assigned to your sub-merchant.  American Express Direct: String (20)  | [optional] 
**name** | **str** | Sub-merchant&#39;s business name.  #### American Express Direct The maximum length of the sub-merchant name depends on the length of the aggregator name. The combined length for both values must not exceed 36 characters.  | [optional] 
**address1** | **str** | First line of the sub-merchant&#39;s street address.  | [optional] 
**locality** | **str** | Sub-merchant&#39;s city.  | [optional] 
**administrative_area** | **str** | Sub-merchant&#39;s state or province.  | [optional] 
**region** | **str** | Sub-merchant&#39;s region.  **Example**\\ &#x60;NE&#x60; indicates that the sub-merchant is in the northeast region.  | [optional] 
**postal_code** | **str** | Partial postal code for the sub-merchant&#39;s address.  | [optional] 
**country** | **str** | Sub-merchant&#39;s country. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  | [optional] 
**email** | **str** | Sub-merchant&#39;s email address.  **Maximum length for processors**   - American Express Direct: 40  | [optional] 
**phone_number** | **str** | Sub-merchant&#39;s telephone number.  **Maximum length for procesors**   - American Express Direct: 20  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


