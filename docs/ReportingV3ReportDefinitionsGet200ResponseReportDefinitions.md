# ReportingV3ReportDefinitionsGet200ResponseReportDefinitions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**report_definition_id** | **int** | | Id  |         Definition Class          | | --- | --------------------------------- | | 210 | TransactionRequestClass           | | 211 | PaymentBatchDetailClass           | | 212 | ExceptionDetailClass              | | 213 | ProcessorSettlementDetailClass    | | 214 | ProcessorEventsDetailClass        | | 215 | FundingDetailClass                | | 216 | AgingDetailClass                  | | 217 | ChargebackAndRetrievalDetailClass | | 218 | DepositDetailClass                | | 219 | FeeDetailClass                    | | 220 | InvoiceSummaryClass               | | 221 | PayerAuthDetailClass              | | 222 | ConversionDetailClass             | | 225 | BillableTransactionsDetailClass   | | 270 | JPTransactionDetailClass          | | 271 | ServiceFeeDetailClass             | | 310 | GatewayTransactionRequestClass    | | 400 | DecisionManagerEventDetailClass   | | 401 | DecisionManagerDetailClass        | | 410 | FeeSummaryClass                   | | 420 | TaxCalculationClass               | | 520 | POSTerminalExceptionClass         | | 620 | SubscriptionDetailClass           |  | [optional] 
**report_defintion_name** | **str** |  | [optional] 
**supported_formats** | **list[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**default_settings** | [**ReportingV3ReportDefinitionsNameGet200ResponseDefaultSettings**](ReportingV3ReportDefinitionsNameGet200ResponseDefaultSettings.md) |  | [optional] 
**subscription_type** | **str** | &#39;The subscription type for which report definition is required. By default the type will be CUSTOM.&#39; Valid Values: - CLASSIC - CUSTOM - STANDARD  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


