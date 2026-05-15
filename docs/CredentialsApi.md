# CyberSource.CredentialsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provision_mpp_credentials**](CredentialsApi.md#provision_mpp_credentials) | **POST** /acp/v1/mpp/credentials | Provision MPP credentials


# **provision_mpp_credentials**
> MppCredentialsResponse200 provision_mpp_credentials(mpp_credentials_request)

Provision MPP credentials

Provisions an encrypted MPP credential for use as the credential payload in an Authorization: Payment header (MPP spec Section 8.2). The caller provides an instrument identifier (referencing a stored card in TMS) and the challenge context from the merchant's 402 response, including the merchant's RSA public encryption key. This service:   1. Calls TMS to retrieve the network token and cryptogram for the instrument.   2. Builds the token plaintext (MPP spec Section 8.3, type: network_token).   3. Encrypts the plaintext using RSA-OAEP with SHA-256 and the merchant's public key.   4. Returns the MPP credential payload fields (MPP spec Section 8.2, Table 4). 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CredentialsApi()
mpp_credentials_request = CyberSource.MppCredentialsRequest() # MppCredentialsRequest | 

try: 
    # Provision MPP credentials
    api_response = api_instance.provision_mpp_credentials(mpp_credentials_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->provision_mpp_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpp_credentials_request** | [**MppCredentialsRequest**](MppCredentialsRequest.md)|  | 

### Return type

[**MppCredentialsResponse200**](MppCredentialsResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

