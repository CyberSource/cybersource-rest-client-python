# InlineResponse20020Products

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Unique product identifier / SKU. | [optional] 
**is_eligible_search** | **bool** | When &#x60;true&#x60;, product appears in AI agent discovery results. | [optional] 
**is_eligible_checkout** | **bool** | When &#x60;true&#x60;, product can be added to a checkout session. | [optional] 
**title** | **str** | Product display name. | [optional] 
**description** | **str** | Product description. | [optional] 
**url** | **str** | URL to the product page on the merchant&#39;s storefront. | [optional] 
**image_url** | **str** | URL to the primary product image. | [optional] 
**product_category** | **str** | Product category hierarchy (e.g. &#x60;Electronics &gt; Audio &gt; Headphones&#x60;). | [optional] 
**brand** | **str** | Product brand or manufacturer. | [optional] 
**material** | **str** | Primary material (relevant for apparel, furniture, etc.). | [optional] 
**weight** | **str** | Product weight including unit. | [optional] 
**price** | **float** | Product price as a decimal number. | [optional] 
**currency** | **str** | ISO 4217 currency code. | [optional] 
**availability** | **str** | Current stock status.  Possible values: - in_stock - out_of_stock - preorder - pre_order - backorder - unknown | [optional] 
**color** | **str** | Primary product color. | [optional] 
**gender** | **str** | Target gender (e.g. \&quot;male\&quot;, \&quot;female\&quot;, \&quot;unisex\&quot;). | [optional] 
**age_group** | **str** | Target age group (e.g. \&quot;adult\&quot;, \&quot;kids\&quot;, \&quot;infant\&quot;). | [optional] 
**shipping_price** | **str** | Shipping cost string as provided by the merchant. | [optional] 
**group_id** | **str** | Product variant group identifier. | [optional] 
**listing_has_variations** | **bool** | Whether this listing has product variations (e.g. different sizes or colors). | [optional] 
**seller_name** | **str** | Merchant or seller display name. | [optional] 
**seller_url** | **str** | URL to the seller&#39;s storefront. | [optional] 
**return_policy** | **str** | Merchant return policy text. | [optional] 
**target_countries** | **list[str]** | Country codes where this product is available. | [optional] 
**store_country** | **str** | ISO 3166-1 alpha-2 country code of the merchant&#39;s store. | [optional] 
**created_at** | **datetime** | ISO 8601 timestamp when this product was first ingested. | [optional] 
**updated_at** | **datetime** | ISO 8601 timestamp of the most recent update. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


