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


class PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies(object):
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
        'currency_codes': 'list[str]',
        'acquirer_id': 'str',
        'processor_merchant_id': 'str'
    }

    attribute_map = {
        'currency_codes': 'currencyCodes',
        'acquirer_id': 'acquirerId',
        'processor_merchant_id': 'processorMerchantId'
    }

    def __init__(self, currency_codes=None, acquirer_id=None, processor_merchant_id=None):
        """
        PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies - a model defined in Swagger
        """

        self._currency_codes = None
        self._acquirer_id = None
        self._processor_merchant_id = None

        if currency_codes is not None:
          self.currency_codes = currency_codes
        if acquirer_id is not None:
          self.acquirer_id = acquirer_id
        if processor_merchant_id is not None:
          self.processor_merchant_id = processor_merchant_id

    @property
    def currency_codes(self):
        """
        Gets the currency_codes of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.

        :return: The currency_codes of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        :rtype: list[str]
        """
        return self._currency_codes

    @currency_codes.setter
    def currency_codes(self, currency_codes):
        """
        Sets the currency_codes of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.

        :param currency_codes: The currency_codes of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        :type: list[str]
        """

        self._currency_codes = currency_codes

    @property
    def acquirer_id(self):
        """
        Gets the acquirer_id of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        The Acquirer ID value, often referred to as the Acquirer BIN, is specific to an Acquirer. The value is created by Cardinal in their system and the Acquirer may not know that the Acquirer ID is different from their Acquiring BIN. It is most often the Acquiring BIN + \"-1000\" but the trailing character can be different. **Note** We will need to double check with Cardinal before setting up the Portfolio Template in production. 

        :return: The acquirer_id of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        :rtype: str
        """
        return self._acquirer_id

    @acquirer_id.setter
    def acquirer_id(self, acquirer_id):
        """
        Sets the acquirer_id of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        The Acquirer ID value, often referred to as the Acquirer BIN, is specific to an Acquirer. The value is created by Cardinal in their system and the Acquirer may not know that the Acquirer ID is different from their Acquiring BIN. It is most often the Acquiring BIN + \"-1000\" but the trailing character can be different. **Note** We will need to double check with Cardinal before setting up the Portfolio Template in production. 

        :param acquirer_id: The acquirer_id of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        :type: str
        """
        if acquirer_id is not None and not re.search('^[a-zA-Z0-9]{6,20}$', acquirer_id):
            raise ValueError("Invalid value for `acquirer_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9]{6,20}$/`")

        self._acquirer_id = acquirer_id

    @property
    def processor_merchant_id(self):
        """
        Gets the processor_merchant_id of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        Processor Merchant ID is the Merchant ID assigned by your acquiring bank. This Merchant ID should also be used by your bank to register your account to the card scheme Directory Server for processing Payer Authentication services. 

        :return: The processor_merchant_id of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        :rtype: str
        """
        return self._processor_merchant_id

    @processor_merchant_id.setter
    def processor_merchant_id(self, processor_merchant_id):
        """
        Sets the processor_merchant_id of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        Processor Merchant ID is the Merchant ID assigned by your acquiring bank. This Merchant ID should also be used by your bank to register your account to the card scheme Directory Server for processing Payer Authentication services. 

        :param processor_merchant_id: The processor_merchant_id of this PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies.
        :type: str
        """
        if processor_merchant_id is not None and not re.search('^[a-zA-Z0-9]{6,35}$', processor_merchant_id):
            raise ValueError("Invalid value for `processor_merchant_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9]{6,35}$/`")

        self._processor_merchant_id = processor_merchant_id

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
        if not isinstance(other, PaymentsProductsPayerAuthenticationConfigurationInformationConfigurationsCardTypesVerifiedByVisaCurrencies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other