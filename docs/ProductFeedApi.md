# CyberSource.ProductFeedApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_products**](ProductFeedApi.md#get_all_products) | **GET** /icc/v1/products | Get All Products
[**get_feed_job_status**](ProductFeedApi.md#get_feed_job_status) | **GET** /icc/v1/products/feed/bulk/{jobId} | Get Feed Job Status
[**get_product**](ProductFeedApi.md#get_product) | **GET** /icc/v1/products/{product_id} | Get Product by ID
[**submit_product_feed_json**](ProductFeedApi.md#submit_product_feed_json) | **POST** /icc/v1/products/feed | Ingest Product Feed


# **get_all_products**
> InlineResponse20020 get_all_products(get_all_products_request, page=page, size=size)

Get All Products

Returns the full product catalog stored in ACG.  **Note:** This endpoint is intended for catalog verification and merchant tooling. It is not a real-time product discovery API for end buyers. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ProductFeedApi()
get_all_products_request = NULL # object | Empty request body.
page = 0 # int | Page number to retrieve (0-based). Defaults to 0. (optional) (default to 0)
size = 300 # int | Number of products per page. Defaults to 300. Server enforces a maximum of 1000; values above 1000 are capped.  (optional) (default to 300)

try: 
    # Get All Products
    api_response = api_instance.get_all_products(get_all_products_request, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductFeedApi->get_all_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_products_request** | **object**| Empty request body. | 
 **page** | **int**| Page number to retrieve (0-based). Defaults to 0. | [optional] [default to 0]
 **size** | **int**| Number of products per page. Defaults to 300. Server enforces a maximum of 1000; values above 1000 are capped.  | [optional] [default to 300]

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_job_status**
> InlineResponse20019 get_feed_job_status(job_id, get_feed_job_status_request)

Get Feed Job Status

Returns the processing and syndication status of a previously submitted product feed job.  Use this to poll the `jobId` returned by the Ingest Product Feed endpoint until processing and syndication complete. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ProductFeedApi()
job_id = '550e8400-e29b-41d4-a716-446655440000' # str | Unique identifier of the feed submission job, returned by the Ingest Product Feed endpoint. 
get_feed_job_status_request = NULL # object | Empty request body.

try: 
    # Get Feed Job Status
    api_response = api_instance.get_feed_job_status(job_id, get_feed_job_status_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductFeedApi->get_feed_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| Unique identifier of the feed submission job, returned by the Ingest Product Feed endpoint.  | 
 **get_feed_job_status_request** | **object**| Empty request body. | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> InlineResponse20021 get_product(product_id, get_product_request)

Get Product by ID

Retrieves a single product from the ACG catalog by its unique product identifier (SKU).  Use this to verify that a product was ingested correctly, inspect its current field values, or check its syndication-eligibility flags (`is_eligible_search`, `is_eligible_checkout`). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ProductFeedApi()
product_id = 'product_id_example' # str | The unique product identifier (SKU) assigned by the merchant and provided during feed ingestion. Example: `SKU-1001`. 
get_product_request = NULL # object | Empty request body.

try: 
    # Get Product by ID
    api_response = api_instance.get_product(product_id, get_product_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductFeedApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The unique product identifier (SKU) assigned by the merchant and provided during feed ingestion. Example: &#x60;SKU-1001&#x60;.  | 
 **get_product_request** | **object**| Empty request body. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_product_feed_json**
> InlineResponse2021 submit_product_feed_json(product_feed_request)

Ingest Product Feed

Submits a merchant product catalog to ACG for asynchronous processing and syndication to all configured protocol backends (e.g. Google Merchant Center).  **Processing pipeline:** 1. The request is accepted immediately and a `jobId` is returned — validation, ingestion,    and syndication all happen asynchronously in the background. 2. Each product is validated against UCP/ACP schema requirements (required fields, format rules) 3. Valid products are saved to the ACG catalog 4. An async syndication job is triggered to push the catalog to configured backends  **Supported content types:** `application/json` (this endpoint). CSV and JSONL uploads are also supported via file upload endpoints.  **Note:** This endpoint no longer returns per-product validation results or syndication outcomes synchronously — only the `jobId` acknowledgement shown below. Use that `jobId` to track processing and syndication status. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.ProductFeedApi()
product_feed_request = CyberSource.ProductFeedRequest() # ProductFeedRequest | Product feed payload. The `products` array is required and must contain at least one product. See `ProductInput` for the full list of required fields. 

try: 
    # Ingest Product Feed
    api_response = api_instance.submit_product_feed_json(product_feed_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductFeedApi->submit_product_feed_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_feed_request** | [**ProductFeedRequest**](ProductFeedRequest.md)| Product feed payload. The &#x60;products&#x60; array is required and must contain at least one product. See &#x60;ProductInput&#x60; for the full list of required fields.  | 

### Return type

[**InlineResponse2021**](InlineResponse2021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

