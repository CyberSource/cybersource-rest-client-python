# RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type** | **str** | Contains the record type of the postal code with which the address was matched.  #### U.S. Addresses Depending on the quantity and quality of the address information provided, this field contains one or two characters:  - One character: sufficient correct information was provided to result in accurate matching. - Two characters: standardization would provide a better address if more or better input address information were available. The second character is D (default).  Blank fields are unassigned. When an address cannot be standardized, how the input data was parsed determines the address type. In this case, standardization may indicate a street, rural route, highway contract, general delivery, or PO box.   #### All Other Countries This field contains one of the following values: - P: Post. - S: Street. - x: Unknown.  | [optional] 
**bar_code** | [**RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationBarCode**](RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationBarCode.md) |  | [optional] 
**applicable_region** | **str** | Value can be - Canada - US - International The values of errorCode and statusCode mean different things depending on the applicable region. Refer to the guide for more info.  | [optional] 
**error_code** | **str** | Four-character error code returned for Canadian, US and international addresses. For possible values, see Verification Services guide. The meaning of the errorCode depends on value of applicableRegion.  | [optional] 
**status_code** | **str** | Four-to-ten character status code returned for Canadian, US and international addresses. For possible values, see Verification Services guide. The meaning of the errorCode depends on value of applicableRegion.  | [optional] 
**care_of** | **str** | Care of data dropped from the standard address. | [optional] 
**match_score** | **int** | Indicates the probable correctness of the address match. Returned for U.S. and Canadian addresses. Returns a value from 0-9, where 0 is most likely to be correct and 9 is least likely to be correct, or -1 if there is no address match.  | [optional] 
**standard_address** | [**RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress**](RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


