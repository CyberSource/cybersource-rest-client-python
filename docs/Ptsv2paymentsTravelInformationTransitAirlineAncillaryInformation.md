# Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_number** | **str** | Ticket number, which consists of the carrier code, form, and serial number, without the check digit. **Important** This field is required in the U.S. in order for you to qualify for either the custom payment service (CPS) or the electronic interchange reimbursement fee (EIRF) program. Format: English characters only. Optional field for ancillary services.  | [optional] 
**passenger_name** | **str** | Name of the passenger. If the passenger&#39;s name is not available, this value is the cardholder&#39;s name. If neither the passenger&#39;s name nor the cardholder&#39;s name is available, this value is a description of the ancillary purchase. **Important** This field is required in the U.S. in order for you to qualify for either the custom payment service (CPS) or the electronic interchange reimbursement fee (EIRF) program. Format: English characters only. Optional field for ancillary service.  | [optional] 
**connected_ticket_number** | **str** | Number for the airline ticket to which the ancillary purchase is connected.  If this purchase has a connection or relationship to another purchase such as a baggage fee for a passenger transport ticket, this field must contain the ticket number for the other purchase.  For a stand-alone purchase, the value for this field must be the same as the value for the &#x60;travelInformation.transit.airline.ancillaryInformation.ticketNumber&#x60; field. **Important** This field is required in the U.S. in order for you to qualify for either the custom payment service (CPS) or the electronic interchange reimbursement fee (EIRF) program. Format: English characters only. Optional request field for ancillary services.  | [optional] 
**credit_reason_indicator** | **str** | Reason for the credit. Possible values: - &#x60;A&#x60;: Cancellation of the ancillary passenger transport purchase. - &#x60;B&#x60;: Cancellation of the airline ticket and the passenger transport ancillary purchase. - &#x60;C&#x60;: Cancellation of the airline ticket. - &#x60;O&#x60;: Other. - &#x60;P&#x60;: Partial refund of the airline ticket. Format: English characters only. Optional field for ancillary services.  | [optional] 
**service** | [**list[Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService]**](Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


