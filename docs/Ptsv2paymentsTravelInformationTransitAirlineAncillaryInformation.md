# Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_number** | **str** | Ticket number, which consists of the carrier code, form, and serial number, without the check digit. Important This field is required in the U.S. in order for you to qualify for either the custompayment service (CPS) or the electronic interchange reimbursement fee (EIRF)program.  | [optional] 
**passenger_name** | **str** | Name of the passenger. If the passenger’s name is not available, this value is the cardholder’s name. If neither the passenger’s name nor the cardholder’s name is available,this value is a description of the ancillary purchase.Important This field is required in the U.S. in order for you to qualify for either the custom payment service (CPS) or the electronic interchange reimbursement fee (EIRF) program.  | [optional] 
**connected_ticket_number** | **str** | Name of the passenger. If the passenger’s name is not available, this value is the cardholder’s name. If neither the passenger’s name nor the cardholder’s name is available,this value is a description of the ancillary purchase. Important This field is required in the U.S. in order for you to qualify for either the custom payment service (CPS) or the electronic interchange reimbursement fee (EIRF) program.  | [optional] 
**credit_reason_indicator** | **str** | Reason for the credit. Possible values: - A: Cancellation of the ancillary passenger transport purchase. - B: Cancellation of the airline ticket and the passenger transport ancillary purchase. - C: Cancellation of the airline ticket. - O: Other. - P: Partial refund of the airline ticket. Format: English characters only.  | [optional] 
**service** | [**list[Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService]**](Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


