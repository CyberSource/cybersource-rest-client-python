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


class PaymentsProductsServiceFeeConfigurationInformationConfigurationsProducts(object):
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
        'service_fee_enabled': 'bool'
    }

    attribute_map = {
        'service_fee_enabled': 'serviceFeeEnabled'
    }

    def __init__(self, service_fee_enabled=None):
        """
        PaymentsProductsServiceFeeConfigurationInformationConfigurationsProducts - a model defined in Swagger
        """

        self._service_fee_enabled = None

        if service_fee_enabled is not None:
          self.service_fee_enabled = service_fee_enabled

    @property
    def service_fee_enabled(self):
        """
        Gets the service_fee_enabled of this PaymentsProductsServiceFeeConfigurationInformationConfigurationsProducts.
        Boolean flag to determine if service fee will be applied to the Product.

        :return: The service_fee_enabled of this PaymentsProductsServiceFeeConfigurationInformationConfigurationsProducts.
        :rtype: bool
        """
        return self._service_fee_enabled

    @service_fee_enabled.setter
    def service_fee_enabled(self, service_fee_enabled):
        """
        Sets the service_fee_enabled of this PaymentsProductsServiceFeeConfigurationInformationConfigurationsProducts.
        Boolean flag to determine if service fee will be applied to the Product.

        :param service_fee_enabled: The service_fee_enabled of this PaymentsProductsServiceFeeConfigurationInformationConfigurationsProducts.
        :type: bool
        """

        self._service_fee_enabled = service_fee_enabled

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
        if not isinstance(other, PaymentsProductsServiceFeeConfigurationInformationConfigurationsProducts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other