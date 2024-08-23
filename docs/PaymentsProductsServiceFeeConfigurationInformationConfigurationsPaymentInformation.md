# PaymentsProductsServiceFeeConfigurationInformationConfigurationsPaymentInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | Payment types accepted by this merchant. The supported values are: MASTERDEBIT, MASTERCREDIT, VISACREDIT, VISADEBIT, DISCOVERCREDIT, AMEXCREDIT, ECHECK | [optional] 
**fee_type** | **str** | Fee type for the selected payment type. Supported values are: Flat or Percentage.  | [optional] 
**fee_amount** | **float** | Fee Amount of the selected payment type if you chose Flat fee type.  | [optional] 
**percentage** | **float** | Percentage of the selected payment type if you chose Percentage Fee type. Supported values use numbers with decimals. For example, 1.0  | [optional] 
**fee_cap** | **float** | Fee cap for the selected payment type. Supported values use numbers with decimals. For example, 1.0  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


