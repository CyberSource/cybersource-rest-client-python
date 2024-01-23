# CyberSource.TokenApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_token_payment_credentials**](TokenApi.md#post_token_payment_credentials) | **POST** /tms/v2/tokens/{tokenId}/payment-credentials | Generate Payment Credentials for a TMS Token


# **post_token_payment_credentials**
> str post_token_payment_credentials(token_id, post_payment_credentials_request, profile_id=profile_id)

Generate Payment Credentials for a TMS Token

|  |  |  |     | --- | --- | --- |     |**Token**<br>A Token can represent your tokenized Customer, Payment Instrument or Instrument Identifier information.|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Payment Credentials**<br>Contains payment information such as the network token, generated cryptogram for Visa & MasterCard or dynamic CVV for Amex in a JSON Web Encryption (JWE) response.<br>Your system can use this API to retrieve the Payment Credentials for an existing Customer, Payment Instrument or Instrument Identifier. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.TokenApi()
token_id = 'token_id_example' # str | The Id of a token representing a Customer, Payment Instrument or Instrument Identifier.
post_payment_credentials_request = CyberSource.PostPaymentCredentialsRequest() # PostPaymentCredentialsRequest | 
profile_id = 'profile_id_example' # str | The Id of a profile containing user specific TMS configuration. (optional)

try: 
    # Generate Payment Credentials for a TMS Token
    api_response = api_instance.post_token_payment_credentials(token_id, post_payment_credentials_request, profile_id=profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->post_token_payment_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The Id of a token representing a Customer, Payment Instrument or Instrument Identifier. | 
 **post_payment_credentials_request** | [**PostPaymentCredentialsRequest**](PostPaymentCredentialsRequest.md)|  | 
 **profile_id** | **str**| The Id of a profile containing user specific TMS configuration. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/jose;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

