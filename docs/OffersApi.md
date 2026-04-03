# CyberSource.OffersApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offer**](OffersApi.md#create_offer) | **POST** /vas/v1/currencyconversion | Create an Offer
[**get_offer**](OffersApi.md#get_offer) | **GET** /vas/v1/currencyconversion/{id} | Retrieve an Offer


# **create_offer**
> InlineResponse2019 create_offer(content_type, x_requestid, v_c_merchant_id, v_c_correlation_id, v_c_organization_id, offer_request)

Create an Offer

Empower global transactions with transparency and choice. Our Dynamic Currency Conversion API lets merchants offer customers the option to pay in their home currency at checkout, delivering real-time exchange rates.  <div style=\"display: flex; gap: 2rem;\"> <div style=\"flex: 1;\">  **Key Benefits:** - **Enhanced Customer Experience:** Provide clarity and convenience for international shoppers. - **Real-Time Rates:** Accurate currency conversion with all the data required for acquirers and their merchants to maintain compliance with card network rules. - **Seamless Integration:** Flexible API endpoints for rate lookup, authorization, and capture. - **Regulatory Compliance:** Provides the data required for acquirers and merchants to meet and maintain card scheme requirements for disclosure and consent.  <br>  Ideal for merchants and payment partners seeking to boost trust and conversion in cross-border commerce.  <br>  **Key Features:** - **Rate Lookup:** Retrieves the most up-to-date exchange rate for eligible cards before authorization. - **Currency Choice:** Enables the merchant to offer customers the option to select between the merchant's local currency and their card's billing currency. - **Compliance:** Ensures merchants have the data required to adhere to card network regulations; exchange rates, markups, etc.  <div style=\"margin-top: 1.5rem;\">  **Supported Scenarios:** - Dynamic Currency Conversion when cardholder's billing currency differs from merchant's pricing currency. - Merchant and acquirer must support the cardholder's billing currency. </div>  <div style=\"margin-top: 1.5rem;\">  **Supported Processors:** - VPC - FDI Global </div>  <div style=\"margin-top: 1.5rem;\">  **Compliance & Disclosure:**  Merchants must: - Adhere to card network rules for Dynamic Currency Conversion (DCC) transactions. - Display the converted amount, exchange rate, and markup percentage and other required disclosures. - Obtain explicit cardholder consent before applying DCC. - Work with your acquirer to obtain full set of compliance requirements. </div>  </div> <div style=\"flex: 1;\">  **Core API Endpoints:**  **Currency Conversion API**  Returns eligibility and exchange rate details, including: - exchangeRate - marginRate - reconciliationId and Id (for subsequent payment requests)  <div style=\"margin-top: 1.5rem;\">  **Payment Authorization with DCC***  POST /pts/v2/payments  Required fields include: - orderInformation.amountDetails.currency - orderInformation.amountDetails.originalCurrency - orderInformation.amountDetails.originalAmount - orderInformation.amountDetails.exchangeRate - currencyConversion.indicator (e.g., 1 = Converted, 2 = Nonconvertible, 3 = Declined) </div>  <div style=\"margin-top: 1.5rem;\">  **Capture with DCC***  POST /pts/v2/payments/{id}/captures  Maps from original authorization and includes original and converted amounts. </div>  <div style=\"margin-top: 1.5rem;\">  **Refund with DCC***  POST /pts/v2/captures/{id}/refunds  Maps from original authorization and includes original and converted amounts.  *Note: DCC is only supported on select processors. Contact your acquirer or account manager for more information.* </div>  </div> </div>  <br>  For more information, see the [Currency Conversion Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/currency-conversion/developer/all/rest/currency-conversion/cc-intro.html). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.OffersApi()
content_type = 'content_type_example' # str | 
x_requestid = 'x_requestid_example' # str | 
v_c_merchant_id = 'v_c_merchant_id_example' # str | 
v_c_correlation_id = 'v_c_correlation_id_example' # str | 
v_c_organization_id = 'v_c_organization_id_example' # str | 
offer_request = CyberSource.OfferRequest() # OfferRequest | 

try: 
    # Create an Offer
    api_response = api_instance.create_offer(content_type, x_requestid, v_c_merchant_id, v_c_correlation_id, v_c_organization_id, offer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OffersApi->create_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **x_requestid** | **str**|  | 
 **v_c_merchant_id** | **str**|  | 
 **v_c_correlation_id** | **str**|  | 
 **v_c_organization_id** | **str**|  | 
 **offer_request** | [**OfferRequest**](OfferRequest.md)|  | 

### Return type

[**InlineResponse2019**](InlineResponse2019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer**
> InlineResponse20016 get_offer(content_type, x_requestid, v_c_merchant_id, v_c_correlation_id, v_c_organization_id, id)

Retrieve an Offer

Retrieves an offer record from the system. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.OffersApi()
content_type = 'content_type_example' # str | 
x_requestid = 'x_requestid_example' # str | 
v_c_merchant_id = 'v_c_merchant_id_example' # str | 
v_c_correlation_id = 'v_c_correlation_id_example' # str | 
v_c_organization_id = 'v_c_organization_id_example' # str | 
id = 'id_example' # str | Request ID generated by Cybersource. This was sent in the header on the request. Echo value from v-c-request-id

try: 
    # Retrieve an Offer
    api_response = api_instance.get_offer(content_type, x_requestid, v_c_merchant_id, v_c_correlation_id, v_c_organization_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OffersApi->get_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **x_requestid** | **str**|  | 
 **v_c_merchant_id** | **str**|  | 
 **v_c_correlation_id** | **str**|  | 
 **v_c_organization_id** | **str**|  | 
 **id** | **str**| Request ID generated by Cybersource. This was sent in the header on the request. Echo value from v-c-request-id | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

