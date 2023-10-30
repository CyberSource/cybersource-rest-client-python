# Boardingv1registrationsOrganizationInformationOwners

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | 
**birth_date** | **date** | &#x60;Format: YYYY-MM-DD&#x60; Example 2016-08-11 equals August 11, 2016  | 
**is_primary** | **bool** | Determines whether the owner is the Primary owner of the organization | 
**ssn** | **str** | Social Security Number | [optional] 
**passport_number** | **str** | Passport number | [optional] 
**passport_country** | **str** |  | [optional] 
**job_title** | **str** |  | 
**has_significant_responsability** | **bool** | Determines whether owner has significant responsibility to control, manage or direct the company | 
**ownership_percentage** | **float** | Determines the percentage of ownership this owner has. For the primary owner the percentage can be from 0-100; for other owners the percentage can be from 25-100 and the sum of ownership accross owners cannot exceed 100 | 
**phone_number** | **str** |  | 
**email** | **str** |  | 
**address** | [**Boardingv1registrationsOrganizationInformationBusinessInformationAddress**](Boardingv1registrationsOrganizationInformationBusinessInformationAddress.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


