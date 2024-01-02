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


class PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors(object):
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
        'merchant_id': 'str',
        'acquirer_id': 'str'
    }

    attribute_map = {
        'merchant_id': 'merchantId',
        'acquirer_id': 'acquirerId'
    }

    def __init__(self, merchant_id=None, acquirer_id=None):
        """
        PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors - a model defined in Swagger
        """

        self._merchant_id = None
        self._acquirer_id = None

        if merchant_id is not None:
          self.merchant_id = merchant_id
        if acquirer_id is not None:
          self.acquirer_id = acquirer_id

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors.
        The merchant identifier for the Currency Conversion service. Check with your Currency Conversion Provider for details.

        :return: The merchant_id of this PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors.
        The merchant identifier for the Currency Conversion service. Check with your Currency Conversion Provider for details.

        :param merchant_id: The merchant_id of this PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def acquirer_id(self):
        """
        Gets the acquirer_id of this PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors.

        :return: The acquirer_id of this PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors.
        :rtype: str
        """
        return self._acquirer_id

    @acquirer_id.setter
    def acquirer_id(self, acquirer_id):
        """
        Sets the acquirer_id of this PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors.

        :param acquirer_id: The acquirer_id of this PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors.
        :type: str
        """

        self._acquirer_id = acquirer_id

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
        if not isinstance(other, PaymentsProductsCurrencyConversionConfigurationInformationConfigurationsProcessors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other