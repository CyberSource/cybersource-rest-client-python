# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
import CyberSource.logging.log_factory as LogFactory

from ..utilities.tracking.sdk_tracker import SdkTracker
class OrdersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config)
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.api_client.mconfig.log_config)



    def create_order(self, create_order_request, **kwargs):
        """
        Create an Order
        A create order request enables you to send the itemized details along with the order. This API can be used by merchants initiating their transactions with the create order API.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_order(create_order_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateOrderRequest create_order_request: (required)
        :return: PtsV2CreateOrderPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `create_order` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_order_with_http_info(create_order_request, **kwargs)
        else:
            (data) = self.create_order_with_http_info(create_order_request, **kwargs)
            return data

    def create_order_with_http_info(self, create_order_request, **kwargs):
        """
        Create an Order
        A create order request enables you to send the itemized details along with the order. This API can be used by merchants initiating their transactions with the create order API.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_order_with_http_info(create_order_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateOrderRequest create_order_request: (required)
        :return: PtsV2CreateOrderPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_order_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_order_request' is set
        if ('create_order_request' not in params) or (params['create_order_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_order_request` when calling `create_order`")
            raise ValueError("Missing the required parameter `create_order_request` when calling `create_order`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_order_request' in params:
            body_params = params['create_order_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'create_order_request', self.api_client.mconfig.run_environment, self.api_client.mconfig.defaultDeveloperId)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/pts/v2/intents', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2CreateOrderPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_order(self, id, update_order_request, **kwargs):
        """
        Update an Order
        This API can be used in two flavours - for updating the order as well as saving the order. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_order(id, update_order_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The ID returned from the original create order response. (required)
        :param UpdateOrderRequest update_order_request: (required)
        :return: PtsV2UpdateOrderPatch201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `update_order` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_order_with_http_info(id, update_order_request, **kwargs)
        else:
            (data) = self.update_order_with_http_info(id, update_order_request, **kwargs)
            return data

    def update_order_with_http_info(self, id, update_order_request, **kwargs):
        """
        Update an Order
        This API can be used in two flavours - for updating the order as well as saving the order. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_order_with_http_info(id, update_order_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The ID returned from the original create order response. (required)
        :param UpdateOrderRequest update_order_request: (required)
        :return: PtsV2UpdateOrderPatch201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'update_order_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `update_order`")
            raise ValueError("Missing the required parameter `id` when calling `update_order`")
        # verify the required parameter 'update_order_request' is set
        if ('update_order_request' not in params) or (params['update_order_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `update_order_request` when calling `update_order`")
            raise ValueError("Missing the required parameter `update_order_request` when calling `update_order`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
            id=id

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_order_request' in params:
            body_params = params['update_order_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'update_order_request', self.api_client.mconfig.run_environment, self.api_client.mconfig.defaultDeveloperId)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/pts/v2/intents/{id}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2UpdateOrderPatch201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)