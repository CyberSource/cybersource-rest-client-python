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
class ReportSubscriptionsApi(object):
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



    def create_standard_or_classic_subscription(self, predefined_subscription_request_bean, **kwargs):
        """
        Create a Standard or Classic Subscription
        Create or update an already existing classic or standard subscription. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_standard_or_classic_subscription(predefined_subscription_request_bean, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PredefinedSubscriptionRequestBean predefined_subscription_request_bean: Report subscription request payload (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `create_standard_or_classic_subscription` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_standard_or_classic_subscription_with_http_info(predefined_subscription_request_bean, **kwargs)
        else:
            (data) = self.create_standard_or_classic_subscription_with_http_info(predefined_subscription_request_bean, **kwargs)
            return data

    def create_standard_or_classic_subscription_with_http_info(self, predefined_subscription_request_bean, **kwargs):
        """
        Create a Standard or Classic Subscription
        Create or update an already existing classic or standard subscription. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_standard_or_classic_subscription_with_http_info(predefined_subscription_request_bean, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PredefinedSubscriptionRequestBean predefined_subscription_request_bean: Report subscription request payload (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['predefined_subscription_request_bean', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_standard_or_classic_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'predefined_subscription_request_bean' is set
        if ('predefined_subscription_request_bean' not in params) or (params['predefined_subscription_request_bean'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `predefined_subscription_request_bean` when calling `create_standard_or_classic_subscription`")
            raise ValueError("Missing the required parameter `predefined_subscription_request_bean` when calling `create_standard_or_classic_subscription`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        body_params = None
        if 'predefined_subscription_request_bean' in params:
            body_params = params['predefined_subscription_request_bean']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'predefined_subscription_request_bean', self.api_client.mconfig.run_environment, self.api_client.mconfig.defaultDeveloperId)
            body_params = process_body(body_params)

        is_mle_supported_by_cybs_for_api = False
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "create_standard_or_classic_subscription,create_standard_or_classic_subscription_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/reporting/v3/predefined-report-subscriptions', 'PUT',
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

    def create_subscription(self, create_report_subscription_request, **kwargs):
        """
        Create Report Subscription for a Report Name by Organization
        Create a report subscription for your organization. The report name must be unique. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_subscription(create_report_subscription_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateReportSubscriptionRequest create_report_subscription_request: Report subscription request payload (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `create_subscription` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_subscription_with_http_info(create_report_subscription_request, **kwargs)
        else:
            (data) = self.create_subscription_with_http_info(create_report_subscription_request, **kwargs)
            return data

    def create_subscription_with_http_info(self, create_report_subscription_request, **kwargs):
        """
        Create Report Subscription for a Report Name by Organization
        Create a report subscription for your organization. The report name must be unique. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_subscription_with_http_info(create_report_subscription_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateReportSubscriptionRequest create_report_subscription_request: Report subscription request payload (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_report_subscription_request', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_report_subscription_request' is set
        if ('create_report_subscription_request' not in params) or (params['create_report_subscription_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_report_subscription_request` when calling `create_subscription`")
            raise ValueError("Missing the required parameter `create_report_subscription_request` when calling `create_subscription`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        body_params = None
        if 'create_report_subscription_request' in params:
            body_params = params['create_report_subscription_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'create_report_subscription_request', self.api_client.mconfig.run_environment, self.api_client.mconfig.defaultDeveloperId)
            body_params = process_body(body_params)

        is_mle_supported_by_cybs_for_api = False
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "create_subscription,create_subscription_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/reporting/v3/report-subscriptions', 'PUT',
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

    def delete_subscription(self, report_name, **kwargs):
        """
        Delete Subscription of a Report Name by Organization
        Delete a report subscription for your organization. You must know the unique name of the report you want to delete. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_subscription(report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_name: Name of the Report to Delete (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `delete_subscription` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_subscription_with_http_info(report_name, **kwargs)
        else:
            (data) = self.delete_subscription_with_http_info(report_name, **kwargs)
            return data

    def delete_subscription_with_http_info(self, report_name, **kwargs):
        """
        Delete Subscription of a Report Name by Organization
        Delete a report subscription for your organization. You must know the unique name of the report you want to delete. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_subscription_with_http_info(report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_name: Name of the Report to Delete (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_name', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_name' is set
        if ('report_name' not in params) or (params['report_name'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `report_name` when calling `delete_subscription`")
            raise ValueError("Missing the required parameter `report_name` when calling `delete_subscription`")


        collection_formats = {}

        path_params = {}
        if 'report_name' in params:
            path_params['reportName'] = params['report_name']
            reportName=report_name

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        body_params = None
        if 'DELETE' in ('POST'):
            body_params = '{}'
        
        file_post_body_and_delimiter = MultipartHelpers.build_post_body_for_files(local_var_files)
        if file_post_body_and_delimiter is not None:
            body_params = file_post_body_and_delimiter[0]
            header_params['Content-Type'] = f"multipart/form-data; boundary={file_post_body_and_delimiter[1]}" 

        is_mle_supported_by_cybs_for_api = False
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "delete_subscription,delete_subscription_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/reporting/v3/report-subscriptions/{reportName}', 'DELETE',
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

    def get_all_subscriptions(self, **kwargs):
        """
        Get All Subscriptions
        View a summary of all report subscriptions. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_subscriptions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportSubscriptionsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_all_subscriptions` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_subscriptions_with_http_info(**kwargs)
        else:
            (data) = self.get_all_subscriptions_with_http_info(**kwargs)
            return data

    def get_all_subscriptions_with_http_info(self, **kwargs):
        """
        Get All Subscriptions
        View a summary of all report subscriptions. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_subscriptions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportSubscriptionsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json'])

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
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "get_all_subscriptions,get_all_subscriptions_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/reporting/v3/report-subscriptions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ReportSubscriptionsGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscription(self, report_name, **kwargs):
        """
        Get Subscription for Report Name
        View the details of a report subscription, such as the report format or report frequency, using the report's unique name. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription(report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_name: Name of the Report to Retrieve (required)
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportSubscriptionsGet200ResponseSubscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_subscription` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscription_with_http_info(report_name, **kwargs)
        else:
            (data) = self.get_subscription_with_http_info(report_name, **kwargs)
            return data

    def get_subscription_with_http_info(self, report_name, **kwargs):
        """
        Get Subscription for Report Name
        View the details of a report subscription, such as the report format or report frequency, using the report's unique name. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_with_http_info(report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_name: Name of the Report to Retrieve (required)
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportSubscriptionsGet200ResponseSubscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_name', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_name' is set
        if ('report_name' not in params) or (params['report_name'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `report_name` when calling `get_subscription`")
            raise ValueError("Missing the required parameter `report_name` when calling `get_subscription`")


        collection_formats = {}

        path_params = {}
        if 'report_name' in params:
            path_params['reportName'] = params['report_name']
            reportName=report_name

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json'])

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
        if MLEUtility.check_is_mle_for_api(self.api_client.mconfig, is_mle_supported_by_cybs_for_api, "get_subscription,get_subscription_with_http_info"):
                body_params = MLEUtility.encrypt_request_payload(self.api_client.mconfig, body_params)
        
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/reporting/v3/report-subscriptions/{reportName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ReportSubscriptionsGet200ResponseSubscriptions',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
