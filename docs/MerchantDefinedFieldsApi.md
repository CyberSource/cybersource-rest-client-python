# CyberSource.MerchantDefinedFieldsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_merchant_defined_field_definition**](MerchantDefinedFieldsApi.md#create_merchant_defined_field_definition) | **POST** /invoicing/v2/{referenceType}/merchantDefinedFields | Create merchant defined field for a given reference type
[**invoicing_v2_reference_type_merchant_defined_fields_id_delete**](MerchantDefinedFieldsApi.md#invoicing_v2_reference_type_merchant_defined_fields_id_delete) | **DELETE** /invoicing/v2/{referenceType}/merchantDefinedFields/{id} | Delete a MerchantDefinedField by ID
[**invoicing_v2_reference_type_merchant_defined_fields_id_put**](MerchantDefinedFieldsApi.md#invoicing_v2_reference_type_merchant_defined_fields_id_put) | **PUT** /invoicing/v2/{referenceType}/merchantDefinedFields/{id} | Update a MerchantDefinedField by ID


# **create_merchant_defined_field_definition**
> list[InlineResponse2002] create_merchant_defined_field_definition(reference_type, merchant_defined_field_definition_request)

Create merchant defined field for a given reference type

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantDefinedFieldsApi()
reference_type = 'reference_type_example' # str | The reference type for which merchant defined fields are to be fetched. Available values are Invoice, Purchase, Donation
merchant_defined_field_definition_request = CyberSource.MerchantDefinedFieldDefinitionRequest() # MerchantDefinedFieldDefinitionRequest | 

try: 
    # Create merchant defined field for a given reference type
    api_response = api_instance.create_merchant_defined_field_definition(reference_type, merchant_defined_field_definition_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantDefinedFieldsApi->create_merchant_defined_field_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_type** | **str**| The reference type for which merchant defined fields are to be fetched. Available values are Invoice, Purchase, Donation | 
 **merchant_defined_field_definition_request** | [**MerchantDefinedFieldDefinitionRequest**](MerchantDefinedFieldDefinitionRequest.md)|  | 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoicing_v2_reference_type_merchant_defined_fields_id_delete**
> invoicing_v2_reference_type_merchant_defined_fields_id_delete(reference_type, id)

Delete a MerchantDefinedField by ID

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantDefinedFieldsApi()
reference_type = 'reference_type_example' # str | 
id = 789 # int | 

try: 
    # Delete a MerchantDefinedField by ID
    api_instance.invoicing_v2_reference_type_merchant_defined_fields_id_delete(reference_type, id)
except ApiException as e:
    print("Exception when calling MerchantDefinedFieldsApi->invoicing_v2_reference_type_merchant_defined_fields_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_type** | **str**|  | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoicing_v2_reference_type_merchant_defined_fields_id_put**
> list[InlineResponse2002] invoicing_v2_reference_type_merchant_defined_fields_id_put(reference_type, id, merchant_defined_field_core)

Update a MerchantDefinedField by ID

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.MerchantDefinedFieldsApi()
reference_type = 'reference_type_example' # str | 
id = 789 # int | 
merchant_defined_field_core = CyberSource.MerchantDefinedFieldCore() # MerchantDefinedFieldCore | 

try: 
    # Update a MerchantDefinedField by ID
    api_response = api_instance.invoicing_v2_reference_type_merchant_defined_fields_id_put(reference_type, id, merchant_defined_field_core)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantDefinedFieldsApi->invoicing_v2_reference_type_merchant_defined_fields_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_type** | **str**|  | 
 **id** | **int**|  | 
 **merchant_defined_field_core** | [**MerchantDefinedFieldCore**](MerchantDefinedFieldCore.md)|  | 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

