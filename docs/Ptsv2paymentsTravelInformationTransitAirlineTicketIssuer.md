# Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | IATA2 airline code. Format: English characters only. Required for Mastercard; optional for all other card types.  | [optional] 
**name** | **str** | Name of the ticket issuer. If you do not include this field, CyberSource uses the value for your merchant name that is in the CyberSource merchant configuration database.  | [optional] 
**address** | **str** | Address of the company issuing the ticket.  | [optional] 
**locality** | **str** | City in which the transaction occurred. If the name of the city exceeds 18 characters, use meaningful abbreviations. Format: English characters only. Optional request field.  | [optional] 
**administrative_area** | **str** | State in which transaction occured.  | [optional] 
**postal_code** | **str** | Zip code of the city in which transaction occured.  | [optional] 
**country** | **str** | Country in which transaction occured.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


