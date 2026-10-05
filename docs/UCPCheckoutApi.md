# CyberSource.UCPCheckoutApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ucp_cancel_checkout**](UCPCheckoutApi.md#ucp_cancel_checkout) | **POST** /icc/v1/checkout-sessions/{session_id}/cancel | Cancel Checkout UCP
[**ucp_complete_checkout**](UCPCheckoutApi.md#ucp_complete_checkout) | **POST** /icc/v1/checkout-sessions/{session_id}/complete | Complete Checkout UCP
[**ucp_create_checkout_session**](UCPCheckoutApi.md#ucp_create_checkout_session) | **POST** /icc/v1/checkout-sessions | Create Checkout Session UCP
[**ucp_get_checkout_session**](UCPCheckoutApi.md#ucp_get_checkout_session) | **GET** /icc/v1/checkout-sessions/{session_id} | Get Checkout Session UCP
[**ucp_update_checkout_session**](UCPCheckoutApi.md#ucp_update_checkout_session) | **PUT** /icc/v1/checkout-sessions/{session_id} | Update Checkout Session UCP


# **ucp_cancel_checkout**
> InlineResponse20113 ucp_cancel_checkout(session_id)

Cancel Checkout UCP

Cancels an active UCP checkout session. No charge is made.  This operation is idempotent — cancelling an already-cancelled session returns a successful response. Sessions also expire automatically after 30 minutes of inactivity. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.UCPCheckoutApi()
session_id = 'sess_abc123' # str | The unique identifier of the UCP checkout session to cancel.

try: 
    # Cancel Checkout UCP
    api_response = api_instance.ucp_cancel_checkout(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UCPCheckoutApi->ucp_cancel_checkout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The unique identifier of the UCP checkout session to cancel. | 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ucp_complete_checkout**
> InlineResponse20113 ucp_complete_checkout(session_id, idempotency_key=idempotency_key, ucp_complete_checkout_request=ucp_complete_checkout_request)

Complete Checkout UCP

**Final step of the UCP checkout flow.**  Finalizes the session and places the order with the merchant. ACG translates the UCP completion request to the merchant's checkout API.  On success, the session transitions to `completed`. An `order_id` is not returned in the UCP response — use the ACP Complete endpoint if you need order confirmation details.  **Always use an `idempotency-key`** to prevent duplicate orders on network retries. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.UCPCheckoutApi()
session_id = 'sess_abc123' # str | The unique identifier of the UCP checkout session to complete.
idempotency_key = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' # str | **Strongly recommended.** A unique key that ensures this order is placed exactly once on retries. Lowercase per UCP spec.  (optional)
ucp_complete_checkout_request = CyberSource.UcpCompleteCheckoutRequest() # UcpCompleteCheckoutRequest | UCP completion payload containing payment instrument and optional risk signals. If payment context was already provided in the Create or Update call, the body can be omitted. Risk signals are logged for fraud analysis and are not forwarded to the merchant.  (optional)

try: 
    # Complete Checkout UCP
    api_response = api_instance.ucp_complete_checkout(session_id, idempotency_key=idempotency_key, ucp_complete_checkout_request=ucp_complete_checkout_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UCPCheckoutApi->ucp_complete_checkout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The unique identifier of the UCP checkout session to complete. | 
 **idempotency_key** | **str**| **Strongly recommended.** A unique key that ensures this order is placed exactly once on retries. Lowercase per UCP spec.  | [optional] 
 **ucp_complete_checkout_request** | [**UcpCompleteCheckoutRequest**](UcpCompleteCheckoutRequest.md)| UCP completion payload containing payment instrument and optional risk signals. If payment context was already provided in the Create or Update call, the body can be omitted. Risk signals are logged for fraud analysis and are not forwarded to the merchant.  | [optional] 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ucp_create_checkout_session**
> InlineResponse20113 ucp_create_checkout_session(ucp_create_checkout_session_request, idempotency_key=idempotency_key)

Create Checkout Session UCP

**Step 1 of the UCP checkout flow.**  Creates a new UCP checkout session using Google's Universal Commerce Protocol format. ACG translates the UCP request into the internal ACP format, applies merchant pricing, and returns a UCP-format session response with a session `id`.  UCP uses `line_items` (instead of `items`) and lowercase header names (`idempotency-key`) per the UCP specification.  **Store the `id`** from the response — it is required for all subsequent UCP calls. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.UCPCheckoutApi()
ucp_create_checkout_session_request = CyberSource.UcpCreateCheckoutSessionRequest() # UcpCreateCheckoutSessionRequest | UCP checkout session creation payload containing line items, buyer details, currency, and optional payment, fulfillment, and discount information. 
idempotency_key = 'fc23729f-dc9b-4619-8742-2cf9d7bfdf1b' # str | Client-generated unique key (UUID recommended) to ensure this request is processed exactly once. Lowercase per UCP specification.  (optional)

try: 
    # Create Checkout Session UCP
    api_response = api_instance.ucp_create_checkout_session(ucp_create_checkout_session_request, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UCPCheckoutApi->ucp_create_checkout_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ucp_create_checkout_session_request** | [**UcpCreateCheckoutSessionRequest**](UcpCreateCheckoutSessionRequest.md)| UCP checkout session creation payload containing line items, buyer details, currency, and optional payment, fulfillment, and discount information.  | 
 **idempotency_key** | **str**| Client-generated unique key (UUID recommended) to ensure this request is processed exactly once. Lowercase per UCP specification.  | [optional] 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ucp_get_checkout_session**
> InlineResponse20113 ucp_get_checkout_session(session_id, ucp_get_checkout_session_request)

Get Checkout Session UCP

Retrieves the current state of a UCP checkout session.  Use this to verify session status, retrieve updated totals after a fulfillment change, or resume a session after an interruption. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.UCPCheckoutApi()
session_id = 'sess_abc123' # str | The unique identifier of the UCP checkout session to retrieve. Obtained from the `id` field in the Create Session response. 
ucp_get_checkout_session_request = NULL # object | Empty request body.

try: 
    # Get Checkout Session UCP
    api_response = api_instance.ucp_get_checkout_session(session_id, ucp_get_checkout_session_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UCPCheckoutApi->ucp_get_checkout_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The unique identifier of the UCP checkout session to retrieve. Obtained from the &#x60;id&#x60; field in the Create Session response.  | 
 **ucp_get_checkout_session_request** | **object**| Empty request body. | 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ucp_update_checkout_session**
> InlineResponse20113 ucp_update_checkout_session(session_id, ucp_update_checkout_session_request, idempotency_key=idempotency_key)

Update Checkout Session UCP

Modifies an active UCP checkout session and returns the updated session state.  Use this to change line item quantities, update fulfillment address or method, or apply discount codes. Totals are recalculated and returned in the response.  Only the fields you include in the request body are updated. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.UCPCheckoutApi()
session_id = 'sess_abc123' # str | The unique identifier of the UCP checkout session to update.
ucp_update_checkout_session_request = CyberSource.UcpUpdateCheckoutSessionRequest() # UcpUpdateCheckoutSessionRequest | UCP session update payload. All fields are optional — only fields you include will be applied. 
idempotency_key = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' # str | Client-generated unique key for idempotency. Lowercase per UCP spec. (optional)

try: 
    # Update Checkout Session UCP
    api_response = api_instance.ucp_update_checkout_session(session_id, ucp_update_checkout_session_request, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UCPCheckoutApi->ucp_update_checkout_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The unique identifier of the UCP checkout session to update. | 
 **ucp_update_checkout_session_request** | [**UcpUpdateCheckoutSessionRequest**](UcpUpdateCheckoutSessionRequest.md)| UCP session update payload. All fields are optional — only fields you include will be applied.  | 
 **idempotency_key** | **str**| Client-generated unique key for idempotency. Lowercase per UCP spec. | [optional] 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

