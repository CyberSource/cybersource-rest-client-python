# CyberSource.MerchantBoardingApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_registration**](MerchantBoardingApi.md#get_registration) | **GET** /boarding/v1/registrations/{registrationId} | Gets all the information on a boarding registration
[**post_registration**](MerchantBoardingApi.md#post_registration) | **POST** /boarding/v1/registrations | Create a boarding registration


# **get_registration**
> InlineResponse2002 get_registration(registration_id)

Gets all the information on a boarding registration

This end point will get all information of a boarding registration 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantBoardingApi()
registration_id = 'registration_id_example' # str | Identifies the boarding registration to be updated

try: 
    # Gets all the information on a boarding registration
    api_response = api_instance.get_registration(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantBoardingApi->get_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| Identifies the boarding registration to be updated | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_registration**
> InlineResponse2012 post_registration(post_registration_body, v_c_idempotency_id=v_c_idempotency_id)

Create a boarding registration

Boarding Product is specifically for resellers who onboard merchants to resell their services to merchants and help integrate REST API into their systems.  The Boarding API is designed to simplify and streamline the onboarding process of merchants by enabling administrators and developers to: 1. Enable and Configure Products: The API helps in adding new products to an existing organization and configuring them to suit specific needs. 2. Update Merchant Information: The API allows for updating an organization's information efficiently. 3. Manage Payment Integration: It provides templates for secure payment integration and management. 

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantBoardingApi()
post_registration_body = CyberSource.PostRegistrationBody() # PostRegistrationBody | Boarding registration data
v_c_idempotency_id = 'v_c_idempotency_id_example' # str | defines idempotency of the request (optional)

try: 
    # Create a boarding registration
    api_response = api_instance.post_registration(post_registration_body, v_c_idempotency_id=v_c_idempotency_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantBoardingApi->post_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_registration_body** | [**PostRegistrationBody**](PostRegistrationBody.md)| Boarding registration data | 
 **v_c_idempotency_id** | **str**| defines idempotency of the request | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

