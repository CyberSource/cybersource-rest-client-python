# CyberSource.InvoicesApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice**](InvoicesApi.md#create_invoice) | **POST** /invoicing/v2/invoices | Create a New Invoice
[**get_all_invoices**](InvoicesApi.md#get_all_invoices) | **GET** /invoicing/v2/invoices | Get a List of Invoices
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /invoicing/v2/invoices/{id} | Get Invoice Details
[**perform_cancel_action**](InvoicesApi.md#perform_cancel_action) | **POST** /invoicing/v2/invoices/{id}/cancelation | Cancel an Invoice
[**perform_send_action**](InvoicesApi.md#perform_send_action) | **POST** /invoicing/v2/invoices/{id}/delivery | Send an Invoice
[**update_invoice**](InvoicesApi.md#update_invoice) | **PUT** /invoicing/v2/invoices/{id} | Update an Invoice


# **create_invoice**
> InvoicingV2InvoicesPost201Response create_invoice(create_invoice_request)

Create a New Invoice

Create a new invoice.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InvoicesApi()
create_invoice_request = CyberSource.CreateInvoiceRequest() # CreateInvoiceRequest | 

try: 
    # Create a New Invoice
    api_response = api_instance.create_invoice(create_invoice_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invoice_request** | [**CreateInvoiceRequest**](CreateInvoiceRequest.md)|  | 

### Return type

[**InvoicingV2InvoicesPost201Response**](InvoicingV2InvoicesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_invoices**
> InvoicingV2InvoicesAllGet200Response get_all_invoices(offset, limit, status=status)

Get a List of Invoices

Get a list of invoices.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InvoicesApi()
offset = 56 # int | Page offset number.
limit = 56 # int | Maximum number of items you would like returned.
status = 'status_example' # str | The status of the invoice.  Possible values:   - DRAFT   - CREATED   - SENT   - PARTIAL   - PAID   - CANCELED  (optional)

try: 
    # Get a List of Invoices
    api_response = api_instance.get_all_invoices(offset, limit, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_all_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Page offset number. | 
 **limit** | **int**| Maximum number of items you would like returned. | 
 **status** | **str**| The status of the invoice.  Possible values:   - DRAFT   - CREATED   - SENT   - PARTIAL   - PAID   - CANCELED  | [optional] 

### Return type

[**InvoicingV2InvoicesAllGet200Response**](InvoicingV2InvoicesAllGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> InvoicingV2InvoicesGet200Response get_invoice(id)

Get Invoice Details

Get the details of a specific invoice.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InvoicesApi()
id = 'id_example' # str | The invoice number.

try: 
    # Get Invoice Details
    api_response = api_instance.get_invoice(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The invoice number. | 

### Return type

[**InvoicingV2InvoicesGet200Response**](InvoicingV2InvoicesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_cancel_action**
> InvoicingV2InvoicesPost201Response perform_cancel_action(id)

Cancel an Invoice

Cancel an invoice.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InvoicesApi()
id = 'id_example' # str | The invoice number.

try: 
    # Cancel an Invoice
    api_response = api_instance.perform_cancel_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->perform_cancel_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The invoice number. | 

### Return type

[**InvoicingV2InvoicesPost201Response**](InvoicingV2InvoicesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_send_action**
> InvoicingV2InvoicesPost201Response perform_send_action(id)

Send an Invoice

Send an invoice.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InvoicesApi()
id = 'id_example' # str | The invoice number.

try: 
    # Send an Invoice
    api_response = api_instance.perform_send_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->perform_send_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The invoice number. | 

### Return type

[**InvoicingV2InvoicesPost201Response**](InvoicingV2InvoicesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> InvoicingV2InvoicesPost201Response update_invoice(id, update_invoice_request)

Update an Invoice

Update an invoice.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.InvoicesApi()
id = 'id_example' # str | The invoice number.
update_invoice_request = CyberSource.UpdateInvoiceRequest() # UpdateInvoiceRequest | Updating the invoice does not resend the invoice automatically. You must resend the invoice separately.

try: 
    # Update an Invoice
    api_response = api_instance.update_invoice(id, update_invoice_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The invoice number. | 
 **update_invoice_request** | [**UpdateInvoiceRequest**](UpdateInvoiceRequest.md)| Updating the invoice does not resend the invoice automatically. You must resend the invoice separately. | 

### Return type

[**InvoicingV2InvoicesPost201Response**](InvoicingV2InvoicesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

