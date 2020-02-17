# Ptsv2paymentsTravelInformationTransitAirline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booking_reference_number** | **str** | Reference number for the airline booking. Required if ticket numbers are not issued.  | [optional] 
**carrier_name** | **str** | Name of the airline. If you do not include this field, CyberSource uses the value for your merchant name that is in the CyberSource merchant configuration database.  | [optional] 
**ticket_issuer** | [**Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer**](Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.md) |  | [optional] 
**ticket_number** | **str** | Ticket number. Format: English characters only  | [optional] 
**check_digit** | **str** | Check digit for the ticket number. CyberSource recommends that you validate the check digit. With Discover and Diners Club, a valid ticket number has these characteristics: - The value is numeric. - The first three digits are a valid IATA2 license plate carrier code. - The last digit is a check digit or zero (0). - All remaining digits are nonzero.  | [optional] 
**restricted_ticket_indicator** | **int** | Flag that indicates whether or not the ticket is restricted (nonrefundable). Possible values: - 0: No restriction (refundable) - 1: Restricted (nonrefundable)  | [optional] 
**transaction_type** | **int** | Type of charge. Possible values: - 01: Charge is for an airline ticket - 02: Charge is for an item that is not an airline ticket  | [optional] 
**extended_payment_code** | **str** | Airline process identifier. This value is the airline’s three-digit IATA1 code which is used to process extended payment airline tickets..  | [optional] 
**passenger_name** | **str** | Name of the passenger to whom the ticket was issued. This will always be a single passenger&#39;s name. If there are more than one passengers, provide only the primary passenger&#39;s name. Do not include special characters such as commas, hyphens, or apostrophes. Only ASCII characters are supported.  | [optional] 
**customer_code** | **str** | 1.Reference number or code that identifies the cardholder. 2. Code provided by the cardholder. 3. Address of the ticket issuer. The first 13 characters will appear onthe cardholder’s statement. 4. Customer reference.  | [optional] 
**document_type** | **str** | Airline document type code that specifies the purpose of the transaction. For the possible values, see Appendix A, \&quot;Airline Document Type Codes\&quot;.  | [optional] 
**document_number** | **str** | Ticket number or a value that might be a booking reference number.  | [optional] 
**document_number_of_parts** | **int** | Number of travel legs. Numbering for the travel legs: 0 to 3.  | [optional] 
**invoice_number** | **str** | Invoice number for the airline transaction.  | [optional] 
**invoice_date** | **int** | Invoice date. The format is YYYYMMDD. If this value is included in the request, it is used in the creation of the invoice number. See \&quot;Invoice Number,\&quot;  | [optional] 
**additional_charges** | **str** | Description of the charge if the charge does not involve an airline ticket. For example: Excess baggage.  | [optional] 
**total_fee_amount** | **str** | Total fee for the ticket. This value cannot exceed 99999999999999999999 (twenty 9s).  | [optional] 
**clearing_sequence** | **str** | Total number of captures when requesting multiple partial captures for one authorization. Used along with airlineData_clearingCount to keep track of which capture is beingprocessed. For example, the second of five captures would be passed to CyberSource as airlineData_clearingSequence &#x3D; 2 and airlineData_clearingCount &#x3D; 5.  | [optional] 
**clearing_count** | **str** | Total number of clearing messages associated with the authorization request. Format: English characters only.  | [optional] 
**total_clearing_amount** | **str** | Total clearing amount for all transactions in the clearing count set. If this field is not set and if the total amount from the original authorization is not NULL, CyberSource sets the total clearing amount to the total amount from the original authorization.  | [optional] 
**number_of_passengers** | **int** | Number of passengers for whom the ticket was issued. If you do not include this field in your request, CyberSource uses a default value of 1.  | [optional] 
**reservation_system_code** | **str** | Code that specifies the computerized reservation system used to make the reservation and purchase the ticket. Format: English characters only  | [optional] 
**process_identifier** | **str** | Airline process identifier. This value is the airline’s three-digit IATA1 code which is used to process extended payment airline tickets.  | [optional] 
**ticket_issue_date** | **str** | Date on which the transactionoccurred. Format: YYYYMMDD  | [optional] 
**electronic_ticket_indicator** | **bool** | Flag that indicates whether an electronic ticket was issued. Possible values: - true - false  | [optional] 
**original_ticket_number** | **str** | Original ticket number when the transaction is for a replacement ticket.  | [optional] 
**purchase_type** | **str** | Type of purchase. Possible values: - EXC: Exchange ticket - MSC: Miscellaneous (not a ticket purchase and not a transaction related to an exchange ticket) - REF: Refund - TKT: Ticket Format: English characters only.  | [optional] 
**credit_reason_indicator** | **str** | Reason for the credit. Possible values: - A: Cancellation of the ancillary passenger transport purchase. - B: Cancellation of the airline ticket and the passenger transport ancillary purchase. - C: Cancellation of the airline ticket. - O: Other. - P: Partial refund of the airline ticket.  | [optional] 
**ticket_change_indicator** | **str** | Type of update. Possible values: - C: Change to the existing ticket. - N: New ticket. Format: English characters only  | [optional] 
**plan_number** | **str** | Plan number based on the fare. This value is provided by the airline. Format: English characters only  | [optional] 
**arrival_date** | **str** | Date of arrival for the last leg of the trip. Format: MMDDYYYY English characters only.  | [optional] 
**restricted_ticket_desciption** | **str** | Text that describes the ticket limitations, such as nonrefundable. Format: English characters only.  | [optional] 
**exchange_ticket_amount** | **str** | Amount of the exchanged ticket. Format: English characters only.  | [optional] 
**exchange_ticket_fee_amount** | **str** | Fee for exchanging the ticket. Format: English characters only  | [optional] 
**reservation_type** | **str** | Type of journey such as one way or round trip.  | [optional] 
**boarding_fee_amount** | **str** | Boarding fee.  | [optional] 
**legs** | [**list[Ptsv2paymentsTravelInformationTransitAirlineLegs]**](Ptsv2paymentsTravelInformationTransitAirlineLegs.md) |  | [optional] 
**ancillary_information** | [**Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformation**](Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


