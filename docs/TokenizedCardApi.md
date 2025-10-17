# CyberSource.TokenizedCardApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tokenized_card**](TokenizedCardApi.md#delete_tokenized_card) | **DELETE** /tms/v2/tokenized-cards/{tokenizedCardId} | Delete a Tokenized Card
[**get_tokenized_card**](TokenizedCardApi.md#get_tokenized_card) | **GET** /tms/v2/tokenized-cards/{tokenizedCardId} | Retrieve a Tokenized Card
[**post_issuer_life_cycle_simulation**](TokenizedCardApi.md#post_issuer_life_cycle_simulation) | **POST** /tms/v2/tokenized-cards/{tokenizedCardId}/issuer-life-cycle-event-simulations | Simulate Issuer Life Cycle Management Events
[**post_tokenized_card**](TokenizedCardApi.md#post_tokenized_card) | **POST** /tms/v2/tokenized-cards | Create a Tokenized Card


# **delete_tokenized_card**
> delete_tokenized_card(tokenized_card_id, profile_id=profile_id)

Delete a Tokenized Card

|  |  |  | | --- | --- | --- | | The Network Token will attempt to be deleted from the card association and if successful the corresponding TMS Network Token will be deleted. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TokenizedCardApi()
tokenized_card_id = 'tokenized_card_id_example' # str | The Id of a tokenized card.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Delete a Tokenized Card
    api_instance.delete_tokenized_card(tokenized_card_id, profile_id=profile_id)
except ApiException as e:
    print("Exception when calling TokenizedCardApi->delete_tokenized_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenized_card_id** | **str**| The Id of a tokenized card. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokenized_card**
> TokenizedcardRequest get_tokenized_card(tokenized_card_id, profile_id=profile_id)

Retrieve a Tokenized Card

|  |  |  | | --- | --- | --- | |**Tokenized Cards**<br>A Tokenized Card represents a network token. Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires.  

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TokenizedCardApi()
tokenized_card_id = 'tokenized_card_id_example' # str | The Id of a tokenized card.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve a Tokenized Card
    api_response = api_instance.get_tokenized_card(tokenized_card_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizedCardApi->get_tokenized_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenized_card_id** | **str**| The Id of a tokenized card. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**TokenizedcardRequest**](TokenizedcardRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_issuer_life_cycle_simulation**
> post_issuer_life_cycle_simulation(profile_id, tokenized_card_id, post_issuer_life_cycle_simulation_request)

Simulate Issuer Life Cycle Management Events

**Lifecycle Management Events**<br>Simulates an issuer life cycle manegement event for updates on the tokenized card. The events that can be simulated are: - Token status changes (e.g. active, suspended, deleted) - Updates to the underlying card, including card art changes, expiration date changes, and card number suffix. **Note:** This is only available in CAS environment. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TokenizedCardApi()
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration.
tokenized_card_id = 'tokenized_card_id_example' # str | The Id of a tokenized card.
post_issuer_life_cycle_simulation_request = CyberSource.PostIssuerLifeCycleSimulationRequest() # PostIssuerLifeCycleSimulationRequest | 

try: 
    # Simulate Issuer Life Cycle Management Events
    api_instance.post_issuer_life_cycle_simulation(profile_id, tokenized_card_id, post_issuer_life_cycle_simulation_request)
except ApiException as e:
    print("Exception when calling TokenizedCardApi->post_issuer_life_cycle_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | 
 **tokenized_card_id** | **str**| The Id of a tokenized card. | 
 **post_issuer_life_cycle_simulation_request** | [**PostIssuerLifeCycleSimulationRequest**](PostIssuerLifeCycleSimulationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tokenized_card**
> TokenizedcardRequest post_tokenized_card(tokenizedcard_request, profile_id=profile_id)

Create a Tokenized Card

|  |  |  | | --- | --- | --- | |**Tokenized cards**<br>A Tokenized card represents a network token. Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TokenizedCardApi()
tokenizedcard_request = CyberSource.TokenizedcardRequest() # TokenizedcardRequest | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Create a Tokenized Card
    api_response = api_instance.post_tokenized_card(tokenizedcard_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizedCardApi->post_tokenized_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenizedcard_request** | [**TokenizedcardRequest**](TokenizedcardRequest.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**TokenizedcardRequest**](TokenizedcardRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

