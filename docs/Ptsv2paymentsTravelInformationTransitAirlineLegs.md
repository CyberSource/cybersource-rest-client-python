# Ptsv2paymentsTravelInformationTransitAirlineLegs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | Carrier Code: IATA1 code for the carrier for this leg of the trip.  | [optional] 
**flight_number** | **str** | Flight number for this leg of the trip.  | [optional] 
**originating_airport_code** | **str** | IATA1 code for the originating airport for this leg of the trip.  | [optional] 
**_class** | **str** | IATA1 code for the class of service for this leg of the trip.  | [optional] 
**stopover_indicator** | **int** | Code that indicates whether a stopover is allowed on this leg of the trip. Possible Values: O(capital letter \&quot;O\&quot;): stopover allowed.  X(capital letter \&quot;X\&quot;): Stopover not allowed.  | [optional] 
**departure_date** | **int** | Departure date for the first leg of the trip. Format: YYYYMMDD.  | [optional] 
**destination_airport_code** | **str** | IATA1 code for the destination airport for this leg of the trip.  | [optional] 
**fare_basis** | **str** | Code for the fare basis for this leg of the trip. The fare basis is assigned by the carriers and indicates a particular ticket type, such as business class or discounted/nonrefundable.  | [optional] 
**depart_tax_amount** | **str** | Amount of departure tax for this leg of the trip.  | [optional] 
**conjunction_ticket** | **str** | Ticket that contains additional coupons for this leg of the trip on an itinerary that has more than four segments.  | [optional] 
**exchange_ticket_number** | **str** | New ticket number that is issued when the ticket is exchanged for this leg of the trip.  | [optional] 
**coupon_number** | **str** | Each leg on the ticket requires a separate coupon, and each coupon is identified by the coupon number.  | [optional] 
**departure_time** | **int** | Time of departure for this leg of the trip. The format is military time and HHMM: If not all zeros, then the hours must be 00-23 and the minutes must be 00-59  | [optional] 
**departure_time_meridian** | **str** | AM or PM for the departure time. Possible values: - A: 12:00 midnight to 11:59 a.m. - P: 12:00 noon to 11:59 p.m  | [optional] 
**arrival_time** | **int** | Time of arrival for this leg of the trip. The format is military time and HHMM: If not all zeros, then the hours must be 00-23 and the minutes must be 00-59  | [optional] 
**arrival_time_meridian** | **str** | AM or PM for the arrival time for this leg of the trip. Possible values: - A: 12:00 midnight to 11:59 a.m. - P: 12:00 noon to 11:59 p.m. Format: English characters only  | [optional] 
**endorsements_restrictions** | **str** | Notes or notations about endorsements and restrictions for this leg of the trip. Endorsements can be notations added by the travel agency, including mandatory government required notations such as value added tax. Restrictions are limitations for the ticket based on the type of fare, such as a nonrefundable tic.  | [optional] 
**total_fare_amount** | **str** | Total fare for this leg of the trip.  | [optional] 
**fee_amount** | **str** | Fee for this leg of the trip, such as an airport fee or country fee.  | [optional] 
**tax_amount** | **str** | Tax for this leg of the trip  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


