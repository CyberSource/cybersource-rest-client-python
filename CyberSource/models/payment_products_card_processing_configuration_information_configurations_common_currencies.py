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


class PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies(object):
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
        'merchant_id': 'str',
        'terminal_id': 'str',
        'terminal_ids': 'list[str]',
        'service_enablement_number': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'enabled_card_present': 'enabledCardPresent',
        'enabled_card_not_present': 'enabledCardNotPresent',
        'merchant_id': 'merchantId',
        'terminal_id': 'terminalId',
        'terminal_ids': 'terminalIds',
        'service_enablement_number': 'serviceEnablementNumber'
    }

    def __init__(self, enabled=None, enabled_card_present=None, enabled_card_not_present=None, merchant_id=None, terminal_id=None, terminal_ids=None, service_enablement_number=None):
        """
        PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies - a model defined in Swagger
        """

        self._enabled = None
        self._enabled_card_present = None
        self._enabled_card_not_present = None
        self._merchant_id = None
        self._terminal_id = None
        self._terminal_ids = None
        self._service_enablement_number = None

        if enabled is not None:
          self.enabled = enabled
        if enabled_card_present is not None:
          self.enabled_card_present = enabled_card_present
        if enabled_card_not_present is not None:
          self.enabled_card_not_present = enabled_card_not_present
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if terminal_id is not None:
          self.terminal_id = terminal_id
        if terminal_ids is not None:
          self.terminal_ids = terminal_ids
        if service_enablement_number is not None:
          self.service_enablement_number = service_enablement_number

    @property
    def enabled(self):
        """
        Gets the enabled of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.

        :return: The enabled of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.

        :param enabled: The enabled of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :type: bool
        """

        self._enabled = enabled

    @property
    def enabled_card_present(self):
        """
        Gets the enabled_card_present of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Indicates whether the card-present transaction is activated for the selected currency. If both enabledCardPresent and enabledCardNotPresent are set to null, then enabledCardPresent will have the value of enabled.

        :return: The enabled_card_present of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :rtype: bool
        """
        return self._enabled_card_present

    @enabled_card_present.setter
    def enabled_card_present(self, enabled_card_present):
        """
        Sets the enabled_card_present of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Indicates whether the card-present transaction is activated for the selected currency. If both enabledCardPresent and enabledCardNotPresent are set to null, then enabledCardPresent will have the value of enabled.

        :param enabled_card_present: The enabled_card_present of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :type: bool
        """

        self._enabled_card_present = enabled_card_present

    @property
    def enabled_card_not_present(self):
        """
        Gets the enabled_card_not_present of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Indicates whether the card-not-present transaction is activated for the selected currency. If both enabledCardPresent and enabledCardNotPresent are set to null, then enabledCardNotPresent will have the value of enabled.

        :return: The enabled_card_not_present of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :rtype: bool
        """
        return self._enabled_card_not_present

    @enabled_card_not_present.setter
    def enabled_card_not_present(self, enabled_card_not_present):
        """
        Sets the enabled_card_not_present of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Indicates whether the card-not-present transaction is activated for the selected currency. If both enabledCardPresent and enabledCardNotPresent are set to null, then enabledCardNotPresent will have the value of enabled.

        :param enabled_card_not_present: The enabled_card_not_present of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :type: bool
        """

        self._enabled_card_not_present = enabled_card_not_present

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Merchant ID assigned by an acquirer or a processor. Should not be overridden by any other party.

        :return: The merchant_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Merchant ID assigned by an acquirer or a processor. Should not be overridden by any other party.

        :param merchant_id: The merchant_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def terminal_id(self):
        """
        Gets the terminal_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        The 'Terminal Id' aka TID, is an identifier used for with your payments processor. Depending on the processor and payment acceptance type this may also be the default Terminal ID used for Card Present and Virtual Terminal transactions. 

        :return: The terminal_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """
        Sets the terminal_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        The 'Terminal Id' aka TID, is an identifier used for with your payments processor. Depending on the processor and payment acceptance type this may also be the default Terminal ID used for Card Present and Virtual Terminal transactions. 

        :param terminal_id: The terminal_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :type: str
        """

        self._terminal_id = terminal_id

    @property
    def terminal_ids(self):
        """
        Gets the terminal_ids of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Applicable for Prisma (prisma) processor.

        :return: The terminal_ids of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :rtype: list[str]
        """
        return self._terminal_ids

    @terminal_ids.setter
    def terminal_ids(self, terminal_ids):
        """
        Sets the terminal_ids of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Applicable for Prisma (prisma) processor.

        :param terminal_ids: The terminal_ids of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :type: list[str]
        """

        self._terminal_ids = terminal_ids

    @property
    def service_enablement_number(self):
        """
        Gets the service_enablement_number of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Service Establishment Number (a.k.a. SE Number) is a unique ten-digit number assigned by American Express to a merchant that accepts American Express cards. 10 digit number provided by acquirer currency. This may be unique for each currency, however it depends on the way the processor is set up for the merchant. 

        :return: The service_enablement_number of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :rtype: str
        """
        return self._service_enablement_number

    @service_enablement_number.setter
    def service_enablement_number(self, service_enablement_number):
        """
        Sets the service_enablement_number of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        Service Establishment Number (a.k.a. SE Number) is a unique ten-digit number assigned by American Express to a merchant that accepts American Express cards. 10 digit number provided by acquirer currency. This may be unique for each currency, however it depends on the way the processor is set up for the merchant. 

        :param service_enablement_number: The service_enablement_number of this PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies.
        :type: str
        """

        self._service_enablement_number = service_enablement_number

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
        if not isinstance(other, PaymentProductsCardProcessingConfigurationInformationConfigurationsCommonCurrencies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other