# Ptsv2paymentsProcessingInformationLoanOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of loan based on an agreement between you and the issuer. Examples: AGROCUSTEIO, AGRO-INVEST, BNDES-Type1, CBN, FINAME. This field is supported only for these kinds of payments: - BNDES transactions on CyberSource through VisaNet. - Installment payments with Mastercard on CyberSource through VisaNet in Brazil.  For BNDES transactions, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP07 TCR2, Position: 27-46, Field: Loan Type  For installment payments with Mastercard in Brazil, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP07 TCR4, Position: 5-24,Field: Financing Type  | [optional] 
**asset_type** | **str** | Indicates whether a loan is for a recoverable item or a non-recoverable item. Possible values: - &#x60;N&#x60;: non-recoverable item - &#x60;R&#x60;: recoverable item This field is supported only for BNDES transactions on CyberSource through VisaNet. The value for this field corresponds to the following data in the TC 33 capture file5:  Record: CP07 TCR2, Position: 26, Field: Asset Indicator  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


