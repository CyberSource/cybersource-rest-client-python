# CyberSource.NetworkTokensApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_card_art_asset**](NetworkTokensApi.md#get_card_art_asset) | **GET** /tms/v2/tokens/{instrumentIdentifierId}/{tokenProvider}/assets/{assetType} | Retrieve Card Art
[**get_tokenized_card**](NetworkTokensApi.md#get_tokenized_card) | **GET** /tms/v2/tokenized-cards/{tokenizedCardId} | Retrieve a Tokenized Card
[**post_issuer_life_cycle_simulation**](NetworkTokensApi.md#post_issuer_life_cycle_simulation) | **POST** /tms/v2/tokenized-cards/{tokenizedCardId}/issuer-life-cycle-event-simulations | Simulate Issuer Life Cycle Management Events
[**post_token_payment_credentials**](NetworkTokensApi.md#post_token_payment_credentials) | **POST** /tms/v2/tokens/{tokenId}/payment-credentials | Generate Payment Credentials v2
[**post_token_payment_credentials_v3**](NetworkTokensApi.md#post_token_payment_credentials_v3) | **POST** /tms/v3/tokens/{tokenId}/payment-credentials | Generate Payment Credentials Latest Version v3
[**post_tokenized_card**](NetworkTokensApi.md#post_tokenized_card) | **POST** /tms/v2/tokenized-cards | Create a Tokenized Card
[**post_tokenized_card_delete**](NetworkTokensApi.md#post_tokenized_card_delete) | **POST** /tms/v2/tokenized-cards/{tokenizedCardId}/delete | Delete a Tokenized Card


# **get_card_art_asset**
> InlineResponse2002 get_card_art_asset(instrument_identifier_id, token_provider, asset_type)

Retrieve Card Art

Retrieves Card Art for a specific Instrument Identifier. The Card Art is a visual representation of the cardholder's payment card. Card Art is only available if a Network Token is successfully provisioned. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.NetworkTokensApi()
instrument_identifier_id = 'instrument_identifier_id_example' # str | The Id of an Instrument Identifier.
token_provider = 'token_provider_example' # str | The token provider.
asset_type = 'asset_type_example' # str | The type of asset.

try: 
    # Retrieve Card Art
    api_response = api_instance.get_card_art_asset(instrument_identifier_id, token_provider, asset_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkTokensApi->get_card_art_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_id** | **str**| The Id of an Instrument Identifier. | 
 **token_provider** | **str**| The token provider. | 
 **asset_type** | **str**| The type of asset. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokenized_card**
> InlineResponse2001 get_tokenized_card(tokenized_card_id, profile_id=profile_id)

Retrieve a Tokenized Card

|**Tokenized Cards**<br>A Tokenized Card represents a network token. Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires. This API returns the details of a tokenized card stored in TMS. You can use this API to check the status of a tokenized card and retrieve details such as the last four digits of the underlying card, expiration date, and card type. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.NetworkTokensApi()
tokenized_card_id = 'tokenized_card_id_example' # str | The Id of a tokenized card.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Retrieve a Tokenized Card
    api_response = api_instance.get_tokenized_card(tokenized_card_id, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkTokensApi->get_tokenized_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenized_card_id** | **str**| The Id of a tokenized card. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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
api_instance = CyberSource.NetworkTokensApi()
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration.
tokenized_card_id = 'tokenized_card_id_example' # str | The Id of a tokenized card.
post_issuer_life_cycle_simulation_request = CyberSource.PostIssuerLifeCycleSimulationRequest() # PostIssuerLifeCycleSimulationRequest | 

try: 
    # Simulate Issuer Life Cycle Management Events
    api_instance.post_issuer_life_cycle_simulation(profile_id, tokenized_card_id, post_issuer_life_cycle_simulation_request)
except ApiException as e:
    print("Exception when calling NetworkTokensApi->post_issuer_life_cycle_simulation: %s\n" % e)
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

# **post_token_payment_credentials**
> str post_token_payment_credentials(token_id, post_payment_credentials_request, profile_id=profile_id)

Generate Payment Credentials v2

**Note**: This resource will be replace by [payment credentials version 3](#/paths/~1tms~1v3~1tokens~1{tokenId}~1payment-credentials/post). The SDK will remain available for now; however, it will no longer be documented or maintain in the Developer Centre.<br> **Token**<br>A Token can represent your tokenized Customer, Payment Instrument, Instrument Identifier or Tokenized Card information.<br> **Payment Credentials**<br>Contains payment information such as the network token, generated cryptogram for Visa & MasterCard or dynamic CVV for Amex in a JSON Web Encryption (JWE) response.<br>Your system can use this API to retrieve the Payment Credentials for an existing Customer, Payment Instrument, Instrument Identifier or Tokenized Card.<br>Optionally, **authenticated identities** information from Passkey authentication can be provided to potentially achieve liability shift, which may result in the return of an e-commerce indicator of 5 if successful. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.NetworkTokensApi()
token_id = 'token_id_example' # str | The Id of a token representing a Customer, Payment Instrument or Instrument Identifier.
post_payment_credentials_request = CyberSource.PostPaymentCredentialsRequest1() # PostPaymentCredentialsRequest1 | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Generate Payment Credentials v2
    api_response = api_instance.post_token_payment_credentials(token_id, post_payment_credentials_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkTokensApi->post_token_payment_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The Id of a token representing a Customer, Payment Instrument or Instrument Identifier. | 
 **post_payment_credentials_request** | [**PostPaymentCredentialsRequest1**](PostPaymentCredentialsRequest1.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/jose;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_token_payment_credentials_v3**
> InlineResponse2011 post_token_payment_credentials_v3(token_id, post_payment_credentials_request, profile_id=profile_id)

Generate Payment Credentials Latest Version v3

**Payment Credentials**<br>Contains payment information such as the network token, generated TAVV cryptogram for Visa & MasterCard, dynamic CVV for Amex, or DTVV cryptogram for VISA. This latest version (v3) returns the Primary Account Number details, if the network token is not present. The response is provided in JSON Web Encryption (JWE) format. <br>Your system can use this API to retrieve the Payment Credentials for an existing Customer, Payment Instrument, Instrument Identifier or Tokenized Card.<br>Optionally, **authenticated identities** information from Passkey authentication can be provided to potentially achieve liability shift, which may result in the return of an e-commerce indicator of 5 if successful. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.NetworkTokensApi()
token_id = 'token_id_example' # str | The Id of a token representing a Customer, Payment Instrument or Instrument Identifier.
post_payment_credentials_request = CyberSource.PostPaymentCredentialsRequest() # PostPaymentCredentialsRequest | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Generate Payment Credentials Latest Version v3
    api_response = api_instance.post_token_payment_credentials_v3(token_id, post_payment_credentials_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkTokensApi->post_token_payment_credentials_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The Id of a token representing a Customer, Payment Instrument or Instrument Identifier. | 
 **post_payment_credentials_request** | [**PostPaymentCredentialsRequest**](PostPaymentCredentialsRequest.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/jose;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tokenized_card**
> InlineResponse2001 post_tokenized_card(post_tokenized_card_request, profile_id=profile_id)

Create a Tokenized Card

**Tokenized cards**<br>A Tokenized card represents a network token. Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires. This API submits a request to the card association to create a network token. If successful, a tokenized card will be created in TMS to represent the network token. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.NetworkTokensApi()
post_tokenized_card_request = CyberSource.PostTokenizedCardRequest() # PostTokenizedCardRequest | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Create a Tokenized Card
    api_response = api_instance.post_tokenized_card(post_tokenized_card_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkTokensApi->post_tokenized_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_tokenized_card_request** | [**PostTokenizedCardRequest**](PostTokenizedCardRequest.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tokenized_card_delete**
> post_tokenized_card_delete(tokenized_card_id, profile_id=profile_id, post_tokenized_card_delete_request=post_tokenized_card_delete_request)

Delete a Tokenized Card

This API attempts to delete a network token from the card association with a specified reason. | If successful, the corresponding tokenized card will be deleted. | The reason for deletion can be specified to provide context for the deletion operation. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.NetworkTokensApi()
tokenized_card_id = 'tokenized_card_id_example' # str | The Id of a tokenized card.
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)
post_tokenized_card_delete_request = CyberSource.TmsTokenizedCardDeleteRequest() # TmsTokenizedCardDeleteRequest |  (optional)

try: 
    # Delete a Tokenized Card
    api_instance.post_tokenized_card_delete(tokenized_card_id, profile_id=profile_id, post_tokenized_card_delete_request=post_tokenized_card_delete_request)
except ApiException as e:
    print("Exception when calling NetworkTokensApi->post_tokenized_card_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenized_card_id** | **str**| The Id of a tokenized card. | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 
 **post_tokenized_card_delete_request** | [**TmsTokenizedCardDeleteRequest**](TmsTokenizedCardDeleteRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

