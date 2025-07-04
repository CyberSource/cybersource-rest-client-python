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
from CyberSource.utilities.MultipartHelpers import MultipartHelpers
from authenticationsdk.util.MLEUtility import MLEUtility
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
from authenticationsdk.util.Utility import process_body

from ..utilities.tracking.sdk_tracker import SdkTracker
class TransientTokenDataApi(object):
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



    def get_payment_credentials_for_transient_token(self, payment_credentials_reference, **kwargs):
        """
        Get Payment Credentials
        Retrieve the Payment data captured by Unified Checkout. This API is used to retrieve the detailed data represented by the Transient Token. This API will return PCI payment data captured by the Unified Checkout platform.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_credentials_for_transient_token(payment_credentials_reference, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str payment_credentials_reference: The paymentCredentialsReference field contained within the Transient token returned from a successful Unified Checkout transaction  (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_payment_credentials_for_transient_token` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_payment_credentials_for_transient_token_with_http_info(payment_credentials_reference, **kwargs)
        else:
            (data) = self.get_payment_credentials_for_transient_token_with_http_info(payment_credentials_reference, **kwargs)
            return data

    def get_payment_credentials_for_transient_token_with_http_info(self, payment_credentials_reference, **kwargs):
        """
        Get Payment Credentials
        Retrieve the Payment data captured by Unified Checkout. This API is used to retrieve the detailed data represented by the Transient Token. This API will return PCI payment data captured by the Unified Checkout platform.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_credentials_for_transient_token_with_http_info(payment_credentials_reference, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str payment_credentials_reference: The paymentCredentialsReference field contained within the Transient token returned from a successful Unified Checkout transaction  (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_credentials_reference']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_credentials_for_transient_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_credentials_reference' is set
        if ('payment_credentials_reference' not in params) or (params['payment_credentials_reference'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `payment_credentials_reference` when calling `get_payment_credentials_for_transient_token`")
            raise ValueError("Missing the required parameter `payment_credentials_reference` when calling `get_payment_credentials_for_transient_token`")


        collection_formats = {}

        path_params = {}
        if 'payment_credentials_reference' in params:
            path_params['paymentCredentialsReference'] = params['payment_credentials_reference']
            paymentCredentialsReference=payment_credentials_reference

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/jwt'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        
        file_post_body_and_delimiter = MultipartHelpers.build_post_body_for_files(local_var_files)
        if file_post_body_and_delimiter is not None:
            body_params = file_post_body_and_delimiter[0]
            header_params['Content-Type'] = f"multipart/form-data; boundary={file_post_body_and_delimiter[1]}" 

        is_mle_supported_by_cybs_for_api = False
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "get_payment_credentials_for_transient_token,get_payment_credentials_for_transient_token_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/flex/v2/payment-credentials/{paymentCredentialsReference}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_transaction_for_transient_token(self, transient_token, **kwargs):
        """
        Get Transient Token Data
        Retrieve the data captured by Unified Checkout. This API is used to retrieve the detailed data represented by the Transient Token. This API will not return PCI payment data (PAN). Include the Request ID in the GET request to retrieve the transaction details.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transaction_for_transient_token(transient_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str transient_token: Transient Token returned by the Unified Checkout application.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_transaction_for_transient_token` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_transaction_for_transient_token_with_http_info(transient_token, **kwargs)
        else:
            (data) = self.get_transaction_for_transient_token_with_http_info(transient_token, **kwargs)
            return data

    def get_transaction_for_transient_token_with_http_info(self, transient_token, **kwargs):
        """
        Get Transient Token Data
        Retrieve the data captured by Unified Checkout. This API is used to retrieve the detailed data represented by the Transient Token. This API will not return PCI payment data (PAN). Include the Request ID in the GET request to retrieve the transaction details.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transaction_for_transient_token_with_http_info(transient_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str transient_token: Transient Token returned by the Unified Checkout application.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transient_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction_for_transient_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transient_token' is set
        if ('transient_token' not in params) or (params['transient_token'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `transient_token` when calling `get_transaction_for_transient_token`")
            raise ValueError("Missing the required parameter `transient_token` when calling `get_transaction_for_transient_token`")


        collection_formats = {}

        path_params = {}
        if 'transient_token' in params:
            path_params['transientToken'] = params['transient_token']
            transientToken=transient_token

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        
        file_post_body_and_delimiter = MultipartHelpers.build_post_body_for_files(local_var_files)
        if file_post_body_and_delimiter is not None:
            body_params = file_post_body_and_delimiter[0]
            header_params['Content-Type'] = f"multipart/form-data; boundary={file_post_body_and_delimiter[1]}" 

        is_mle_supported_by_cybs_for_api = False
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "get_transaction_for_transient_token,get_transaction_for_transient_token_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/up/v1/payment-details/{transientToken}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
