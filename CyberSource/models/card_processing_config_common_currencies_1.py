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


class CardProcessingConfigCommonCurrencies1(object):
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
        'enabled': 'bool',
        'enabled_card_present': 'bool',
        'enabled_card_not_present': 'bool',
        'terminal_ids': 'list[str]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'enabled_card_present': 'enabledCardPresent',
        'enabled_card_not_present': 'enabledCardNotPresent',
        'terminal_ids': 'terminalIds'
    }

    def __init__(self, enabled=None, enabled_card_present=None, enabled_card_not_present=None, terminal_ids=None):
        """
        CardProcessingConfigCommonCurrencies1 - a model defined in Swagger
        """

        self._enabled = None
        self._enabled_card_present = None
        self._enabled_card_not_present = None
        self._terminal_ids = None

        if enabled is not None:
          self.enabled = enabled
        if enabled_card_present is not None:
          self.enabled_card_present = enabled_card_present
        if enabled_card_not_present is not None:
          self.enabled_card_not_present = enabled_card_not_present
        if terminal_ids is not None:
          self.terminal_ids = terminal_ids

    @property
    def enabled(self):
        """
        Gets the enabled of this CardProcessingConfigCommonCurrencies1.

        :return: The enabled of this CardProcessingConfigCommonCurrencies1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CardProcessingConfigCommonCurrencies1.

        :param enabled: The enabled of this CardProcessingConfigCommonCurrencies1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def enabled_card_present(self):
        """
        Gets the enabled_card_present of this CardProcessingConfigCommonCurrencies1.
        Indicates whether the card-present transaction is activated for the selected currency. If both enabledCardPresent and enabledCardNotPresent are set to null, then enabledCardPresent will have the value of enabled. 

        :return: The enabled_card_present of this CardProcessingConfigCommonCurrencies1.
        :rtype: bool
        """
        return self._enabled_card_present

    @enabled_card_present.setter
    def enabled_card_present(self, enabled_card_present):
        """
        Sets the enabled_card_present of this CardProcessingConfigCommonCurrencies1.
        Indicates whether the card-present transaction is activated for the selected currency. If both enabledCardPresent and enabledCardNotPresent are set to null, then enabledCardPresent will have the value of enabled. 

        :param enabled_card_present: The enabled_card_present of this CardProcessingConfigCommonCurrencies1.
        :type: bool
        """

        self._enabled_card_present = enabled_card_present

    @property
    def enabled_card_not_present(self):
        """
        Gets the enabled_card_not_present of this CardProcessingConfigCommonCurrencies1.
        Indicates whether the card-present transaction is activated for the selected currency. If both enabledCardPresent and enabledCardNotPresent are set to null, then enabledCardNotPresent will have the value of enabled. 

        :return: The enabled_card_not_present of this CardProcessingConfigCommonCurrencies1.
        :rtype: bool
        """
        return self._enabled_card_not_present

    @enabled_card_not_present.setter
    def enabled_card_not_present(self, enabled_card_not_present):
        """
        Sets the enabled_card_not_present of this CardProcessingConfigCommonCurrencies1.
        Indicates whether the card-present transaction is activated for the selected currency. If both enabledCardPresent and enabledCardNotPresent are set to null, then enabledCardNotPresent will have the value of enabled. 

        :param enabled_card_not_present: The enabled_card_not_present of this CardProcessingConfigCommonCurrencies1.
        :type: bool
        """

        self._enabled_card_not_present = enabled_card_not_present

    @property
    def terminal_ids(self):
        """
        Gets the terminal_ids of this CardProcessingConfigCommonCurrencies1.
        Applicable for Prisma (prisma) processor.

        :return: The terminal_ids of this CardProcessingConfigCommonCurrencies1.
        :rtype: list[str]
        """
        return self._terminal_ids

    @terminal_ids.setter
    def terminal_ids(self, terminal_ids):
        """
        Sets the terminal_ids of this CardProcessingConfigCommonCurrencies1.
        Applicable for Prisma (prisma) processor.

        :param terminal_ids: The terminal_ids of this CardProcessingConfigCommonCurrencies1.
        :type: list[str]
        """

        self._terminal_ids = terminal_ids

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
        if not isinstance(other, CardProcessingConfigCommonCurrencies1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other