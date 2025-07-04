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
class ReversalApi(object):
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



    def auth_reversal(self, id, auth_reversal_request, **kwargs):
        """
        Process an Authorization Reversal
        Include the payment ID in the POST request to reverse the payment amount.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auth_reversal(id, auth_reversal_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The payment ID returned from a previous payment request. (required)
        :param AuthReversalRequest auth_reversal_request: (required)
        :return: PtsV2PaymentsReversalsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `auth_reversal` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.auth_reversal_with_http_info(id, auth_reversal_request, **kwargs)
        else:
            (data) = self.auth_reversal_with_http_info(id, auth_reversal_request, **kwargs)
            return data

    def auth_reversal_with_http_info(self, id, auth_reversal_request, **kwargs):
        """
        Process an Authorization Reversal
        Include the payment ID in the POST request to reverse the payment amount.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auth_reversal_with_http_info(id, auth_reversal_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The payment ID returned from a previous payment request. (required)
        :param AuthReversalRequest auth_reversal_request: (required)
        :return: PtsV2PaymentsReversalsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'auth_reversal_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_reversal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `auth_reversal`")
            raise ValueError("Missing the required parameter `id` when calling `auth_reversal`")
        # verify the required parameter 'auth_reversal_request' is set
        if ('auth_reversal_request' not in params) or (params['auth_reversal_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `auth_reversal_request` when calling `auth_reversal`")
            raise ValueError("Missing the required parameter `auth_reversal_request` when calling `auth_reversal`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
            id=id

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        body_params = None
        if 'auth_reversal_request' in params:
            body_params = params['auth_reversal_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'auth_reversal_request', self.api_client.mconfig.run_environment, self.api_client.mconfig.defaultDeveloperId)
            body_params = process_body(body_params)

        is_mle_supported_by_cybs_for_api = True
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "auth_reversal,auth_reversal_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/pts/v2/payments/{id}/reversals', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2PaymentsReversalsPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def mit_reversal(self, mit_reversal_request, **kwargs):
        """
        Timeout Reversal
        This is to reverse a previous payment that merchant does not receive a reply(Mostly due to Timeout). To use this feature/API, make sure to pass unique value to field - clientReferenceInformation -> transactionId in [/pts/v2/payments](https://developer.cybersource.com/api-reference-assets/index.html#payments_payments) API call and use same transactionId in this API request payload to reverse the payment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mit_reversal(mit_reversal_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MitReversalRequest mit_reversal_request: (required)
        :return: PtsV2PaymentsReversalsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `mit_reversal` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.mit_reversal_with_http_info(mit_reversal_request, **kwargs)
        else:
            (data) = self.mit_reversal_with_http_info(mit_reversal_request, **kwargs)
            return data

    def mit_reversal_with_http_info(self, mit_reversal_request, **kwargs):
        """
        Timeout Reversal
        This is to reverse a previous payment that merchant does not receive a reply(Mostly due to Timeout). To use this feature/API, make sure to pass unique value to field - clientReferenceInformation -> transactionId in [/pts/v2/payments](https://developer.cybersource.com/api-reference-assets/index.html#payments_payments) API call and use same transactionId in this API request payload to reverse the payment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mit_reversal_with_http_info(mit_reversal_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MitReversalRequest mit_reversal_request: (required)
        :return: PtsV2PaymentsReversalsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mit_reversal_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mit_reversal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mit_reversal_request' is set
        if ('mit_reversal_request' not in params) or (params['mit_reversal_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `mit_reversal_request` when calling `mit_reversal`")
            raise ValueError("Missing the required parameter `mit_reversal_request` when calling `mit_reversal`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        body_params = None
        if 'mit_reversal_request' in params:
            body_params = params['mit_reversal_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'mit_reversal_request', self.api_client.mconfig.run_environment, self.api_client.mconfig.defaultDeveloperId)
            body_params = process_body(body_params)

        is_mle_supported_by_cybs_for_api = True
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "mit_reversal,mit_reversal_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/pts/v2/reversals', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2PaymentsReversalsPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
