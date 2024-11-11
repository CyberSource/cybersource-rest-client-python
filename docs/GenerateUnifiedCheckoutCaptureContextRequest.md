# GenerateUnifiedCheckoutCaptureContextRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_origins** | **list[str]** | The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) of the website on which you will be launching Unified Checkout is defined by the scheme (protocol), hostname (domain) and port number (if used).    You must use https://hostname (unless you use http://localhost) Wildcards are NOT supported.  Ensure that subdomains are included. Any valid top-level domain is supported (e.g. .com, .co.uk, .gov.br etc)  Examples:   - https://example.com   - https://subdomain.example.com   - https://example.com:8080&lt;br&gt;&lt;br&gt;  If you are embedding within multiple nested iframes you need to specify the origins of all the browser contexts used, for example:    targetOrigins: [     \&quot;https://example.com\&quot;,     \&quot;https://basket.example.com\&quot;,     \&quot;https://ecom.example.com\&quot;   ]  | [optional] 
**client_version** | **str** | Specify the version of Unified Checkout that you want to use. | [optional] 
**allowed_card_networks** | **list[str]** | The list of card networks you want to use for this Unified Checkout transaction.  Unified Checkout currently supports the following card networks:   - VISA   - MASTERCARD   - AMEX   - DISCOVER   - DINERSCLUB   - JCB  | [optional] 
**allowed_payment_types** | **list[str]** | The payment types that are allowed for the merchant.    Possible values when launching Unified Checkout:   - PANENTRY                 - GOOGLEPAY   - SRC   - CHECK &lt;br&gt;&lt;br&gt;  Possible values when launching Unified Checkout with Checkout API: - PANENTRY               - SRC &lt;br&gt;&lt;br&gt;  Possible values when launching Click To Pay Drop-In UI: - CLICKTOPAY &lt;br&gt;&lt;br&gt;  **Important:**    - SRC and CLICKTOPAY are only available for Visa, Mastercard and AMEX.  | [optional] 
**country** | **str** | Country the purchase is originating from (e.g. country of the merchant).  Use the two-character ISO Standard  | [optional] 
**locale** | **str** | Localization of the User experience conforming to the ISO 639-1 language standards and two-character ISO Standard Country Code.  Please refer to list of [supported locales through Unified Checkout](https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix-languages.html)  | [optional] 
**capture_mandate** | [**Upv1capturecontextsCaptureMandate**](Upv1capturecontextsCaptureMandate.md) |  | [optional] 
**order_information** | [**Upv1capturecontextsOrderInformation**](Upv1capturecontextsOrderInformation.md) |  | [optional] 
**checkout_api_initialization** | [**Upv1capturecontextsCheckoutApiInitialization**](Upv1capturecontextsCheckoutApiInitialization.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


