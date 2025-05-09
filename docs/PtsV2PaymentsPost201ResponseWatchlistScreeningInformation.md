# PtsV2PaymentsPost201ResponseWatchlistScreeningInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_country_confidence** | **int** | Likelihood that the country associated with the customer&#39;s IP address was identified correctly. Returns a value from 1–100, where 100 indicates the highest likelihood. If the country cannot be determined, the value is –1.  | [optional] 
**info_codes** | **list[str]** | Returned when the Denied Parties List check (first two codes) or the export service (all others) would have declined the transaction. This field can contain one or more of these values: - &#x60;MATCH-DPC&#x60;: Denied Parties List match. - &#x60;UNV-DPC&#x60;: Denied Parties List unavailable. - &#x60;MATCH-BCO&#x60;: Billing country restricted. - &#x60;MATCH-EMCO&#x60;: Email country restricted. - &#x60;MATCH-HCO&#x60;: Host name country restricted. - &#x60;MATCH-IPCO&#x60;: IP country restricted. - &#x60;MATCH-SCO&#x60;: Shipping country restricted.  | [optional] 
**watch_list** | [**PtsV2PaymentsPost201ResponseWatchlistScreeningInformationWatchList**](PtsV2PaymentsPost201ResponseWatchlistScreeningInformationWatchList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


