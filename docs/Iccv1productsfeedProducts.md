# Iccv1productsfeedProducts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Your unique product identifier (SKU). Must be unique within your merchant catalog. Max 100 characters.  | 
**title** | **str** | Product display name. Max 150 characters. | 
**description** | **str** | Detailed product description. Max 5000 characters. | 
**url** | **str** | Canonical URL to the product page on your storefront. Max 1000 characters. | 
**image_url** | **str** | URL to the primary product image. Must be publicly accessible (HTTPS). Max 1000 characters.  | 
**additional_image_urls** | **str** | Optional. Additional product image URLs (comma-separated or single URL). Must be HTTPS. | [optional] 
**video_url** | **str** | Optional. URL to a product video. Must be HTTPS and publicly accessible. | [optional] 
**model_3d_url** | **str** | Optional. URL to a 3D model asset for the product (GLTF/GLB format preferred). | [optional] 
**availability** | **str** | Current stock status: - &#x60;in_stock&#x60; — available for immediate purchase - &#x60;out_of_stock&#x60; — temporarily unavailable - &#x60;preorder&#x60; or &#x60;pre_order&#x60; — not yet released - &#x60;backorder&#x60; — out of stock but accepting orders - &#x60;unknown&#x60; — availability status is not determined   Possible values: - in_stock - out_of_stock - preorder - pre_order - backorder - unknown | 
**availability_date** | **date** | Optional. Date when the product becomes available (for preorder/backorder). | [optional] 
**expiration_date** | **date** | Optional. Date after which the product listing expires. | [optional] 
**price** | **float** | Product price as a positive decimal number. Pair with &#x60;currency&#x60; for full price representation. Must be greater than zero.  | 
**currency** | **str** | 3-letter ISO 4217 currency code for the product price (e.g. \&quot;USD\&quot;, \&quot;EUR\&quot;, \&quot;GBP\&quot;).  | 
**sale_price** | **float** | Optional. Discounted sale price. Only shown when lower than &#x60;price&#x60;. | [optional] 
**sale_price_start_date** | **date** | Optional. Start date of the sale price window. | [optional] 
**sale_price_end_date** | **date** | Optional. End date of the sale price window. | [optional] 
**unit_pricing_measure** | **str** | Optional. Unit measure for unit-priced items (e.g. \&quot;1kg\&quot;, \&quot;750ml\&quot;). Used for per-unit price display. | [optional] 
**base_measure** | **str** | Optional. Base measure used for unit pricing comparison (e.g. \&quot;100g\&quot;, \&quot;1L\&quot;). Enables price-per-unit comparison. | [optional] 
**pricing_trend** | **str** | Optional. Pricing trend indicator (e.g. \&quot;dropping\&quot;, \&quot;rising\&quot;). Max 80 characters. | [optional] 
**geo_price** | **str** | Optional. Geography-specific pricing overrides (JSON or structured string). | [optional] 
**geo_availability** | **str** | Optional. Geography-specific availability overrides (JSON or structured string). | [optional] 
**brand** | **str** | Product brand or manufacturer name. Max 70 characters. | 
**gtin** | **str** | Optional. Global Trade Item Number (UPC, EAN, ISBN). Must be 8–14 digits. Required for Google Merchant Center syndication.  | [optional] 
**mpn** | **str** | Optional. Manufacturer Part Number. Max 70 characters. | [optional] 
**product_category** | **str** | Optional. Product category hierarchy. Used for UCP validation and Google Merchant Center syndication. Max 255 characters.  | [optional] 
**condition** | **str** | Optional. Product condition. Typical values: &#x60;new&#x60;, &#x60;used&#x60;, &#x60;refurbished&#x60;. Used for UCP syndication and Google Merchant Center feed.  | [optional] 
**material** | **str** | Optional. Primary material of the product. Max 100 characters. | [optional] 
**weight** | **str** | Optional. Product weight (e.g. \&quot;1.2kg\&quot;). Max 100 characters. | [optional] 
**dimensions** | **str** | Optional. Combined dimension string (e.g. \&quot;10x5x3 cm\&quot;). Max 100 characters. | [optional] 
**length** | **str** | Optional. Product length. | [optional] 
**width** | **str** | Optional. Product width. | [optional] 
**height** | **str** | Optional. Product height. | [optional] 
**dimensions_unit** | **str** | Optional. Unit for dimension values (e.g. \&quot;cm\&quot;, \&quot;in\&quot;). | [optional] 
**item_weight_unit** | **str** | Optional. Unit for weight value (e.g. \&quot;kg\&quot;, \&quot;lb\&quot;). | [optional] 
**age_group** | **str** | Optional. Target age group (e.g. \&quot;adult\&quot;, \&quot;kids\&quot;, \&quot;infant\&quot;, \&quot;toddler\&quot;, \&quot;newborn\&quot;). | [optional] 
**color** | **str** | Optional. Product color. Max 40 characters. | [optional] 
**size** | **str** | Optional. Product size (e.g. \&quot;M\&quot;, \&quot;42\&quot;, \&quot;XL\&quot;). Max 20 characters. Used for variant filtering. | [optional] 
**size_system** | **str** | Optional. Size standard used (e.g. \&quot;US\&quot;, \&quot;EU\&quot;, \&quot;UK\&quot;, \&quot;AU\&quot;). | [optional] 
**gender** | **str** | Optional. Target gender (e.g. \&quot;male\&quot;, \&quot;female\&quot;, \&quot;unisex\&quot;). | [optional] 
**group_id** | **str** | Product variant group ID — links products that are variations of the same item. Max 70 characters.  | 
**listing_has_variations** | **bool** | Whether this listing has product variations. | 
**item_group_title** | **str** | Optional. Display title for the variant group. Max 150 characters. | [optional] 
**offer_id** | **str** | Optional. Merchant-assigned offer identifier for marketplace deduplication. | [optional] 
**variant_dict** | **dict(str, str)** | Optional. Key-value map of variant attribute names to values (e.g. color, size). | [optional] 
**custom_variant1_category** | **str** | Optional. Custom variant 1 category label. | [optional] 
**custom_variant1_option** | **str** | Optional. Custom variant 1 option value. | [optional] 
**custom_variant2_category** | **str** | Optional. Custom variant 2 category label. | [optional] 
**custom_variant2_option** | **str** | Optional. Custom variant 2 option value. | [optional] 
**custom_variant3_category** | **str** | Optional. Custom variant 3 category label. | [optional] 
**custom_variant3_option** | **str** | Optional. Custom variant 3 option value. | [optional] 
**seller_name** | **str** | Merchant or seller display name. Max 70 characters.  | 
**seller_url** | **str** | URL to the seller&#39;s storefront. Max 1000 characters. | 
**marketplace_seller** | **str** | Optional. Marketplace seller identifier for multi-seller platforms. Max 70 characters. | [optional] 
**seller_privacy_policy** | **str** | Optional. URL to the seller&#39;s privacy policy page. | [optional] 
**seller_tos** | **str** | Optional. URL to the seller&#39;s terms of service page. | [optional] 
**shipping_price** | **str** | Optional. Shipping price for this product (e.g. \&quot;5.99 USD\&quot; or \&quot;Free\&quot;). | [optional] 
**delivery_estimate** | **date** | Optional. Estimated delivery date. | [optional] 
**pickup_method** | **str** | Optional. Available pickup method (e.g. \&quot;in-store\&quot;, \&quot;curbside\&quot;, \&quot;locker\&quot;). | [optional] 
**pickup_sla** | **str** | Optional. Pickup SLA commitment (e.g. \&quot;same-day\&quot;, \&quot;2 hours\&quot;, \&quot;next-day\&quot;). | [optional] 
**is_digital** | **bool** | Optional. Whether this product is a digital/downloadable item. | [optional] 
**return_policy** | **str** | Human-readable return policy description. | 
**accepts_returns** | **bool** | Optional. Whether the product is eligible for returns. | [optional] 
**return_deadline_in_days** | **int** | Optional. Number of days within which a return is accepted. Must be a positive integer. | [optional] 
**accepts_exchanges** | **bool** | Optional. Whether the product is eligible for exchanges. | [optional] 
**is_eligible_search** | **bool** | Controls whether this product appears in AI agent product discovery and search results. | 
**is_eligible_checkout** | **bool** | Controls whether this product can be added to cart and purchased via AI agents. | 
**popularity_score** | **float** | Optional. Numeric popularity score (higher is more popular). | [optional] 
**return_rate** | **str** | Optional. Product return rate indicator (e.g. \&quot;low\&quot;, \&quot;medium\&quot;, \&quot;high\&quot;, or \&quot;5%\&quot;). | [optional] 
**warning** | **str** | Optional. Safety or compliance warning text for the product (e.g. Prop 65, choking hazard). | [optional] 
**warning_url** | **str** | Optional. URL to a detailed warning or compliance information page. | [optional] 
**age_restriction** | **int** | Optional. Minimum age required to purchase this product (e.g. 18). | [optional] 
**review_count** | **int** | Optional. Total number of customer reviews for this product. | [optional] 
**star_rating** | **str** | Optional. Average star rating for this product (e.g. \&quot;4.5\&quot;). | [optional] 
**store_review_count** | **int** | Optional. Total number of store-level reviews. | [optional] 
**store_star_rating** | **str** | Optional. Average star rating for the store (e.g. \&quot;4.8\&quot;). | [optional] 
**related_product_id** | **str** | Optional. Item ID of a related product (e.g. accessory, replacement). | [optional] 
**relationship_type** | **str** | Optional. Type of relationship to &#x60;related_product_id&#x60; (e.g. \&quot;accessory\&quot;, \&quot;replacement\&quot;, \&quot;bundle\&quot;).  | [optional] 
**target_countries** | **list[str]** | List of ISO 3166-1 alpha-3 country codes where this product is available. | 
**store_country** | **str** | ISO 3166-1 alpha-2 country code of the merchant&#39;s store. Max 2 characters. | 
**q_and_a** | **list[dict(str, object)]** | Optional. List of Q&amp;A entries for this product. | [optional] 
**qand_a** | **list[dict(str, object)]** | Optional. Alias for &#x60;q_and_a&#x60;. Included for compatibility with alternate field naming conventions. | [optional] 
**reviews** | **list[dict(str, object)]** | Optional. List of customer review objects for this product. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


