# Ptsv2paymentreferencesTravelInformationAutoRental

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Merchant to send their auto rental company name  | [optional] 
**affiliate_name** | **str** | When merchant wants to send the affiliate name.  | [optional] 
**rental_address** | [**Ptsv2paymentsTravelInformationAutoRentalRentalAddress**](Ptsv2paymentsTravelInformationAutoRentalRentalAddress.md) |  | [optional] 
**return_address** | [**Ptsv2paymentsTravelInformationAutoRentalReturnAddress**](Ptsv2paymentsTravelInformationAutoRentalReturnAddress.md) |  | [optional] 
**return_date_time** | **str** | Date/time the auto was returned to the rental agency. Format: &#x60;&#x60;yyyy-MM-dd HH-mm-ss z&#x60;&#x60; This field is supported for Visa, MasterCard, and American Express.  | [optional] 
**rental_date_time** | **str** | Date/time the auto was picked up from the rental agency. Format: &#x60;yyyy-MM-dd HH-mm-ss z&#x60; This field is supported for Visa, MasterCard, and American Express.  | [optional] 
**customer_name** | **str** | Name of the individual making the rental agreement.  Valid data lengths by card:  |Card Specific Validation|VISA|MasterCard|Discover|AMEX| |--- |--- |--- |--- | | Filed Length| 40| 40| 29| 26| | Field Type| AN| ANS| AN| AN| | M/O/C| O| M| M| M|  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


