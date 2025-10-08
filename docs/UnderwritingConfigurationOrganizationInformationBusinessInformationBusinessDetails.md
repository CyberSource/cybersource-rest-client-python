# UnderwritingConfigurationOrganizationInformationBusinessInformationBusinessDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_type** | **str** | Who is the business interacting with? Business to Business, Business to Consumer, Both  Possible values: - B2B - B2C - Both | [optional] 
**percentage_split_by_b2_b** | **float** | % Split | [optional] 
**percentage_split_by_b2_c** | **float** | % Split | [optional] 
**interaction_types** | **str** | Merchant Facing: Face to Face, Card Not Present, Both  Possible values: - F2F - CNP - Both | 
**percentage_split_by_f2_f** | **float** | % Split | 
**percentage_split_by_cnp** | **float** | % Split | 
**when_is_customer_charged** | **str** | When is the customer charged?  Possible values: - OneTimeBeforeServiceDelivery - OneTimeAfterServiceDelivery - Other | 
**when_is_customer_charged_description** | **str** |  | [optional] 
**offer_subscriptions** | **bool** | Does Merchant Offer Subscriptions? | 
**monthly_subscription_percent** | **float** | % of business is monthly subscriptions | [optional] 
**quarterly_subscription_percent** | **float** | % of business is quarterly subscriptions | [optional] 
**semiannual_subscription_percent** | **float** | % of business is semi-annual subscriptions | [optional] 
**annual_subscription_percent** | **float** | % of business is annual subscriptions | [optional] 
**currency_type** | **str** | Processing Currency. ISO 4217, 3 characters.  Possible values: - USD - CAD - EUR - GBP - CHF | [optional] 
**estimated_monthly_sales** | **float** | Merchant&#39;s estimated monthly sales | [optional] 
**average_order_amount** | **float** | Merchant&#39;s average order amount | [optional] 
**largest_expected_order_amount** | **float** | Merchant&#39;s largest expected order amount | [optional] 
**primary_account_usage** | **str** | Primary purpose of account usage  Possible values: - Paying for goods / services - Repatriating overseas earnings - Intercompany transfers - Collecting funds from clients - Liquidity / FX - Payment to an individual - Investment activity - Property purchase/sale - Other | [optional] 
**source_of_funds** | **str** | Source of Funds  Possible values: - Business revenue - External or shareholder investment - Loan, advance or other borrowing - Donations or grants - Inter-company transfers - Proceeds of sales of assests - Other | [optional] 
**receive_money3rd_parties** | **bool** | Will you recieve money from 3rd parties into your account? | [optional] 
**receive_transaction_frequency** | **str** | Roughly how often do you expect to send or receive transactions?  Possible values: - One-off or infrequently - 1-20 per month - 20-50 per month - 50-100 per month - 100+ per month | [optional] 
**estimated_monthly_spend** | **str** | What is your estimated total monthly spend?  Possible values: - &lt;$10,000 - $10,000 - $50,000 - $50,000 - $100,000 - $100,000 - $500,000 - $500,000+ | [optional] 
**country_transactions** | **list[str]** |  | [optional] 
**currencies_in** | **list[str]** |  | [optional] 
**currencies_out** | **list[str]** |  | [optional] 
**product_services_subscription** | [**list[UnderwritingConfigurationOrganizationInformationBusinessInformationBusinessDetailsProductServicesSubscription]**](UnderwritingConfigurationOrganizationInformationBusinessInformationBusinessDetailsProductServicesSubscription.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


