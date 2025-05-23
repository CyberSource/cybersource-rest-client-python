# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class CreateSubscriptionRequest1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_reference_information': 'Rbsv1subscriptionsClientReferenceInformation',
        'processing_information': 'Rbsv1subscriptionsProcessingInformation',
        'plan_information': 'Rbsv1subscriptionsPlanInformation',
        'subscription_information': 'Rbsv1subscriptionsSubscriptionInformation',
        'order_information': 'GetAllPlansResponseOrderInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'processing_information': 'processingInformation',
        'plan_information': 'planInformation',
        'subscription_information': 'subscriptionInformation',
        'order_information': 'orderInformation'
    }

    def __init__(self, client_reference_information=None, processing_information=None, plan_information=None, subscription_information=None, order_information=None):
        """
        CreateSubscriptionRequest1 - a model defined in Swagger
        """

        self._client_reference_information = None
        self._processing_information = None
        self._plan_information = None
        self._subscription_information = None
        self._order_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if processing_information is not None:
          self.processing_information = processing_information
        if plan_information is not None:
          self.plan_information = plan_information
        if subscription_information is not None:
          self.subscription_information = subscription_information
        if order_information is not None:
          self.order_information = order_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this CreateSubscriptionRequest1.

        :return: The client_reference_information of this CreateSubscriptionRequest1.
        :rtype: Rbsv1subscriptionsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this CreateSubscriptionRequest1.

        :param client_reference_information: The client_reference_information of this CreateSubscriptionRequest1.
        :type: Rbsv1subscriptionsClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this CreateSubscriptionRequest1.

        :return: The processing_information of this CreateSubscriptionRequest1.
        :rtype: Rbsv1subscriptionsProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this CreateSubscriptionRequest1.

        :param processing_information: The processing_information of this CreateSubscriptionRequest1.
        :type: Rbsv1subscriptionsProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def plan_information(self):
        """
        Gets the plan_information of this CreateSubscriptionRequest1.

        :return: The plan_information of this CreateSubscriptionRequest1.
        :rtype: Rbsv1subscriptionsPlanInformation
        """
        return self._plan_information

    @plan_information.setter
    def plan_information(self, plan_information):
        """
        Sets the plan_information of this CreateSubscriptionRequest1.

        :param plan_information: The plan_information of this CreateSubscriptionRequest1.
        :type: Rbsv1subscriptionsPlanInformation
        """

        self._plan_information = plan_information

    @property
    def subscription_information(self):
        """
        Gets the subscription_information of this CreateSubscriptionRequest1.

        :return: The subscription_information of this CreateSubscriptionRequest1.
        :rtype: Rbsv1subscriptionsSubscriptionInformation
        """
        return self._subscription_information

    @subscription_information.setter
    def subscription_information(self, subscription_information):
        """
        Sets the subscription_information of this CreateSubscriptionRequest1.

        :param subscription_information: The subscription_information of this CreateSubscriptionRequest1.
        :type: Rbsv1subscriptionsSubscriptionInformation
        """

        self._subscription_information = subscription_information

    @property
    def order_information(self):
        """
        Gets the order_information of this CreateSubscriptionRequest1.

        :return: The order_information of this CreateSubscriptionRequest1.
        :rtype: GetAllPlansResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this CreateSubscriptionRequest1.

        :param order_information: The order_information of this CreateSubscriptionRequest1.
        :type: GetAllPlansResponseOrderInformation
        """

        self._order_information = order_information

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CreateSubscriptionRequest1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
