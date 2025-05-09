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


class Invoicingv2invoicesProcessingInformation(object):
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
        'request_phone': 'bool',
        'request_shipping': 'bool'
    }

    attribute_map = {
        'request_phone': 'requestPhone',
        'request_shipping': 'requestShipping'
    }

    def __init__(self, request_phone=False, request_shipping=False):
        """
        Invoicingv2invoicesProcessingInformation - a model defined in Swagger
        """

        self._request_phone = None
        self._request_shipping = None

        if request_phone is not None:
          self.request_phone = request_phone
        if request_shipping is not None:
          self.request_shipping = request_shipping

    @property
    def request_phone(self):
        """
        Gets the request_phone of this Invoicingv2invoicesProcessingInformation.
        Collect the payers phone number during the payment.

        :return: The request_phone of this Invoicingv2invoicesProcessingInformation.
        :rtype: bool
        """
        return self._request_phone

    @request_phone.setter
    def request_phone(self, request_phone):
        """
        Sets the request_phone of this Invoicingv2invoicesProcessingInformation.
        Collect the payers phone number during the payment.

        :param request_phone: The request_phone of this Invoicingv2invoicesProcessingInformation.
        :type: bool
        """

        self._request_phone = request_phone

    @property
    def request_shipping(self):
        """
        Gets the request_shipping of this Invoicingv2invoicesProcessingInformation.
        Collect the payers shipping address during the payment.

        :return: The request_shipping of this Invoicingv2invoicesProcessingInformation.
        :rtype: bool
        """
        return self._request_shipping

    @request_shipping.setter
    def request_shipping(self, request_shipping):
        """
        Sets the request_shipping of this Invoicingv2invoicesProcessingInformation.
        Collect the payers shipping address during the payment.

        :param request_shipping: The request_shipping of this Invoicingv2invoicesProcessingInformation.
        :type: bool
        """

        self._request_shipping = request_shipping

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
        if not isinstance(other, Invoicingv2invoicesProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
