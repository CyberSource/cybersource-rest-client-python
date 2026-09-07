# UnifiedriskCustomer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_customer_id** | **str** | Your identifier for the customer.When a subscription or customer profile is being created, the maximum length for this field for most processors is 30. Otherwise, the maximum length is 100.#### Comercio Latino For recurring payments in Mexico, the value is the customer&#39;s contract number. Note Before you request the authorization, you must inform the issuer of the customer contract numbers that will be used for recurring transactions.#### Worldpay VAP For a follow-on credit with Worldpay VA | [optional] 
**username** | **str** | Specifies the customer account user name. | [optional] 
**hashed_password** | **str** | The merchant&#39;s password that CyberSource hashes and stores as a hashed password. | [optional] 
**personal_identification** | [**UnifiedriskCustomerPersonalIdentification**](UnifiedriskCustomerPersonalIdentification.md) |  | [optional] 
**enrollment_date** | **date** | The date in which the customer signed up to use Mobile/online banking | [optional] 
**flags** | **list[str]** | Field to be used for specific customer flags that may determine treatment strategies. This is an array that can include free text values.  For retail customers this may be a vulnerability or a VIP mar  | [optional] 
**customer_id** | **str** | A unique identifier for the customer. | A unique identifier for the customer. This field should be considered mandatory for the payments solution, but not otherwise. | [optional] 
**type** | **str** | The customer type. If the identifier in customerId represents an individual, set this attribute to \&quot;Retail\&quot;, if it represents a business, set this attribute to \&quot;Business\&quot;. | [optional] 
**agent_type** | **str** | Type of agent initiating transaction: HUMAN, AI_AGENT, or HYBRID  Possible values: - HUMAN - AI_AGENT - HYBRID | [optional] 
**agent_id** | **str** | Unique identifier for the AI agent acting on behalf of customer | [optional] 
**agent_confidence_score** | **float** | Confidence score (0-1) for agent&#39;s alignment with customer preferences | [optional] 
**agent_delegation_scope** | **str** | Scope of authority delegated to agent: discovery, purchase, or full  Possible values: - discovery - purchase - full | [optional] 
**agent_interaction_timestamp** | **datetime** | Timestamp of agent interaction with customer | [optional] 
**is_business** | **bool** | Whether customer is a business entity | [optional] 
**business_name** | **str** | Name of business if customer is a business | [optional] 
**id** | **str** | The unique id of the customer | [optional] 
**address** | [**UnifiedriskCustomerAddress**](UnifiedriskCustomerAddress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


