# CyberSource.AgentCapabilitiesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_agent_key**](AgentCapabilitiesApi.md#activate_agent_key) | **POST** /icc/v1/agents/{agentId}/keys/{keyId}/activate | Activate a key
[**add_agent_key**](AgentCapabilitiesApi.md#add_agent_key) | **POST** /icc/v1/agents/{agentId}/keys | Add a key to an agent
[**cancel_purchase_intent**](AgentCapabilitiesApi.md#cancel_purchase_intent) | **PUT** /icc/v1/instructions/{instructionId}/cancel | Cancel a purchase intent
[**confirm_transaction_events**](AgentCapabilitiesApi.md#confirm_transaction_events) | **POST** /icc/v1/instructions/{instructionId}/confirmations | Confirm transaction events
[**deactivate_agent_key**](AgentCapabilitiesApi.md#deactivate_agent_key) | **DELETE** /icc/v1/agents/{agentId}/keys/{keyId} | Deactivate a key
[**enroll_card**](AgentCapabilitiesApi.md#enroll_card) | **POST** /icc/v1/tokens | Enroll a card
[**get_agent**](AgentCapabilitiesApi.md#get_agent) | **GET** /icc/v1/agents/{agentId} | Get an agent
[**get_agent_key**](AgentCapabilitiesApi.md#get_agent_key) | **GET** /icc/v1/agents/{agentId}/keys/{keyId} | Get a key by agent and key ID
[**initiate_purchase_intent**](AgentCapabilitiesApi.md#initiate_purchase_intent) | **POST** /icc/v1/instructions | Initiate a purchase intent
[**list_agent_keys**](AgentCapabilitiesApi.md#list_agent_keys) | **GET** /icc/v1/agents/{agentId}/keys | List keys for an agent
[**register_agent**](AgentCapabilitiesApi.md#register_agent) | **POST** /icc/v1/agents | Register an agent
[**retrieve_payment_credentials**](AgentCapabilitiesApi.md#retrieve_payment_credentials) | **POST** /icc/v1/instructions/{instructionId}/credentials | Retrieve payment credentials
[**update_agent**](AgentCapabilitiesApi.md#update_agent) | **PUT** /icc/v1/agents/{agentId} | Update an agent
[**update_agent_key**](AgentCapabilitiesApi.md#update_agent_key) | **PUT** /icc/v1/agents/{agentId}/keys/{keyId} | Update a key
[**update_purchase_intent**](AgentCapabilitiesApi.md#update_purchase_intent) | **PUT** /icc/v1/instructions/{instructionId} | Update a purchase intent


# **activate_agent_key**
> AddAgentKeyResponse201 activate_agent_key(agent_id, key_id)

Activate a key

Activate a deactivated key. Raises 404 if agent or key not found, 403 if agent is deactivated.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_id = 'agent_id_example' # str | Unique agent identifier
key_id = 'key_id_example' # str | Unique key identifier

try: 
    # Activate a key
    api_response = api_instance.activate_agent_key(agent_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->activate_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique agent identifier | 
 **key_id** | **str**| Unique key identifier | 

### Return type

[**AddAgentKeyResponse201**](AddAgentKeyResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_agent_key**
> AddAgentKeyResponse201 add_agent_key(agent_id, key_request)

Add a key to an agent

[category 1 — Agent_Capabilities] Upload a Base64-encoded public key for an agent.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_id = 'agent_id_example' # str | Unique agent identifier
key_request = CyberSource.KeyRequest() # KeyRequest | Key creation request

try: 
    # Add a key to an agent
    api_response = api_instance.add_agent_key(agent_id, key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->add_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique agent identifier | 
 **key_request** | [**KeyRequest**](KeyRequest.md)| Key creation request | 

### Return type

[**AddAgentKeyResponse201**](AddAgentKeyResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_purchase_intent**
> AgenticCreatePurchaseIntentResponse200 cancel_purchase_intent(instruction_id, agentic_cancel_purchase_intent_request)

Cancel a purchase intent

Cancel an existing purchase intent (instruction) identified by its instructionId. The agent calls this endpoint when the consumer decides to abandon the purchase before payment credentials have been used. Requires device information and assurance data for identity verification. Returns status CANCELLED (HTTP 200) on success, or PENDING (HTTP 202) with pendingEvents if cardholder authentication is required before cancellation can proceed.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
instruction_id = 'instruction_id_example' # str | 
agentic_cancel_purchase_intent_request = CyberSource.AgenticCancelPurchaseIntentRequest() # AgenticCancelPurchaseIntentRequest | Unique identifier for the purchase intent instruction.

try: 
    # Cancel a purchase intent
    api_response = api_instance.cancel_purchase_intent(instruction_id, agentic_cancel_purchase_intent_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->cancel_purchase_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instruction_id** | **str**|  | 
 **agentic_cancel_purchase_intent_request** | [**AgenticCancelPurchaseIntentRequest**](AgenticCancelPurchaseIntentRequest.md)| Unique identifier for the purchase intent instruction. | 

### Return type

[**AgenticCreatePurchaseIntentResponse200**](AgenticCreatePurchaseIntentResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_transaction_events**
> AgenticConfirmTransactionEventsResponse202 confirm_transaction_events(instruction_id, agentic_confirm_transaction_events_request)

Confirm transaction events

Confirm transaction events for a completed purchase. The agent calls this endpoint after the payment has been submitted to notify the Intelligent Commerce Connect of the transaction outcome. The request includes processor information (transaction type, status, approval codes), order details (shipping, tracking, product information), and merchant information. Returns HTTP 202 acknowledging receipt of the confirmation.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
instruction_id = 'instruction_id_example' # str | Unique identifier for the purchase intent instruction.
agentic_confirm_transaction_events_request = CyberSource.AgenticConfirmTransactionEventsRequest() # AgenticConfirmTransactionEventsRequest | 

try: 
    # Confirm transaction events
    api_response = api_instance.confirm_transaction_events(instruction_id, agentic_confirm_transaction_events_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->confirm_transaction_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instruction_id** | **str**| Unique identifier for the purchase intent instruction. | 
 **agentic_confirm_transaction_events_request** | [**AgenticConfirmTransactionEventsRequest**](AgenticConfirmTransactionEventsRequest.md)|  | 

### Return type

[**AgenticConfirmTransactionEventsResponse202**](AgenticConfirmTransactionEventsResponse202.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_agent_key**
> deactivate_agent_key(agent_id, key_id)

Deactivate a key

Deactivate a key (soft delete). Raises 404 if key not found.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_id = 'agent_id_example' # str | Unique agent identifier
key_id = 'key_id_example' # str | Unique key identifier

try: 
    # Deactivate a key
    api_instance.deactivate_agent_key(agent_id, key_id)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->deactivate_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique agent identifier | 
 **key_id** | **str**| Unique key identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_card**
> AgenticCardEnrollmentResponse200 enroll_card(agentic_card_enrollment_request)

Enroll a card

Enroll a payment card for agentic or e-commerce transactions. This is typically the first step in the Intelligent Commerce payment lifecycle — the agent calls this endpoint to register a consumer's card, creating a tokenized reference that can be used in subsequent purchase instructions and payment credential retrieval. Requires device information, consumer identity, billing details, and payment instrument references. Returns a status of ACTIVE (HTTP 200) if enrollment completes immediately, or PENDING (HTTP 202) with pendingEvents if cardholder authentication is required. Call this endpoint when a consumer wants to add a new payment card or when setting up a card for agentic payment flows.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agentic_card_enrollment_request = CyberSource.AgenticCardEnrollmentRequest() # AgenticCardEnrollmentRequest | 

try: 
    # Enroll a card
    api_response = api_instance.enroll_card(agentic_card_enrollment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->enroll_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentic_card_enrollment_request** | [**AgenticCardEnrollmentRequest**](AgenticCardEnrollmentRequest.md)|  | 

### Return type

[**AgenticCardEnrollmentResponse200**](AgenticCardEnrollmentResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent**
> AgentRegistrationResponse201 get_agent(agent_id)

Get an agent

[category 1 — Agent_Capabilities] Get agent by ID with all keys. Raises 404 if agent not found.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_id = 'agent_id_example' # str | Unique agent identifier

try: 
    # Get an agent
    api_response = api_instance.get_agent(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->get_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique agent identifier | 

### Return type

[**AgentRegistrationResponse201**](AgentRegistrationResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_key**
> AddAgentKeyResponse201 get_agent_key(agent_id, key_id)

Get a key by agent and key ID

Get a specific key by agent ID and key ID. Raises 404 if key not found.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_id = 'agent_id_example' # str | Unique agent identifier
key_id = 'key_id_example' # str | Unique key identifier

try: 
    # Get a key by agent and key ID
    api_response = api_instance.get_agent_key(agent_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->get_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique agent identifier | 
 **key_id** | **str**| Unique key identifier | 

### Return type

[**AddAgentKeyResponse201**](AddAgentKeyResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_purchase_intent**
> AgenticCreatePurchaseIntentResponse200 initiate_purchase_intent(agentic_create_purchase_intent_request)

Initiate a purchase intent

Create a new purchase intent (instruction) for an agentic transaction. The agent calls this endpoint after a card has been enrolled to define what the consumer wants to buy. The request includes payment instrument references, device and assurance data, mandates (spending limits, merchant preferences, and product descriptions), and optional buyer information. Return an instructionId (HTTP 200) if the intent is created immediately, or PENDING (HTTP 202) with pendingEvents if cardholder authentication is required. The instructionId returned is used in all subsequent operations - update, cancel, retrieve credentials, and confirm transaction.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agentic_create_purchase_intent_request = CyberSource.AgenticCreatePurchaseIntentRequest() # AgenticCreatePurchaseIntentRequest | 

try: 
    # Initiate a purchase intent
    api_response = api_instance.initiate_purchase_intent(agentic_create_purchase_intent_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->initiate_purchase_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentic_create_purchase_intent_request** | [**AgenticCreatePurchaseIntentRequest**](AgenticCreatePurchaseIntentRequest.md)|  | 

### Return type

[**AgenticCreatePurchaseIntentResponse200**](AgenticCreatePurchaseIntentResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_keys**
> ListAgentKeysResponse200 list_agent_keys(agent_id, page=page, page_size=page_size)

List keys for an agent

[category 1 — Agent_Capabilities] List all keys for a specific agent with pagination.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_id = 'agent_id_example' # str | Unique agent identifier
page = 1 # int | Page number (1-indexed) (optional) (default to 1)
page_size = 30 # int | Items per page (max 100) (optional) (default to 30)

try: 
    # List keys for an agent
    api_response = api_instance.list_agent_keys(agent_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->list_agent_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique agent identifier | 
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Items per page (max 100) | [optional] [default to 30]

### Return type

[**ListAgentKeysResponse200**](ListAgentKeysResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_agent**
> AgentRegistrationResponse201 register_agent(agent_request)

Register an agent

Register a new AI agent in the VARS. Once registered, the agent can upload public keys that merchants and Visa services use to verify request signatures. Raises 409 if domain, contactEmail, or tokenRequestorId already exists.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_request = CyberSource.AgentRequest() # AgentRequest | Agent registration request

try: 
    # Register an agent
    api_response = api_instance.register_agent(agent_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->register_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_request** | [**AgentRequest**](AgentRequest.md)| Agent registration request | 

### Return type

[**AgentRegistrationResponse201**](AgentRegistrationResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_payment_credentials**
> AgenticRetrievePaymentCredentialsResponse200 retrieve_payment_credentials(instruction_id, agentic_retrieve_payment_credentials_request)

Retrieve payment credentials

Retrieve tokenized payment credentials for a purchase intent to complete the transaction at a merchant. The agent calls this endpoint after a purchase intent has been created and approved, providing transaction-level details including order information, merchant details, payment options, and production information. Returns COMPLETED (HTTP 200) with a signed payload containing encrypted payment credentials (authorization token and JWS-signed payload), or PENDING (HTTP 202) with pendingEvents if additional cardholder authentication is required. The signed payload is used by the merchant's payment processor to complete the transaction.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
instruction_id = 'instruction_id_example' # str | Unique identifier for the purchase intent instruction.
agentic_retrieve_payment_credentials_request = CyberSource.AgenticRetrievePaymentCredentialsRequest() # AgenticRetrievePaymentCredentialsRequest | 

try: 
    # Retrieve payment credentials
    api_response = api_instance.retrieve_payment_credentials(instruction_id, agentic_retrieve_payment_credentials_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->retrieve_payment_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instruction_id** | **str**| Unique identifier for the purchase intent instruction. | 
 **agentic_retrieve_payment_credentials_request** | [**AgenticRetrievePaymentCredentialsRequest**](AgenticRetrievePaymentCredentialsRequest.md)|  | 

### Return type

[**AgenticRetrievePaymentCredentialsResponse200**](AgenticRetrievePaymentCredentialsResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent**
> AgentRegistrationResponse201 update_agent(agent_id, agent_update)

Update an agent

[category 1 — Agent_Capabilities] Update agent information. Updatable fields are name, domain, description, contactEmail, and agentMetadata. Extra fields (e.g. tokenRequestorId, keys) will return 422 Validation Error. Raises 404 if agent not found, 403 if agent is deactivated, 409 if new domain or contactEmail already exists.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_id = 'agent_id_example' # str | Unique agent identifier
agent_update = CyberSource.AgentUpdate() # AgentUpdate | Agent update request

try: 
    # Update an agent
    api_response = api_instance.update_agent(agent_id, agent_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->update_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique agent identifier | 
 **agent_update** | [**AgentUpdate**](AgentUpdate.md)| Agent update request | 

### Return type

[**AgentRegistrationResponse201**](AgentRegistrationResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_key**
> AddAgentKeyResponse201 update_agent_key(agent_id, key_id, key_update)

Update a key

Update key information. Updatable fields are keyName, publicKey, algorithm, and expirationDate. Raises 404 if agent or key not found, 403 if agent or key is deactivated, 409 if new keyName already exists.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
agent_id = 'agent_id_example' # str | Unique agent identifier
key_id = 'key_id_example' # str | Unique key identifier
key_update = CyberSource.KeyUpdate() # KeyUpdate | Key update request

try: 
    # Update a key
    api_response = api_instance.update_agent_key(agent_id, key_id, key_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->update_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique agent identifier | 
 **key_id** | **str**| Unique key identifier | 
 **key_update** | [**KeyUpdate**](KeyUpdate.md)| Key update request | 

### Return type

[**AddAgentKeyResponse201**](AddAgentKeyResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_purchase_intent**
> AgenticCreatePurchaseIntentResponse200 update_purchase_intent(instruction_id, agentic_update_purchase_intent_request)

Update a purchase intent

Update an existing purchase intent (instruction) identified by its instructionId. The agent calls this endpoint when the consumer modifies their order — for example, changing the quantity, updating mandates, switching payment instruments, or changing shipping details. The request body has the same structure as the initiate request. Returns the same instructionId (HTTP 200) on success, or PENDING (HTTP 202) with pendingEvents if additional cardholder authentication is required for the updated intent.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.AgentCapabilitiesApi()
instruction_id = 'instruction_id_example' # str | Unique identifier for the purchase intent instruction.
agentic_update_purchase_intent_request = CyberSource.AgenticUpdatePurchaseIntentRequest() # AgenticUpdatePurchaseIntentRequest | 

try: 
    # Update a purchase intent
    api_response = api_instance.update_purchase_intent(instruction_id, agentic_update_purchase_intent_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCapabilitiesApi->update_purchase_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instruction_id** | **str**| Unique identifier for the purchase intent instruction. | 
 **agentic_update_purchase_intent_request** | [**AgenticUpdatePurchaseIntentRequest**](AgenticUpdatePurchaseIntentRequest.md)|  | 

### Return type

[**AgenticCreatePurchaseIntentResponse200**](AgenticCreatePurchaseIntentResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

