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
class SecureFileShareApi(object):
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



    def get_file(self, file_id, **kwargs):
        """
        Download a File with File Identifier
        Download a file for the given file identifier
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file(file_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_id: Unique identifier for each file (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_file` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_file_with_http_info(file_id, **kwargs)
        else:
            (data) = self.get_file_with_http_info(file_id, **kwargs)
            return data

    def get_file_with_http_info(self, file_id, **kwargs):
        """
        Download a File with File Identifier
        Download a file for the given file identifier
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file_with_http_info(file_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_id: Unique identifier for each file (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_id', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params) or (params['file_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `file_id` when calling `get_file`")
            raise ValueError("Missing the required parameter `file_id` when calling `get_file`")


        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']
            fileId=file_id

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/xml', 'text/csv', 'application/pdf'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['*/*;charset=utf-8'])

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        
        file_post_body_and_delimiter = MultipartHelpers.build_post_body_for_files(local_var_files)
        if file_post_body_and_delimiter is not None:
            body_params = file_post_body_and_delimiter[0]
            header_params['Content-Type'] = f"multipart/form-data; boundary={file_post_body_and_delimiter[1]}" 

        is_mle_supported_by_cybs_for_api = False
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "get_file,get_file_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/sfs/v1/files/{fileId}', 'GET',
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

    def get_file_detail(self, start_date, end_date, **kwargs):
        """
        Get List of Files
        Get list of files and it's information of them available inside the report directory
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file_detail(start_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date start_date: Valid start date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)   **Example date format:**   - yyyy-MM-dd  (required)
        :param date end_date: Valid end date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)   **Example date format:**   - yyyy-MM-dd  (required)
        :param str organization_id: Valid Cybersource Organization Id
        :param str name: **Tailored to searches for specific files with in given Date range** example : MyTransactionDetailreport.xml 
        :return: V1FileDetailsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_file_detail` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_file_detail_with_http_info(start_date, end_date, **kwargs)
        else:
            (data) = self.get_file_detail_with_http_info(start_date, end_date, **kwargs)
            return data

    def get_file_detail_with_http_info(self, start_date, end_date, **kwargs):
        """
        Get List of Files
        Get list of files and it's information of them available inside the report directory
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file_detail_with_http_info(start_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date start_date: Valid start date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)   **Example date format:**   - yyyy-MM-dd  (required)
        :param date end_date: Valid end date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)   **Example date format:**   - yyyy-MM-dd  (required)
        :param str organization_id: Valid Cybersource Organization Id
        :param str name: **Tailored to searches for specific files with in given Date range** example : MyTransactionDetailreport.xml 
        :return: V1FileDetailsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'organization_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `start_date` when calling `get_file_detail`")
            raise ValueError("Missing the required parameter `start_date` when calling `get_file_detail`")
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `end_date` when calling `get_file_detail`")
            raise ValueError("Missing the required parameter `end_date` when calling `get_file_detail`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))
        if 'name' in params:
            query_params.append(('name', params['name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['*/*;charset=utf-8'])

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        
        file_post_body_and_delimiter = MultipartHelpers.build_post_body_for_files(local_var_files)
        if file_post_body_and_delimiter is not None:
            body_params = file_post_body_and_delimiter[0]
            header_params['Content-Type'] = f"multipart/form-data; boundary={file_post_body_and_delimiter[1]}" 

        is_mle_supported_by_cybs_for_api = False
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "get_file_detail,get_file_detail_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/sfs/v1/file-details', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='V1FileDetailsGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
