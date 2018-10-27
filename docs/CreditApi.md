# CyberSource.CreditApi

All URIs are relative to *https://api.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit**](CreditApi.md#create_credit) | **POST** /v2/credits/ | Process a Credit
[**get_credit**](CreditApi.md#get_credit) | **GET** /v2/credits/{id} | Retrieve a Credit


# **create_credit**
> InlineResponse2014 create_credit(create_credit_request)

Process a Credit

POST to the credit resource to credit funds to a specified credit card.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CreditApi()
create_credit_request = CyberSource.CreateCreditRequest() # CreateCreditRequest | 

try: 
    # Process a Credit
    api_response = api_instance.create_credit(create_credit_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditApi->create_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_credit_request** | [**CreateCreditRequest**](CreateCreditRequest.md)|  | 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit**
> InlineResponse2006 get_credit(id)

Retrieve a Credit

Include the credit ID in the GET request to return details of the credit.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.CreditApi()
id = 'id_example' # str | The credit ID returned from a previous stand-alone credit request. 

try: 
    # Retrieve a Credit
    api_response = api_instance.get_credit(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditApi->get_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The credit ID returned from a previous stand-alone credit request.  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

